while (True):
    dog_age = input ("Input a dog's age in human years: (PRESS quit to STOP)")

    if dog_age == "quit":
        break;

    if int(dog_age) == 1:
        print(f"The dog's age in dog years is {(2 * 10 )}")
    else:
        print(f"The dog's age in dog years is {(2 * 10 ) + (int(dog_age) - 2) * 7}")