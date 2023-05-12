while True:
    input_str = input ("Please enter a letter from the alphabet (a-z or A-Z): (PRESS quit to STOP)")

    if input_str == "quit":
        break;
    match input_str.lower():
        case "a" | "e" | "i" | "o" | "u":
            print (f"The letter {input_str} is a vowel")
        case _:
            print (f"The letter {input_str} is a consonant")