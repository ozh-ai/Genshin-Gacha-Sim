def choice(FourNpity, FiveNpity, FourEpity, FiveEpity):
    print("   ")
    print("4* pity on normal banner =", FourNpity)
    print("5* pity on normal banner =", FiveNpity)
    print("4* pity on event banner =", FourEpity)
    print("5* pity on event banner =", FiveEpity)
    banner = input("Type 'n' for normal banner, 'e' for event banner:")
    wish_num = eval(input("Type '1' for single wish, '10' for bundle wish:"))
    print("    ")

    if banner == "n":
        if wish_num == 1:
            FourNpity, FiveNpity = NB(FourNpity, FiveNpity)
        elif wish_num == 10:
            for i in range(1,11):
                FourNpity, FiveNpity = NB(FourNpity, FiveNpity)
                i = i + 1
        else:
            print("error")

    elif banner == "e":
        if wish_num == 1:
            FourEpity, FiveEpity = EB(FourEpity, FiveEpity)
        elif wish_num == 10:
            for i in range(1,11):
                FourEpity, FiveEpity = EB(FourEpity, FiveEpity)
                i = i + 1
        else:
            print("error")

    elif banner == "zhongli":
        for i in range(1,wish_num+1):
            print("Big Dong Zhong!!")
            i = i + 1

    else:
        print("error")
    choice(FourNpity, FiveNpity, FourEpity, FiveEpity)

#-------------------------------------------------

def NB(FourNpity, FiveNpity):
    if int(FiveNpity) == 88 and int(FourNpity) == 8:
        import random
        rng = random.randint(61,570)
    elif int(FiveNpity) == 89:
        import random
        rng = random.randint(1,60)
    elif int(FourNpity) == 9:
        import random
        rng = random.randint(61,570)
    else:
        import random
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
        rng = three(rng)
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

def EB(FourEpity, FiveEpity):
    if int(FiveEpity) == 88 and int(FourEpity) == 8:
        import random
        rng = random.randint(61,570)
    elif int(FiveEpity) == 89:
        import random
        rng = random.randint(1,60)
    elif int(FourEpity) == 9:
        import random
        rng = random.randint(61,570)
    else:
        import random
        rng = random.randint(1,10000)
    if rng in range(1,31):
        print("Eula ***")
    if rng in range(31,37):
        print("Mona ***")
    if rng in range(37,43):
        print("Diluc ***")
    if rng in range(43,49):
        print("Keqing ***")
    if rng in range(49,55):
        print("Qiqi ***")
    if rng in range(55,61):
        print("Jean ***")
    if rng in range(61,146):
        print("Xinyan *")
    if rng in range(146,231):
        print("Xingqiu *")
    if rng in range(231,316):
        print("Beidou *")
    if rng in range(316,324):
        print("Rosaria *")
    if rng in range(324,332):
        print("Sucrose *")
    if rng in range(332,340):
        print("Diona *")
    if rng in range(340,348):
        print("Chongyun *")
    if rng in range(348,356):
        print("Noelle *")
    if rng in range(356,364):
        print("Bennett *")
    if rng in range(364,373):
        print("Fischl *")
    if rng in range(373,382):
        print("Ningguang *")
    if rng in range(382,391):
        print("Xiangling *")
    if rng in range(391,400):
        print("Razor *")
    if rng in range(400,409):
        print("Barbruh *")
    if rng in range(409,418):
        print("Rust *")
    if rng in range(418,427):
        print("Sacrificial Bow *")
    if rng in range(427,436):
        print("The Stringless *")
    if rng in range(436,445):
        print("Favonius Warbow *")
    if rng in range(445,454):
        print("Eye of Perception *")
    if rng in range(454,463):
        print("Sacrificial Fragments *")
    if rng in range(463,472):
        print("The Widsith *")
    if rng in range(472,481):
        print("Favonius Codex *")
    if rng in range(481,490):
        print("Favonius Lance *")
    if rng in range(490,499):
        print("Dragon's Bane *")
    if rng in range(499,508):
        print("Rainslasher *")
    if rng in range(508,517):
        print("Sacrificial Greatsword *")
    if rng in range(517,526):
        print("The Bell *")
    if rng in range(526,535):
        print("Favonius Greatsword *")
    if rng in range(535,544):
        print("Lion's Roar *")
    if rng in range(544,553):
        print("Sacrificial Sword *")
    if rng in range(553,562):
        print("The Flute *")
    if rng in range(562,571):
        print("Favonius Sword *")
    if rng in range(571,10001):
        rng = three(rng)
    if rng in range(1,61):
        FiveEpity = 0
    else:
        FiveEpity = int(FiveEpity) + 1
    if rng in range(61,571):
        FourEpity = 0
    else:
        FourEpity = int(FourEpity) + 1
    return FourEpity, FiveEpity


#-------------------------------------------------

def three(rng):
    if rng in range(571,1296):
        print("Slingshot")
    if rng in range(1296,2021):
        print("Sharpshooter's Oath")
    if rng in range(2021,2746):
        print("Raven Bow")
    if rng in range(2746,3471):
        print("Emerald Orb")
    if rng in range(3471,4196):
        print("Thrilling Tales of Dragon Slayers")
    if rng in range(4196,4921):
        print("Magic Guide")
    if rng in range(4921,5646):
        print("Black Tassel")
    if rng in range(5646,6372):
        print("Debate Club")
    if rng in range(6372,7098):
        print("Bloodstained Greatsword")
    if rng in range(7098,7824):
        print("Ferrus Shadow")
    if rng in range(7824,8549):
        print("Skyrider Sword")
    if rng in range(8549,9275):
        print("Harbinger of Dawn")
    if rng in range(9275,10001):
        print("Cool Steel")
    return rng

#-------------------------------------------------


print("GENSHIN IMPACT WISH SIMULATOR V1.5 (EULA BANNER)")
print("THIS SIMULATOR IS NOT EXACT, IT IS ONLY A ROUGH ESTIMATE")
choice(0,0,0,0)


           




    
