#References
#https://ascii.co.uk/ - some of the ascii art seen here
#https://www.asciiart.eu/ - other ascii art seen here
#https://stackoverflow.com/questions/19911346/create-a-typewriter-effect-animation-for-strings-in-python?lq=1 - typewriter effect seen in the game
#https://www.geeksforgeeks.org/global-keyword-in-python/ - global keyword
#https://www.w3schools.com/python/python_functions.asp - function

#Special thanks to
#https://www.youtube.com/watch?v=4m8LLfLXvMM - Do you know da wae
#https://www.ascii-art-generator.org/ - picture to ascii generator

#Orrin Uy
#Andrei Ang
#STEM11-G


import time
import sys

#let your response be
ansA = ["A", "a", "A.", "a."]
ansB = ["B", "b", "B.", "b."]
ansC = ["C", "c", "C.", "c."]
ansD = ["D", "d", "D.", "d."]
yes = ["yes", "Yes", "YEs", "YeS", "YES", "yEs", "yES", "yeS", "Y", "y"]
no = ["no", "No", "NO", "nO", "n", "N"]

#story variables
lever = 0
potion = 0
mystkey = 0
HEgear = 0
bird = 0
cage = 0
saber = 0
archer = 0
druid = 0
monk = 0
#invalid, duh
invalid = ("\nUse only A or B\n")
invalid2 = ("\nYes or No only\n")

def typewriter(txt):
    for y in txt:
        print(y, end="")
        sys.stdout.flush()
        time.sleep(0.2)       

def typewriter2(narr):
    for r in narr:
        print(r, end="")
        sys.stdout.flush()
        time.sleep(0.04)

def dramatic(drama):
    for d in drama:
        print(d, end="")
        sys.stdout.flush()
        time.sleep(0.5)
        
def start():
    global playername
    playername = input("Enter player name: ")
    
    typewriter2("\nHello, ")
    typewriter2(playername)
    typewriter2(". The game will load soon, kakugo shinasai.\n\n")
    typewriter("...")
    typewriter("\n..")
    typewriter("\n.\n\n")
        
    time.sleep(1)
    intro()
#section 1: slime or human
def intro():
    print("8b        d8                                 88 88                     88")
    print(" Y8,    ,8P                                  88 ''                     88")
    print("  Y8,  ,8P                                   88                        88")
    print("   '8aa8' ,adPPYba,  88       88     ,adPPYb,88 88  ,adPPYba,  ,adPPYb,88")
    print("    `88' a8'     '8a 88       88    a8'    `Y88 88 a8P_____88 a8'     `Y8")
    print("     88  8b       d8 88       88    8b       88 88 8PP''''''' 8b       88")
    print("     88  '8a,   ,a8' '8a,   ,a88    '8a,   ,d88 88 '8b,   ,aa '8a,   ,d88")
    print("     88   `'YbbdP''   `'YbbdP'Y8     `'8bbdP'Y8 88  `'Ybbd8''  `\8bbdP'Y8")

    time.sleep(1)

    typewriter2("\n\nGreetings, ")
    typewriter2(playername)
    typewriter2(".")
    typewriter2("\n\nIt is I, Voice-in-your-head, welcome to your subconscious.")
    typewriter2("\nIt's pretty comfy in here, all the patches of void aside.")
    typewriter2("\nWhat were you here for again?")
    typewriter2("\nOh... right...\n")
    typewriter2("\nCongratulations! You have won a new iPhone 11!")
    dramatic("\n...")
    typewriter2("\nI mean another chance at life in a fantasy world!")
    typewriter2("\nThis time, however, you get to choose your race!")
    typewriter2("\nAlthough")
    dramatic("...")
    typewriter2(" you only get to choose between two races... \nSo, what'll it be?\n")
    
    
    time.sleep(.2)
    print("""A.Slime \nB.Human""")
    race = input(">>> ")

    if race in ansA:
        typewriter2("\nA mighty fine choice, ")
        typewriter2(playername)
        typewriter2(".")
        slimemeadow()

    elif race in ansB:
        typewriter2("\nSo you like a sense of familiarity, ")
        typewriter2(playername)
        typewriter2(".")
        humanrace()

    else:
        print(invalid)
        intro()
        
#section 2: slime - part 1 - spawn
def slimemeadow():
    time.sleep(.3)
    print("\n\n      wWWWw               wWWWw         ")
    print("vVVVv (___) wWWWw         (___)  vVVVv  ")
    print("(___)  ~Y~  (___)  vVVVv   ~Y~   (___)  ")
    print("~Y~   \|    ~Y~   (___)    |/    ~Y~    ")
    print(" \|   \ |/   \| /  \~Y~/   \|    \ |/   ")
    print("\\|// \\|// \\|/// \\|//  \\|// \\\|/// ")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    time.sleep(.3)
    typewriter2("Nice meadow we got here, don't you think so?")
    print("\n*Yes or No*")
    useless = input(">>> ")
    if useless in yes:
        typewriter2("\n\nYes... really nice")
        dramatic("\n...")
        slimelever()
    elif useless in no:
        typewriter2("\n\nI'm literally the voice in your head, yet you're disagreeing with me...")
        dramatic("\n...")
        slimelever()
    else:
        print(invalid2)
        slimemeadow()

def slimelever():
    typewriter2("\nDo you see that lever over there, ")
    typewriter2(playername)
    typewriter2("?")
    typewriter2("\nY/N")
    useless = input("\n>>> ")
    if useless in yes:
        typewriter2("\n\nYou reckon it does something?")
        typewriter2("\n\n**You approach the lever")
        slimelever2()
    elif useless in no:
        typewriter2("\n\nDude... on *our* right.")
        typewriter2("\n\n**You see the lever and start to approach it")
        slimelever2()
    else:
        print(invalid2)
        slimelever()

def slimelever2():
    typewriter2("\n\nAre *we* gonna ")
    dramatic("*gasps*...")
    typewriter2(" flip it?")
    typewriter2("\nY/N")
    choice = input("\n>>> ")
    if choice in yes:
        typewriter2("\n\n**You quickly flipped the lever")
        typewriter2("\n\nDid you even think about how you could have killed us just now?")
        global lever
        lever = 1
        narrative1()
    elif choice in no:
        typewriter2("\n\n**You backed away from the lever")
        typewriter2("\n\nWhat if the lever gave *us* powers or something? Didn't think of that, did you?")
        lever = 0
        narrative1() 
    else:
       print(invalid2)
       slimelever2()

def narrative1():
    dramatic("\n...")
    time.sleep(.7)
    typewriter2("\nHey")
    time.sleep(.5)
    typewriter2("\nHey")
    time.sleep(.5)
    typewriter2("\nHey, listen.")
    typewriter2("\nEat a flower.")
    typewriter2("\nYou're a slime, just do it.")
    typewriter2("\n\n**You 'eat' the flower")
    typewriter2("\n\n%ANALYZING FLOWER CONTENT%")
    time.sleep(1)
    typewriter2("\n%CRAFT HEALTH POTION NOW AVAILABLE%")
    slimepotion()

def slimepotion():
    typewriter2("\n\n**Will you craft the potions?\n")
    typewriter2("Y/N\n")
    choice = input(">>> ")
    if choice in yes:
        typewriter2("\nLike a true adventurer, huh")
        dramatic("\n...")
        typewriter2("\nAdventurer slime, I mean")
        typewriter2("\n\n%x99999 HEALTH POTIONS CRAFTED%")
        typewriter2("\n**You put them in your inventory")
        global potion
        potion = 1
        slimetravel()
    elif choice in no:
        typewriter2("\nConserving resources already I see")
        potion = 0
        slimetravel()
    else:
        print(invalid2)
        slimepotion()

#section 4: slime-part3 - travel 
def slimetravel():
    typewriter2("\n\n**You decide that eating flowers all day won't do you good anymore")
    typewriter2("\n**You proceed to travel around without a destination in mind\n")
    dramatic("\n...")
    dramatic("\n...")
    typewriter2(playername)
    typewriter2(", look to your right! It's a dungeon!")
    time.sleep(.5)
    print("\n")    
    print(" .  \   \ .   |   | ||  / \     / \ II / \     / \  || |   |   .     \    / ")
    print("    /    .  . |   | || /   \   /   \||/   \   /   \ || |   |      .     \   ")
    print("     .   \    |   | ||/     \ /     ||     \ /     \|| |   |     \    /     ")
    print(" /         .  |   | ||       X      ||      X       || |   | /       \  .   ")
    print("    .  /  .   |   | ||\     / \     ||     / \     /|| |   |     .     \  . ")
    print("              |   | || \   /   \   /||\   /   \   / || |   | \      /   .   ")
    print(".      .   /  |   |_||  \ /     \ / || \ /     \ /  ||_|   |    .     \    .")
    print("  \     \  ,  |   |~||   X       X  ||  X       X   ||~|   |   /   .     \  ")
    print("    .     .   |   | ||  / \     / \ || / \     / \  || |   |    .   \   .   ")
    print("  .    /    \ |   | || /   \   /   \||/   \   /   \ || |   | \     .   /  . ")
    print("    .     .   |   | ||/     \ /     ||     \ /     \|| |   |  .       .     ")
    print("       /      |   | ||       X      ||      X       || |   |    \        /  ")
    print("  /   .       |   | ||\     / \     ||     / \     /|| |   | .      /   .   ")
    print(".          \  |   | || \   /   \   /||\   /   \   / || |   |   .  .         ")
    print("    .    .    |   | ||  \ /     \ / || \ /     \ /  || |   |          .     ")
    print("      /       |   | ||   X       X  ||  X       X   || |   | . / .      \   ")
    print("  \        .  |   | ||  / \     / \ || / \     / \  || |   |        \       ")
    print("   . \   /    |   | || /   \   /   \||/   \   /   \ || |   |   .         /  ")
    print(".    .    .   |   | ||/     \ /    /||\    \ /     \|| |   |     \.    .    ")
    print("              |   |_||       X    / II \    X       ||_|   |  .     .   /   ")
    print("==============|   |~II~~~~~~~~~~~~~~OO~~~~~~~~~~~~~~II~|   |==============\n")
    time.sleep(1)
    typewriter2("\n\nNow, look to your left! It's a village!")
    time.sleep(.5)
    print("\n      ~         ~~          __")
    print("       _T      .,,.    ~--~ ^^")
    print(" ^^   // \                    ~")
    print("      ][O]    ^^      ,-~ ~")
    print("   /''-I_I         _II____")
    print("__/_  /   \ ______/ ''   /'\_,__")
    print("  | II--'''' \,--:--..,_/,.-{ },")
    print("; '/__\,.--';|   |[] .-.| O{ _ }")
    print(":' |  | []  -|   ''--:.;[,.'\,/")
    print("'  |[]|,.--'' '',   ''-,.    |")
    print("  ..    ..-''    ;       ''. '")

    time.sleep(.4)
    slimedv()

def slimedv():
    typewriter2("\nSo, what say you? Where do we go?\n")
    print("A. Dungeon \nB. Village")
    choice = input(">>> ")
    if choice in ansA:
        if lever == 1:
            slimedungeon()
        elif lever == 0:
            typewriter2("\n**You make your way to the dungeon but the doors are closed shut! You try to move it but it just won't budge")
            typewriter2("\n*We* should try the village instead.")
            slimevillage()
        else:
            print("Error")
    elif choice in ansB:
        slimevillage()
    else:
        print(invalid)
        slimedv()

