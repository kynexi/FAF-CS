ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"   
LATIN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            
N = 31

def text_formatting(text, alphabet):
    if text == "":
        print("Input text is empty")
        return None

    text = text.upper() # conversion to uppercase
    text = text.replace(" ", "") # remove spaces
    text = text.replace("Ş", "Ș").replace("Ţ", "Ț") # adjust for cedilla edge case
    
    valid = True
    for char in text:
        if char not in alphabet:
            valid = False
            print(f"Invalid character '{char}' in the text. Please use only characters from the alphabet '{alphabet}'.")
            break
    
        if valid:
            break

    return text
