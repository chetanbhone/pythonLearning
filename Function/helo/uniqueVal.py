# get unique value from word without using set()
while True:
    def unique(word):
        lst = []
        for char in word:
            if char not in lst:  # Check if char is already in the list
                lst.append(char)
        return lst

    word = input("Enter your word here: ").strip()     # remove spaces

    if len(word) == 0:  # If the input is empty, ask for input again
        print("Don't leave it blank. Please enter some words.")
        continue  # Go back to asking for input again
    else:
        value = unique(word)
        print("Unique characters:", value)
        break  # Exit the loop after getting a valid input
