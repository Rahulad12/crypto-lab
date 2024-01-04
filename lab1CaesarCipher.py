def main():
    plain = input("\nEnter the plain text: ")
    
    # Validate key input
    while True:
        try:
            key = int(input("\nEnter the key value: "))
            break
        except ValueError:
            print("Invalid key. Please enter a valid integer.")

    length = len(plain)
    cipher = []

    print("\nPLAIN TEXT:", plain)
    print("\nENCRYPTED TEXT:")

    for i in range(length):
        char = plain[i]
        if char.isupper():
            cipher_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            cipher_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            cipher_char = char
        cipher.append(cipher_char)
        print(cipher_char, end='')

    print("\nAFTER DECRYPTION:")
    for i in range(length):
        plain_char = cipher[i]
        if plain_char.isupper():
            plain_char = chr((ord(plain_char) - ord('A') - key) % 26 + ord('A'))
        elif plain_char.islower():
            plain_char = chr((ord(plain_char) - ord('a') - key) % 26 + ord('a'))
        print(plain_char, end='')

if __name__ == "__main__":
    main()
