alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
# print(len(alphabet)) = 31

def encrypt(text, alphabet, key):
    encrypted_text = ""
    for char in text:
        position = alphabet.index(char)
        new_position = (position + key) % len(alphabet)
        encrypted_text += alphabet[new_position]
    return encrypted_text

def decrypt(text, alphabet, key):
    decrypted_text = ""
    for char in text:
        position = alphabet.index(char)
        new_position = (position - key) % len(alphabet)
        decrypted_text += alphabet[new_position]
    return decrypted_text

def main():
    while True:
        operation = input("Choose an operation (e / d): ").lower()

        if operation in ['e', 'd']:
            break
        else:
            print("Invalid operation. Please choose 'e' for encryption or 'd' for decryption.")

    while True:
        user_text = input("Enter a text: ")
        user_text = user_text.upper() # conversion to uppercase
        user_text = user_text.replace(" ", "") # remove spaces
        user_text = user_text.replace("Ş", "Ș").replace("Ţ", "Ț") # adjust for cedilla edge case

        valid = True
        for char in user_text:
            if char not in alphabet:
                valid = False
                print(f"Invalid character '{char}' in the text. Please use only characters from the alphabet '{alphabet}'.")
                break

        if valid:
            break

    while True:
        try:
            key = int(input("Enter a key (integer): "))

            if key < 1 or key > 30:
                print("Invalid key. Please enter a key between 1 and 30.")

            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if operation == 'e':
        encrypted_text = encrypt(user_text, alphabet, key)
        print("Encrypted text:", encrypted_text)

    elif operation == 'd':
        decrypted_text = decrypt(user_text, alphabet, key)
        print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()  