#section 5b: slime - part4b - village
def slimevillage():
    typewriter2("\n**You start heading to the village in hopes there will be something there")
    typewriter2("\n**You find a dead body")
    typewriter2("\n**As disgusting as it is, you close your eyes and start 'eating' it as per instruction from Voice-in-your-head")
    typewriter2("\n\n%SHAPESHIFT ABILITY AQUIRED%")
    typewriter2("\n%YOU CAN NOW SHAPESHIFT INTO A MURLOC!%")
    typewriter2("\n\nNeat! But, what in the world is a Murloc?")
    typewriter2("\nYou think I should know this?")
    typewriter2("\nDo I look like I'm all knowing?")
    typewriter2("\nYeah, I thought so!")
    typewriter2("\n\n**You arrive in the village only to find murlocs**")

    time.sleep(.5)
    print("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOdONMMMWMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMM")
    print("MMMMMMMMWX0KXNWMMMMMMMMMMMMMMMMMNkld0XK0XWMMMMMMMMMMMMMMMNk0WMMMMMMMMMMMMMM")
    print("MMMMMMMMMN0xodkO0XWMMMMMMMMMMMMMMXxloxxdoONMMMMMMMMMMMMMMNdl0WMMMMMMMMMMMMM")
    print("MMMMMMMMMMMWXkdoodONMMMMMMMMMMMMMMXxoldxolkNMNKKNWMMMMMMMXxcl0WMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMWXOxddkXWMMMMMMMMMMMMWKdodOOddKWNOoodONWMMMMXkl:kWMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMWX0kxkKWMMMMMMMMMMMMN0xxOXKk0WWNkocl0KKWMMNOlo0WMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMWN0xxOXWMMMMMMMMMMMNKkxKW0kXMWXkod0kxXMMW0dOWMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMWKxdx0NMMMMMMMMMMWWKxkX0xKMMWKdoOko0WMNOkXMMMNNWMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMWXkodxkXWMMMMMMMMMWXkdO0d0WMNOocoxd0WW0x0WMMM0kXMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMN0xdddxxONWMMMMMMMMNOdxkdkNWKdolldkKWKdxXMMMNxl0MMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMWNXOoood0WMMMMMMMWKxdocdXXxcoxodkXXxd0WMMMKdcOMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMWKdlooxKWMMMMWMNkol:okdc:xOxdkOdlONMMMW0ooKMMMMMMMM")
    print("MMMMMMMMMMMWWMMMMMMMMMMMMMNkll:ckNMMMMMMKdoc::::l0KkddlcxNMMMMWOd0WMMMMMMMM")
    print("MMMMMMMMN0kxkO0XWWMMMMMMMMMW0o:,;l0NMMMWKdc:;::cdK0xdl:xXMMMMN0kKWMMMMMMMMM")
    print("MMMMMMMMNKOOkkkkO0XNWMMMMMMMWXx:,,:dKXXKOxl,,lOOkdodl;oKWMMMWOd0WMMMMMMMMMM")
    print("MMMMMMMMMMMMMWWNX0kk0XWMMMMMMMXd:;;l0XNXXXOl:xKXK0xolxNMMMMWKdkNMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMWNKkxk0XWMMMMXxxxkXNNNKKXX0O0KXXXxlo0WMMWKxdxKWMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMWKkooxONWN0ddox00O000KXXXXXNNKdcd0KK0xlox0WMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMWXkl:ck0Okxkdc:;:::oxxk0XNXKxcx0dc:cldONMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMWXkdOKKKXXOdoodxollddoxKNNXKKXkl:ccxNMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMWXXX0OOO0KKKKKX0doddooOWWNNWNXkc,lXMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMWNNXXKK0kk0K0OOOOO0klclxxoloOXNKxoo0WMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMWNWWWNNXXXXK0kxxkOOkO0O0XOl::cllc;xNWXK00XWMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMWKkxkKXXXXXXK0OOkddxkOKK00Kk;,ckNXd'lNWNXKKKKNMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMWKkk0KKKK00000OkkkkkxdOK0O0Xk;':dkd;;xNWWNNXKKXWMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMWWWMWX0OOOOkxkkOO0KOxdO0OkkKKo,;::cdddOWWWNXK0KXWMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMNOddddollclollxdokOxdkO0KXK00XWWNXXNWKO0KK0OKWMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMNOollc:::clllc;;::ldooodxxxkO0KKKK00KXKKKKXX0OOKWMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMWk::lllloxO00o;',;::codoccoolloxxoxxoOkldOkxkxk0NMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMXdoO00OO0XKx:,,,;;:ccllloodddoxdcxO:oxcdkodxxO0WMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMX0KKKO0XXOdocccllooolc:lddooooddddlxKo:xxxkxk0NMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMNK0K0OKXOxxdddollccc:;,;lxxdoolooooddookxddONMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMWKOO0Ok00dooldo:;cllokkxkKK0OxxxddoolllldkxkKMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMX0OOkxdxo:cldOkc:ldxxkOOO0OkxkxollcddccdkkxONMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMKOKK0Okoc:cdkOxdxOO00000OOOOOOkxxddOXkcodoxKWMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMWKO0KXXXKxodxkxoOWMMMWWNX0kkkO00KK0kdxO0KkoOXXWMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMN0OkkO000dloocdXMMMMMMMWNX0kxxkOO00kook0dd0K00NMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMWXK00Okxxdolcl0MMMMMMMMMMMWNKkxdxxxkdcloldKKdoKMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMX00XX0koodddONMMMMMMMMMMMMNKOxlloolc::ccd00xdKMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMNOxkO0K0kooddKMMMMMMMMMMMMNOkxooodoc;:c::oOkxkNMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMKdxK0xxOOxdxONMMMMMMMMMMMNkoxkOOOkdclxOo;lkxdONMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMNxd0KxdxddxkOXWMMMMMMMMMMWOccdxkkxooxKWM0ccddoONMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMM0okOxxOkdoodk0XNNWWWWMMMW0occcloodkXWMMMWk:lox0WMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMNxdkxkK0kxdooodxxkkOOOOOOkdl:ccokKNWMMMMMMXo:dOKWMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMKddxOXKOO0K0dlodddddddolc:::;;:o0WMMMMMMMMWOco0XWMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMWOdkOXX00NWMNkodkkoddddoc:cccclx0NMMMMMMMMMKocokXMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMXxdOKX0KNMMMWKxx0Kkdxxdoclxkxkkkk0XXXXNNWW0oclodKMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMM0dk00KXNMMMMMNkok0Oxxkxdlodkkkxdocc::;:cooccoood0WMMMMMMMMMM")
    print("MMMMMMMMMMMMMMNkxO00NWMMMMMMWOcclddoxkkxocldoololc;'.,cololccclOWMMMMMMMMMM")
    print("MMMMMMMMMMMMMW0dx0O0NMMMMMMMMNdccclooddol:;;,,',:oxo:,cxxl:;;::oKWMMMMMMMMM")
    print("MMMMMMMMMMMMMNkdkO0OKMMMMMMMMMXkolclodddddo;''''';cldxxl;,,'',lOXWMMMMMMMMM")
    print("MMMMMMMMMMMMW0ddxkOk0WMMMMMMMMMW0ol::lkNWWNOdolldkd::oxdcloc;:OWMMMMMMMMMMM")
    print("MMMMMMMMMMMMXxodoodkkOKXWMMMMMMMW0dlc::lKMMMWWNNWWNK0Oxdk0XXKXWMMMMMMMMMMMM")
    print("MMMMMMMMMMMMKolo:;;coddlcokKNMMMMWXOkkxkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMKl:l::;,,:lc'.;:ldOKNWMWWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMWKd;dXXXKo,;loc;dKOl;:dkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMXOxdc,oNMMMKc;cdxccKWNxd0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMN00OkxkXMMMWKd::l:;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMWX0OkONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")

    time.sleep(.5)
    typewriter2("\n\n**You proceed into the village using your shapeshift ability to blend in")
    typewriter2("\n**The murlocs start gathering around you in a circle")
    typewriter2("\n\nWOAH! Calm down, calm down. This is nothing to be worried about.")
    typewriter2("\nI mean, *we* are in shapeshift form")
    typewriter2("\nHold up")
    dramatic("...")
    typewriter2(" is that a crown?")
    typewriter2("\n\n*We're* the king?")
    typewriter2("\n*We're* KING!")
    typewriter2("\n\n**Murloc Messenger: Mgmlrgmlmmmrgl mgrlml mgrllg")
    typewriter2("\n\n*Ahem* Let me translate that for you.")
    typewriter2("\n'There is a human on their way to the village, what is our plan Your Majesty?'")
    typewriter2("\nIs what it's trying to tell you.")
    typewriter2("\n\nBased on the information I have here, it seems that humans, especially younger lower level ones, tend to kill murlocs for loot drops")
    typewriter2("\nSeeing as *we* are royalty here, *we* should defend *our* new base")

def murlocarmy():
    typewriter2("\nDo you want to defend *our* new base?")
    typewriter2("\nY/N\n")
    choice = input(">>> ")
    if choice in yes:
        typewriter2("\n*We're* on the same page... Good.")
        typewriter2("\nTime to recruit some more murlocs then!")
        typewriter2("\n\n**A few murloc hours later...")
        typewriter2("\n\nTHE CAVALRY IS HERE!")
        typewriter2("\nAnd so is the human.")
        slimevillage2()
    elif choice in no:
        typewriter2("\nYeah no. *We* are defending this whether you want to or not.")
        typewriter2("\nAnyways, time to recruit more murlocs!")
        typewriter2("\n\n*A few murloc hours later...\n\n")
        typewriter2(playername)
        typewriter2(", I trust you with this now.")
        typewriter2("\nOur backup has arrived but so has the human. I believe in you!")
        slimevillage2()

def slimevillage2():
    typewriter2("\n\n**You approach the human at the village entrance.")
    typewriter2("\n\nYou (in Nerglish): Hello, human! We mean you no harm. In fact, we wish to secure a peaceful relationship with you.")
    typewriter2("\nHuman: *tilts their head in confusion*")
    typewriter2("\nI don't he understands *us*, mate.")
    typewriter2("\nHuman: *slashes you with his rusty sword*")
    typewriter2("\n\n**You start losing consciousness")
    typewriter2("\n\nThat was a deep, clean cut, mate. Amazing.")
    dramatic("\n...")
    if potion == 1:
        typewriter2("\n\nDRINK YOUR POTIONS!")
        time.sleep(.2)
        print("\n   _____   ")
        print("  `.___,'  ")
        print("   (___)   ")
        print("   <   >   ")
        print("    ) (    ")
        print("   /`-.\   ")
        print("  /     \  ")
        print(" / _    _\ ")
        print(":,' `-.' `:")
        print("|         |")
        print(":         ;")
        print(" \       / ")
        print("  `.___.'  ")
        time.sleep(.3)
        typewriter2("\n\n**You reach for your chest to get a potion from your wonderful unlimited inventory")
        typewriter2("\n**You drink your potion and heal up completely")
        typewriter2("\n**But the human slashes you down almost immediately")
        typewriter2("\n**You start drinking potions as soon as the human slashes you")
        typewriter2("\n**With your endless amount of potions, you think to yourself: 'I can do this all day'")
        typewriter2("\n**Your murloc army general sees the opportunity to strike down the human and orders the army to attack")
        typewriter2("\n**You have been saved from the repeated process of barely dying thanks to your army")
        typewriter2("\n**A celebration of murloc proportions is called for")
        typewriter2("\n**Word spreads of the deeds of")
        typewriter2(playername)
        typewriter2(" and their army.")
        typewriter2("\n**Eventually, ")
        typewriter2(playername)
        typewriter2("'s army grew to be unstoppable even by the united front of the world")    
        end1()
    elif potion == 0:
        typewriter2("\n\n**You watch your army try to fight the human as you slowly lose consciousness and die")
        end2()

#section 5a: slime - part 4a - dungeon
def slimedungeon():
    time.sleep(.5)
    print("       _________________________________________________________")
    print(" /|     -_-                                             _-  |\ ")
    print("/ |_-_- _                                         -_- _-   -| \ ")  
    print("  |                            _-  _--                      | ")
    print("  |                            ,                            |")
    print("  |      .-'````````'.        '(`        .-'```````'-.      |")
    print("  |    .` |           `.      `)'      .` |           `.    |")        
    print("  |   /   |   ()        \      U      /   |    ()       \   |")
    print("  |  |    |    ;         | o   T   o |    |    ;         |  |")
    print("  |  |    |     ;        |  .  |  .  |    |    ;         |  |")
    print("  |  |    |     ;        |   . | .   |    |    ;         |  |")
    print("  |  |    |     ;        |    .|.    |    |    ;         |  |")
    print("  |  |    |____;_________|     |     |    |____;_________|  |")
    print("  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |")
    print("  |  |  / __  ()        -|        -  |  /  __--      -   |  |")
    print("  |  | /        __-- _   |   _- _ -  | /        __--_    |  |")
    print("  |__|/__________________|___________|/__________________|__|")
    print(" /                                             _ -        lc \ ")
    print("/   -_- _ -             _- _---                       -_-  -_ \ ")
    time.sleep(.5)
    typewriter2("\nNeat dungeon we have here")
    typewriter2("\nI bet you could find all sorts of materials and monsters here.")
    slimedungeon2()
          
def slimedungeon2():
    typewriter2("\nWanna explore? I bet we can get super strong here.")
    typewriter2("\nI'm talkin' Goku level.")
    typewriter2("\nY/N")
    useless = input("\n>>>")
    if useless in yes:
        typewriter2("\nAwesome, it's training time!")
        slimetraining()
    elif useless in no:
        typewriter2("\nWhaddaya mean no? *We* are gonna explore this dungeon and YOU ARE GONNA LIKE IT.")
        slimetraining()

