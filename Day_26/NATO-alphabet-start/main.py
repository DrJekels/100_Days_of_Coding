import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
npa = nato_phonetic_alphabet.set_index('letter').T.to_dict('records')[0]

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Put in a word.")
phonetic_list = [npa.get(letter) for letter in word.upper() if letter in npa]
print(phonetic_list)