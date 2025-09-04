# 1. Ask a user for their age and how long they have had their subscription for (in years)
# The user qualifies for a discount if they meet the following criteria
# the user is a student (under 25yrs old) or a senior citizen (65yrs or older)
# the user has had their subscription for at least 12 months

# 2. Print out the following message if the user doesnt qualify for a discount:
# "great news! you qualify for a discount on your music streaming subscription"
# or this if they dont qualify ("sorry, you dont qualify for a discount at this time")


age = input("How old are you?")
subscription_length = input("How long have you had your subscription for?")

if (int(age) < 25 or int(age) >= 65) and (int(subscription_length) < 1):
    print("Great news! you qualify for discount on your music streaming subscription!")
else:
    print("Sorry, you dont qualify for a discount this time")

