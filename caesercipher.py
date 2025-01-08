#caeser cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    new_text = ""
    if encode_or_decode == "decode":
        shift_amount = -shift_amount
    for letter in original_text:

        if letter not in alphabet:
            new_text += letter
        else:
            new_position = alphabet.index(letter) + shift_amount
            new_position %= len(alphabet) # other ways to do that is to add another list at the end so that the 28,29,30th
                                          # position will be a,b,c ... and so on
            new_text += alphabet[new_position]
    print(f"Here is the {encode_or_decode}d result: {new_text}")

continue_again = True

while continue_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        continue_again = False
        print("Goodbye")