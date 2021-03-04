# assignment 7:refactoring assignment 1 as a dictionary
def guessValue(x, y):  # x holds the keys while y holds the value passed from
    # the songAttribute and songInfo variable
    # respectively
    for _ in favSong_traits:  # iterate through the dictionary,

        if favSong_traits.get(x) == y:  # if any key(x) matches the entered value y
            return True  # program returns true otherwise False

        else:
            return False


favSong_traits = {
    'artist': 'zuchu',
    'song_genre ': ' afrobeats',
    'message': "love is sweet",
    'language': "swahili",
    'country': 'tanzania',
    'year': '2021',
    'time': '3.01',
    'views': '9.3',

}
songAttribute = input("enter a attribute :")
songInfo = input(f'give more information about the {songAttribute} :')

print(guessValue(songAttribute, songInfo))
print()

for attribute, value in favSong_traits.items():  # items() method loops through both keys and values
    print(attribute, " :", value)
