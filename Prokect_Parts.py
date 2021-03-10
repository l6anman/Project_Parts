import time 
import random
print("Hello!")
time.sleep(2)
print("Welcome to Project Parts, the game where you help AT&T fix their satellites!")
time.sleep(2)
print("DISCLAIMER : This is for school, and this product that AT&T is using is a product we are 'giving' to them")
class hell_please_save_me_from_coding_lol():
    def START():
        print("You've been sent to Mars, to find parts to repair the new satellites that gives everyone AT&T service! ")
        time.sleep(0.5)
        print("The rocket blows dust everywhere. There's a sea of rust and red. You go out, on a mission")
        time.sleep(0.5)
        print("Your ready for your mission, and your paycheck")
        help_me.FIND_PART()
    def FIND_PART():
        where_to_find = input("Where do you look for parts? The Junkyard, The Field, or the area near your rocket? USE NO CAPS AND DO use spacebar (where your searching) and then no spacebar.")
        if where_to_find == ' the junkyard':
            print("You look around, and then out of the blue-")
            time.sleep(0.5)
            help_me.TRIVA()
        if where_to_find == ' the field':
            print("You look around, but then out of the blue-")
            time.sleep(0.5)
            help_me.TRIVA()
        if where_to_find == ' near my rocket':
            print("You literally see nothing because why would there be something near your rocket?")
            help_me.FIND_PART()
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
                Conculsion()
            else:
                Conculsion()
                print("You found no parts. You return home and see the pink slip. It reads 'Termination Notice : Employee Terminated For Not Correctly Repairing Satellite.' You sob.")
            if Triva_Random == 3:
                print("When was the AT&T monopoly broken up?")
                Triva_Answer = input()
            if Triva_Answer == ' 1982':
                print("CORRECT!")
                print("You return to earth, AND FINALLY GET YOUR PAYCHECK!!! And then you see a pink slip reading 'You have been fired for ' Being bad at repairs, and not repairing the ship fully.' You sob. ")
                help_me.Conculsion()
            else:
                print("You found no parts. You return home and see the pink slip. It reads 'Termination Notice : Employee Terminated For Not Correctly Repairing Satellite.' You sob.")
                help_me.Conculsion()
            if Triva_Random == 4 or 5 or 6 or 7 or 8 or 9 or 10:
                Triva_Answer = input("When was Alexander Graham Bell born?")
                if Triva_Answer == ' 1847':
                    print("You return to earth, AND FINALLY GET YOUR PAYCHECK!!! And then you see a pink slip reading 'You have been fired for ' Being bad at repairs, and not repairing the ship fully.' You sob. ")
                    help_me.Conculsion()
                else:
                    print("You found no parts. You return home and see the pink slip. It reads 'Termination Notice : Employee Terminated For Not Correctly Repairing Satellite.' You sob.")
                    help_me.Conculsion()
    def Conculsion():
        print("This game was based off of the satellites that would go around Mars in 2030. They are created in order to service customers on Mars and other planets in the growing market that will be the colonists of Mars, the Moon, Venus, and others. The design inculdes a docking port, a small area where a technician can live, solar panels, a long range connecter, a small emergency oxygen producer, and a emergency signal producer. These will help AT&T establish a foothold in a market where no Internet servicer has gone before!")
help_me = hell_please_save_me_from_coding_lol()
help_me.START(hell_please_save_me_from_coding_lol)

