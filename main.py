# Written by Alexander Dave Flores Respicio

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}


# Prints the welcome banner for the program
def printWelcomeBanner():
    for count in range(0, 37):
        print("*", end="")
    print("\nWELCOME TO THE MORSE CODE TRANSLATOR!")
    for count in range(0, 37):
        print("*", end="")
    print("")


# Function that turns the string entered by the user into its Morse Code counterpart
def englishToMorse(englishString):
    for word in englishString.split(" "):  # For loop that traverses through the words entered by the user
        codeString = ""  # Empty string that will contain the morse code character sequences
        for character in word:  # For loop that goes through each character in a word
            if character == " ":  # If block that handles space characters
                codeString += " "
            else:  # Else block that converts characters to their morse code equivalents
                uppercaseCharacter = character.upper()  # Make a character uppercase
                codeCharacter = MORSE_CODE_DICT[uppercaseCharacter]  # Find its morse code counterpart in the dictionary
                codeString += codeCharacter  # Add the morse code sequence to codeString
        print(f"{word} -> {codeString}")  # Print the word and its full morse code equivalent


# Prints the exit banner for the program
def printExitBanner():
    for count in range(0, 22):
        print("*", end="")
    print("\nTHANK YOU FOR PLAYING!")
    for count in range(0, 22):
        print("*", end="")
    print("")

while True:  # While loop that will keep translating strings to morse code until the exit code is entered
    printWelcomeBanner()
    textInput = input("Please enter the string you'd like to translate (Enter EXIT! to exit): ")
    if textInput == "EXIT!":
        break
    else:
        englishToMorse(textInput)
        print("")

printExitBanner()
