import requests

# Write a function called get_song that asks the user to input a song title along with the artists name, using two input prompts
def get_song():
    Song_name = input("What is the song title?:")
    Artist = input("What is the artists name?:")
    return [Song_name, Artist]

get_song()

# Write another function called get_lyrics that makes a HTTP GET request and print the response to the endpoint:
# https://api.lyrics.ovh/v1/{artist}/{title}

def get_lyrics(Artist, Song_name):
    lyrics = requests.get(f"https://api.lyrics.ovh/v1/{Artist}/{Song_name}")
    print(lyrics.json())
    
# Combine these functions into a main function that calls get_song then calls get_lyrics, with the information that the user entered 

def main_function():
    Song_info = get_song()
    Artist = Song_info[1]
    Song_name = Song_info[0]
    get_lyrics(Artist, Song_name)

main_function()