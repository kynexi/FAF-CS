ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"   
LATIN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            
N = 31

def text_formatting(text, alphabet):
    text = text.upper() # conversion to uppercase
    text = text.replace(" ", "") # remove spaces
    text = text.replace("Ş", "Ș").replace("Ţ", "Ț") # adjust for cedilla edge case

    if text == "":
        print("Input text is empty")
        return None

    for char in text:
        if char not in alphabet:
            print(f"Invalid character '{char}' in the text. Please use only characters from the alphabet '{alphabet}'.")
            return None

    return text

def vigenere(text, key, sign):
    result = ""
    for i in range(len(text)):
        m = ALPHABET.index(text[i])            # letter code from the text
        k = ALPHABET.index(key[i % len(key)])  # letter code from the key
        result += ALPHABET[(m + sign * k) % N]
    return result


def main():
    # encrypt / decrypt choice
    while True:
        op = input("Choose an operation (e / d): ")

        if op in ["e", "d"]:
            break
        else:
            print("Invalid operation. Please choose 'e' for encryption or 'd' for decryption.")

    # keyword
    while True:
        key = text_formatting(input("Enter a keyword (at least 7 letters): "), LATIN)

        if key is None:
            continue

        if len(key) < 7:
            print("Invalid keyword. Please enter a keyword with at least 7 characters")
            continue

        break

    # text for encryption / decryption
    while True:
        if op == "e":
            text = text_formatting(input("Enter a message: "), LATIN)
        else:
            text = text_formatting(input("Enter a ciphertext: "), ALPHABET)

        if text is not None:
            break

    if op == "e":
        print("Ciphertext:", vigenere(text, key, 1))
    else:
        print("Message:", vigenere(text, key, -1))

if __name__ == "__main__":
    main()
