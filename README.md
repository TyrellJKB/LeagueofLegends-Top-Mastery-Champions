# League of Legends Mastery Checker

## Overview

The League of Legends Mastery Checker is a Flask-based web application designed to provide users with detailed insights into their champion masteries. Leveraging the Riot Games API, this tool retrieves account information and presents the top champion masteries of a specified player. Additionally, it fetches champion details from the Data Dragon API to enhance the displayed information.

## Features

1. **User Interface:**
    - The web application provides a simple user interface with a form to input the Riot ID (username and tagline).

2. **API Integration:**
    - Utilizes the Riot Games API to retrieve account information, including the Player Universally Unique Identifier (PUUID).

3. **Champion Mastery Display:**
    - Displays the top 6 champion masteries based on mastery points for the specified player.

4. **Data Dragon Integration:**
    - Retrieves champion details (name, image, classes, title) from the Data Dragon API to enhance the displayed champion mastery information.

5. **Error Handling:**
    - Handles errors gracefully, providing informative messages for invalid Riot IDs or API request failures.
  
6. **Responsive Design""
     -  Dynamically adapts and optimises content layout and presentation based on the user's device, ensuring a seamless and user-friendly experience across various screen sizes and resolutions. 

## Functionality

### API Endpoints

The application defines the following API endpoints:

- `RIOT_API_ENDPOINT`: Endpoint to retrieve the PUUID based on the provided Riot ID.
- `CHAMPION_MASTERY_ENDPOINT`: Endpoint to retrieve champion mastery data for a given PUUID.
- `CHAMPION_LIST_ENDPOINT`: Endpoint to retrieve the list of champions and their details from the Data Dragon API.

### Routes

1. **Home Page (`/`):**
    - Renders the `index.html` template, providing the main form for users to input their Riot ID.

2. **PUUID Retrieval (`/get_puuid`, POST):**
    - Handles the form submission to retrieve the PUUID based on the provided Riot ID.
    - Calls the Riot API to fetch account information.
    - If successful, calls the `get_top_champion_mastery` function and renders the `result.html` template with the obtained PUUID and mastery data.
    - Handles errors and displays appropriate messages on the home page.

### Helper Functions

1. **`get_top_champion_mastery(puuid)`:**
    - Takes a PUUID as input and retrieves the top 6 champion masteries for that player.
    - Utilizes the Riot API's champion mastery endpoint.
    - Retrieves champion details from the Data Dragon API.
    - Constructs a list of dictionaries containing champion details and mastery information.

## Development Process

During the development process:

1. Started attempting to use the summoner name to find champion masteries, but this approach proved ineffective.
   
3. Shifted the goal to using the summoner name + tag line to obtain the PUUID.
   
5. Expanded the scope to retrieve the most played champions' number, mastery points, and level using the PUUID.
   
7. Further expanded the scope to use the champion number to find the champion name, icon, and other descriptive points.

## Planned Enhancements

1. **Tracking Account Details:**
    - Implement enhanced user tracking features to allow users to save and track their champion masteries over time.

2. **Detailed Champion Information:**
    - Provide additional information about each champion, such as lore, abilities, and skins.

3. **Seperate HTML and CSS:**
    - Refactor the code to include separate HTML and CSS files for better organization and maintainability.

4. **Caching Mechanism:**
    - Implement a caching mechanism to store frequently accessed data and reduce the number of API requests.

5. **Leaderboard Feature:**
    - Add a leaderboard feature to compare users' champion masteries and rankings.

