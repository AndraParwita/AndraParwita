#Kingdom Come - Andra Parwita
#2019 year 8


#Update Log:
#01/04/19 0.1 - 0.5 battle & random healing & randome enemies
#02/04/19 0.5 - 0.6 battle & time & bug fixes & fireball
#03/04/19 0.7 more enemies & beta shop & alpha boss & beta travel 
#04/04/19 0.8 & 1.0 - travel update & mountains & Heavy attack - Removed shop & added boss
#05/04/19 1.1 & 1.2 - re-added shop & some easter eggs & damage upgrade
#07/04/19 1.3 - 1.5 added town purpose & keys & bug fixes & easter eggs & random enemy attack type & more health upgrade
#08/04/19 1.6 added loop and bug fixes 
#09/04/19 1.6.1 Bug fixes with health
#25/06/19 1.6.2 Bug fixes with battle
#26/06/19 1.6.2 Added secret options
#27/06/19 1.6.3 - 1.7 Added Super and added beta sprites
Restart = 1




#intro section
while Restart == 1:
    import random # the random module
    Yar = 0
    Hsasl = (0,0,20,25)# enemy heavy attack list
    Hsas = (random.choice(Hsasl))# enemy heavy attack
    Man = 50 # enemy health
    HealingP= 3 # amount of helaing potions
    coins = 10 # how much money you have
    sasl = (0,5,10) # enemy attack damage range
    atklist = (0,5,10,15,20) # how much light attack can do
    atk = (random.choice(atklist))# randomly chooses the attack dmg
    fireball = 40 # fire ball damage
    fireballSCK = 1 # how much uses the fire ball has
    Hlist = (0,0,20,30)
    Hatk = random.choices(Hlist)
    heallist = (10,15,20,25,30) # the amount you can heal up to
    Heal = (random.choice(heallist)) # randomly chooses heal form the heallist
    sas = (random.choice(sasl))# randomly chooses enemy damage
    EXLlst = (1,2,3) # the choices of which enemy it will choose
    EXLf = (random.choice(EXLlst))# chooses a random enemy
    EXL = 1 # The base starting charater to define EXL
    health = 100 # sets health
    Ender = 0
    Tato = 100000
    special = 0
    Specialatk = 70
    health_max = 100
    Multilist = (1,2,3,3,2,1)
    Multi = random.choice(Multilist)


    import sys
    import time # the time module
    Name = input("What is your name? ") # names the charater
    print ("Hello there, " + Name + "!")
    if Name.lower() == "chase": # a promised easter egg for a friend
        print ("Here is your easter egg")
        atklist = (1,1,1,2) #special damage value
        Hlist = (2,2,2,2,2,2,100)
        heallist = (100,95) #special Healing value
    elif Name.lower() == "admin": #Op admin
        print ("Admin mode enabled")
        atklist = (40,50,60)
        Hlist = (70,80,90)
        heallist = (1000,1005)
        coins = 1000
    else:
        print ("")
    time.sleep(2) # pauses for the desired time in seconds
    print ("**You seem to be in a cave left with only a sword and some armour**") # dialogue
    print ("")
    print ("**You start trying to find a way out**")
    time.sleep(2)
    print ("**Something jumps out at you!**")
    print ("")
    time.sleep(1)
    print (" It is too dark to see!")
    print ("")
    print ("")


    if EXLf == 1: #if it is one it will be knight
        EXL = "Barbarian"
        Man = 55
    elif EXLf == 2: #if it is two it will be skeleton
        EXL = "Skeleton"
        Man = 40
    elif EXLf == 3: #if it is three it will be warrior
        EXL = "Zombie"
        Man = 50
        
    EXLspriteNum = 0

    # sprites
    def PlayerSprite():
        print ("      .-.")
        print ("______|=|_____________________________________________________________________________________________")
        print ("   (_/`-`\_)")
        print ("   //\___/\\")
        print ("   <>/   \<> ")
        print ("    \|_._|/  ")
        print ("     <_I_>")
        print ("      ||| ")
        print ("     /_|_\ ")

    def PlayerAtk():
        print ("        .-.")
        print ("________|=|_____________________________________________________________________________________________")
        print ("     (_/`-`\_)     | | | ")
        print ("    //\/ /_/\\   _______")
        print ("    <>/ / \ <>--|______/")
        print ("     /_/_._|  ")
        print ("     <_I I_>")
        print ("      || || ")
        print ("     /_||_\ ")
        
    def PlayerLightAtk():
        print ("        .-.")
        print ("________|=|_______________________________________________________________________________________________")
        print ("     (_/`-`\_)  )___ ")
        print ("    //\/ /_/\\   _______")
        print ("    <>/ / \ <>--|______/")
        print ("     /_/_._|   )---")
        print ("     <_I I_>")
        print ("      || || ")
        print ("     /_||_\ ")

    def PlayerHeal():
        print ("      .-. _==[]")
        print ("______|=|/___\\______________________________________________________________________________________________")
        print ("   (_/`-`\_)__\\")
        print ("   //\___/ ")
        print ("  <> /   \ ")
        print (" //  |_._| ")
        print ("     <_I_>")
        print ("      ||| ")
        print ("     /_|_\ ")

    def PlayerFireball():
        print ("      .-. ")
        print ("______|=|_________________________________________________________________________________________________________")
        print ("   (_/`-`\_)__[] - /      \ ")
        print ("   \\\___/_      - |      |")
        print ("    <>___ _[]   -  \______/")
        print ("     |_._| ")
        print ("     <_I_>")
        print ("      ||| ")
        print ("     /_|_\ ")
        
    def PlayerDamage():
        print ("                                                              .-.   /")
        print ("                                                            __|=#__/")
        print ("                                                           (_/`-`\/_)")
        print ("                                                           //\___/\\")
        print ("                                                           <>/  /\<> ")
        print ("                                                          // |_/_| \\  ")
        print ("                                                             </I_>")
        print ("                                                             /||| ")
        print ("                                                            //_|_\ ")
        print ("_____________________________________________________________________________________________________")

    def diesprite():
        print ("      .-.")
        print ("______|=#_____________________________________________________________________________________________")
        print ("   (_/`-`\_)")
        print ("   //\_____\\")
        print ("   <>|\_____|--")
        print ("  // |_._|/  ")
        print ("     <_I_>")
        print ("      ||| ")
        print ("     /_|_\ ")

    def SuperSprite():
        print ("      .-.    ---\")")
        print ("______|=|________\______________________________\________________________________________________________")
        print ("   (_/`-`\_)__[] |                               \"")
        print ("   \\\___/_      |                               |")
        print ("    <>___ _[]    |_______________________________/")
        print ("     |_._|       /                              /")
        print ("     <_I_>   ___/")
        print ("      |||")
        print ("     /_|_\ ")
        
    def GolemSprite():
        print("")
    def KnightSprite():
        print ("                                                                        <.-.>")
        print ("                                                                       __|=|__")
        print ("                                                                      [_/`-`\/]")
        print ("                                                                      //\/__/\\")
        print ("                                                                      []/   \[] ")
        print ("                                                                       \|_|_|/  ")
        print ("                                                                        (_I_)")
        print ("                                                                         ||| ")
        print ("                                                                        /_|_\ ")
        print ("_____________________________________________________________________________________________________")

    def KnightAtk():
        print ("       <.-.>")
        print ("________|=|___________________________________________________________________________________________")
        print ("     [_/__`\ ]     | | | ")
        print ("    //\/ /_/\\   /_________")
        print ("    []/ / \ []--|_________/")
        print ("     /_/_|_|     \"")
        print ("     (_I I_)")
        print ("      || || ")
        print ("     /_||_\ ")
        
    def KnightDamage():
        print ("                                                             <.-.>  /")
        print ("                                                            __|=#__/")
        print ("                                                           [_/`-`\/_]")
        print ("                                                           //\___/\\")
        print ("                                                          [] /  /\ [] ")
        print ("                                                          || |_/_| || ")
        print ("                                                             (/I_)")
        print ("                                                             /||| ")
        print ("                                                            //_|_\ ")
        print ("_____________________________________________________________________________________________________")

    

    def TitanSprite():
        print ("                                                                            |   _______   |")
        print ("                                                                            |___|_| |_|___|")
        print ("                                                                                |_| |_|")
        print ("                                                                        ________|_| |_|________")
        print ("                                                                       |        |_|_|_|        |  ")
        print ("                                                                       |_______/      \________|")
        print ("                                                                       |  |\    -------    /|  |")
        print ("                                                                       |  | \             / |  |")
        print ("                                                                       |  |  |       /   |  |  |")
        print ("                                                                       |  |  |      /    |  |  |")
        print ("                                                                       |  |  |           |  |  |")
        print ("                                                                       |  |  |___________|  |  |")
        print ("                                                                       |  |  |     T     |  |  |")
        print ("                                                                       |   | |     |     | |   |")
        print ("                                                                       |___| |_____|_____| |___|")
        print ("                                                                             |     |     |")
        print ("                                                                             |_____|_____|")
        print ("                                                                             |     |     |")
        print ("                                                                             /     |     \"")
        print ("                                                                            /______|______\"")
        print ("_____________________________________________________________________________________________________")

    def TitanDamage():
        print ("                                                                            |   _______   |  /")
        print ("                                                                            |___|_| |#|___| /")
        print ("                                                                                |_| |_|    /")
        print ("                                                                        ________|_| |_|___/_____")
        print ("                                                                       |        |_|_|_|  /     |  ")
        print ("                                                                       |_______/      \ /______|")
        print ("                                                                       |  |\    -------/   /|  |")
        print ("                                                                       |  | \         /   / |  |")
        print ("                                                                       |  |  |       /   |  |  |")
        print ("                                                                       |  |  |      /    |  |  |")
        print ("                                                                       |  |  |     /     |  |  |")
        print ("                                                                       |  |  |____/______|  |  |")
        print ("                                                                       |  |  |   / T     |  |  |")
        print ("                                                                       |   | |  /  |     | |   |")
        print ("                                                                       |___| |_/___|_____| |___|")
        print ("                                                                             |/    |     |")
        print ("                                                                             /_____|_____|")
        print ("                                                                            /|     |     |")
        print ("                                                                           / /     |     \"")
        print ("                                                                          / /______|______\"")
        print ("_____________________________________________________________________________________________________")

    def TitanAtk():
        print ("      |   _______   |")
        print ("      |___|_| |_|___|")
        print ("          |_| |_|")
        print ("  ________|_| |_|________")
        print (" |        |_|_|_|        |\  ")
        print (" |_______/      \________| \"")
        print (" |  |\    -------    /  \   \"")
        print (" |  | \             /    \   \"")
        print (" |  |  |       /   |      \   \"")
        print (" |  |  |      /    |       \   \"")
        print (" |  |  |           |        \   \           |   |    |    |    |")
        print (" |  |  |___________|         \   \        _______________________")
        print ("_|  |__|     T     |__________\___\_ ____/                       \______________________________________")
        print (" |   | |     |     |        |_|_____|____                        |")
        print (" |___| |_____|_____|                     \_______________________/")
        print ("       |     |     |")
        print ("       |_____|_____|")
        print ("       |     |     |")
        print ("       /     |     \"")
        print ("      /______|______\"")

    
        
    def ImpSprite():
        print("                                                                 <_>")
        print("                                                                 (=)")
        print("                                                                /\_/\"")
        print("                                                                 / \"")
        print ("_____________________________________________________________________________________________________")
              
    def ImpAtk():
        print ("____________ /_______________________________________________________________________________________")
        print("     <_>   - /")
        print("     (=)  - /")
        print("    /\_/---/")
        print("     / \"")
        

    def ImpDamage():
        print("                                                                 <_>/")
        print("                                                                 (=/")
        print("                                                                /\//\"")
        print("                                                                 / \"")
        print ("_____________________________________________________________________________________________________")


    def SirConSprite():
        print ("")
        print ("                                                             \\           _!_")
        print ("                                                              \\         /___\"")
        print ("                                                               \\        [+++]")
        print ("                                                                \\    _ _\^^^/_ _")
        print ("                                                                 \\/ (    '-'  ( )")
        print ("                                                                 /( \/ | {&}   /\ \"")
        print ("                                                                   \  / \     / _> )")
        print ("                                                                    '`   >:::;-'`'''-.")
        print ("                                                                        /:::/         \"")
        print ("                                                                       /  /||   {&}   |")
        print ("                                                                      (  / (\         /")
        print ("                                                                      / /   \'-.___.-'")
        print ("                                                                    _/ /     \ \"")
        print ("                                                                   /___|    /___|")
        print ("_____________________________________________________________________________________________________")

    def SirConAtk():
        print ("")
        print ("                                                                           _!_")
        print ("                                                                          /___\"")
        print ("                                                                          [+++]")
        print ("                                                                       _ _\^^^/_ _")
        print ("                                                                     (    '-'  ( )")
        print ("                                                _______________|  ___/ | {&}   /\ \"")
        print ("                                               \_______________ }-[ ___  / \     / _> )")
        print ("                                                               |    '`   >:::;-'`'''-.")
        print ("                                                                        /:::/         \"")
        print ("                                                                       /  /||   {&}   |")
        print ("                                                                      (  / (\         /")
        print ("                                                                      / /   \'-.___.-'")
        print ("                                                                    _/ /     \ \"")
        print ("                                                                   /___|    /___|")
        print ("_____________________________________________________________________________________________________")

    def SirConDamage():
        print ("")
        print ("                                                             \\           _!_")
        print ("                                                              \\         /#__\  /")
        print ("                                                               \\        [+++] /")
        print ("                                                                \\    _ _\^^^// _")
        print ("                                                                 \\/ (    '-'/ ( )")
        print ("                                                                 /( \/ | {&}/  /\ \"")
        print ("                                                                   \  / \  /  / _> )")
        print ("                                                                    '`   >/::;-'`'''-.")
        print ("                                                                        //::/         \"")
        print ("                                                                       // /||   {&}   |")
        print ("                                                                      (/ / (\         /")
        print ("                                                                      / /   \'-.___.-'")
        print ("                                                                    _/ /     \ \"")
        print ("                                                                   //__|    /___|")
        print ("_____________________________________________________________________________________________________")
        


        

    def KingAtk():
        print ("     \ ++ / ")
        print ("      |__|")
        print ("   ___|--|___             |  |     |   | | |")
        print ("__/(_/`--`\_)\______|____|_________|__|___|________________________________________________________")
        print (" | //\____/\\____   |__________________________")
        print (" | <>___[]------]----| -----------------------  \ ")
        print (" |   /_||_\   |     |___________________________/")
        print (" |   |_||_|   |     |")
        print (" |   |_||_|   |")
        print (" |   | || |   |  ")
        print (" |___/_||_\ __|")
    
    def King():
        print ("                                                            \ ++ / ")
        print ("                                                             |__|")
        print ("                                                           __|--|___")
        print ("                                                         /(_/`--`\_)\"")
        print ("                                                        | //\____/\\ |")
        print ("                                                        | <> |  |<>  | ")
        print ("                                                        | \\/_||_\// |")
        print ("                                                        |   |_II_|   |")
        print ("                                                        |   |_||_|   |")
        print ("                                                        |   | || |   |  ")
        print ("                                                        |___/_||_\ __|")
        print ("_____________________________________________________________________________________________________")
    
    def KingDamage():
        print ("                                                            \ ++ / ")
        print ("                                                             |_#|")
        print ("                                                           __|--|_/_")
        print ("                                                         /(_/`--`/_)\"")
        print ("                                                        | //\___//\\ |")
        print ("                                                        | <> | /  |<>| ")
        print ("                                                        | \\/_/|_\// |")
        print ("                                                        |   |/II_|   |")
        print ("                                                        |   /_||_|   |")
        print ("                                                        |  /| || |   |  ")
        print ("                                                        |___/_||_\ __|")
        print ("_____________________________________________________________________________________________________")

    def ShopKeepSprite():
        print("                                                                        __")
        print("                                                                       |  |")
        print("                                                                      _|__|_  ")
        print("                                                                       |''|  ")
        print("                                                                     []|--|[]")
        print("                                                                    // |__| \\")
        print("                                                                       //\\")
        print("                                                                       ||||")
        print("_____________________________________________________________________________________________________")

    def ShopKeepDamage():
        print("                                                                        __")
        print("                                                                       |  |    *Yawn*")
        print("                                                                      _|_-|_  ")
        print("                                                                       |''|  ")
        print("                                                                     []|--|[]")
        print("                                                                    // |__| \\")
        print("                                                                       //\\")
        print("                                                                       ||||")
        print("_____________________________________________________________________________________________________")

    def ShopKeepAtk():
        print("     __")
        print("    |  |")
        print("   _|\/|_  ")
        print("    |''|         -    ___")
        print("  []|--|[]===== -    |___|")
        print(" //_|__|_________-_______________________________________________________________________________")
        print("    //\\")
        print("    ||||")

    def MysManSprite():
        print("                                                                            ______    ")      
        print("                                                                           /   \  /  ")     
        print("                                                                      /\\ |     ||  ")     
        print("                                                                    ////\\|     ||  ")     
        print("                                                                  ////   \\ ___//|  ")     
        print("                                                                 ///      \\     \ ")     
        print("                                                                ///       |\\     \  ")   
        print("                                                               //  /\\    | \\  \  \ ")    
        print("                                                               /  ///\\   |  \\  \  \   ")
        print("                                                                 //// \\ /|   \\ /  /   ")
        print("                                                                ///    \\ |    \/  /    ")
        print("                                                               //       \\|     \\/|     ")
        print("                                                               /         \|________|     ")
        print("                                                                          |   ||   \     ")
        print("                                                                          |   ||   |\     ")
        print("                                                                          |   ||   | \    ")
        print("                                                                          |   ||   |  \   ")
        print("                                                                          |   ||   |   \  ")
        print("                                                                          |   ||   | ___\ ")
        print("                                                                         /____||____\ ")
        print("_____________________________________________________________________________________________________")

    def MysManDamage():
        print("                                                                            ______    ")      
        print("                                                                           /   \ #/  ")     
        print("                                                                      /\\ |     ||  ")     
        print("                                                                    ////\\|     ||  ")     
        print("                                                                  ////   \\ ___//|  ")     
        print("                                                                 ///      \\     \ ")     
        print("                                                                ///       |\\     \  ")   
        print("                                                               //  /\\    | \\  \  \ ")    
        print("                                                               /  ///\\   |  \\  \  \   ")
        print("                                                                 //// \\ /|   \\ /  /   ")
        print("                                                                ///    \\ |    \/  /    ")
        print("                                                               //       \\|     \\/|     ")
        print("                                                               /         \|________|     ")
        print("                                                                          |   ||   \     ")
        print("                                                                          |   ||   |\     ")
        print("                                                                          |   ||   | \    ")
        print("                                                                          |   ||   |  \   ")
        print("                                                                          |   ||   |   \  ")
        print("                                                                          |   ||   | ___\ ")
        print("                                                                         /____||____\ ")
        print("_____________________________________________________________________________________________________")




















    #battle section


    def Battle(): # defines battle
        global Man #gets Man outside of the definition
        while Man > 0:
            global EXL #gets EXL outside of the definition
            global health #gets health outside of the definition
            global atklist #gets atklist outside of the definition
            global heallist #gets heallist outside of the definition
            global HealingP #gets HealingP outside of the definition
            global fireball #gets fireball outside of the definition
            global fireballSCK #gets fireballSCK outside of the definition
            global Hlist #gets Hlist outside of the definition
            global Hatk #gets Hatk outside of the definition
            Heal = (random.choice(heallist)) # chooses how much you heal randomly each turn
            atk = (random.choice(atklist)) # chooses Damage of light attack randomly
            Hatk = (random.choice(Hlist)) # choose damage of Heavy attack randomly
            global Ender
            global Multi
            global Multilist
            global special
            global EXLspriteNum
            global health_max
            if special == 100:
                print ()
            elif special < 100:
                special = special + 10 
            
            

            print ("") #line skip
            print ("")
            print ("")
            print ("")
            print ("")
            print ("")
            print ("")
            print ("")
            print ("|Your health is at " + str(health) +"| The Enemy health is at " + str(Man) + "|")
            print ("")
            time.sleep(1)
            print ("")
            print ("")
            time.sleep(1)
            PlayerSprite()
            if EXLspriteNum == 10:
                King()
            elif EXLspriteNum == 9:
                SirConSprite()
            elif EXLspriteNum == 8:
                KnightSprite()
            elif EXLspriteNum == 7:
                ImpSprite()
            elif EXLspriteNum == 6:
                TitanSprite()
            elif EXLspriteNum == 5:
                ShopKeepSprite()
            else:
                print("")
            print ("| Super at " + str(special) + "% | [super]")
            print("|  Multi-light [80% to hit][Light] | Fireball [" + str(fireballSCK) + " Left][100% to hit] |")
            oof = input  ("|  Heavy Attack [50% chance to hit][Heavy] | Heal [" + str(HealingP) + " left] | ") # the choices, Input light,heavy,fireball or heal to use
            print("")
            
                
            if oof.lower() == "light": # if you choose light it will print the green and it checks if you have enough health and if the enemy has enough health to continue
                    atk = random.choice(atklist)
                    Catk = atk*Multi
                    Man = (Man - atk)
                    PlayerLightAtk()
                    time.sleep(1)
                    print("")
                    if atk > 0:
                        if EXLspriteNum == 10:
                           KingDamage()
                        elif EXLspriteNum == 9:
                            SirConDamage()
                        elif EXLspriteNum == 8:
                            KnightDamage()
                        elif EXLspriteNum == 7:
                             ImpDamage()
                        elif EXLspriteNum == 6:
                             TitanDamage()
                        elif EXLspriteNum == 5:
                             ShopKeepDamage()
                        else:
                            print("")
                        print ("You deal " + str(atk) + " Damage!")
                        print ("They have " + str(Man) + " Health")
                    elif atk == 0:
                        print ("You missed!") 
                        print ("They have " + str(Man) + " Health")
                    else:
                        print("")   
                    time.sleep(2)
                    Gameover()
                    Gameover()
                    if Ender == 0:
                        if Man >= 1: # check to end battle or not
                            ALK()
                            Battle()
                        elif Man < 1:
                            dedEXL()
                        else:
                            Battle()
                    elif Ender == 1:
                        Travel()
                        
            if oof.lower() == "tato": # if you choose Tato(secret) it will print the green and it checks if you have enough health and if the enemy has enough health to continue
                    atk = random.choice(atklist)
                    Man = (Man - Tato)
                    time.sleep(2)
                    print("You take the lengendary Tato out your pocket")
                    print ("")
                    time.sleep(1)
                    print ("You throw the legendary tato at the " + (EXL) + " and it deals " + str(Tato) + " Damage!")
                    print ("")
                    print ("They have died [" + str(Man) + " health left]")
                    time.sleep(2)
                    Gameover()
                    Gameover()
                    if Ender == 0:
                        if Man >= 1: # check to end battle or not
                            ALK()
                            Battle()
                        elif Man < 1:
                            dedEXL()
                        else:
                            Battle()
                    elif Ender == 1:
                        Travel()
                        
            elif oof.lower()  == "super":
                if special < 100:
                    print ("Charge Super to 100!")
                    Battle()
                elif special == 100:
                    Man = (Man - Specialatk)
                    special = special - 100
                    SuperSprite()
                    time.sleep(2)
                    if EXLspriteNum == 10:
                       KingDamage()
                    elif EXLspriteNum == 9:
                        SirConDamage()
                    elif EXLspriteNum == 8:
                        KnightDamage()
                    elif EXLspriteNum == 7:
                         ImpDamage()
                    elif EXLspriteNum == 6:
                         TitanDamage()
                    elif EXLspriteNum == 5:
                         ShopKeepDamage()
                    else:
                       print("")
                    print ("You deal " + str(Specialatk) + " Damage!")
                    print ("They have " + str(Man) + " Health")
                    time.sleep(2)
                    Gameover()
                    if Ender == 0:
                        if Man >= 1: # check to end battle or not
                            ALK()
                            Battle()
                        elif Man < 1:
                            dedEXL()
                        else:
                            Battle()
                    elif Ender == 1:
                        Travel()
                    
                

            elif oof.lower() == "heavy": # if you choose heavy it will print the green and it checks if you have enough health and if the enemy has enough health to continue
                    Hatk = random.choice(Hlist)
                    Multi = random.choice(Multilist)
                    Man = (Man - Hatk)
                    PlayerAtk()
                    time.sleep(1)
                    print("")
                    if Hatk > 0:
                        if EXLspriteNum == 10:
                           KingDamage()
                        elif EXLspriteNum == 9:
                            SirConDamage()
                        elif EXLspriteNum == 8:
                            KnightDamage()
                        elif EXLspriteNum == 7:
                             ImpDamage()
                        elif EXLspriteNum == 6:
                             TitanDamage()
                        elif EXLspriteNum == 5:
                             ShopKeepDamage()
                        else:
                            print("")
                        print ("You hit " + str(Multi) + " Times")
                        print ("You deal " + str(Hatk) + " Damage!")
                        print ("They have " + str(Man) + " Health")
                    elif Hatk == 0:
                        print ("You missed!") 
                        print ("They have " + str(Man) + " Health")
                    else:
                        print("")
                    time.sleep(2)
                    Gameover()
                    Gameover()
                    if Ender == 0:
                        if Man >= 1: # check to end battle or not
                            ALK()
                            Battle()
                        elif Man < 1:
                            dedEXL()
                        else:
                            Battle()
                    elif Ender == 1:
                        Travel()

            elif oof.lower() == "heal": #if you choose heal
                if health > health_max: # if  you have over 90 health you cannot heal/ this sends you back if you have too much health
                    print ("You have enough health")
                    if Man >= 1: # check to end battle or not
                        Battle()
                    elif Man < 1:
                            dedEXL()
                    else:
                        Battle()
                   
                        
                elif HealingP <= 0: # check if you have enough healing potions/ if under or equal 0 send you back 
                    print ("Not enough Heals")
                    Gameover()
                    if Man >= 1:# check to end battle or not
                        Battle()
                    elif Man < 1:
                            dedEXL()
                    else:
                        Battle()
                
                elif health < health_max: # check if you have enough health to heal
                    HealingP = (HealingP - 1)#takes a healing
                    health = (health + Heal)#adds health
                    PlayerHeal()
                    time.sleep(2)
                    print ("You healed " + str(Heal) + "!")
                    print ("Your health is " + str(health))
                    Gameover()
                if Man >= 1: # check to end battle or not
                    Battle()
                    
            elif oof.lower() == "die":
                diesprite()
                print ("You stab yourself with your sword....")
                time.sleep(2)
                health = 0
                Gameover()
                
                    
            elif oof.lower() == "fireball":# if you choose fireball
                if fireballSCK <= 0: # checks if you have enough fireball scrolls
                    print ("Out of fireball scrolls")
                    Battle()#sends you back to choosing what to use

                elif fireballSCK > 0: #if you have more than 0 fireball scrolls
                    Man = (Man - fireball)#takes enemy health away
                    PlayerFireball()
                    time.sleep(1)
                    if EXLspriteNum == 10:
                       KingDamage()
                    elif EXLspriteNum == 9:
                        SirConDamage()
                    elif EXLspriteNum == 8:
                        KnightDamage()
                    elif EXLspriteNum == 7:
                         ImpDamage()
                    elif EXLspriteNum == 6:
                         TitanDamage()
                    elif EXLspriteNum == 5:
                         ShopKeepDamage()
                    else:
                       print("")
                    fireballSCK = (fireballSCK - 1)
                    print ("You dealt " + str(fireball) + " damage!") 
                    print ("They have " +str(Man) + " Health")
                    time.sleep(1)
                    Gameover()
                    if Ender == 0:
                        if Man >= 1: # check to end battle or not
                            ALK()
                            Battle()
                        elif Man < 1:
                            dedEXL()
                        else:
                            Battle()
                    if Ender == 1:
                        Travel()
            else:
                print("")
                   

    Coinslist = (10,20,) #how much coins you can earn (10 or 20)
    CoinsM = 10 # default coins

    def ALK(): # enemy turn
        global health # gets health outside of the definition
        global sasl # gets sasl outside of the definition
        global EXL # gets EXL outside of the definition
        global Hsasl
        Hsas = (random.choice(Hsasl))
        sas = (random.choice(sasl))# chooses a random damage to deal
        Chance()
        time.sleep(2)
        print ("You have " + str(health) + " Health Left")

    def dedEXL(): # checks if enemy is dead
        time.sleep(3)
        global special
        special = 0
        print ("")
        global EXL # gets EXL out of def
        global coins # gets coins of of def
        global Coinslist # gets the coinlist of of def
        global health
        global HealingP
        global fireballSCK
        print ("You killed the " + EXL + "!!") #dialouge
        print ("You got plus 1 Heal!")
        fireballSCK = 1 #puts your fireball scrolls back to normal
        HealingP = (HealingP + 1) #adds one healing potion
        CoinsM = random.choice(Coinslist) #chooses how much money you get
        coins = (CoinsM + coins) #add the coins to your coins
        print ("+" + str(CoinsM) + " Coins! You now have " + str(coins) + " coins!")
        time.sleep(1)
        

    def Gameover(): #defines gameover
        global Man
        global Restart
        global Ender
        global health # gets healh out of def
        if health <= 0: # checks if you have under or equal to zero health
            print ("Game Over!")
            Merp = input ("Play again?[yes or no]")#if you want to restart
            if Merp == "yes":#if yes ??
                Ender = 1
                Restart = 1
                Man = -1
                print ("{{LOL do it manually, also Ima break now}}")

            elif Merp == "no": # if no exits
                Restart = 0
                sys.exit()
            

    def Chance(): # enemy attack chances & what type of attack
                global EXL
                global sas
                global Hsas
                global health
                global Man
                global EXLspriteNum
                Chelist = (0,0,1,2)
                Che = random.choice(Chelist)
                if Che == 1:
                    Hsas = random.choice(Hsasl)
                    health = (health - Hsas)
                    print ("")
                    print (EXL + " did a Heavy attack!")
                    print ("") # dialogue
                    if EXLspriteNum == 10:
                        KingAtk()
                    elif EXLspriteNum == 9:
                        SirConAtk()
                    elif EXLspriteNum == 8:
                         KnightAtk()
                    elif EXLspriteNum == 7:
                         ImpAtk()
                    elif EXLspriteNum == 6:
                         TitanAtk()
                    elif EXLspriteNum == 5:
                         ShopKeepAtk()
                    else:
                        print("")
                    time.sleep(2)
                    if Hsas > 0:
                        print ("The " + EXL + " dealt " + str(Hsas) + " Damage to you!")
                        PlayerDamage()
                    elif Hsas == 0:
                        print ("The " + EXL + " missed!")
                    else:
                        print("")   
                    time.sleep(2)
                elif Che == 0:
                    sas = random.choice(sasl)
                    health = (health - sas)
                    print("")
                    print (EXL + " did a light attack!")
                    print ("") # dialogue
                    if EXLspriteNum == 10:
                       KingAtk()
                    elif EXLspriteNum == 9:
                        SirConAtk()
                    elif EXLspriteNum == 8:
                         KnightAtk()
                    elif EXLspriteNum == 7:
                         ImpAtk()
                    elif EXLspriteNum == 6:
                         TitanAtk()
                    elif EXLspriteNum == 5:
                         ShopKeepAtk()
                    else:
                       print("")
                    time.sleep(2)
                    if sas > 0:
                        print ("The " + EXL + " dealt " + str(Hsas) + " Damage to you!")
                        PlayerDamage()
                    elif sas == 0:
                        print ("The " + EXL + " missed!")
                    else:
                        print("")
                    time.sleep(2)
                elif Che == 2:
                        Man = (Man + 10)
                        print("")
                        print (EXL + " Healed 10 health")
                        print("")
                        time.sleep(1)
                        print ("It now has " + str(Man))
                        



    #travel section
                


    skip = input("skip first battle? [yes or no]")#skips the first fight

    if skip.lower() == "yes": #if you want to skip(hidden cheat to skip first part)
        print("")
    else:
        Battle()#starts the battle
    skop = input("skip dialogue?[yes or no]")
    if skop.lower() == "yes":
        print ("")
    else:
        time.sleep(2)
        print ("") # dialogue
        print ("**You wipe your sword and continue trying to find a way out**")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        time.sleep(2)
        print ("**You finally find the exit**") # more dialogue
        time.sleep(2)
        print ("")
        print ("       ___________")
        print ("      / | -       \"")
        print ("     /__| -      { \"")
        print ("    / | | \    {    \"")
        print ("   /            {   }\"")
        print ("  /              | |  \"")
        print (" /   _____       | |   \"")
        print ("/  __|_|_|_______|_|__  \"")
        print ("**Your eyes take time to adjust to the sunlight**")
        print ("")
        print ("")
        time.sleep(2)
        print ("**You see a brown horse next to a carrage**") # even more
        print ("")
        print ("")
        print ("")
        print ("       _ ____")
        print ("     /( ) _   \"")
        print ("    / //   /\` \,  ||--||--||-")
        print ("      \|   |/  \|  ||--||--||-")
        print ("~^~^~^~~^~~~^~~^^~^^^^^^^^^^^^")
        print ("** You proceed to calm it down and ride ride it**")
        time.sleep(4)
        print ("")
        print ("")
        print ("")
        



    def Travel(): # travelling
        global Ender
        if Ender == 0:
            global HealingP # gets the stuff from out the definition if it has global at the start
            global coins # gets coins
            global EXL # gets EXL(enemy name)
            global sasl # #gets enemy attack list
            global sas # gets enemy attack damage
            global Man # gets enemy health
            global Name # gets your name
            print ("") #dialogue
            print ("")
            print ("")
            print ("")
            print ("")
            
            place = "town"
            print ("Where do you want to go?")
            place = input("| Town  |  Castle  |  Shop  |  Mountains |") # chooses where you want to go
            if place.lower() == "town": # if you choose town
                print ("")#dialogue
                print ("Travelling...")
                time.sleep(3)
                print ("**you arrive at the town**")
                print ("")
                print ("")
                print ("               ~         ~~          __")
                print ("       _T      .,,.    ~--~ ^^")
                print (" ^^   // \                    ~")
                print ("      ][O]    ^^      ,-~ ~")
                print ("   /''-I_I         _II____")
                print ("__/_  /   \ ______/ ''   /'\_,__")
                print ("  | II--'''' \,--:--..,_/,.-{ },")
                print ("; '/__\,.--';|   |[] .-.| O{ _ }")
                print (":' |  | []  -|   ''--:.;[,.'\,/")
                print ("'  |[]|,.--'' '',   ''-,.    |")
                print ("  ..    ..-''    ;       ''. '")
                print ("")
                print ("")
                time.sleep(1)
                print ("**nothing seems to be here**") # town is empty!!
                Explore()#loot the place
                Travel()
                
            elif place.lower() == "mountains": # if you choose mountains
                print ("Travelling...")
                SpawnC()# gets info from spawnc which chooses a random enemy
                print ("")
                time.sleep(3)
                sasl = (0,5,10,0)# random enemy damage list
                sas = (random.choice(sasl))#choose random enemy damage
                print ("BRRR... COLD!") # dialogue
                print ("")
                print ("")
                print ("                    _    .  ,   .           .")
                print ("    *  / \_ *  / \_      _  *        *   /\'__        *")
                print ("      /    \  /    \,   ((        .    _/  /  \  *'.")
                print (" .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.")
                print ("    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *")
                print ("  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \"")
                print (" /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-")
                print ("/      `.  / /       `.~-^=-=~=^=.-'      '-._ `._")
                print ("")
                time.sleep(2)
                if SpawnType == 1: #types of enemy and health
                    EXL = "Frost Warrior"
                    Man = 50
                elif SpawnType == 2:
                    EXL = "Ice Imp"
                    Man = 20
                elif SpawnType == 3:
                    EXL = "Cold Knight"
                    Man = 60
                elif SpawnType == 4:
                    EXL = "Snow Golem"
                    Man = 75
                elif SpawnType == 5:
                    EXL = "Ice Titan"
                    Man = 115
                print ("A " + EXL + " Attacks!")# what enemy attacks you
                Battle()# starts the battle
                Travel()# back to travel menu
                
            elif place.lower() == "castle": #boss castle
                print ("")
                print ("")
                print ("")
                print ("")
                print ("                    |>>>                        |>>>")
                print ("                    |                           |")
                print ("                _  _|_  _                   _  _|_  _")
                print ("               | |_| |_| |                 | |_| |_| |")
                print ("               \  .      /                 \ .    .  /")
                print ("                \    ,  /                   \    .  /")
                print ("                 | .   |_   _   _   _   _   _| ,   |")
                print ("                 |    .| |_| |_| |_| |_| |_| |  .  |")
                print ("                 |   . |  .     . .   .  ,   |.    |")
                print ("     ___----_____| .   |.   ,  _______   .   |   , |---~_____")
                print ("_---~            |     |  .   /+++++++\    . | .   |         ~---_")
                print ("                 |.    | .    |+++++++| .    |   . |              ~-_")
                print ("              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_")
                print ("     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__")
                print ("-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~")
                print ("")
                print ("")
                KeyTest() #if you have a key
                print ("**A large knight stops you**")
                time.sleep(1)
                print ("Stop right there!")
                SirCon()
                print ("")
                print ("**The knight's head rolls to the king's throne**")
                time.sleep(2)
                KingDia()
                Boss()# the bosses stats and health etc, and the boss battle
                End()# ending
                
            elif place.lower() == "shop": # the shop (only sells potions for now)
                shoop()#the shop menu
                shoopb() # secret boss
                Travel()#the travel menu
                
            else:
                Travel()#the travel menu
        if Ender == 1:
            print("")






























     #spawn section       




    def SpawnC():#chooses a random enemy
        global SpawnType #global again
        global Spawntypelist
        global EXLspriteNum
        Spawntypelist =(1,2,3,4,5)# the numbers which are assigned to enemies
        SpawnType = (random.choice(Spawntypelist))#chooses a random enemy

        if SpawnType == 1: #types of enemy and health
            EXL = "Frost Warrior"
            Man = 50
            EXLspriteNum = 8
        elif SpawnType == 2:
            EXL = "Ice Imp"
            Man = 20
            EXLspriteNum = 7
        elif SpawnType == 3:
            EXL = "Cold Knight"
            Man = 60
            EXLspriteNum = 8
        elif SpawnType == 4:
            EXL = "Snow Golem"
            Man = 75
        elif SpawnType == 5:
            EXL = "Ice Titan"
            Man = 115
            EXLspriteNum = 6
                       
                       
    def Boss(): # the boss stats
        global EXL# to get the variables out of the definitions/ Enemy type/name
        global Man # Enemy health
        global sasl # enemy attack list
        global sas # enemy attack
        global Hsas
        global EXLspriteNum
        global Hsasl
        EXL = "King Indieus" #name of boss
        Man = 200 #health of boss
        sasl = (0,20,30,20) #damage of boss
        Hsasl = (0,50,60,0)
        Hsas = random.choice(Hsasl)
        sas = (random.choice(sasl))#randomly chooses his damage
        EXLspriteNum = 10
        Battle()#starts the boss battle
        
    def SirCon(): #the guard
        global EXL# to get the variables out of the definitions/ Enemy type/name
        global Man # Enemy health
        global sasl # enemy attack list
        global sas # enemy attack
        global Hsas 
        global Hsasl
        global EXLspriteNum
        EXL = "Knight Overlord" #name 
        Man = 120 #health 
        sasl = (0,0,20,10,) #damage 
        sas = (random.choice(sasl))#randomly chooses his damage
        Hsasl = (0,0,40,50,0)
        Hsas = random.choice(Hsasl)
        EXLspriteNum = 9
        Battle()#starts the battle


























    # shop section
        
        
    Anger = 0 #shopkeeper boss variable
    def AngryBoi():
        print("                __")
        print("               |  |")
        print("              _|\/|_  ")
        print("               |''|  ")
        print("             []|  |[]====-")
        print(" ___________ //|__|___________")
        print("|    _           ___    ___  |")
        print("|   |_   |  |   |   |  |   | |")
        print("|     |  |--|   |   |  |___| |")
        print("|    _|  |  |   |___|  |     |")
        print("")
        

    def shooppotion():# defines buying potions
        global Anger # how angry the shopkeep is
        global HealingP # gets heals out of def
        global coins # gets coins out of def
        coins = (coins - 10) # takes coins away
        Anger = (Anger - 1) # removes anger (5 anger used to make shop keeper boss)
        HealingP = (HealingP + 1) # adds a healing
        time.sleep(2)
        print ("     ")
        print ("     _  ")
        print ("    |>|")
        print ("  __|<|__")
        print (" |      |")
        print ("| <><><> |")
        print (" |______|")
        print ("")
        print ("You now have " + str(HealingP) + " healing potions!") #dialouge
        print ("you have " + str(coins) + " coins")
        time.sleep(2)
        
    def Look(): #if not enough coins
        global Anger # gets anger out of def
        global coins # gets coins out of def
        if coins >= 10: #if you have more than 10 coins
            shooppotion() #sends you the the potion definition(above)
        elif coins < 10:#if under 10 coins
            time.sleep(2)
            AngryBoi()
            print ("Not enough money, Get OUT!")#dialouge
            time.sleep(2)
            Anger = (Anger + 1)#adds anger

    def Look2(): #if not enough coins
        global Anger # gets anger out of def
        global coins # gets coins out of def
        if coins >= 30: #if you have more than 30 coins
            shoopdamage() #sends you the the potion definition(below)
        elif coins < 30:#if under 30 coins
            time.sleep(2)
            AngryBoi()
            print ("Not enough money, Get OUT!")#dialouge
            time.sleep(2)
            Anger = (Anger + 1)#added anger


    def look3(): #if not enough coins
        global Anger # gets anger out of def
        global coins # gets coins out of def
        if coins >= 20: #if you have more than 20 coins
            shoopkey() #sends you the the potion definition(below)
        elif coins < 20:#if under 20 coins
            time.sleep(2)
            AngryBoi()
            print ("Not enough money, Get OUT!")#dialouge
            time.sleep(2)
            Anger = (Anger + 1)#added anger

    def look4():
        global Anger # gets anger out of def
        global coins # gets coins out of def
        if coins >= 50: #if you have more than 50 coins
            shoophealth() #sends you the the potion definition(below)
        elif coins < 50:#if under 50 coins
            time.sleep(2)
            AngryBoi()
            print ("Not enough money, Get OUT!")#dialouge
            Anger = (Anger + 1)#added anger
            time.sleep(2)


    def shoop():#shop menu
        global coins#gets coins out of def
        global Anger#gets the anger out of def
        time.sleep(1)
        print("")
        print("")
        print("")
        print("")
        print("                __")
        print("               |  |")
        print("              _|__|_  //")
        print("               |''|  //")
        print("             []|  |[]/")
        print(" ___________ //|__|___________")
        print("|    _           ___    ___  |")
        print("|   |_   |  |   |   |  |   | |")
        print("|     |  |--|   |   |  |___| |")
        print("|    _|  |  |   |___|  |     |")
        print("")
        print ("Welcome to the shop")# dialouge
        time.sleep(1)
        print("")
        print ("what would you like?")
        print ("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print ("you have " + str(coins) + " coins")
        print ("|  Press Enter to exit!  |")
        print ("|  Potions [cost: 10 coins]  |  Increase Damage [damage][cost: 30 coins]  |")
        Option = input("|  Castle Key [key][cost: 20 coins]  |  Increase health [health][cost: 50]  |")
        Option = Option.lower()
        if Option == "potions":#if you say potions leads you to the look definiton(above)
            Look()
        elif Option ==  "damage":#if you say damage leads you to the second look definition(above)
            Look2()
        elif Option == "key": #if you say key leads you to the def above
            look3()
        elif Option == "health":
            look4()
        elif Option == "donate":
            Anger = Anger - coins
            coins = coins - coins
            print ("Thanks!")
            time.sleep(1)
            Travel()

        else: #if you say anything else send you back to travel menu
            Travel()

    def End():# the ending
        global Ender
        global Name
        print ("")
        print ("")
        print ("Horray you won!!!!")# dialouge
        time.sleep(2)
        print ("")
        print ("You are now King " + Name + "!")
        Merp = input ("Play again?[Yes or No]")
        if Merp == "yes":# if yes?
            Ender = 1
            Travel()
            
        elif Merp == "no":# if no exits game
            sys.exit()
        
    def shoopb():
        global Anger
        if Anger == 5:
            global EXL# to get the variables out of the definitions/ Enemy type
            global Man # gets enemy health
            global sasl # gets enemy attack list
            global sas # gets enemy attack
            global Hsasl
            global Hsas
            global coins
            global EXLspriteNum
            EXLspriteNum = 5
            EXL = "Deran the Shopkeeper" #name of boss
            Man = 400 #health of boss
            sasl = (0,0,40,30,40,50,0)#damage of boss
            Hsasl = (0,80,90,0,)
            sas = (random.choice(sasl))#randomly chooses his damage
            Hsas = (random.choice(Hsasl))#randomly chooses his damage
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("THAT'S IT, TIME FOR YOU TO DIE!!!")
            time.sleep(1)
            Battle()
            Anger = 0
            coins = (coins + 1000)
            Travel()
            
    def shoopdamage():
        global Specialatk
        global Anger #secret boss meter
        global atklist # gets the dmglist
        global atk # gets the dmg
        global Hlist # gets the Heavy dmg list
        global Hatk # get the heavy dmg
        global coins # gets coins out of def
        global fireball #gets the fireball
        coins = (coins - 30) # takes coins away
        Anger = (Anger - 2) # removes anger (5 anger used to make shop keeper boss)
        Hlist = (0,0,35,45)# the new list for heavy atk
        atklist = (0,15,20,25,30)# the new list for atk
        fireball = (fireball + 10) #more damage for fireball
        Specialatk = (Specialatk + 20)
        time.sleep(2)
        print ("")
        print ("   |___________________")
        print ("===|__________________/")
        print ("   |")
        print ("")
        print ("You now have a Great Sword!")
        print ("You now have more damage!") #dialouge
        print ("")
        print ("you have " + str(coins) + " coins")
        time.sleep(2)

    Key = 0

    def shoopkey():
        global coins
        global Anger #secret boss meter
        global Key
        coins = (coins - 20) # takes coins away
        Anger = (Anger - 3) # removes anger (5 anger used to make shop keeper boss)
        Key = (Key + 1)
        time.sleep(2)
        print ("    __")
        print ("   |  |")
        print ("  | <> |")
        print ("   |  |")
        print ("    ||")
        print ("    ||_")
        print ("    | _|")
        print ("    |__|")
        print ("")
        print ("You now have the castle key") #dialouge
        print ("you have " + str(coins) + " coins")
        time.sleep(2)
        


    def shoophealth():
        global coins
        global Specialatk
        global Anger #secret boss meter
        global health
        global Yar
        global health_max
        coins = (coins - 50) # takes coins away
        Anger = (Anger - 3) # removes anger (5 anger used to make shop keeper boss)
        health = 200
        health_max = 200
        Yar = 1
        time.sleep(2)
        print ("      .-.")
        print ("    __|=|__")
        print ("   (_/`-`\_)")
        print ("   //\___/\\")
        print ("   <>/   \<> ")
        print ("    \|_._|/  ")
        print ("     <_I_>")
        print ("      ||| ")
        print ("     /_|_\ ")
        print ("")
        print ("You have Reignsfall armour")
        print ("You now have 200 health") #dialouge
        print ("")
        print ("you have " + str(coins) + " coins")
        time.sleep(2)

    def Explore(): # if you want to scavenge dialouge
        print ("")
        print ("")
        print ("")
        Treal = input("Scavenge? [Yes or No]") #asks if you want to scavenge
        Treal = Treal.lower()# makes the answer it all lowercase
        if Treal == "yes":  #if yes
            ItemCh()

        elif Treal == "no": # if no sends you back
            Travel()

        elif Treal == "key":
            RarTest()
            
        else:
            Explore()

    def RarTest(): # check if you have enough keys for secret boss
        global Key
        if Key >= 3:
            RAS()
            End1()

        else:
            Travel()

    def RAS():
            global EXL# to get the variables out of the definitions/ Enemy type
            global Man # gets enemy health
            global sasl # gets enemy attack list
            global sas # gets enemy attack
            global Hsasl
            global Hsas
            print ("**The three keys go into three holes in the pillar arranged in a triangle**")
            time.sleep(2)
            print ("")
            print ("**A portal Appears**")
            time.sleep(3)
            print ("")
            print ("")
            print ("**A Hooded Figure appears out of a portal!**")
            EXL = "Rifter" #name of boss
            Man = 500 #health of boss
            sasl = (0,0,30,40,50,60,0)#damage of boss
            Hsasl = (0,0,0,90,0,0)
            sas = (random.choice(sasl))#randomly chooses his damage
            Hsas = (random.choice(Hsasl))#randomly chooses his damage
            Battle()
        
        

    def ItemCh(): # chance for an item
        global heallist
        global HealingP
        Itemr = (0,0,0,1,1,2) #random number list
        ItemR = random.choice(Itemr)# picks a number
        if ItemR == 0: # 0 = nothing
            print ("        ~'.' ")
            print ("")
            print (" '.'~")
            print ("              ~'.'")
            print ("     '.'~")
            print ("")
            time.sleep(1)
            print ("nothing here")
        elif ItemR == 1: # 1 = a potion
            time.sleep(2)
            print ("     ")
            print ("     _  ")
            print ("    |>|")
            print ("  __|<|__")
            print (" |      |")
            print ("| <><><> |")
            print (" |______|")
            print ("")
            print ("you found 1 potion!")
            HealingP = (HealingP + 1)
        elif ItemR == 2: # 2 = more healing
            print (" ______________")
            print ("|How 2 heal More|")
            print ("| <>><<><><><   |")
            print ("|  <><><><<><>< |")
            print ("| <><AD<><><AS  |")
            print ("|  <><<>><><><  |")
            print ("| <><><><><><>  |")
            print ("|  <><><><><><> |")
            print ("|_______________|")
            print ("")
            print ("")
            print ("You found a healing Scroll!")
            print ("More healing for each potion! (x1 Max)")
            heallist = (20,25,30,35,40)
        
    def KeyTest(): # the key to enter the boss fight
        global Key
        if Key >= 1: # if you have a key it allows you to enter
            Key = (Key - 1)
            print("")
            print ("**You use the key on the castle gates**")
            time.sleep(2)
            print ("**You enter the Castle**") # dialogue
            
        elif Key <= 0: # if you don't you can't enter
            print ("")
            print ("")
            print ("")
            print ("You walk to the castle gates")
            time.sleep(2)
            print ("")
            print ("")
            print ("")
            print("The gate door is locked!!")
            time.sleep(1)
            print ("")
            print ("")
            print ("")
            print ("You need a Castle Key [Get one from shop]")
            time.sleep(2)
            Travel()

    def KingDia(): # Boss dialogue
        global Name
        print ("**The king stares at the head for a while**")
        time.sleep(4)
        print ("**The King stands from his throne and pulls out his greatsword**")
        print("")
        time.sleep(1)
        print ("A Challenger to the throne...")
        time.sleep(2)
        print ("I thought I exiled you...")
        time.sleep(2)
        print ("very well...")
        time.sleep(3)
        NameL = Name.upper()
        print ("TIME TO DIE " + NameL + "!")
        
    def End1():
        print ("")
        print ("")
        print ("")
        print ("**You fall and disapear**")
        time.sleep(3)
        print ("")
        print ("$%^!&@")
        print (")(*&a5sa6%$#@#%")
        print ("#&*&^$@%#!!!")
        print ("")
        time.sleep(2)
        sys.exit()

        


    Travel()# sends you to travel menu
    continue


