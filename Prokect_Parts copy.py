import time 
import random
print("START?")
start = input("Yes or no.")
print("Hello!")
time.sleep(2)
print("Welcome to Project Parts, the game where you help AT&T fix their satellites!")
time.sleep(2)
print("DISCLAIMER : This is for school, and this product that AT&T is using is a product we are 'giving' to them")
def START():
    print("You've been sent to Mars, to find parts to repair the new satellites that gives everyone AT&T service! ")
    time.sleep(0.5)
    print("The rocket blows dust everywhere. There's a sea of rust and red. You go out, on a mission")
    time.sleep(0.5)
    print("Your ready for your mission, and your paycheck")
    FIND_PART()
def FIND_PART():
    where_to_find = input("Where do you look for parts? The Junkyard, The Field, or the area near your rocket? USE NO CAPS AND DO use spacebar (where your searching) and then no spacebar.")
    if where_to_find == ' the junkyard':
        print("You look around, and then out of the blue-")
        time.sleep(0.5)
        TRIVA()
    if where_to_find == ' the field':
        print("You look around, but then out of the blue-")
        time.sleep(0.5)
        TRIVA()
    if where_to_find == ' near my rocket':
        print("You literally see nothing because why would there be something near your rocket?")
        FIND_PART()
def TRIVA():
    print("You search! The parts are near, you can feel it, all you have to do is answer one triva question!")
    time.sleep(0.5)
    Triva_Random = random.randint(1, 10)
    if Triva_Random == 1 or 2:
        print("When was AT&T Founded???")
        Triva_Answer = input()
        if Triva_Answer == '1885':
            print("CORRECT!")
            time.sleep(0.5)
            print("You found a part, now you can repair the ship!!")
            print("You return to earth, AND FINALLY GET YOUR PAYCHECK!!! And then you see a pink slip reading 'You have been fired for ' Being bad at repairs, and not repairing the ship fully.' You sob. ")
        else:
            print("You found no parts. You return home and see the pink slip. It reads 'Termination Notice : Employee Terminated For Not Correctly Repairing Satellite.' You sob.")
        if Triva_Random == 3:
            print("When was the AT&T monopoly broken up?")
            Triva_Answer = input()
            if Triva_Answer == '1982':
                print("CORRECT!")
                print("You return to earth, AND FINALLY GET YOUR PAYCHECK!!! And then you see a pink slip reading 'You have been fired for ' Being bad at repairs, and not repairing the ship fully.' You sob. ")
            else:
                print("You found no parts. You return home and see the pink slip. It reads 'Termination Notice : Employee Terminated For Not Correctly Repairing Satellite.' You sob.")



START() 

    