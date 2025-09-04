# 1. As a user to input how many songs they would like to add to their playlist

# 2. Store this information in a variable called: playlist length
playlist_length = int(input("How many songs would you like to add to your playlist?"))
print(playlist_length)
# 3. Using a for loop, prompt the user the enter the duration of each song in their playlist

# 4. Store the duration of each song in a list called: song_durations, and print these to the console
song_duration = []

for song in range(playlist_length):
    duration = input(f"What is the length of song {song + 1}?" )
    song_duration.append(duration)

print(song_duration)