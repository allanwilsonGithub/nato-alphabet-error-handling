import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def product_letters_from_input():
    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)


done = 0
while done == 0:
    try:
        product_letters_from_input()
    except KeyError:
        print("Please use only letters from the alphabet")
    else:
        done = 1
