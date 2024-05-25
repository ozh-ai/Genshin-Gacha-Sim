def choice(FourNpity, FiveNpity, FourEpity, FiveEpity, FourEguarantee, FiveEguarantee):
    print("   ")
    print("4* pity on normal banner =", FourNpity)
    print("5* pity on normal banner =", FiveNpity)
    print("4* pity on event banner =", FourEpity)
    print("5* pity on event banner =", FiveEpity)
    banner = input("Type 'n' for normal banner, 'e' for event banner:")
    if banner == 'end':
        return
    wish_num = input("Type '1' for single wish, '10' for bundle wish:")
    print("    ")

    if wish_num.isdigit() == False:
        print("error")

    else:
        wish_num = int(wish_num)
        if banner[0] == "n":
            if wish_num == 1:
                FourNpity, FiveNpity = NB(FourNpity, FiveNpity)
            elif wish_num == 10:
                for i in range(1,11):
                    FourNpity, FiveNpity = NB(FourNpity, FiveNpity)
                    i = i + 1
            else:
                print("error")

        elif banner[0] == "e":
            if wish_num == 1:
                FourEpity, FiveEpity, FourEguarantee, FiveEguarantee = EB(FourEpity, FiveEpity, FourEguarantee, FiveEguarantee)
            elif wish_num == 10:
                for i in range(1,11):
                    FourEpity, FiveEpity, FourEguarantee, FiveEguarantee = EB(FourEpity, FiveEpity, FourEguarantee, FiveEguarantee)
                    i = i + 1
            else:
                print("error")

        elif banner == "zhongli":
            for i in range(1,wish_num+1):
                print("Big Dong Zhong!!")
                i = i + 1

        elif banner == "paimon":
            for i in range(1,wish_num+1):
                print("Ehe te nandayo!")
                i = i + 1

        else:
            print("error")

    choice(FourNpity, FiveNpity, FourEpity, FiveEpity, FourEguarantee, FiveEguarantee)

#-------------------------------------------------

def NB(FourNpity, FiveNpity):
    import random
    if int(FiveNpity) == 88 and int(FourNpity) == 8:        
        rng = random.randint(61,570)
    elif int(FiveNpity) == 89:        
        rng = random.randint(1,60)
    elif int(FourNpity) == 9:
        rng = random.randint(61,570)
    else:        
        rng = random.randint(1,10000)

    if rng in range(1,5):
        print("Keqing ***")
    if rng in range(5,9):
        print("Mona ***")
    if rng in range(9,13):
        print("Qiqi ***")
    if rng in range(13,17):
        print("Diluc ***")
    if rng in range(17,21):
        print("Jean ***")
    if rng in range(21,25):
        print("Amos Bow ***")
    if rng in range(25,29):
        print("SKyward Harp ***")
    if rng in range(29,33):
        print("Lost Prayer to the Sacred Winds ***")
    if rng in range(33,37):
        print("Skyward Atlas ***")
    if rng in range(37,41):
        print("Primorial Jade Winged-Spear ***")
    if rng in range(41,45):
        print("Skyward Spine ***")
    if rng in range(45,49):
        print("Wolf's Gravestone ***")
    if rng in range(49,53):
        print("Skyward Pride ***")
    if rng in range(53,57):
        print("Skyward Blade ***")
    if rng in range(57,61):
        print("Aquila Favonia ***")
    if rng in range(61,76):
        print("Sucrose *")
    if rng in range(76,91):
        print("Chongyun *")
    if rng in range(91,107):
        print("Noelle *")
    if rng in range(107,123):
        print("Bennett *")
    if rng in range(123,139):
        print("Fischl *")
    if rng in range(139,155):
        print("Ningguang *")
    if rng in range(155,171):
        print("Xingqiu *")
    if rng in range(171,187):
        print("Beidou *")
    if rng in range(187,203):
        print("Xiangling *")
    if rng in range(203,219):
        print("Amber *")
    if rng in range(219,235):
        print("Razor *")
    if rng in range(235,251):
        print("Kaeya *")
    if rng in range(251,267):
        print("Barbruh *")
    if rng in range(267,283):
        print("Lisa *")
    if rng in range(283,299):
        print("Rust *")
    if rng in range(299,315):
        print("Sacrificial Bow *")
    if rng in range(315,331):
        print("The Stringless *")
    if rng in range(331,347):
        print("Favonius Warbow *")
    if rng in range(347,363):
        print("Eye of Perception *")
    if rng in range(363,379):
        print("Sacrificial Fragments *")
    if rng in range(379,395):
        print("The Widsith *")
    if rng in range(395,411):
        print("Favonius Codex *")
    if rng in range(411,427):
        print("Favonius Lance *")
    if rng in range(427,443):
        print("Dragon's Bane *")
    if rng in range(443,459):
        print("Rainslasher *")
    if rng in range(459,475):
        print("Sacrificial Greatsword *")
    if rng in range(475,491):
        print("The Bell *")
    if rng in range(491,507):
        print("Favonius Greatsword *")
    if rng in range(507,523):
        print("Lion's Roar *")
    if rng in range(523,539):
        print("Sacrificial Sword *")
    if rng in range(539,555):
        print("The Flute *")
    if rng in range(555,571):
        print("Favonius Sword *")
    if rng in range(571,10001):
        rng = three()
    if rng in range(1,61):
        FiveNpity = 0
    else:
        FiveNpity = int(FiveNpity) + 1
    if rng in range(61,571):
        FourNpity = 0
    else:
        FourNpity = int(FourNpity) + 1
    return FourNpity, FiveNpity
        
    
#-------------------------------------------------