def slimetraining():
    typewriter2("\n\n**You go around the dungeon")
    typewriter2("\n**You find many monsters, some weak, some extremely strong.")
    typewriter2("\n**Thanks to how the dungeon was designed, however, enemies only got stronger the further you are in the dungeon")
    typewriter2("\n\nWoah, *we* are crazy strong now! *We're* like Saitama, but we have hair!")
    typewriter2("\n\n**You explore even further until you reach a deadend")

    time.sleep(.2)
    print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
    print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
    print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
    print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
    print("_|___|___|___|___|___|___|___|xxx|___|___|___|___|___|___|___|___|___|")
    print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
    print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
    print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
    print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
    print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
    time.sleep(.2)
    dramatic("\n\n...")
    typewriter2("\nSubtle")
    dramatic("\n...")
    typewriter2("\n**You push the 'secret' entrance open")
    dramatic("\n\n...")
    typewriter2("\nIt's so dark in here")
    typewriter2("\nAnd why do I hear boss music?")

    typewriter2("\n\n???: Allow me to fix that for you\n\n")

    time.sleep(.5)
    print("######################~~..'|.##############.|`..~~#######################")
    print("##############~./`.~~./' ./ ################ \. `\. ~~.`\.~##############")
    print("############~.' `.`-'   /   ~#############~ .  \   `-'.'  `.~############")
    print("##########~.'    |     |  .'\ ~##########~ /`.  |     |     `.~##########")
    print("########~.'      |     |  |`.`._ ~####~ _.'.'|  |     |       `.~########")
    print("######~.'        `.    |  `..`._|\.--./|_.'..'  |    .'         `.~######")
    print("####~.'            \   | #.`.`._`.'--`.'_.'.'.# |   /             `.~####")
    print("##~.'       ......  \  | ###.`~'(o\||/o)`~'.### |  /  ......        `.~##")
    print("~.`.......'~      `. \  \~####  |\_  _/|  ####~/  / .'      ~`........'.~")
    print(";.'                 \ .----.__.'`(n||n)'`.__.----. /                   `;")
    print("`.                  .'    .'   `. \`'/ .'   `.    `.                   .'")
    print("#:               ..':      :    '. ~~ .`    :      :`..                :#")
    print("#:             .'   :     .'     .'  `.     `.     :   `.              :#")
    print("#:           .'    .`   .'       . || .       `.   '.    `.            :#")
    print("#:         .'    .' :       ....'      `....       : `.    `.          :#")
    print("#:       .'    .' ) )        (      )     (      (    )`.    `.        :#")
    print("#:     ..'    .  ( ((   )  ) )) (  ((  (  ))  )  ))  ((  `.   `..      :#")
    print("#:  ..'      .'# ) ) ) (( ( ( (  ) ) ) ))( ( (( ( (  ) ) #`.     `...  :#")
    print("#;.'        .'##|((  ( ) ) ) ) )( (  (( ( ) )) ) ) )( (||##`.        `.:#")
    print("#`.        .'###|\__  )( (( ( ( )  )  )) )  (  (( ( )_)/|###`.        .'#")
    print("##.`       '#####\__~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~__/#####`       '.##")
    print("###        #######  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #######        ###")
    time.sleep(.5)
    typewriter2("\n**You freak out to the point you would have peed yourself if you were a human.")
    time.sleep(.5)
    typewriter2("\n\n%FIGHT OR FLIGHT MODE ACTIVATED%")
    typewriter2("\n%POWERING UP%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%BOOST!%")
    typewriter2("\n%AUTO-PILOT ENGAGED%")
    typewriter2("\n\n**You lose control of your body due to your auto-pilot skill")
    typewriter2("\n\nWhy do I hear the One Punch Man opening 1 now?")
    typewriter2("\n**Your body swiftly moves in towards the monster")
    typewriter2("\n**Your hand starts to form a fist and your arm prepares for a punch")
    typewriter2("\n**Your body jumps towards the massive monster in front of you")
    typewriter2("\n**Your body suddenly shifts mid-air")
    typewriter2("\n**You roundhouse kick the monster to oblivion")
    typewriter2("\n\nWhat... why... how...")
    dramatic("\n...")
    typewriter2("\nYEAAA WE BEAT IT!")
    typewriter2("\nNow eat it.")
    typewriter2("\n\n**You eat the monster and gain abilities beyong human comprehension.")
    typewriter2("\n\nCheers for plot armor!")
    typewriter2("\n\n**You find your way out the now empty dungeon.")
    typewriter2("\n**You unknowingly emit an incredible aura felt all throughout the world causing them to fear and attack you on sight.")
    typewriter2("\n**Through countless battles, you gained even more strength.")
    typewriter2("\n**Eventually the whole world kneels before you.")
    end1()

