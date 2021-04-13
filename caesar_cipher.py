# Set the alphabet
alphabet = "- abcdefghijklmnopqrstuvwxyz"

# Putting in our sentence
sentence_randomcase = input("Enter your sentence: ")
sentence = sentence_randomcase.lower()

# Asking the shift length
shift_random = int(input("Shift value: "))
shift = shift_random % 26

# Set the empty ciphertext
ciphertext = []

# Function to find the final index of the shifted alphabet
def encode(x):
    final_shift = x + shift

    if final_shift <= 27:
        return final_shift
    else:
        final_shift = final_shift - 26
        return final_shift

# Function to see if the character is within the alphabet
def is_it_there(x):
    try:
        y = alphabet.index(x)
        return y
    except:
        return 69

# Shift the sentence
for i in range(len(sentence)):
    x = is_it_there(sentence[i])

    if x == 1 or x == 0:
        ciphertext += alphabet[x]
    elif x == 69:
        ciphertext += sentence[i]
    else:
        res = encode(x)
        ciphertext += alphabet[res]

print("".join(ciphertext))

# This is hot garbage
