from art import logo
# this code encrypts or decrypts text preserving all the original characters within the text even after en/de/cryption

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def solve_caesar(cipher_task,text, key):
    if key >= 26:
        key %= 26
    return_str = ""
    if cipher_task == 'decode':
        key *= -1
    for letter in text:
        if letter not in letters:
            return_str += letter
            continue
        index = letters.index(letter)
        actual_index = index + key
        return_str += letters[actual_index]

    print(f"\nYour {cipher_task}d is {return_str}")



def start_processing():
    go_again = "yes"

    print(f"\n{logo}")

    while go_again == "yes":
        direction = input("\ntype 'encode' to encode or type 'decode' to decode: ")
        message = input("\ntype your message: ").lower()
        shift = int(input("\ntype the shift number: "))

        # we need to create a function that does all the heavy lifting including all the decoding and encoding 
        solve_caesar(direction,message,shift)

        go_again = input("\n Do you want to go again? (yes/no) : ")
start_processing()