#section 6 HUMAN
def humanrace():

    time.sleep(1)
    print("\n\n__________________ §§")
    print("__________________ §§")
    print("__________________ §§")
    print("__________________ §§")
    print("__________________ §§")
    print("__________________ §§")
    print("__________________ §§")
    print("_________________ §§§§")
    print("________________ §§§§§§")
    print("_______________ §§§___§§")
    print("______________ §§_§§§§§§")
    print("______________ §§§_§_§§§§")
    print("_____________ §___§§§§§§§")
    print("____________ §§§§________§")
    print("____________ §§ §§§§§§§§§§§")
    print("___________ §§_________§§§§")
    print("___________ §§__§_§§§§____§")
    print("__________ §§___§_§§§§_§__§")
    print("__________ §§§§§§_§§___§__§")
    print("__________ §§§§§§§§§§§§§§§§")
    print("__________ §§___________§ §§§")
    print("_________ §§___§_______§___§§")
    print("_________ §§___§_§_§§__§______§§")
    print("______ §§_________________§___§§")
    print("_____ §§§§§§§§§§§§_§§___________§")
    print("_____ §§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    print("_____ §_§§_§__§_§§_§§_§_§§_§§_§_§§§§§§§§")
    print("____ §§_§§_§__§_§§_§§_§_§§_§§_§_§_§§§§§§")
    print("____ §§_§§_§__§§§§§§§§§§§§§§§§__§_§§§§§§")
    print("____ §§_§§_§_§________$_______§_§_§§§§§§")
    print("___ §§§_§§_§_§___________§____§_§_§§§§§§")
    print("__ §§§§_§§_§_§_____§____§_____§_§_§§§§§§")
    print("_ §§§§§_§§_§_§______§__§______§_§_§§§§§§")
    print("_ §§§§§_§§_§_§$______$$______$§_§_§§§§§§")
    print("_ §§§§§_§§_§_§________________§_§_§§§§§§")
    print("_ §§§§§_§§_§_§________________§_§_§§§§§§")
    print("_ §§§§§_§§_§_§________$_______§_§_§§§§§§")
    print("_ §§§§§_§§_§__§§§§§§§§§§§§§§§§__§_§§§§§§")
    print("_ §§§§§_§§_§___§__§__§__§__§____§_§§§§§§")
    print("_ §§§§§_§§_§___§__§__§__§__§____§_§§§§§§")
    print("_ §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    print("§§§§§§ _§_§§_§§_§§_§§_§§_§§_§§_§§_§§")
    print("_ §§§§§_§_§§_§§_§§_§§_§§_§§_§§_§§_§§")
    print("_ §§§§§_§_§§_§§_§§_§§_§§_§§_§§_§§_§§")
    print("_ §§§§§_§_§§_§§_§§_§§_§§_§§_§§_§§_§§")
    print("_ §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    print("_ §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    print("§§§§§§ __§§_____§__§_____§__§__§§_§§")
    print("§§§§§§ __§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    print("§§§§§§ __§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    print("§§§§§§ __§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")
    print("_ §§§§§__§§_____§__§_____§__§__§§_§§")

    time.sleep(.5)
    typewriter2("\n\nRemember that anime called Sword Art Online? The bad one, not gun gale alternative.")
    typewriter2("\nYeah, I'm getting that kind of vibe right now.")
    typewriter2("\nFirst step though, is to choose a class...")
    humanclass()

def humanclass():
    typewriter2("\nPick one you like:")
    typewriter2("\nA. Saber (DPS)")
    typewriter2("\nB. Archer (DPS)")
    typewriter2("\nC. Druid (Support/Healer)")
    typewriter2("\nD. Monk (Tank)\n")

    option = input(">>> ")
    if option in ansA:
        typewriter2("\n\nGood choice! As a saber, you can deal quite a bit of damage and you can also tank some strong hits.")
        global saber
        saber = 1
        humanrace2()
    elif option in ansB:
        typewriter2("\n\nAre you Legolas? As an archer, you're ability to output damage is exceptional. Although, you can't take too many hits")
        global archer
        archer = 1
        humanrace2()
    elif option in ansC:
        typewriter2("\n\nClassic fantasy class! As a druid, you can't take too many hits without healing, so you depend on others to take the damage for you.")
        typewriter2("\nDespite this though, your ability to heal others is phenomenal. You can even resurrect others!")
        global druid
        druid = 1
        humanrace2()
    elif option in ansD:
        typewriter2("\n\nWooah, didn't think anybody actually willingly picks that class! Anyways, as a monk, your ability to damage others is pretty mediocre at best.")
        typewriter2("\nBut, you can take quite a lot of hits. Pair that with a healer and all your self-healing, you'd be unkillable!")
        global monk
        monk = 1
        humanrace2()
    else:
        typewriter2("\n\nA, B, C, or D only")
        humanclass()

def humanrace2():
    typewriter2("\nAnywho, since we're in the starting town with beginner gear, why not join/form a party?")
    typewriter2("\n\n**Will you form a party?")
    typewriter2("\n**Y/N\n")
    choice = input(">>> ")
    if choice in yes:
        typewriter2("\nYeah, good choice. It's gonna be hard to do all this adventuring stuff alone when it's your first time.")
        humanpartyformed()
    elif choice in no:
        humansoload()
    else:
        print("Yes or No only")
        humanrace2()

#section 7 PARTAY
def humanpartyformed():
    typewriter2("\n\n**You form your party of five with other able adventurers, filling out the important roles such as the tank and healer.")

    if saber == 1:
        typewriter2("\nYour team:\n")
        typewriter2(playername)
        typewriter2(" - Saber(DPS)")
        typewriter2("\nEmiya - Archer(DPS)")
        typewriter2("\nMeteora - Mage(DPS)")
        typewriter2("\nRikka - Technician(Healer)")
        typewriter2("\nKorosensei - ???(Tank)")

        typewriter2("\n\nEmiya: We should get a move on.")
        typewriter2("\nRikka: I agree, getting stronger as soon as we can will help us alot")
        typewriter2("\nMeteora: We could also use the loot for money... I need a new grimoire after all.")
        typewriter2("\nKorosensei:")
        dramatic("...")
        humanparty2()
    elif archer == 1:
        typewriter2("\nYour team:\n")
        typewriter2(playername)
        typewriter2(" - Archer(DPS)")
        typewriter2("\n2B - Blademaster(DPS)")
        typewriter2("\nIllidan - Demon Hunter(DPS)")
        typewriter2("\nNurse Joy - Pokemon Nurse(Healer)")
        typewriter2("\nDeath - Death(Tank)")

        typewriter2("\n2B: YoRHa No.2 Type B at your service.")
        typewriter2("\nNurse Joy: Just get in the ball and I'll heal you!")
        typewriter2("\nDeath: Slay monsters, get stronger. Let's go already!")
        typewriter2("\nIllidan: WE ARE NOT PREPARED!")
        humanparty2()
    elif druid == 1:
        typewriter2("\nYour team:")
        typewriter2("\nChrissy Costanza - Lead Vocalist(DPS)")
        typewriter2("\nAimer - Pianist(DPS)")
        typewriter2("\nLindsey Stirling - Violin(DPS)\n")
        typewriter2(playername)
        typewriter2(" - Druid(Healer)")
        typewriter2("\nPat Kirch - Drummer(Tank)")
        typewriter2("\n\nWhat a weird bunch you have here.")

        typewriter2("\n\nAimer: ...")
        typewriter2("\nLindsey Stirling: *plays the violin like she's in a music video")
        typewriter2("\nPat Kirch: *too busy talking with his fans*")
        typewriter2("\nChrissy Costanza: *in game... it's League of Legends btw...")
        humanparty2()
    elif monk == 1:
        typewriter2("\nYour team:")
        typewriter2("\nSheldon Cooper - Theoretical Physicist(DPS)")
        typewriter2("\nMichael Bay - Explosion Enthusiast(DPS)")
        typewriter2("\nWilliam Shakespeare - Poetic Legend(DPS)")
        typewriter2("\nMasahiro Sakurai - Game Director(Healer)\n")
        typewriter2(playername)
        typewriter2(" - Monk(Tank)")
        time.sleep(.5)
        print("coddocccc::::;,',,;,,''',,;,,,,,;:ccllooooooloodxkkxdoc:;,,'''''''...............  .....''';:codddxxdddxxdc.   .....',.    ...........")
        print(";,,,,''''''..'',,,,,,,,;;;;::cloddddoooooooolllc;,,,,,,''.......                     ..':odxxxxxxdc.   ...''''. ............    ......")
        print(",'........''''''',,,,,;;;::ccclloooooolllllllllc:;,,,'.........                         ..;cccldddc.   .',,'.''............ .... .....") 
        print(",,,,'''',,,,;;;;;;;;;::ccllllllloooooooollollllc:,''.......                                . ..cddc.  ..''..',,.......................") 
        print("',,,;;;;;;;;::::::::cccloooooodxxxdooooooooolllc;'.......                                     .cdd:.  ..............................  ") 
        print(",',,;;;;;::::::::::ccllllllcldOKXXXK000Oxdooool;..... .                                       .:dd:.  ............................... ") 
        print(";,,,,;;;;::::::::cccllllc::oOXXKOOKNNNNNXKOxooc'..                                            .:dd:.   .....  ......................  ") 
        print(";;;;,,;;;:::::::ccclllc:;:dKX0dc:lkKKXWWWWNKko;..                                             .,od:.   ....      ..  ................ ") 
        print(";;;;;;;:::::::::cllllc;,;o0X0o::;,;::lkKNWWWXd'   ..                                           'ld:.  ...              ...........'.. ") 
        print(":;;;;;:::::::::cclllc;,,cxKKo;cl;'''';lx0NWWNk'  .. ..                   .                     .ld:.  .,..              ...........   ") 
        print(":;;;;;;;::::::cclllc:;,;lOXKl,:c,....;coxKNWWd. ..  ..                  ...                    .ld:.  .,,...         ......  ...      ") 
        print(";;;;;;;;;::::ccclllc:::cxKNKd;:c,...,:clx0NWNl.                       .......   .......        .cd:.  .;:'.          ......   ...     ") 
        print(":;;;;;;;;:::ccclllcc:,'':xKKo,;:,''',,;:d0NWNl.                      ..........',::;;:,.        ;oc.  .,,..          .....     ...    ") 
        print("::::;;;'',:cccclllcc;....cOKO:',clllllccxKWMX:             .       ...........'',;:::;,,'.      .::.  .''....         ...       ..... ") 
        print(":::;;;,..';cccclccc:;'...'lOKk:;:lloodxOXWWW0;            ...      ...,,;,'......';;;,,;:'.     .::.  .';,....       ....             ") 
        print("::;;;;,...',:clccc:;;,....'lOOdl:;;cd0XWNNNXO:.      ......,,........':looc,'....,,.';:clc,.    'l:.  .;:::,..      .':c;.         ...")
        print(";,,'''......,:cccc:;,,,''''':ddlcoddx0XNXK0ko;.      .;c:;:;,'...;c;',codolc;;,,;::;;clool:'.  .;oc.  .;cc:,..... ..,ldlc;...','. ..''")
        print("..............';:::;;;;;;;,',oxoldOOOOOOxdlcc;.      .:lllc;,,;;;clccloddollcccclllloooolll:.  .coc..,:lll::::cc:::coolllllllodo, ..''")
        print("................';:::::::::;:xxol:,,,;;;:cccc:.     .,codddooooooooodooddolllllooooooooollcc;..;do,':odddoooooolclodollodddollo:...':c")
        print(".................';::::::c:;lxxdoc;;;::cccccc:.     .;clodddddddddddoloxxdolcclooooooooollc:,'..;;. .',,;cloool;,;cclllccc:;''''',;coo")
        print("............... ..';::::::::okxdlc:::::cccc:::;..   .,:cloodddddxxdoc:ldddoc;;clooooolllllc;'.. ...     .:c;,cooc,':loc:ccc;'...'..,::")
        print(" .............    .';:::::cldxdolc::::::::c::::;,....':::clooddddddc,'';;;;,',:cloooollllc:;'...''..',,,;cl;;codl:;;:;',:c;,'....  ...")
        print("   ..........     .,;:::coxkxddolc::::;;;:::::::;;;;,',;;:cclooddddl:::::;:ccclooooollllcc:,.......':oddoloooodool;'..':c;,,'......,cc")
        print("                 ..;:::ldxxkkkxdlcclc:;;;;::::::,'......,;::clooooodooooooollllooooollllcc:,....    .,lddddddddolc:;;:::;,'''......,cl")
        print("                ..;:cloxxdddxkxxoclol::;;;::;;;;'..  ....',;:cclloooooolllc::ccllllllllccc:;'........,:cloollooc:;;,'.';:;...''',,;:cl")
        print("...  ............;cldxkkkxdoccodolc:cc::;,,,'''''..  ....''',;:clloolc;'.....,;:clllllcccc:;'.  .,:clc;,';:;,,,,,'''..,oxd;..,::::clod")
        print("................;ldxxxxxxxxdo;;cllc;,:c:'................'''',;:clllc:;;,,;;;;:ccccccccc:::'..  ..;cc;,'..,:;'.........lxdoccccclllcll")
        print("......... ....,ldxkkxxdolodddl;,:lo:;;c:.       ..   ......''.',;:ccc:;,,'''',::cc:;,;;;;;,.,'.   ............... .....,cc:,'',cool:;:")
        print("..............lxddddxxxxdcclloc'.;:;:cc:'......''''''............',,;;;;,,',,;:cc:,....''..';,.      ..       .......  .....  ........")
        print("...........',:ddoc;',:lddolc::c:,;ccclcccccclollllllc,''.............';ccccllcc:;'.. .....';:'  .    ....  .  .........               ") 
        print("'''''',''..';cdxdl;....,;::c:::::looll:::cccc:::c:;;;,'...  ...      ..',,;:;;,'..      ..;c,. ..     ... .     ...      ....         ") 
        print(",,,,,,'......'lxxxdl;'....''..,:looolc;...........  ...      ..        .........       ..;c,.     ..  ...    ............   .....     ") 
        print("'''''..      .cxxxxddo:,',;,,;cooolcc;.  ..       ....       ...                     ..'::'      ...   ...  .......  .....   ........ ") 
        print("              ,ddddddddoloooooollcc:;.  .....   .....         .;,..                ..':c,.      ..................  .....  ...........")
        print("..            .cooooooooooooollc:;,'........     ....         .;c:,..            ..,:c;.       ..................   ..... ............") 
        print("..             ,lllllllllllllcc:,'........       ....          .:cc:;,..........,;:c;.        .....          ...   ...  ............. ") 
        print(".             .:olllcccc:c:::::;..... .....                     .,ccc:::;;;;;::cc;'.          ..             ..   ...   ..   .........") 
        print("              ,odolc:;;;;;:::::.  ... ........                    .,:ccllllcc:,..             .             ... ....  ...   ..........")
        print("             .lddddlc:::::::::,.  ... .......                        ..'''...           .               ...... ...   ....   ........'.")
        print("             ,dxxxdollccccccc;...  .  .....             .;.                             .  ..... ';.   ...........  ....   .,'........")
        time.sleep(.5)
        typewriter2("\n\nI have several questions...")

        typewriter2("\n\nSheldon Cooper: *explaining why the party should start grinding levels in a very technical manner*")
        typewriter2("\nWilliam Shakespeare: To be or not to be, that is the question.")
        typewriter2("\nMasahiro Sakurai: Super Smash Bros. Ultimate is for good boys and girls of many different ages")
        typewriter2("\nMichael Bay: *imitating explosion noises*")
        humanparty2()
    else:
        print("error")

def humanparty2():
    typewriter2("\n\n**You and your party make your way to the nearest open field with monsters to start leveling up.")
    typewriter2("\n**On the way, you meet an old man in a cloak offering you a mysterious key in exchange for loot from nearby monsters.")
    typewriter2("\n\nDo you accept his offer? \nY/N only\n")
    choice = input(">>> ")
    if choice in yes:
        typewriter2("\n**You and your party collect the required materials while leveling up. Talk about hitting two birds with one stone.")
        typewriter2("\n**You return to the man and exchange the loot for his key. After the exchange, the man vanishes into thin air.")
        global mystkey
        mystkey = 1
        dungeonhuman()
    elif choice in no:
        mystkey = 0
        nokey()
    else:
        print(invalid2)
        humanpartyformed()

#section 8a
def nokey():
    typewriter2("\n\n**You continue on your travels after denying the man's offer.")
    typewriter2("\n**Your party finally arrives at an open field filled with monsters")
    typewriter2("\n**You and your party have leveled up quite a bit and have gotten so much loot.")
    global mystkey
    if saber == 1:
        typewriter2("\n\nMeteora: Are you sure you don't want to exchange some of this loot for the key?")
        typewriter2("\nMeteora: It might help us in the long run.")
        choice = input("\n>>> ")
        if choice in yes:
            typewriter2("\n\n**Your party returns to the man and exhanges the loot for his key.")
            typewriter2("\nMeteora: Thank you.")
            mystkey = 1
            typewriter2("\n\n**After retrieving the key, your party heads to the nearest dungeon.")
            dungeonhuman()
        elif choice in no:
            typewriter2("\n\nMeteora: I see... I'm sorry for bringing it up.")
            typewriter2("\n\n**Your party heads to the nearby dungeon without the key.")
            dungeonhuman()
        else:
            print(invalid)
            nokey()
    elif archer == 1:
        typewriter2("\n\nDeath: We should go back to the man and give him what he wants. They key might help us... ")
        typewriter2("\nNurse Joy: How would you know that?")
        typewriter2("\nDeath: I do this all the time. 60% of the time, it works all the time.")
        typewriter2("\n2B: Sound argument... ")
        typewriter2(playername)
        typewriter2(", should we?")
        choice = input("\n>>> ")
        if choice in yes:
            typewriter2("\nDeath: Good choice.")
            typewriter2("\n\n**Your party returns to the man and exhanges the loot for his key.")
            mystkey = 1
            typewriter2("\n\n**After retrieving the key, your party heads to the nearest dungeon.")
            dungeonhuman()
        elif choice in no:
            typewriter2("\n\nDeath: You're gonna regret this.")
            typewriter2("\n\n**Your party heads to the nearby dungeon without the key.")
            dungeonhuman()
        else:
            print(invalid)
            nokey()
    elif druid == 1:
        typewriter2("\n\nChrissy Costanza: I think we should get the key, it might help us.")
        typewriter2("\nPat Kirch: *reliving The Mirror Tour with his drums*")
        typewriter2("\nAimer: あなたは どこで それを てにいれましたか?")
        typewriter2("\nChrissy: ")
        typewriter2(playername)
        typewriter2(", what do you think? Should we go back or not?")
        choice = input("\n>>> ")
        if choice in yes:
            typewriter2("\n\n**Your party returns to the man and exhanges the loot for his key.")
            typewriter2("\nChrissy: Nice.")
            mystkey = 1
            typewriter2("\n\n**After retrieving the key, your party heads to the nearest dungeon.")
            dungeonhuman()
        elif choice in no:
            typewriter2("\n\nChrissy: Yeah, I guessed as much. We could sell the loot instead.")
            typewriter2("\n\n**Your party heads to the nearby dungeon without the key.")
            dungeonhuman()
        else:
            print(invalid)
            nokey()
    elif monk == 1:
        typewriter2("\n\nSheldon Cooper: You don't think that key from before would help us do you?")
        typewriter2("\nWilliam Shakespeare: Why dost thou doubt thine leader's decision?")
        typewriter2("\nMasahiro Sakurai: For Joker's neutral special, he wields a")
        dramatic("...")
        typewriter2(" GUN")
        typewriter2("\nSheldon: Say, ")
        typewriter2(playername)
        typewriter2(", what do you propose? Should we get the key?")
        choice = input("\n>>> ")
        if choice in yes:
            typewriter2("\n\n**Your party returns to the man and exhanges the loot for his key.")
            typewriter2("\nMichael Bay: *explosion noises*")
            mystkey = 1
            typewriter2("\n\n**After retrieving the key, your party heads to the nearest dungeon.")
            dungeonhuman()
        elif choice in no:
            typewriter2("\n\nSheldon: Leonard would have said yes.")
            typewriter2("\n\n**Your party heads to the nearby dungeon without the key.")
            dungeonhuman()
        else:
            print(invalid)
            nokey()

def dungeonhuman():
    typewriter2("\n**You arrive at the dungeon entrance and try to open the door.")
    typewriter2("\n\nHey, it's me Voice-in-your-head, didn't forget about me did you?")
    typewriter2("\nI think it's locked.")
    typewriter2("\nIt says something about a key.")
    if mystkey == 1:
        mysteriouskey()
    elif mystkey == 0:
        dungeonlocked()
    else:
        print("Error")

def mysteriouskey():
    typewriter2("\n\n**You pull out the key from your inventory but you find no key hole.")
    typewriter2("\n**In a fit of rage, you throw the key furiously at the door.")
    typewriter2("\n**The door opens.")
    typewriter2("\n\nWho knew your anger issues would help *us* in our journey.")
    typewriter2("\n\n**You and your party enter the dungeon and start clearing it.")
    typewriter2("\n**After a long and tiring dungeon run, your party sits down and looks at the loot you have collected.\n")
    global HEgear
    HEgear = 1

    if saber == 1:
        typewriter2("\n\nMeteora: A NEW GRIMOIRE! YES!")
        typewriter2("\nEmiya: My long lost noble phantasm!")
        typewriter2("\nRikka: IT'S GRIDMAN!")
        typewriter2("\nKorosensei: What a wonderful turn of events!")
        hardquest()
    elif archer == 1:
        typewriter2("\n2B: It's the Demon's Cry bracers! And more pods!")
        typewriter2("\nNurse Joy: CHANSEY!")
        typewriter2("\nDeath: My scythe... Finally.")
        typewriter2("\nIllidan: *facing into the void* YOU ARE NOT PREPARED!")
        hardquest()
    elif druid == 1:
        typewriter2("\nChrissy: My microphone!")
        typewriter2("\nAimer: 私のピアノ!")
        typewriter2("\nPat: MORE DRUM STICKS MUAHAHAHAHAHAHA!")
        typewriter2("\nLindsey: A tuner? *checks bag* Oh...")
        hardquest()
    elif monk == 1:
        typewriter2("\nSheldon: It's the ring of power Penny wouldn't give me!")
        typewriter2("\nSakurai: *grabs two Nintendo Pro Controllers* POWER IS MINE")
        typewriter2("\nShakespeare: Thou has been granted a great quill by thy leader")
        typewriter2("\nMichael Bay: *grabs Megumin's staff* EXXXXPLOSIOOOOOOOOOOON")
        hardquest()
    else:
        print("Error")
    
#section 9
def dungeonlocked():
    typewriter2("\n\n**You realize that the man from before has the key you need.")
    typewriter2("\n**Will you go back?")
    typewriter2("\nY/N\n")
    choice = input(">>> ")
    if choice in yes:
        typewriter2("\n**You return to the area where the man was earlier.")
        typewriter2("\n\n*We* can't find him anywhere. *We* should just continue our adventure without it.")
        hardquest()
    elif choice in no:
        hardquest()
    else:
        print(invalid2)
        dungeonlocked()
#section 10
def hardquest():
    typewriter2("\n\n**You, along with your party, head to the nearby town looking for a quest.")
    typewriter2("\n**A woman approaches you and your party.")
    typewriter2("\n\nWoman: Adventurers, you must help me! I lost my recipe book in Anor Londo. There lies Ornstein and Smough but you can handle it right?")
    typewriter2("\n**Do you accept?")
    typewriter2("\nY/N\n")
    choice = input(">>> ")
    if choice in yes:
        typewriter2("\nWoman: Thank you so much adventurers! I pray for your safe return!")
        hardquest2()
    elif choice in no:
        typewriter2("\nWoman: Please adventurers, I promise you will be paid handsomely. Just bring back my recipe book.")
        typewriter2("\n*We* should just do the quest, dude.")
        hardquest2()
    else:
        print(invalid2)
        hardquest()

def hardquest2():
    typewriter2("\n\nWe're here! It's Anor Londo!")
    typewriter2("\nIt's quite dark here.")
    typewriter2("\nAnyways, let's just get this over with.")

    if HEgear == 1:
        if saber == 1:
            typewriter2("\n\nEmiya: I am the bone of my sword...")
            typewriter2("\nMeteora: Magical Artillery!")
            typewriter2("\n**Korosensei uses his extreme speed and strength to overpower Smough in a split second.")
            typewriter2("\nRikka: GRIDMAN!")
            typewriter2("\nYou: EXCALIBUUUUUUUUUUUUUUUUR!")
            goodend1()
        elif archer == 1:
            typewriter2("\n\nNurse Joy: Welcome to the pokemon center!")
            typewriter2("\n2B: *charges in to engage in hand-to-hand combat.")
            typewriter2("\nIllidan: YOU ARE NOT PREPARED!")
            typewriter2("\nDeath: *twirls his scythe around multi-hitting the two bosses like crazy*.")
            typewriter2("\n\You: *opens the Gate of Babylon, unleashing thousands of thousands of unique swords flying at mach speed*")
            goodend1()
        elif druid == 1:
            typewriter2("\n\nChrissy: *singing* My head's chained down by the voices...")
            typewriter2("\nAimer: *harmonizes with her piano.*")
            typewriter2("\nLindsey: *goes full music video mode and harmonizes*")
            typewriter2("\nPat: *somehow also harmonizes pretty well with his drums*")
            typewriter2("\nYou: *transforms into a treant* TRANQUILITY!")
            goodend1()
        elif monk == 1:
            typewriter2("\n\nSheldon: I HAVE THE RING OF POWER. FEAR ME!")
            typewriter2("\nShakespeare: Thou must disappear!")
            typewriter2("\nMichael Bay: *inhales*")
            typewriter2("\nMichael Bay: EXX...")
            typewriter2("\nMichael Bay: ...PLOSIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON")
            typewriter2("\nSakurai: *summons the Hero from Dragon Quest and Joker from Persona 5.*")
            typewriter2("\nSakurai: *Sakurai spikes with Hero and shoots Joker's gun simultaneously using his two controllers.*")
            typewriter2("\nYou: Fortifying brew!")
            goodend1()
        else:
            print("Error")
    elif HEgear == 0:
        if saber == 1:
            typewriter2("\n\n**Rikka and Emiya are killed by Ornstein while you get incapacitated because of Smough... Korosensei grabs you and the recipe book and runs for your lives.")
            typewriter2("\n**Meteora disappears forever.")
            typewriter2("\n**You're able to make out alive thanks to Korosensei")
            typewriter2("\n**Korosensei retires as an adventurer and becomes a teacher.")
            badending()
        elif archer == 1:
            typewriter2("\n\n**Nurse Joy ended up incapacitated with no nearby pokemon centers")
            typewriter2("\n**2B self-destructs, hoping to save the rest of the team. Ornstein is defeated.")
            typewriter2("\n**Smough proves too difficult for what remains of your party.")
            typewriter2("\n**Death dies temporarily, to be resurrected once the horsemen are called once more.")
            typewriter2("\n\nIllidan: WE WERE NOT PREPARED!")
            typewriter2("\n\n**Illidan flies you out to safety with the recipe book.")
            typewriter2("\n**Illidan now resides in the Black Temple, no longer an adventurer.")
            badending()
        elif druid == 1:
            typewriter2("\n\n**Your ragtag party of musicians from different genres is unable to serenade Ornstein and Smough.")
            typewriter2("\n**In a futile attempt to keep them healed, you waste a lot of mana.")
            typewriter2("\n**You lose hope and start running with the recipe book, you start healing only yourself.")
            typewriter2("\n**You abandoned your party to their deaths but was able to survive the dangerous encounter/")
            badending()
        elif monk == 1:
            typewriter2("\n\n**Sheldon tries to train and condition the two bosses like he did Penny. It didn't go so well for him.")
            typewriter2("\n**Shakespeare proved to be inferior to Smough in literary pieces. He is now Smough's apprentice. A betrayal.")
            typewriter2("\n**Michael Bay tries to use his explosion powers to defeat Ornstein but his explosions proved to be too small. One could only guess what happened to him after that.")
            typewriter2("\n**Sakurai uses his Sakurai spike on Ornstein as he chases both of you.")
            typewriter2("\n**It proved to be effective and both of you were able to escape with the recipe book in hand.")
            typewriter2("\n**Sakurai went on to the gaming industry to develop games.")
            badending()
        else:
            print("Error")
    else:
        print("error")
#section 11 solo adventure
def humansoload():
    typewriter2("\n\nWe've got a lone wolf over here bois.")
    typewriter2("\nSince *we're* going solo, *we* should start grinding levels.")
    typewriter2("\nGetting stronger is gonna matter way more now that you've decided that we don't need a party.")
    typewriter2("\nSo let's get going then.")
    typewriter2("\n\n**You start heading to the nearby open area to train.")
    typewriter2("\n**You spend the day battling countless monsters in the area and learn many new skills.")
    typewriter2("\n**You also learn special skills only learnable and usable when you are going solo.")
    humanbirdcaged()

def humanbirdcaged():
    typewriter2("\n**You sit down to rest.")
    dramatic("\n...")
    typewriter2("\nMysterious Lady: Young adventurer, I have noticed you training and I could not help but watch you.")
    typewriter2("\nMysterious Lady: As thanks for giving me such a spectacular sight, I offer you a medallion.")
    typewriter2("\nMysterious Lady: Please choose between the two.")
    time.sleep(.5)
    print("\n\nMMMMMMMMMMMMMMMMMMMMMMWNXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMKddxdONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0o0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMX:lNWk;xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx,xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMWKkdccddlcok0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx,kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMNlcKWXOkKWWx:OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk,kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMXc,oddllodd:;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMW0olo::d:,ol,ldlkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx,kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMNOxddOKxxXWxcKWOoO0xddkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMk;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKONMMMMMMMMMMMMMMMM")
    print("MMMMMMMWXOoc,,lO0x:cO0Oc;x00d:oO0xc;:okKNMMMMMMMMMMMMMMMMMMMMMMMMk;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWkdXMMMMMMMMMMMMMXo'lNMMMMMMMWNXNMMMMM")
    print("MMMMMM0l,.,codc;ldxkOOk:,dOOOkxo::odo:',ckNMMMMMMMMMMMMMMMMMMMMMMk;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;.oWMMMMMMMMMMNO:..dWMMNKkdoccxNMMMMM")
    print("MMMMMO,..':x00coNWWWWWNl;0WWWWWWkcxKOl;,''oNMMMMMMMMMMMMMMMMMMMMMk;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;'.cXMMMMMMMMMKl'...dXkl:'..'l0WMMMMMM")
    print("MMMM0,.o00ko:,;lddddxxo,.cdxxxxxo:,;lk0Kk:'dWMMMMMMMMMMMMMMMMMMMMk;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,''.:KMMMMMMMW0:.....;;....'l0WMMMMMMMM")
    print("MMMXc.oNMMMWdc0NNNNNNNXl;ONNNNNNNXdcKMMMMO;,OMMMMMMMMMMMMMMMMMMMMk;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl,'''.cNMMMMMMW0:....'.....'cOWMMMMMMMMMM")
    print("MMXl..l0KKKO:;xOOkkkkkx:,okOkkOOOkl;d0KKKx;':0WMMMMMMMMMMMMMMMMMM0d0MMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:''''''dWMMMMMMXl..........:kNMMMMMMWNKKWM")
    print("MW0o,...'.''...':ccc:,.''.';cll:,'''',,,,,,,cONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl,'''''.:0MMMMMMM0;........,dXMMMMMN0xc;c0WM")
    print("MMMWo..;okd,.'l0NWWWWKo,'cONWWWNXk:',lkxl,':0MMMMMMMMMMMXkdddox0WMMXxoddooodONMMMMMMMMMMMMMMMXx;''''''';xWMMMMMMMx'......'lKWMMMW0o;'..:KMMM")
    print("MMMWl.;0WMMd.cXMMMMMMMNl,0MMMMMMMWk'cXMMNd';0MMMMMMMMMWOclk0K0dcoKM0co000OOx:dWMMMMMMMMMMMMNk:'''''''',dNMMMMMMMK:.'''..,xNMMMNOc'....cXMMMM")
    print("MMMWl.dWMMMx'lNMMMMMMMWl;0MMMMMMMM0;cNMMMK:;0MMMMMMMMMO:dWMMMMM0:oXk:lkO000x:dWMMMMMMMMMMW0l'','''''''oNMMMMMN0x;......'xWMMWOc'.....lXMMMMM")
    print("MMMMo.xMMMMk,oNMMMMMMMWl;0MMMMMMMM0;lNMMMXc;0MMMMMMMMMk,xMMMMMMXco0o:cddo:;oONMMMMMMMMMMXo,',',,'''''oNMMWXko:,''.'...,xNMW0l'.....'dNMMMMMM")
    print("MMMMo.kMMMM0;oNMMMMMMMWl;0MMMMMMMMK:oWMMMXc:0MMMMMMMMMXo:kXWWN0ocOW0cxNWMO:oNMMMMMMMMMW0c'''''',''''oNWXkl;'.'''''...;OWNOl'......,xWMMMMMMM")
    print("MMMMo.lkkkdc';dxxxxxxkd,'lxxkkxxkko;:dxkkx;:0MMMMMMMMMMNOolooooxKWMKokNWMWOlkWMMMMMMMW0:'''''''''''lXXd;'.'''''''''.:KWO:'.''....,kWMMMMMMMM")
    print("MMMWo.;dxkko,cKNNXNNXNO,.oKNNNNNNNk,ckOkxl';0MMMMMMMMMMMMWNXKXWMMMMWNWMMMMWNNWMMMMMMM0:''''''''',',ox;.''''''''....,dkc'........,OMMMMMMMMMM")
    print("MMMWo.lOOOOo':xOO000OOd,.ck00OOOOOo,:k0OOd;:0MMMMMMMMMMMMMMMMMMMMX0NMMMMMMMMMMMMMMMMWd,,,'',,''''''''''''''''''''..''..........;0MMMMMMMMMMM")
    print("MMMWl.xNXXXx';xOOOOOOOd,.ckOOOOOOOl,l0XNNKl;OMMMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMKc',,''',,'''''''''''''''''''''........'.'cKMMMMMMMMMMMM")
    print("MMMXc'kMMMMK:cXMMMMMMMNc'kWMMMMMMMO:dWMMMXl,kMMMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMXc.'''''','''''''''...'''''.'''.........'oXMMMMMMMMMMMMM")
    print("MMMX:.kMMMM0:lNMMMMMMMNc,OMMMMMMMMO;oNMMMXl'xMMMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMWd'','''',,''''''''','''''.'''''.'.....'xNMMMMMMMMMMMMMM")
    print("MMMK:'kMMMM0;lNMMMMMMMNc'OMMMMMMMMO:dWMMMXl'xMMMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMNOoc:;,,,,,,''''''''''''''..'.......,l0WMMMMMMMMMMMMMMM")
    print("MMMK:'OMMMMK:lNMMMMMMMNc'kWMMMMMMM0cdWMMMNo'xMMMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMWWWNKOxoc,',,'''''''''..'.....''.';dKWMMMMMMMMMMMMMMMMM")
    print("MMMK:'kMWX0o,;dxxxxxxxo,.cxxxkkxkxl,cOKNMXl'xMMMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMWkclll:;,''''''''''''';okOxocccccokXWMMMMMMMMMMMMMMMMMMM")
    print("MMM0;.:dxxdc',dOO00O00d,.lO0000O0kc';odxxo;'xMMMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMKo:,''','''''.'',:ldOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMKc..oXWMMK;:XMMMMMMMX:.xWMMMMMMMk;dWMWNO:.;kWMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMMWXOdlccccclodxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMKo;.,oxOOo';kXNNNNWNx,.lKWNNNNNKo,ck0Oxc,:oOWMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMNO;.......';;::::;'..',:::::;,''''...,dNMMMMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMKxdol::;;,,''........'''',;;::clodx0NMMMMMMMMMMMMMMMMMMMMMMx,kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMWNNXK00000OOOO00000KXNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMXOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    time.sleep(.5)
    typewriter2("\nA. Cage \nB. Bird\n")
    choice = input(">>> ")
    if choice in ansA:
        global cage
        cage = 1
        humannarr()
    elif choice in ansB:
        global bird
        bird = 1
        humannarr()
    else:
        print("\nA or B only")
        humanbirdcaged()

#section 12 human bird cage
def humannarr():
    typewriter2("\n\nMysterious Lady: A fine choice.")
    typewriter2("\n**The mysterious lady vanishes into thin air.")
    typewriter2("\n\n**You resume your training for five more days.")
    typewriter2("\n**5 days later")
    typewriter2("\n\nDon'tcha think we need to train somewhere else?")
    typewriter2("\nYou know, where there would be stronger monsters around? \nY/N")
    choice = input("\n>>> ")
    if choice in yes:
        typewriter2("\n\nYea, solid choice.")
        humannarr2()
    elif choice in no:
        typewriter2("\n\n*We're* going whether you like it or not.")
        typewriter2("\n**Voice-in-your-head controls your movement now")
        humannarr2()
    else:
        print(invalid2)
        humanarr()

def humannarr2():
    typewriter2("\n\nOooh look, *we're* at a crossroads.")
    time.sleep(.5)
    			
    print("                    .--._..--.                  ")
    print("             ___   ( _'-_  -_.'                 ")
    print("          _.-'   `-._|  - :- |                  ")
    print("     _.-'           `--...__|                   ")
    print("  .-'                       '--..___            ")
    print(" / `._                              \           ")
    print("  `. `._                             |          ")
    print("    `. `._                           /          ")
    print("      '. `._    :__________....-----'           ")
    print("        `..`---'    |-_  _- |___...----..._     ")
    print("                    |_....--'             `.`.  ")
    print("              _...--'                       `.`.")
    print("         _..-'                            _.'.' ")
    print("      .-'                               _.'.'   ")
    print("      |                               _.'.'     ")
    print("      |                   __....------'-'       ")
    print("      |     __...------''' _|                   ")
    print("      '--'''        |-  - _ |                   ")
    print("                    | _   - |                   ")
    print("                    |   -  _|                   ")
    print("                    | _     |                   ")
    print("                    |     _ |                   ")
    print("                    |  _    |                   ")
    print("                    |    _  |                   ")       
    print("                    | -    -|                   ")     
    print("                    |.____  |                   ")
    print(";;;:::.           (\| - _ ``|---.._.'           ")
    print("       ..        ;::|   - _ |/)    ;;;:::.      ")
    print("(o)         ;;::.,  |_ -  - |;;;:               ") 
    print("(\'/)   ::;;   (o)  | -_  -_L     ``::;;;.      ")
    print(".;;'         (\ '/) |  -_ _ G (o)  ..;;         ")
    print("      '''    ;:;;.,|(o)  _-B(\'/)               ")
    print(" ;;;;:::        ;::(\'/);;:|;:; ;'              ")

    time.sleep(.5)
    typewriter2("\n\nWeird... there is nothing written on the sign.")
    typewriter2("\n\n**Your pocket starts to glow.")
    typewriter2("\n**You grab the medallion that is in that pocket.")
    typewriter2("\n**You realize that the medallion is telling you where to go.")
    if bird == 1:
        typewriter2("\n**You go to the right as directed by the glowing medallion.")
        humanbird()
    elif cage == 1:
        humancage()
    else:
        print("error")

#section 13a human cage 
def humancage():
    typewriter2("\n**You go to the left as directed by the glowing medallion.")
    typewriter2("\n**You walk for 5 minutes but the fog is getting heavier and you can not see anything 1 meter ahead of you anymore.")
    typewriter2("\n**A flash of light hits your eyes and you find yourself in an unknown town.")
    richdude()
    
def richdude():
    typewriter2("\n**A rich looking fellow with their small local fanbase approaches you.")
    typewriter2("\n\nRich Fellow in Armor: You must be new here. Say, are you an adventurer?")
    typewriter2("\nRich Fellow: Of course you are! Nobody wears ugly armor like that except for adventurers.")
    typewriter2("\nRich Fellow: All you adventurers in your ugly gear, killing weak monsters pffft.")
    typewriter2("\nRich Fellow: You lot don't stand a chance against elegant knights like me.")
    typewriter2("\n\n**In a spite of anger, you punch him so hard, you send him flying.")
    typewriter2("\n\nWe really need to get you to an anger management class.")
    typewriter2("\n\nRich Fellow: That was uncalled for! Now you've made a fool of me!")
    typewriter2("\nRich Fellow: I challenge you to a duel!")
    typewriter2("\n**Do you accept? \nY/N\n")
    choice = input("\n>>> ")
    if choice in yes:
        challengeaccepted()
    elif choice in no:
        typewriter2("\n\nRich Fellow: You scared little kid?")
        typewriter2("\nRich Fellow: We've got a scaredy cat over here you guys!")
        typewriter2("\n\n**The nearby crowd giggles*")
        typewriter2("\n**Annoyed, you angrily accept the challenge.")
        typewriter2("\n\nSeriously dude, your anger needs some managing.")
        challangeaccepted()
    else:
        print(invalid2)
        richdude()
    
def challengeaccepted():
    typewriter2("\nRich Fellow: The duel is in 3 days. Goodluck, you're gonna need it.")
    typewriter2("\n\n3 days later...")
    typewriter2("\n\n**You can hear the crowd roaring with excitement for this duel.")
    typewriter2("\n**The only thing that crosses your mind during this time is 'Why do I have to deal with this buffoon again?")
    typewriter2("\n\n*Ahem* It's because of your anger issues dude.")
    typewriter2("\n**You think 'oh, oops'.")
    typewriter2("\n\nRich Fellow: What are you looking at, ")
    typewriter2(playername)
    typewriter2("?")
    typewriter2("\n\n**You snap back into reality and quickly sweeped the rich fellow's legs, tripping him.")
    typewriter2("\n**You quickly chop the vital point in his neck before he falls to the ground, rendering him unconscious.")
    typewriter2("\n**The crowd gasps in disbelief, and soon after cheers for you were heard.")
    typewriter2("\n**A man that looks like royalty approaches you")



def challengeafter():
    typewriter2("\n\nMan: Hello, ")
    typewriter2(playername)
    typewriter2(". That such a magnificent maneuver. Your skill is without a doubt, amazing to say the least. I have a quest I'd like you to take on.")
    typewriter2("\nMan:There is a dungeon located to the right of the only crossroads here in the kingdom.")
    typewriter2("\nMan:I would like you to go into the dungeon and retrieve my queen's crown")
    typewriter2("\nMan:In exchange for your service, I give you partial rule over my kingdom.")
    typewriter2("\nMan:Do you accept? \nY/N\n")
    choice = input(">>> ")
    global bird
    if choice in yes:
        typewriter2("\n\nMan: Thank you, this means a lot to me.")
        typewriter2("\nMan: Here is the second medallion you need in order to travel to the dungeon.")
        typewriter2("\nMan: Head back to the crossroads and you shall find your way there.")
        typewriter2("\n\n**You somehow find your way back to the crossroads and head left this time.")
        typewriter2("\n**The bird medallion you were given starts to glow*")
        bird = 1
        humanbird()
    elif choice in no:
        typewriter2("\n\nMan: I'm sorry, you give me no choice.")
        typewriter2("\n\n**The man swiftly steals your cage medallion, claps with the two medallions in hand, and throws the two medallions at you.")
        bird = 1
        humanbird()
    else:
        print(invalid2)
        challengeafter()
    

#section 14
def humanbird():
    typewriter2("\n\n**You hear a soft voice from somewhere.")
    typewriter2("\nWAKE UP!")
    typewriter2("\nWAKE UP!")
    typewriter2("\nWAKE UP!")
    typewriter2("\nFine, sleep all day for all I care.")
    typewriter2("\n\n**You wake up")
    typewriter2("\n\nWe're in a dungeon!")
    typewriter2("\nYou know, the dungeon the man wanted *us* to go to.")
    typewriter2("\nThere doesn't seem to be any exit.")
    typewriter2("\n\n**You see a sign.")
    typewriter2("\n\nIt says: 'only the chosen one can leave dungeon.'")
    typewriter2("\n'The judge at the end of the dungeon will be the judge of you.'")
    typewriter2("\nI guess that means *we* have to clear this dungeon then.")
    typewriter2("\n\n5 hours later")
    typewriter2("\n\n*We've* been walking and killing monsters for hours. WHERE IS THE EXIT?")
    typewriter2("\nOh look, the boss room.")
    typewriter2("\n\n**You enter the boss room.")
    typewriter2("\n**It's so dark, you can't see anything")
    typewriter2("\n\nJeez, you'd think they would at least put up some torches here but nooooo.")
    typewriter2("\n\n**You hear a voice**")
    typewriter2("\n\n???: Do you know da wae?")
    typewriter2("\nYou: What way? I got here thanks to the medallion.")
    typewriter2("\n???: ")
    dramatic("DO. YOU. KNOW. DA. WAE?")
    typewriter2("\n\n**You suddenly hear mass clucking from what sounds like hundreds of who-knows-what.")

    if bird == 1 and cage == 1:
        typewriter2("\n**You realize that 'the way' could be referring to your medallions.")
        typewriter2("\n**You fearfully take them out of your inventory.")
        typewriter2("\n**The medallions start glowing once more.")
        typewriter2("\n**The medallions float out of your hands and start swirling around each other.")
        typewriter2("\n**They fuse in a flash of light, lighting up the entire room, and become a crown.")
        typewriter2("\n**The medallions, now a crown, rest atop your head.")

        time.sleep(.5)
        print("OOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkOOOOOOOOOOOOOO00000000000KKKKKKKKKKOkxolllc:::;;;,,,;;;::::lodddkOKKKKKKKKK000000000000000OOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkkkkkkOO")
        print("OOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkOOOOOOOOOOOOOO00000000KKKKKKKK0kxoc:;,'',,,;;;;;;;;;;;;;;;;,,''''';:lox0KXKKKKKK00000000000000OOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkkkOOO")
        print("OOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkOOOOOOOOOOOOO0000000KKKKKKKK0kdlc;,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'',:lox0KKKKKKKK00000000000OOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkOOOO")
        print("OOOOOOOOOOOOOOOOOOOOOOkkkkkkkOOOOOOOOOOOO0000000000KKKKOxoc:,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,'';:ldk0XKKKKK00000000OOOOOOOOOOOkkkkkkkkkkkkkkkkkkkOOOOO")
        print("OOOOOOOOOOOOOOOOOOOOOOOkkkkOOOOOOOOOOOO0000000000KK0koc;,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'';cdOKKKKKKK00000OOOOOOOOOOOOkkkkkkkkkkkkkkkkOOOOOO")
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO000000000KKK0ko:,',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,';:okKKKKKK000000OOOOOOOOOkkkkkkkkkkkkkkkOOOOOOO")
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0000000KKKKko:,,;;;;;;;;;;;;;;;;;;;;;;;;;:::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;,',:okKKKK0000000OOOOOOOOOOkkkkkkkkkkkOOOOOOOO")
        print("OOOOOOOOOOOOOOOOOOOOOOOO0OOOOOO0000000000KKOo:,,;;;;;;;;;;;;;;;;;;;;;;;::::ccccccccccccccccccccccccccc:::::;;;;;;;;;;;;;;;;,,:oOKK00000000OOOOOOOOOOkkkkkkkkOOOOOOOOO")
        print("OOOOOOOOOOOOOOOOOOOOOOO0000OO000000000KK0xl,',;;;;;;;;;;;;;;;;;;;;;:::cccccccccccccccccccccccccccccccccccccc::::;;;;;;;;;;;;;,',ckKK0000000OOOOOOOOOOOkkkkkOOOOOOOOOO")
        print("OOOOOOOOOOOOOOOOOOOO000000000000000KKKOd:',;;;;;;;;;;;;;;;;;;;;;::ccccccccccccccccccccccccccccccccccccccccccccccc::;;;;;;;;;;;;;,,cx0K0000000OOOOOOOOOOOkOOOOOOOOOOOO")
        print("OOOOOOOOOOOOOOO00000000000000000KKKKkl,,,;;;;;;;;;;;;;;;;;;;;::ccccccccccccccccccccccccccccccccccccccccccccccccccccc:::;;;;;;;;;;;,,:kKK00000000OOOOOOOOOOOOOOOOOOOOO")
        print("OOOOOOOO00000000000000000KKKKK0KK0x:,,;;;;;;;;;;;;;;;;;;;;;::cccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:::;;;;;;;;;;,,cOKK0000000OOOOOOOOOOOOOOOOOOOO")
        print("O00000000000000000000000KKKKKKKKx:',;;;;;;;;;;;;;;;;;;;;;::ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc::;;;;;;;;;;',dKK00000000OOOOO00OOOOOOOOOOO")
        print("OO000000000000000000KKKKKKKKXKx:,,;;;;;;;;;;;;;;;;;;;;;::cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;;;;;;;;;,,o0KK0000000OO00000OOOOOOOOOO")
        print("OO0000000000000000KKKKKKKKKXOl'';;;;;;;;;;;;;;;;;;;;;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc::;;;;;;;,'c0K000000OO000000OOOOOOOOOO")
        print("00O000000000000KKKKKKKKKKXKd,',;;;;;;;;;;;;;;;;;;;;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc::;;;;;;;,l0K0000000000000OOOOOOOOOO")
        print("0000000K0KKKKKKKKKKKKKKXXO:',;;;;;;;;;;;;;;;;;;;;;;:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc::;;;;;;,o0K000000000000000OOOOOOO")
        print("0000000KKKKKKKKKKKKKXXXXd,';;;;;;;;;;;;;;;;;;;;;;;:ccccccccccccccccccccc:;;;;;::::::;;;;:cccccccccccccccccccccccccccccccccccccccccccc::;;;;,;dKK000KK000000000OOOOOOO")
        print("KKKKKKKKKKKKKKKKKXKXXXKo'';;;;;;;;;;;;;;;;;;;;;;;ccccccccccccccccccccc:;;lxO0OxxOOkkxxdol:;;:cccccccccccccccccccccccccccccccccccccccccc:;;;;,;dKKKKKK000000000OOOOOOO")
        print("OKKKKKKKKKKXKKXXXXXXXKl',;;;;;;;;;;;;;;;;;;;;;;;:cccccccccccccccccccc:':0NNNNNN0oox0NNNNNKOdc;;:ccccccccccccccccccccccccccccccccccccccccc:;;;,:xKKKKKKK000000000OOOOO")
        print("clodxk0XXKKKXXXXXXXX0c',;;;;;;;;;;;;;;;;;;;;;;;:cccccccccccccccccc:c:,..lkXWWWWWx..'oKWNNNNWXOo:;:cccccccccccccccccccccccccccccccccccccccc::;;,:OXKKKKKK000000000OOOO")
        print("cc::;:clodxOKXXXXXXO:';;;;;;;;;;;;;;;;;;;;;;;;:ccccccccccccccccccccc;.   .'coddo,.   .dXWNNNNNNKd;;:cccccccccccccccccccccccccccccccccccccccc:;;,c0XKKKKKK000000000OOO")
        print("cccccccc:;;;:ldOXN0;.;;;;;;;;;;;;;;;;;;;;;;;;:cccccccccccccccccccccc'.                 ,ONNNNNNNNKo;:cccccccccccccccccccccccccccccccccccccccc:;,'oXXKKKKK0000000000OO")
        print("ccccccccc:;;;,',co;.,;;;;;;;;;;;;;;;;;;;;;;;:ccccccccccccccccccccccc'                .  .dNNNNNNNNNk:;cccccccccccccccccccccccccccccccccccccccc::,;kXKKKKKK0000000000O")
        print("ccccccccc:;;;;;;;'.';;;;;;;;;;;;;;;;;;;;;;;;cccccccccccc:;;ccccccccc'                    .oNNNNNNNNN0c;ccccccccccccccccccccccccccccccccccccccccc:'cKXKKKKK0000000000O")
        print("ccccccccc:;;;;;;;'.,;;;;;;;;;;;;;;;;;;;;;;;:cccccccccccc,,:ccccccccc;.                    .dNNNNNNNNNKc,ccccccccccccccccccccccccccccccccccccccccc;,xXKKKKKK0000000OOk")
        print("ccccccccc:;;;;;;;.';;;;;;;;;;;;;;;;;;;;;;;:ccccc:;;;::::;:cccc:::;;;;'.                    ,0WNNNNNNNNO:;ccccccccccccccccccccccccccccccccccccccccc,lKXKKKKK000000OOOO")
        print("cccccccccc;;;;;;,.';;;;;;;;;;;;;;;;;;;;;;;:cccc;;codxkkkOOOOOkkkxdoolc,..                  .xWNNNNNNNNNl,ccccccccccccccccccccccccccccccccccccccccc;;kXKKKKKK0000OOOOk")
        print("cccccccccc:;;;;;,.';;;;;;;;;;;;;;;;;;;;;;:cccc;,oOOOOOOOOOOkOOOOOOOOOOOkdl;'.              ,0WNNNNNNNNNd,:cccccccccccccccccccccccccccccccccccccccc:;dXXKKKKKK00OOOOOO")
        print("ccccccccccc;;;;;,.';;;;;;;;;;;;;;;;;;;;;;:cccc,ckOOOOOOOOOOOOOkOO000KKKKKKK0xl,.         .:ONNNNNNNNNNNd,:ccccccccccccccccccccccccccccccccccccccccc,lKXKKKKKK0OOOOOOO")
        print("ccccccccccc:;;;;,.';;;;;;;;;;;;;;;;;;;;;:ccccc,;xOkkOOOOOOOOkOO0KKKKKKKKKKKKKKKkl;,,;:cld0NNNNNNNNNNNWKl,cccccccccccccccccccccccccccccccccccccccccc;c0XXKKKK0OOOOOOOO")
        print("cccccccccccc:;;;;'';;;;;;;;;;;;;;;;;;;;;:ccccc:,:xOOOOOOOOkkkO0KKKKKKKKKKKKKKKKKK0xdoxXWNNNNNNNNNNNNNNd,:cccccccccccccccccccccccccccccccccccccccccc;:OXXKKK0000OOOOOO")
        print("ccccccccccccc;;;;'.;;;;;;;;;;;;;;;;;,,;;ccccccc:;;okOOOOOOOkkkO0KKKKKKKKKKKKKKKKKKKK0dokXNNNNNNNWNWWXo,;::::ccccccccccccccccccccccccccccccccccccccc:;xXXKK00000OOOOOO")
        print("ccccccccccccc:;;;'.,;;;;;;;;;;;;;;::',;:ccccccccc:;:dOOOOOkkOkxddddddxk0KKKKKKKKKKKKKK0dd0NWNK0Oxdooc:clccccccc:;;,;;:ccccccccccccccccccccccccccccc:,dXXK0000000OOOOO")
        print("cccccccccccccc:;;,.';;;;;;;;;;;;:cc;',;:ccccccccccc;':okOOOkOOOOOkxdollooodx0KKKKKKKKKKKkdkkxxdxxxkOKKKKKKKKKK0Okxdoll:;;;:cccccccccccccccccccccccc:,dXKKK000000OOOOO")
        print("ccccccccccccccc:;;'.;;;;;;;;;;;:ccc,.,:cccccccccccc,';;:okOOkkOkkkOOOOOOkdoc:cdxxOO0KKKKK0kOKKKKKKKKKKKKKKKKKKKKKKKKKK0Oxlc;;:ccccccccccccccccccccc:,oXKKKK000000OOOO")
        print("cccccccccccccccc:;,.,;;;;;;;;;:ccc;..,:ccccccccccc:',cc:;;lkOkOOOOOOOOOOOOOOxocldxkOKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOo:;;ccccccccc:;;;:ccc;;,'oXKKKK000000OOOO")
        print("ccccccccccccccccc:;.';;;;;;;;:ccc;'..;:ccccccccccc:';cccc:;;okOOOOOOOOOOOO00KKOookKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0x:;:cccc:;:cldk0KKxx0kdx0KKKK000000OOOO")
        print("cccccccccccccccccc:'.,;;;;;;:ccc:'''.;cccccccccccc;':c:cccc:,lkOOOOOOOOkO0KKKKKKkoloOKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0d;;cc::ok00KNNN0xKWNWNXK00KK000000OOO")
        print("ccccccccccccccccccc;.';;;;;;cccc,';'.;ccccccccccc:,,cccccccc:;lkOOOOOOkO0KKKKKKKKK0xlx0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx;;;cO0OOKNNNWKx0WNNNNNNK00K00000OOO")
        print("cccccccccccccccccccc,',;;;;:ccc;',;,.,ccccccccccc;';ccccccccc:,ckOOOOOO0KKKKKKKKKKKK0dokKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOxoddxk0Kd,l00OOKNNNNWKcoNNNNNNNNX0000000000")
        print("cccccccccccccccccccc;.';;;;:cc:'';;,.,ccccccccccc,':c:cccccccc:,:xOOOkO0KKKKKKKKKKKKKKklx0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKOl.    ...;c;cdkO0XNNNNk, .oXWNNNNWNol000000K0")
        print("cccccccccccccccccccc:'';;;:ccc,';;;;.,cccccccccc:',cccc:cccccccc,:xOOkO0KKKKKKKKKKKKKKKOoo0KKKKKKKKKKKKKKKKKKKKKKKKKKKKOc.     . .:oddllkNNNNk.   .,xXWNWWO'.xKKKKK00")
        print("ccccccccccccccccccccc,.,;;:cc;',;;;;'':ccccccccc,.;cccccccccccccc;;dOkO0KKKKKKKKKKKKKKKK0dlkKKKKKKKKKKKKKKKKKKKKKKKKKKKKOo,.       ..;:..;dKK;      .'cdxo' .dXKKK000")
        print("ccccccccccccccccccccc;.';:cc:'';;;;;,';cccccccc:..':cccccccccccccc;;oOO0KKKKKKKKKKKKKKKKKKxlkKKKKKKKKKKKKKKKKKKKKKKKKKKK0Okdl:;'...    ...;xx.              'kXKKK000")
        print("ccccccccccccccccccccc:'';:c:,';;;;;;:',ccccccc:'. .':cccc:ccccccccc;;okOKKKKKKKKKKKKKKKKKKKklxKKKKKKKKKKKKKKKKKKKKKKKKKK0OkOOOOO0kccdoddOKXWx.              cKKKKK000")
        print("cccccccccccccccccccccc,.;cc;',;;;;;:c,':cccccc;..  .'ccccccccccccccc;,oO0KKKKKKKKKKKKKKKKKKKOld0KKKKKKKKKKKKKKKKKKKKKKKKKOkkkOO0Kd:odxO0KNNW0,             ,OXKKKK000")
        print("cccccccccccccccccccccc;.;c:',;;;;;;:c;';ccccc:'''.  .':cccccccccccccc;,lOKKKKKKKKKKKKKKKKKKKK0oo0KKKKKKKKKKKKKKKKKKKKKKKK0OkOO00dokkxdookNNNNd.          .:OXKKKKKK00")
        print("cccccccccccccccccccccc:',c,,;;;;;;:ccc,,:ccc:'';;..  .':cccccccccccccc;,lOKKKKKKKKKKKKKKKKKKKK0dlkKKKKKKKKKKKKKKKKKKKKKKKK0OO0kld0KKKK0kodKWWXl.       .;xKXKKKKKKK00")
        print("ccccccccccccccccccccccc,,,,::;;;;:cccc;';ccc,',;;;..  .':cccccccccccccc:,ckKKKKKKKKKKKKKKKKKKKKKkloOKKKKKKKKKKKKKKKKKKKKKKK0xookKKKKKKKKKdlOWWXx;. .,cdOXXKKKKKKK0000")
        print("ccccccccccccccccccccccc:;,:c:;;;::cccc:',cc;',;;;;,.   ..:cccccccccccccc:,;xKKKKKKKKKKKKKKKKKKKKK0dlokKKKKKKKKKKKKKKKKKKOxdddOKKKKKKKKKKKKo;lodocldkKXXXXKKKKKKKK0000")
        print("ccccccccccccccccccccccccccccc:;;ccccccc,':;',;;;;;;,.    .;ccccccccccccccc;,lOKKKKKKKKKKKKKKKKKKKKK0xoodk0KKKKKKK0OkxxdxddOKKKKKKKKKKKKKK0l,:::,lXXXXXXXXXKKKKKKK000O")
        print("ccccccccccccccccccccc::ccccccc:cccccccc:'',;c:;;;;;;,.    .,ccccccccccccccc:,:xKKKKKKKKKKKKKKKKKKKKKKKOxddxxxxdxxxddxkOKKKKKKKKKKKKKKKK0kc;:cc;lKXXXXXXXXXKKKKKK00000")
        print("ccccccccccccccccccc;;,;ccccccccccccccccc:::cc::::;;;;,.    .':ccccccccccccccc;,ckKKKKKKKKKKKKKKKKKKKKKKKKKKK0000KKKKKKKKKKKKKKKKKKK0kdoc;:ccc;:ONXXXXXXXXXXKKK0000000")
        print("ccccccccccccccccc:;lx:;cccccccccccccccccccccccccc:;;;;,..    .,:cc:ccccccccccc:;,cox0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0xodddooolllc:;;;:cccc:,dXXXXXXXXXXXKKKKK000000")
        print("cccccccccccccccc;;dXKc,ccccccccccccccccccccccccccc:;;;;,..    ..;:cccccccccccccc:;,;:ok0KKKKKKKKKKKKKKKKKKKKKKKKKK0Odlc;;:;;;;..;:ccccccccc:;dXXXXXXXXXXXKKKKKKKK0000")
        print("ccccccccccccccc;;xNWNo':ccccccccccccccccccccccccccc:;;;;;'.     ..,:cccccccccccccccc:;;cloxOKKKKKKKKKKKKKKKK0Okdolc:;:cccccc:,.':cccccccccc,,dkOKXXXXXXXXXKKKKKKKK000")
        print("cccccccccccccc;,xNNNNO;,cccccccccccccccccccccccccccc:;;;;;,..     ..';:cccccccccccccccc:;;;:ccloooddddddollcc:;;;:ccccccccc:,''':ccccccccc;';;;:coodkOKXXXXXKKKKKKKKK")
        print("ccccccccccccc:,dNNNNNXo':cccccccccccccccccccccccccccc:;;;;;;,..      ..';:ccccccccccccccccccc:;;;;;;;;;;;:::cccccc:ccccccc:',;',ccccccccc;';cccccc:;;:cllox0XXXKKKKKK")
        print("ccccccccccccc,:KNNNNNW0:,:ccccccccccccccccccccccccccccc:;;;;;;,...      ...',;:ccccccccccccccccccccccccc::ccccccccccccccc;',;,';cccccccc;';cccccccccccc:;,,:oxOKXKKKK")
        print("cccccccccccc;,xWNNNNNNNk,;ccccccccccccccccccccccccccccccc:;;;;;;;'...       ....',,,;;::::ccc:c:::;;,;;',:ccccccccccc:c:,',;;'':ccccccc;';ccccccccccccccccc:;,;lx0XXK")
        print("cccccccccccc;;0WNNNNNNNXo,;ccccccccccccccccccccccccccccccc::;;;;;;;;,'....           ..........''''',,'':ccccccccccccc:,';;;,.,ccccccc;';cccccccccccccccccccccc:;:dO0")
        print("cccccccccccc,lXWNNNNNNNNXo';ccccccccccccccccccccccccccccccccc::;;;;;;;;;,,''...............''',;;;;;;'':cccccccccccc:,',;;;;'':cccccc;,;cccccccccccccccccccccccccc:::")
        print("ccccccccccc:'lNWNNNNNNNNNXo,;cccccccccccccccccccccccccccccccccc:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;',:ccccccccccc:;',;;;;;,';cccccc;':ccccccccccccccccccccccccccccc:")
        print("cccccccccccc'lXWNNNNNNNNNNXd,;:ccccccccccccccccccccccccccccccccccc:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,',ccccccccccc:;,';;;;;;;',ccccc:,,:ccccccccccccccccccccccccccccccc")
        print("cccccccccccc'cXWNNNNNNNNNNNNO:,:cccccccccccccccccccccccccccccccccccccc::::::;;;;;;;;;:;;;;;;;;;;;',:cccccccccc:;,,;;;;;;;;'':cccc:,,:cccccccccccccccccccccccccccccccc")
        print("cccccccccccc,;OWNNNNNNNNNNNNNKo,;cccccccccccccccccccccccccccccccccccccccccccccccccccc:;;;;;;;;;,',:ccccccccc:;,;::;;;;;;;,';ccc:;,;cccccccccccccccccccccccccccccccccc")
        print("cccccccccccc;'dNNNNNNNNNNNNNNNNO:,:cccccccccccccccccccccccccccccccccccccccccccccccc::;;;;;;;;,,,:ccccc:cc:;;;;:c:;;;;;;;,';ccc;,,:ccccccccccccccccccccccccccccccccccc")
        print("ccccccccccccc,:KWNNNNNNNNNNNNNNNXx:,:cccccccccccccccccccccccccccccccccccccccccccc::;;;;;;;;,,,:ccccccc:;;,;:ccc:;;;;;;;;,,cc:,;:ccccccccccccccccccccccccccccccccccccc")
        print("ccccccccccccc:'oNNNNNNNNNNNNNNNNNNKx:,;ccccccccccccccccccccccccccccccccccccccccc:;;;;;;;;,,,:cccccc:;;;;:cccccc:;;;;;::,,:;,,:ccccccccccccccccccccccccccccccccccccccc")
        print("cccccccccccccc;,kNNNNNNNNNNNNNNNNNNNXkc;,:cccccccccccccccccccccccccccccccccccc:;;;;;;;;,,;:cc:;;;;;;;:cccccccc:;;;;:cc;.,;;:ccccccccccccccccccccccccccccccccccccccccc")
        print("ccccccccccccccc,;ONNNNNNNNNNNNNNNNNNNNN0d:;;:cccccccccccccccccccccccccccccccc::;::::c;,,;;;;;;;;;:ccccccccccc:;;::cccc:;:cccccccccccccccccccccccccccccccccccccccccccc")
        print("ccccccccccccccc:,;ONNNNNNNNNNNNNNNNNNNNNNXOo:,,:ccccccccccccccccccccccccccccccccccccc::::::ccccccccccccccccc::::ccccc:ccccccccccccccccccccccccccccccccccccccccccccccc")
        print("cccccccccccccccc:':0WNNNNNNNNNNNNNNNNNNNNNNWKx:,,:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccc::cccccccccccccccccccccccccccccccccccccccccccccccccccccccc")

        time.sleep(.5)
        goodend2()
    elif bird == 0 or cage == 0:
        typewriter2("\n**You realize that 'the way' could be referring to your medallion.")
        typewriter2("\n**You quickly take take our medallion out of your inventory.")
        typewriter2("\n\nNothing is happening, ")
        typewriter2(playername)
        typewriter2(". The clucking won't stop!")
        typewriter2("\n???: LET US SPIT ON DEM!")
        typewriter2("\n\n**A barrage of spit comes at you in all directions.")
        typewriter2("\n\nWHAT IS THIS?")
        badend()
    else:
        print("ERROR")
    
        
#ENDINGS

def end1():
    typewriter2("\n\n@YOU ARE NOW THE RULER OF THE WORLD@")
    typewriter("\n\n@THE END@\n\n")
    time.sleep(2)
    restart()
def end2():
    typewriter2("\n\n**You wake up once more in your sub-conscious**")
    typewriter2("\n\nI'm sorry, ")
    typewriter2(playername)
    typewriter2(", that was your last chance at life.")
    dramatic("\n...")
    typewriter2("\n**'Goodbye, my partner, I'll miss you' Voice-in-your-head says as both you slowly fade away into nothingness\n\n")
    time.sleep(2)
    restart()
def goodend1():
    typewriter2("\n\n**You and your party easily overpower Ornstein and Smough, retrieving the recipe book in the process.")
    typewriter2("\n**Your achievements have spread far and wide.")
    typewriter2("\n**Congratulations, you are now legends in the history of adventurers.")
    time.sleep(2)
    restart()
def badending():
    typewriter2("\n**Scarred physically and mentally, you give up being an adventurer after the quest was completed.")
    time.sleep(2)
    restart()
def goodend2():
    typewriter2("\n\nAn army of Ugandan Knuckles: You know da wae...")
    typewriter2("\nUgandan Knuckles #420: MY BRUDDAS, WE HAVE FOUND OUR QUEEN!")
    typewriter2("\nUgandan Knuckles #042: SHE IS AS BEAUTIFUL AS DEY SAE!")
    typewriter2("\nUgandan Knuckles #025: SHE SMELLS SO NICE!")
    typewriter2("\nUgandan Knuckles #177: SHE SMELLS LIKE DA GREAT EBOLA!")
    typewriter2("\nUgandan Knuckles #013: ALL HEIL DE QUEEN!")
    time.sleep(2)
    restart()
def badend():
    typewriter2("\n???: YOU DO NOT KNOW DA WAE!")
    typewriter2("\n???: YOU ARE NOT OUR QUEEN!")
    time.sleep(2)
    restart()
#RESTART
def restart():
    typewriter2("\n\nWould you like to restart?")
    choice = input(">>> ")
    if choice in yes:
        start()
    elif choice in no:
        quit()
    else:
        print("Yes or No only")
        restart()
start()

