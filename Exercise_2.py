# Create two variables to store the title and artist of a song
Title = "What else can I do"
Artist = "Mirabel and Isabella"

# Create a formatted string to display the message
Message = "My favourite song is {} by {}".format(Title, Artist)
print(Message)

# Create a list called "playlist" that contains three song titles of your choice
playlist = ['Dos Oruguitas', 'Surface Pressure', 'We dont talk about Bruno']

# Add a new song to the playlist using .extend()
playlist.extend(["Waiting on a miracle", "All of you"])

print(playlist)
