from flask import Flask, render_template, request
import requests
from config import RIOT_API_KEY

app = Flask(__name__)

RIOT_API_ENDPOINT = 'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'
CHAMPION_MASTERY_ENDPOINT = 'https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/'
CHAMPION_LIST_ENDPOINT = 'https://ddragon.leagueoflegends.com/cdn/14.1.1/data/en_US/champion.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_puuid', methods=['POST'])
def get_puuid():
    if request.method == 'POST':
        game_name = request.form['game_name']
        tag_line = request.form['tag_line']
        riot_id = f'{game_name}/{tag_line}'

        headers = {
            'X-Riot-Token': RIOT_API_KEY,
        }

        try:
            response = requests.get(f'{RIOT_API_ENDPOINT}{riot_id}', headers=headers)
            data = response.json()

            if 'puuid' in data:
                puuid = data['puuid']
                mastery_data = get_top_champion_mastery(puuid)
                return render_template('result.html', puuid=puuid, mastery_data=mastery_data)
            else:
                error_message = 'Invalid Riot ID. Please check your input.'
                return render_template('index.html', error_message=error_message)

        except requests.exceptions.RequestException as e:
            return render_template('index.html', error_message=f'Error: {str(e)}')

def get_top_champion_mastery(puuid):
    headers = {
        'X-Riot-Token': RIOT_API_KEY,
    }

    # Get top 6 mastery point champions
    mastery_response = requests.get(f'{CHAMPION_MASTERY_ENDPOINT}{puuid}/top?count=6', headers=headers)
    mastery_data = mastery_response.json()

    # Get champion details from Data Dragon
    champion_list_response = requests.get(CHAMPION_LIST_ENDPOINT)
    champion_list_data = champion_list_response.json()['data']

    champions = []
    for mastery in mastery_data:
        champion_key = str(mastery['championId'])
        try:
            champion_data = next((data for data in champion_list_data.values() if data['key'] == champion_key), None)
            if champion_data:
                champion_name = champion_data['name']
                mastery_level = mastery['championLevel']
                mastery_points = mastery['championPoints']
                champion_image = f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{champion_data['id']}_0.jpg"
                champion_classes = champion_data.get('tags', [])
                champion_title = champion_data.get('title', '') 

                champions.append({
                    'name': champion_name,
                    'level': mastery_level,
                    'points': mastery_points,
                    'image': champion_image,
                    'classes': champion_classes,
                    'title': champion_title,
                })
            else:
                print(f"Error: Champion with key {champion_key} not found in champion_list_data.")
        except KeyError:
            print(f"Error: Champion with ID {champion_key} not found in champion_list_data.")

    return champions







if __name__ == '__main__':
    app.run(debug=True)