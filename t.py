import requests

def get_jokes(category="Any", blacklist_flags=None, type=None):
    """
    Fetch a joke from the JokeAPI with optional filters.
    
    Parameters:
    category (str): The category of joke (default is "Any").
    blacklist_flags (list): List of flags to exclude (e.g., ["nsfw", "religious"]).
    type (str): Type of joke ("single" or "twopart").
    
    Returns:
    str: The fetched joke or an error message.
    """

    # Base URL for JokeAPI endpoint
    url = f"https://v2.jokeapi.dev/joke/{category}"  # UPDATED: Ensure category is correctly included in the URL

    # Prepare query parameters
    params = {}
    if blacklist_flags:
        params["blacklistFlags"] = ",".join(blacklist_flags)  # Join all the blacklist flags into a single string separated by commas
    if type:
        params["type"] = type

    # Make GET request to the API with the parameters
    response = requests.get(url, params=params)

    # Check for successful response
    if response.status_code != 200:
        return "Error fetching joke, please try again later."

    # Parse the JSON response
    joke_data = response.json()

    # Debugging information
    print("API Response:", joke_data)  # UPDATED: Add debugging information

    # Check if the 'type' key is present in the response
    if "type" not in joke_data:
        return "No matching joke found. Please check your query parameters."  # UPDATED: Improved error message

    # Format the joke type accordingly
    if joke_data["type"] == "single":
        return joke_data["joke"]
    else:
        return f'{joke_data["setup"]} - {joke_data["delivery"]}'

if __name__ == "__main__":
    joke = get_jokes(category="Programming", blacklist_flags=["nsfw"], type="single")
    print(joke)
