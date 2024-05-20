import requests


def get_jokes(category="Any", language="en", contains=None, type=None):
    """
    Fetch a joke from the JokeAPI with optional filters.
    
    Parameters:
    category (str): The category of joke (default is "Any").
    blacklist_flags (list): List of flags to exclude (e.g., ["nsfw", "religious"]).
    type (str): Type of joke ("single" or "twopart").
    
    Returns:
    str: The fetched joke.
    """

    #base url for jokeAPI endpoint
    url = f"https://v2.jokeapi.dev/joke/{category}"

    # Prepare query parameters
    params = {"lang": language}  # UPDATED: Include language parameter
    if contains:
        params["contains"] = contains  # UPDATED: Include contains parameter
    if type:
        params["type"] = type




    #printing the url and params for debugging
    # Show the final URI of the request
    #prepared request is used to get the final url
    final_uri = requests.Request('GET', url, params=params).prepare().url
    print("Final URI:", final_uri)

    
    #get req to the api w the params
    response = requests.get(url,params=params)

    #if response not ok return error
    if response.status_code != 200 :
        return "Error fetching joke, please try again later"
    
    
    #parse to json
    joke_data = response.json()


    #debug by printing api response :
    print("Api response :",joke_data)

    #check if type present in the response
    if "type" not in joke_data :
        return "you fucked up the joke query ya el batata"

    #format the joke type accordingly
    if joke_data["type"] == "single" :
        return joke_data["joke"]
    else :
        return f'{joke_data["setup"]} - {joke_data["delivery"]}'
    

if __name__ == "__main__":
    joke = get_jokes(contains="dog")
    print(joke)