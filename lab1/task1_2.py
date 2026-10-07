alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"

def cipher(text, alphabet, key, keyword, operation):
    permuted_alphabet = ""  
    for char in keyword:
        if char not in permuted_alphabet:
            permuted_alphabet += char  
    for char in alphabet:
        if char not in permuted_alphabet:
            permuted_alphabet += char 
    print("Permuted alphabet:", permuted_alphabet) 

    output = ""
    for char in text:
        position = permuted_alphabet.index(char)
        if operation == 'd':
            new_position = (position - key) % len(permuted_alphabet)
        else:
            new_position = (position + key) % len(permuted_alphabet)
        output += permuted_alphabet[new_position]
    return output

def main():
    # encrypt / decrypt choice
    while True:
        operation = input("Choose an operation (e / d): ").lower()

        if operation in ['e', 'd']:
            break
        else:
            print("Invalid operation. Please choose 'e' for encryption or 'd' for decryption.")

    # text for encryption / decryption
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

    # key 2 aka keyword
    while True:
        keyword = input("Enter a keyword (string): ")
        keyword = keyword.upper() # conversion to uppercase
        keyword = keyword.replace(" ", "") # remove spaces
        keyword = keyword.replace("Ş", "Ș").replace("Ţ", "Ț")
        valid = True

        if len(keyword) < 7:
            valid = False
            print("Invalid keyword. Please enter a keyword with at least 7 characters.")
            continue

        for char in keyword:
            if char not in alphabet:
                valid = False
                print(f"Invalid character '{char}' in the keyword. Please use only characters from the alphabet '{alphabet}'.")
                break

        if valid:
            break

    # numeric key, key 1
    while True:
        try:
            key_numeric = int(input("Enter a key (integer): "))

            if key_numeric < 1 or key_numeric > 30:
                print("Invalid key. Please enter a key between 1 and 30.")

            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    output = cipher(user_text, alphabet, key_numeric, keyword, operation)
    print("Output text:", output)


if __name__ == "__main__":
    main()  