def EB(FourEpity, FiveEpity, FourEguarantee, FiveEguarantee):
    import random
    if int(FiveEpity)<76: #Soft pity, probability of getting a 5* based on current pity
        fivestar = 6000 #0.6% chance to get 5*
    else:
        fivestar = 324000 #32.4% chance to get 5*

    if int(FiveEpity) == 88 and int(FourEpity) == 8: #give 4* #hard pity
        rng = random.randint(1,51000)
    elif int(FiveEpity) == 89: #give 5*
        rng = random.randint(51000,51000+fivestar)
    elif int(FourEpity) == 9: #give 4*
        rng = random.randint(1,51000)
    else:        
        rng = random.randint(1,1000000)

    if rng in range(1,51001) and FourEguarantee == True: #check for guaranteed 4*
        rng = random.randint(1,25500)
        FourEguarantee = False
    elif rng in range(25501,51001) and FourEguarantee == False:
        FourEguarantee = True
    if rng in range(51001,51001+fivestar) and FiveEguarantee == True: #check for guaranteed 5*
        rng = random.randint(51000,int(51000+5*(fivestar/10)))
        FiveEguarantee = False
    elif rng in range(int(51001+5*(fivestar/10)),51001+fivestar) and FiveEguarantee == False:
        FiveEguarantee = True
    
    if rng in range(1,8501):
        print("Xinyan *")
    if rng in range(8501,17001):
        print("Xingqiu *")
    if rng in range(17001,25501): 
        print("Beidou *")
    if rng in range(25501,26380): 
        print("Rosaria *")
    if rng in range(26380,27259):
        print("Sucrose *")
    if rng in range(27259,28138):
        print("Diona *")
    if rng in range(28138,29017):
        print("Chongyun *")
    if rng in range(29017,29896):
        print("Noelle *")
    if rng in range(29896,30775):
        print("Bennett *")
    if rng in range(30775,31654):
        print("Fischl *")
    if rng in range(31654,32533):
        print("Ningguang *")
    if rng in range(32533,33412):
        print("Xiangling *")
    if rng in range(33412,34291):
        print("Razor *")
    if rng in range(34291,35170):
        print("Barbruh *")
    if rng in range(35170,36049):
        print("Rust *")
    if rng in range(36049,36928):
        print("Sacrificial Bow *")
    if rng in range(36928,37807):
        print("The Stringless *")
    if rng in range(37807,38686):
        print("Favonius Warbow *")
    if rng in range(38686,39565):
        print("Eye of Perception *")
    if rng in range(39565,40444):
        print("Sacrificial Fragments *")
    if rng in range(40444,41323):
        print("The Widsith *")
    if rng in range(41323,42202):
        print("Favonius Codex *")
    if rng in range(42202,43081):
        print("Favonius Lance *")
    if rng in range(43081,43961): 
        print("Dragon's Bane *")
    if rng in range(43961,44841):
        print("Rainslasher *")
    if rng in range(44841,45721):
        print("Sacrificial Greatsword *")
    if rng in range(45721,46601):
        print("The Bell *")
    if rng in range(46601,47481):
        print("Favonius Greatsword *")
    if rng in range(47481,48361):
        print("Lion's Roar *")
    if rng in range(48361,49241):
        print("Sacrificial Sword *")
    if rng in range(49241,50121):
        print("The Flute *")
    if rng in range(50121,51001):
        print("Favonius Sword *")
    if rng in range(51001,int(51001+5*(fivestar/10))):
        print("Eula ***")
    if rng in range(int(51001+5*(fivestar/10)),int(51001+6*(fivestar/10))):
        print("Mona ***")
    if rng in range(int(51001+6*(fivestar/10)),int(51001+7*(fivestar/10))):
        print("Diluc ***")
    if rng in range(int(51001+7*(fivestar/10)),int(51001+8*(fivestar/10))):
        print("Keqing ***")
    if rng in range(int(51001+8*(fivestar/10)),int(51001+9*(fivestar/10))):
        print("Qiqi ***")
    if rng in range(int(51001+9*(fivestar/10)),51001+fivestar):
        print("Jean ***")
    if rng in range(51001+fivestar,1000001):
        three()

    if rng in range(51001,51001+fivestar):
        FiveEpity = 0
    else:
        FiveEpity = int(FiveEpity) + 1
    if rng in range(1,51001):
        FourEpity = 0
    else:
        FourEpity = int(FourEpity) + 1
    return FourEpity, FiveEpity, FourEguarantee, FiveEguarantee


#-------------------------------------------------

def three():
    import random
    threerng = random.randint(1,130)
    if threerng in range(1,11):
        print("Slingshot")
    if threerng in range(11,21):
        print("Sharpshooter's Oath")
    if threerng in range(21,31):
        print("Raven Bow")
    if threerng in range(31,41):
        print("Emerald Orb")
    if threerng in range(41,51):
        print("Thrilling Tales of Dragon Slayers")
    if threerng in range(51,61):
        print("Magic Guide")
    if threerng in range(61,71):
        print("Black Tassel")
    if threerng in range(71,81):
        print("Debate Club")
    if threerng in range(81,91):
        print("Bloodstained Greatsword")
    if threerng in range(91,101):
        print("Ferrus Shadow")
    if threerng in range(101,111):
        print("Skyrider Sword")
    if threerng in range(111,121):
        print("Harbinger of Dawn")
    if threerng in range(121,131):
        print("Cool Steel")

#-------------------------------------------------

print("GENSHIN IMPACT WISH SIMULATOR V1.5 (EULA BANNER)")
print("THIS SIMULATOR IS NOT EXACT, IT IS ONLY A ROUGH ESTIMATE")
choice(0,0,0,0,False,False)
           




    
