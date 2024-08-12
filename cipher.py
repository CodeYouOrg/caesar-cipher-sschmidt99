def caesar_cipher_encryption(plain_text, shift):
    encrypted_text = " "
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in plain_text:
        if char in alphabet_lower:
            #Finds index of character in lowercase alphabet
            index = alphabet_lower.index(char)
            #Should shift to encrypted letter
            new_char = alphabet_lower[(index + shift) % 26]
            encrypted_text += new_char
        
        elif char in alphabet_upper:
            #Find index of character in uppercase alphabet
            index = alphabet_upper.index(char)
            #should shift to encrypted letter
            new_char = alphabet_upper[(index + shift) % 26]
            encrypted_text += new_char
        else:
            #If not an alphabetic character just add it as is
            encrypted_text += char
    
    return encrypted_text

plain_text = input("Enter the text you want encrypted: ")

shift = 5
            
encrypted_text = caesar_cipher_encryption(plain_text, shift)

print("Encrypted text: ", encrypted_text)
