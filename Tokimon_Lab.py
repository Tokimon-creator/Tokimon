from Tokimon_save_file import load_game, save_game
import time
global request, check
print("\nSigning into Tokimon Lab!")
time.sleep(2)
def Tokimon_Lab():
    team, box, progress = load_game()
    check = input("Right now in this very moment your team is " + str(team) + "Correct? if not press \"b\"")
    if check == "b":
        print("Oh dear well then, please reboot!")
    else:
        request = input("Ok so choose a Tokimon you have in your box by typing in for example if you're are trying to send in \"Tichu\" then type in \"Tichu\"")    
        if request in box:
            print("Great!")
            if len(team) >= 6:
                i_love_Pichu_SOMUCH = input("Oh dear looks like you have too many Tokimon! Choose a Tokimon to replace!" + str(team))
                if i_love_Pichu_SOMUCH in team:
                    team.remove(i_love_Pichu_SOMUCH)
                    box.append(i_love_Pichu_SOMUCH)
                    box.remove(request)
                    team.append(request)
                    save_game(team, box, progress)
                    return
            else: 
                box.remove(request)
                team.append(request)    
                save_game(team, box, request)
                print("Thank you for making a transaction at Tokimon Lab!")
                return
        else:
            print(f"Hmmm it seems you don't have this Tokimon \" {request} \"")
            Tokimon_Lab()        
Tokimon_Lab()            