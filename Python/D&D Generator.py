import random

def wWeatherGen(avgTempS,avgTempD):
    tempChange = random.randrange(0,51)
    if tempChange >= 10:
        tempChange = random.randrange(0,51)
        if tempChange >= 30:
            tempChange = random.randrange(0,51)
    cH = random.randrange(0,2)
    if cH == 0:
       sTemp = avgTempS - tempChange
       dTemp = avgTempD - tempChange
    else:
       sTemp = avgTempS + tempChange
       dTemp = avgTempD + tempChange
    print("If the party is in surface water, the temperature is:",sTemp,"degrees",sep=" ")
    print("If the party is in deep water, the temperature is:",dTemp,"degrees",sep=" ")
    precip = random.randrange(0,12)
    if precip == 0:
        print("It is sunny.")
    elif precip == 1:
        print("It is mildly windy.")
    elif precip == 2:
        print("It is moderately windy.")
    elif precip == 3:
        print("It is heavily windy.")
    elif precip == 4:
        print("It is mildly raining/snowing.")
    elif precip == 5:
        print("It is moderately raining/snowing.")
    elif precip == 6:
        print("It is heavily raining/snowing.")
    elif precip == 7:
        print("It is mildly storming.")
    elif precip == 8:
        print("It is moderately storming.")
    elif precip == 9:
        print("It is heavily storming.")
    elif precip == 10:
        print("It is partly cloudy.")
    elif precip == 11:
        print("It is overcast.")
    print()

def dWeatherGen(avgTempD,avgTempN):
    tempChange = random.randrange(0,51)
    if tempChange >= 10:
        tempChange = random.randrange(0,51)
        if tempChange >= 30:
            tempChange = random.randrange(0,51)
    cH = random.randrange(0,2)
    if cH == 0:
       dTemp = avgTempD - tempChange
       nTemp = avgTempN - tempChange
    else:
       dTemp = avgTempD + tempChange
       nTemp = avgTempN + tempChange
    print("If it is daytime, the temperature is:",dTemp,"degrees",sep=" ")
    print("If it is nighttime, the temperature is:",nTemp,"degrees",sep=" ")
    precip = random.randrange(0,12)
    if precip == 0:
        print("It is sunny.")
    elif precip == 1:
        print("It is mildly windy.")
    elif precip == 2:
        print("It is moderately windy.")
    elif precip == 3:
        print("It is heavily windy.")
    elif precip == 4:
        print("It is mildly raining/snowing.")
    elif precip == 5:
        print("It is moderately raining/snowing.")
    elif precip == 6:
        print("It is heavily raining/snowing.")
    elif precip == 7:
        print("It is mildly storming.")
    elif precip == 8:
        print("It is moderately storming.")
    elif precip == 9:
        print("It is heavily storming.")
    elif precip == 10:
        print("It is partly cloudy.")
    elif precip == 11:
        print("It is overcast.")
    print()

def precipGen():
    precip = random.randrange(0,12)
    if precip == 0:
        print("It is sunny.")
    elif precip == 1:
        print("It is mildly windy.")
    elif precip == 2:
        print("It is moderately windy.")
    elif precip == 3:
        print("It is heavily windy.")
    elif precip == 4:
        print("It is mildly raining/snowing.")
    elif precip == 5:
        print("It is moderately raining/snowing.")
    elif precip == 6:
        print("It is heavily raining/snowing.")
    elif precip == 7:
        print("It is mildly storming.")
    elif precip == 8:
        print("It is moderately storming.")
    elif precip == 9:
        print("It is heavily storming.")
    elif precip == 10:
        print("It is partly cloudy.")
    elif precip == 11:
        print("It is overcast.")
    print()

def weatherGen(avgTempW,avgTempSA,avgTempS):
    tempChange = random.randrange(0,51)
    if tempChange >= 10:
        tempChange = random.randrange(0,51)
        if tempChange >= 30:
            tempChange = random.randrange(0,51)
    cH = random.randrange(0,2)
    if cH == 0:
       wTemp = avgTempW - tempChange
       saTemp = avgTempSA - tempChange
       sTemp = avgTempS - tempChange
    else:
       wTemp = avgTempW + tempChange
       saTemp = avgTempSA + tempChange
       sTemp = avgTempS + tempChange
    print("If it is Winter, the temperature is:",wTemp,"degrees",sep=" ")
    print("If it is Spring/Autumn, the temperature is:",saTemp,"degrees",sep=" ")
    print("If it is Summer, the temperature is:",sTemp,"degrees",sep=" ")
    precip = random.randrange(0,12)
    if precip == 0:
        print("It is sunny.")
    elif precip == 1:
        print("It is mildly windy.")
    elif precip == 2:
        print("It is moderately windy.")
    elif precip == 3:
        print("It is heavily windy.")
    elif precip == 4:
        print("It is mildly raining/snowing.")
    elif precip == 5:
        print("It is moderately raining/snowing.")
    elif precip == 6:
        print("It is heavily raining/snowing.")
    elif precip == 7:
        print("It is mildly storming.")
    elif precip == 8:
        print("It is moderately storming.")
    elif precip == 9:
        print("It is heavily storming.")
    elif precip == 10:
        print("It is partly cloudy.")
    elif precip == 11:
        print("It is overcast.")
    print()

def trackingGen():
    directionNum = random.randrange(0,8)
    if directionNum == 0:
        direction = "North"
    elif directionNum == 1:
        direction = "Northeast"
    elif directionNum == 2:
        direction = "East"
    elif directionNum == 3:
        direction = "Southeast"
    elif directionNum == 4:
        direction = "South"
    elif directionNum == 5:
        direction = "Southwest"
    elif directionNum == 6:
        direction = "West"
    elif directionNum == 7:
        direction = "Northwest"
    return direction

def locationGen(locationList):
    yn = "yes"
    while yn == "yes":
        print("Your generated location is:")
        location = random.randrange(0,len(locationList))
        print(locationList[location])
        print()
        yn = input("Do you want to generate another location? ").lower()
        print()

def creatureGen(creaturesList):
    yn = "yes"
    while yn == "yes":
        num = random.randrange(1,15)
        if num == 1 or num == 2 or num == 3:
            print("Your generated encounter is:")
            creature = random.randrange(0,len(creaturesList))
            print(creaturesList[creature])
        elif num == 4 or num == 5 or num == 6:
            print("Your generated encounter is:")
            num2 = random.randrange(1,5)
            if num2 == 1 or num2 == 2:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 == 3 or num2 == 4:
                print("Two ",end="")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 ==5:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
                print("They are fighting.")
        elif num == 7 or num == 8:
            print("Your generated encounter is:")
            num2 = random.randrange(1,5)
            if num2 == 1 or num2 == 2:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 == 3 or num2 == 4:
                print("Three ",end="")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 ==5:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
                print("They are fighting.")
        elif num == 9 or num == 10:
            print("Your generated encounter is:")
            num2 = random.randrange(1,5)
            if num2 == 1 or num2 == 2:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 == 3 or num2 == 4:
                print("Four ",end="")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 ==5:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
                print("They are fighting.")
        elif num == 11 or num == 12:
            print("Your generated encounter is:")
            num2 = random.randrange(1,5)
            if num2 == 1 or num2 == 2:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 == 3 or num2 == 4:
                print("Five ",end="")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 ==5:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
                print("They are fighting.")
        elif num == 13:
            print("Your generated encounter is:")
            num2 = random.randrange(1,5)
            if num2 == 1 or num2 == 2:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 == 3 or num2 == 4:
                print("Six ",end="")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 ==5:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
                print("They are fighting.")
        elif num == 14:
            print("Your generated encounter is:")
            num2 = random.randrange(1,5)
            if num2 == 1 or num2 == 2:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 == 3 or num2 == 4:
                print("Seven ",end="")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 ==5:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
                print("They are fighting.")
        elif num == 15:
            print("Your generated encounter is:")
            num2 = random.randrange(1,5)
            if num2 == 1 or num2 == 2:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 == 3 or num2 == 4:
                print("Eight ",end="")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
            elif num2 ==5:
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature],end=", ")
                creature = random.randrange(0,len(creaturesList))
                print(creaturesList[creature])
        print()
        yn = input("Do you want to generate another encounter? ").lower()
        while yn != "yes" and yn != "no":
            print()
            print("Please enter yes or no.")
            yn = input("Do you want to generate another encounter? ").lower()
        print()

def genType():
    print("Generator Options:")
    print("0. Reselect Generator")
    print("1. Encounter")
    print("2. Weather")
    print("3. Location")
    gen = int(input("Which generator (input the number) do you want to run? "))
    print()
    return gen

def loot():
    yn = "yes"
    while yn == "yes":
        lootType = random.randrange(1,7)
        if lootType == 1 or lootType == 2 or lootType == 3:
            #Trinkets
            rawLoot = "A harp which only plays while in the moonlight.-SPLIT-A map faded beyond use.-SPLIT-A corner piece of a map, showing only ocean.-SPLIT-A horn that produces no sound unless near the ocean.-SPLIT-A glass bone.-SPLIT-A thin metal rod that plays out a tune when repeatedly tapped.-SPLIT-A sharp dagger that will not harm any creatures for no apparent reason.-SPLIT-An ebony and ivory hair comb that darken and lighten your hair respectively with continued use.-SPLIT-A razor-sharp piece of metal wrapped in a bloody bandage.-SPLIT-A blank book and a sack of ashes which, if rubbed onto paper, remove ink.-SPLIT-A sharp tooth as long as your hand.-SPLIT-A glass bottle which holds a tiny gelatinous cube; feed it organic material and it will grow in time, but for some reason it won’t leave its makeshift terrarium.-SPLIT-A smooth, flat stone which fits in the palm of your hand, yet somehow weighs twenty pounds.-SPLIT-A ceramic tablet, etched in Elven writing with a short yet entrancing poem about two lovers separated by the sea.-SPLIT-A metal canteen filled with vinegar. But why?-SPLIT-A hermit crab, alive and well, although unhappy to be disturbed by such meddlesome colossi.-SPLIT-A small steel statuette of a frog playing an instrument, preferably the fiddle.-SPLIT-A single fork, inscribed with the dwarven runes for SOUP.-SPLIT-A well-preserved drawing of a very pompous cat.-SPLIT-A mortar and pestle which smells heavily of sulfur.-SPLIT-A bottle of extremely old wine.  Has a chance of either being really good wine, really bad wine, or wine with psychedelic effects (might also be really good depending on who you ask).-SPLIT-A single arrow with a barbed tip. If shot, deals +2 damage on a hit and shatters.-SPLIT-A perfect cube of pure silver, 2 inches on each edge.-SPLIT-A small rubber ball, perfect for entertaining children and frightening cats.-SPLIT-A tattered note which reads “I. O. U.”-SPLIT-Rat poop. So much poop.-SPLIT-A very ornate walking stick, complete with carvings of the local wildlife.-SPLIT-A set of onyx playing dice, but with unusual numbers of sides, such as 7, 13, and 35.-SPLIT-A single spoon, inscribed with the Dwarven runes for STEAK.-SPLIT-A cubic device composed of rotating layers of squares arranged 3 by 3, each side of the cube is in different colors.  Be careful when playing with it or you may never be able to get it back to its original arrangement.-SPLIT-A glass eyeball.-SPLIT-A human skull with two distinct punctures at the top.-SPLIT-A flute that can either [1 on d6] emit no audible sound (makes the nearest animal hostile), [2 on d6] an extremely high-pitched one, [3 on d6] bass strong enough to cause 1d4 damage in a d6 metre area or [4,5,6 on d6] sound like a regular flute. Hide the rolls.-SPLIT-A mushroom that, if ingested, makes one’s tongue glow turquoise for 1d4 hours.-SPLIT-A vial containing a preserved gecko.-SPLIT-A vial containing a living newt in water.-SPLIT-3d6 silver pieces so tarnished that they couldn’t possibly hold their original value.-SPLIT-A black conch shell.-SPLIT-A skeletal snail.  What kind of snail could this have been to have a skeleton?-SPLIT-A stone so smooth it feels as if it had bathed in a divine river of silk for a millenium before finding its way into your hand.-SPLIT-A cracked stone ring, with the words “Carpe Diem” written in druidic on the inside.-SPLIT-1d6 acorns, each of which will grow into an orange tree if planted or produce the same effect as drunkenness if consumed.-SPLIT-A broken femur.  You’re not sure how, but you can tell it came from an elf.-SPLIT-A dried animal stomach, filled with aromatic pine needles.-SPLIT-A fishing net which will catch anything but fish when cast.  It especially likes frogs.-SPLIT-A tattered loincloth which smells of cattle.-SPLIT-A coil of hempen rope which crumbles when tied in any knot.-SPLIT-1d8 fist sized rocks which, when inspected further, turn out to be the hardened droppings of a stone giant.-SPLIT-A set of crude eating utensils made for giants.-SPLIT-A petrified egg of unknown origin.-SPLIT-A dead beetle whose outer shell pattern resembles a face/skull.-SPLIT-A padlock whose key is permanently jammed into it, making both useless.-SPLIT-A jar of dirt that smells - and tastes - like honey, but is only dirt.-SPLIT-A number of old medical utensils, including a scalpel caked with what is either rust or ancient blood - or a combination of the two.-SPLIT-An expertly skinned fox pelt.-SPLIT-A poorly skinned rabbit pelt.-SPLIT-A jackalope skull, complete with antlers.-SPLIT-A rabbit’s foot.-SPLIT-A shard of obsidian that always feels warm.-SPLIT-A tin can filled to the brim with inhuman nail clippings.-SPLIT-A small birdcage containing the skeletal remains of something that definitely was not a bird.-SPLIT-A porous, flat stone with an impression the shape of a paw print.-SPLIT-A string necklace that loops through the tooth/fang of a large predator.-SPLIT-A silver piece etched with the inscription “In Eldinger We Trust”-SPLIT-A wicker basket entwined with ornate copper string.  Placing it on the ground causes a random nearby bird to land in it.  The bird retains full control of itself; it just likes the basket.-SPLIT-A glass onion.  It has no opening, but is filled with a cloudy white-ish liquid.  If the onion is broken, it is revealed to contain, you guessed it, onion juice.-SPLIT-An ages-old message in a bottle [roll a d4: 1,2 - it is water damaged beyond reading it. 3-Short message asking for help. 4-Short message telling not to send help.]-SPLIT-A jar containing a single eyeball preserved in vinegar. DC 15 Medicine check reveals it to be from a goblin.-SPLIT-A live lizard, who attempts to escape upon being detected.-SPLIT-A book describing a ritual which would allow one to “become one with magic.” The casting time and cost are astronomically high and require things that the party has never heard of. The ritual does not work."
            lootList = rawLoot.split("-SPLIT-")
            loot = random.randrange(0,len(lootList))
            print("Your generated loot is:")
            print(lootList[loot])
            print()
        if lootType == 4 or lootType == 5:
            #Minor Magic Items
            rawLoot = "A candle that, when lit, causes anyone within its 15-foot radius of light to have a hard time inventing lies (disadvantage on deception checks.)-SPLIT-An electrum spoon with a shield emblem on the back.  Most poisons and diseases in food eaten with this spoon are magically neutralized.-SPLIT-A silver ring with an amethyst bearing an infinity symbol on the gem.  The wearer experiences their most recent dream every night until sleeping with the ring removed.-SPLIT-A pouch containing 2d4 chalk sticks and a note explaining their use.  Though they wear out quickly (one use apiece, up to 20 words), the message can be written on anything, even water, fire, and even thin air. If not written on a normal, solid surface, the message dissipates in 1d4 minutes or until disturbed.  On normal surfaces it acts like normal chalk. May or may not be found in a dry spot near a message saying “Try Finger But Hole”-SPLIT-A copper hairpin shaped like a lightning bolt.  If the wearer is unlucky enough to be struck by lightning (not including magical), the pin absorbs it and disintegrates shortly after, protecting the wearer.-SPLIT-A cloak fashioned from the pelt of a dire wolf, the wearer is immune to adverse natural environmental temperature conditions, such as blistering heat from the sun or a freezing blizzard.-SPLIT-A scrap of mottled skin bearing a 3” tall tattoo of a hiker.  Touching it with bare skin transfers the tattoo to one’s (roll a d6: 1-face 2-chest 3-leg 4- back 5-arm 6-neck). If someone else touches the tattoo it transfers to them, and so on.-SPLIT-A quartz whetstone that never wears down. If placed over a broken non-magical weapon wrapped in an oily cloth for 8 hours, the weapon is repaired.-SPLIT-A mummified cat paw on a golden string.  When someone first touches it, a charm (could be considered a curse) is placed on them for 2d6 months, and the paw disappears.  For the duration, cats are generally overly fond of the affected person and follow them around, meow at them, sit at their doorstep etc.  GM discretion at whether or not the charm/curse can be removed and how, if so.-SPLIT-A bag of holding that regurgitates all items within immediately after they are placed inside. -SPLIT-An animated gold coin that attempts to run away. -SPLIT-An incredibly intricate armillary sphere that can be collapsed into a ring which has the phrase “May the stars guide you to victory” inscribed on it. When not in its ring form it perfectly tracks every visible star on its own.-SPLIT-A coin that always lands on what the owner calls if they flip it. Observers forget the last result if flipped again.-SPLIT-An insulated shield which grants resistance to fire and cold damage.-SPLIT-A glass bottle containing within it a miniature land mass with tiny civilization living there. Observers must make a DC 15 (20?) perception check to notice the beings.-SPLIT-A leather pouch containing a compass and stone. The compass always points to the stone.-SPLIT-A hand mirror that shows an image of anyone you may be thinking about (the most if more than one).-SPLIT-A clay teapot which refills with fresh tea at sunrise everyday.-SPLIT-A pocket watch that runs backward when touched.-SPLIT-A small figurine that can answer any question. The answer is whatever the person asking wants to hear, not necessarily the correct answer.-SPLIT-A feather quill which writes in the same exquisite handwriting despite the user.-SPLIT-A compass that spins endlessly until near a mimic, at which point it points at the mimic. Found pointing at a chest in the corner of the room.-SPLIT-A large rock that looks like a diamond when touching it...or is it a diamond? The owner loses the ability to discard it after two days and is never sure if it is a rock or diamond.-SPLIT-A medallion resembling a wolf’s head, attached to a leather string. The eyes glow yellow when in the presence of residual magic, which is everywhere in the new world.-SPLIT-A 5” tall painted porcelain figurine of a stereotypical garden gnome; when it thinks no one is watching, it picks its nose.-SPLIT-A single arrow, which is always found later - in good condition - by the owner after firing it, even if it left behind.-SPLIT-A leather pouch which can convert inserted coins into an equal value of a different variety of coin. For example, 300 copper could become 30 silver or 3 gold.-SPLIT-A whistle that, if attuned to, can play any melody the user can imagine, despite not having holes to change the pitch.-SPLIT-An idol of a frightening beast, which gives nightmares to a randomly chosen person who sleeps near it.-SPLIT-A pair of eyeglasses that make you appear invisible - to yourself.-SPLIT-A sword seemingly from a vastly different culture (katana). It is sentient but only yells HYAAAH (Bruce Lee noise) every time it is unsheathed and is otherwise treated as a regular long sword.Deck of Many Tricks: A deck that is magically enhanced for card tricks. Useless in combat but a cool party trick.-SPLIT-Pen of Ink - A pen that does not require regular ink dipping. When it stops writing, it can be refilled by dipping it in an inkwell, which will consume the ink.-SPLIT-Arrow of Returning - An arrow that, when misfired, returns to the owner…at the same velocity. (If the roll to hit is lower than the target’s AC but higher than the wielder’s, it hits the wielded)-SPLIT-Paper of Seeing - A small piece of paper that, when ingested, grants a buff to WIS but also causes the user to suffer hallucinations."
            lootList = rawLoot.split("-SPLIT-")
            loot = random.randrange(0,len(lootList))
            print("Your generated loot is:")
            print(lootList[loot])
            print()
        if lootType == 6:
            #Side Quest Hooks
            rawLoot = "A scroll case with an unfinished spell scroll within. -SPLIT-A box containing a mold for a key.-SPLIT-An obsidian token of an ancient deity.-SPLIT-A broken sword hilt with strange runes on the remains of the blade.-SPLIT-A wooden carving of a strange unknown beast. (Tarrasque)-SPLIT-An unfinished autobiography.-SPLIT-A key that does not fit any locks nearby.-SPLIT-A pocket notebook with cryptic notes scrawled through it.-SPLIT-A brilliant gold coin, bearing a sinister sigil on one side and the head of a demon on the other. Flipping the coin causes the user (and only him/her) to hear an evil laugh of unknown origin.-SPLIT-A brightly multicolored chicken egg. If broken, it reveals two smaller eggs of similar coloration. One egg is rotten inside, the other hatches in 1d4 days to reveal a sentient chick which will grow to the size of a fist but never mature.  It cannot speak but understands any languages known by the first person it sees upon hatching, whom it views as its mother.-SPLIT-An ornate scabbard that matches no blade that you have seen - yet.-SPLIT-A gold ring that turns the player invisible, but the player is hunted by a small group of revenant until the ring is destroyed. -SPLIT-A talking human skull that promises to tell an interesting story for a bottle of fine wine. (The skull has no way of drinking the wine on its own, and no way of fighting the party if they decide to take him. Though he will bluff that he is very dangerous.)-SPLIT-A small compass that points toward the desert. (tracks a big monster in the desert.)-SPLIT-A sword that glows when aberrations are nearby. Found glowing while stuck in a rock. DC 15 (or greater if DM wants to challenge players) STR (athletics) to remove. Sword is +1 normally with a +3 against aberrations."
            lootList = rawLoot.split("-SPLIT-")
            loot = random.randrange(0,len(lootList))
            print("Your generated loot is:")
            print(lootList[loot])
            del lootList[loot]
            print()
        if lootType == 7:
            #Magic Items
            rawLoot = "A small rectangular stone, approximately 1in x 1.5in in size, crudely attached to a twig with an inscription that reads “Whosoever holds this hammer, if he be worthy, shall possess the power of Throg.” When wielded it does 1d4 bludgeoning + 1d4 lightning damage requiring no attunement. If attuned to the hammer, gain the ability to wild shape into a frog once per short rest.-SPLIT-A ring or amulet that, when worn, gives the users magic a 25% chance to go wild regardless of how it is cast, but gives a +1 to spell save DC and a +1 to any spell attacks. (Includes rituals and cantrips. Roll a d100 whenever any magic is cast, on a roll of 25 or below magic goes wild. Rituals go wild at the end of the casting time not the beginning so materials are still consumed.)-SPLIT-The Blade of Diversity - this sword acts differently each day.  [Roll a d6 at daybreak, one effect can not occur two days in a row] 6-The sword unsheathes coated in black ooze, deals +1d6 necrotic damage. 5-The sword glows brightly when unsheathed, giving off 30 feet of bright light, and all its damage is radiant. 4-The sword becomes a swarm of bees sprouting from the handle in the shape of a sword, dealing piercing damage with reach. 3-The sword behaves as a normal sword, and all damage is nonmagical.  2-The sword turns a random color every time it is unsheathed [d6 ROYGBP]. 1- The sword sprouts a second hilt on the end of the blade (dealing bludgeoning damage instead); somehow the user has no issue sheathing it.-SPLIT-The Sword of Bipolarity - Each day roll a d12 on a 1-6 the sword is a sword of -3. On a 7-12 it is a sword of +3.-SPLIT-Armor that takes a single action to don/doff. (The armor could be further magical)-SPLIT-A large sword stuck into a pedestal. The pedestal reads “Whosoever pulls this sword must thusly have the strength to rule this land.” Requires a DC 30 Str (Athletics) check to pull out. Functions as a +3 great sword that deals an extra 1d8 radiant damage. Also allows for the player to enter a castle (place this castle somewhere on the map). The castle is relatively undestroyed and cannot be entered by other means. The sword is also sentient and telepathically works like a lawful good warlock patron (asking for things to be done or else it will lose its powers).-SPLIT-Cloak of Lycanthropy - A cloak made of (roll a d4, 1-Bear, 2-Boar, 3-Tiger, 4-Wolf) fur. Upon donning the cloak, the player is transformed into the lycanthrope version of whichever creature was rolled. The player can remove the cloak even while transformed. (MM 207 features a chart about players as lycanthropes.)-SPLIT-Ring of Lycanthopy - The ring seems like a plain ring until in moonlight where it displays a (roll a d4, 1-Bear, 2-Boar, 3-Tiger, 4-Wolf). Upon wearing the ring, the player cannot remove the ring without [something]. The ring causes the player to transform into the lycanthrope form of whatever the ring has on it every night-SPLIT-The Cloak of Truths…You Think - Player believes it to help them detect lies. Actually does the opposite. Player rolls with disadvantage against all insight checks but believes that they have advantage (or that the other person has disadvantage on deception). If they fail their insight check while wearing the cloak they wholeheartedly believe whatever was said. They should not be told that they failed.-SPLIT-The Ring of Truths - The wearer of this ring cannot lie about anything. This includes omitting any part of the truth. Once put on the ring cannot be removed for 24 hours.-SPLIT-The Deck of Many Things (can we do it?)-SPLIT-Masquerader’s Mask - Masquerade mask that allows the wearer to take on the facial appearance of anyone who has previously worn the mask.-SPLIT-Seer’s Blindfold - A white blindfold that provides True Sight for 30? feet; however, it also permanently removes the wearers eyes.-SPLIT-Scope of Farsight - A scope which shows you something out of sight but does not necessarily show you something in the distance you are looking. -SPLIT-Hell’s Bell - A small hand bell that, when rung, summons a demonic butler (Sebastian) who will carry out whatever task is given to him in a chaotic evil fashion. This is not made immediately known to the user.-SPLIT-Lycan’s Cloak - A cloak which causes the wearer to appear to transform into a werewolf at will. This does not change anything about the wearer. The cloak looks like a wolfskin cloak when not in use.-SPLIT-Wristband of Stability - A small rubber wristband with two small metal circles in it. The wearer cannot be knocked prone.-SPLIT-Petrock (pronounced like Patrick) - A relatively large rock with a pair of eyes painted on it. The owner of this rock can converse with it and it can offer decent advice. Everyone else just sees a normal rock with eyes painted on.-SPLIT-The Pied Pipe: A flute like instrument that summons a swarm of rats for an unattuned and non-proficient user. If attuned and non-proficient, it summons 1 swarm of rats per player level. If both, it casts [mind control spell] on everyone in a [range] radius.-SPLIT-Forest Guardian’s Armor - A suit of armor made from magical wood that counts as light? armor with an AC of 18?. In addition, animals with a CR of ½ the player level or less will be friendly towards the wearer."
            lootList = rawLoot.split("-SPLIT-")
            loot = random.randrange(0,len(lootList))
            print("Your generated loot is:")
            print(lootList[loot])
            print()
        yn = input("Do you want to generate more loot? ").lower()
        while yn != "yes" and yn != "no":
            print()
            print("Please enter yes or no.")
            yn = input("Do you want to generate more loot? ").lower()
        print()

def main():    
    stopGen = 0
    while stopGen != 1:
        print("Generator Options:")
        print("0. Exit Generator")
        print("1. Arctic Generator")
        print("2. Coastal Generator")
        print("3. Desert Generator")
        print("4. Forest Generator")
        print("5. Grassland Generator")
        print("6. Hill Generator")
        print("7. Mountain Generator")
        print("8. Swamp Generator")
        print("9. Urban Generator")
        print("10. Underdark Generator")
        print("11. Underwater Generator")
        print("12. Dice Roll Generator")
        print("13. Tracking Generator")
        print("14. Loot Generator")
        print()
        biome = int(input("Which generator (input the number) do you want to run? "))
        print()


        if biome == 0:
            stopGen = 1

    ### ARCTIC ###############################################
            
        if biome == 1:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Owl (MM 333).Blood Hawk (MM 319).Kobold (MM 195).Giant Owl (MM 327).Gnoll Witherling (VGM 155).Winged Kobold (MM 195).Gnoll Hunter (VGM 154).Ice Mephit (MM 215).Orc (MM 246).Brown Bear (MM 319).Gnoll Flesh Gnawer (VGM 154).Half-ogre (MM 238).Griffon (MM 174).Guard Drake (VGM 158).Ogre (MM 237).Orc Eye of Gruumsh (MM 247).Orog (MM 247).Polar Bear (MM 334).Saber-toothed Tiger (MM 336).Manticore (MM 213) .Vampiric Mist (MTF  246).Winter Wolf (MM 340).Yeti (MM 305).Revenant (MM 259).Troll (MM 291).Werebear (MM 208).Young Remorhaz (MM 258).Mammoth (MM 332).Young White Dragon (MM 101).Bheur Hag (VGM 160).Lost Sorrowsworn (MTF  233).Frost Giant (MM 155).Shoosuva (VGM 137).Abominable Yeti (MM 306).Flind (VGM 153).Frost Salamander (MTF  223).Winter Eladrin (MTF  197).Remorhaz (MM 258).Roc (MM 260).Boneclaw (MTF  121).Frost Giant Everlasting One (VGM 148).Adult White Dragon (MM 101).Dire Troll (MTF  243).Storm Giant Quintessent (VGM 151).Ancient White Dragon (MM 100).Nightwalker (MTF  216).Elder Tempest (MTF  200).Storm Giant Quintessent (VGM 151).Boneclaw (MTF  121).Frost Giant Everlasting One (VGM 148).Adult White Dragon (MM 101).Dire Troll (MTF  243).Boneclaw (MTF  121).Frost Giant Everlasting One (VGM 148).Adult White Dragon (MM 101).Dire Troll (MTF  243).Abominable Yeti (MM 306).Flind (VGM 153).Frost Salamander (MTF  223).Winter Eladrin (MTF  197).Remorhaz (MM 258).Roc (MM 260).Abominable Yeti (MM 306).Flind (VGM 153).Frost Salamander (MTF  223).Winter Eladrin (MTF  197).Remorhaz (MM 258).Roc (MM 260).Abominable Yeti (MM 306).Flind (VGM 153).Frost Salamander (MTF  223).Winter Eladrin (MTF  197).Remorhaz (MM 258).Roc (MM 260).Mammoth (MM 332).Young White Dragon (MM 101).Bheur Hag (VGM 160).Lost Sorrowsworn (MTF  233).Frost Giant (MM 155).Shoosuva (VGM 137).Mammoth (MM 332).Young White Dragon (MM 101).Bheur Hag (VGM 160).Lost Sorrowsworn (MTF  233).Frost Giant (MM 155).Shoosuva (VGM 137).Mammoth (MM 332).Young White Dragon (MM 101).Bheur Hag (VGM 160).Lost Sorrowsworn (MTF  233).Frost Giant (MM 155).Shoosuva (VGM 137).Mammoth (MM 332).Young White Dragon (MM 101).Bheur Hag (VGM 160).Lost Sorrowsworn (MTF  233).Frost Giant (MM 155).Shoosuva (VGM 137).Manticore (MM 213) .Vampiric Mist (MTF  246).Winter Wolf (MM 340).Yeti (MM 305).Revenant (MM 259).Troll (MM 291).Werebear (MM 208).Young Remorhaz (MM 258).Manticore (MM 213) .Vampiric Mist (MTF  246).Winter Wolf (MM 340).Yeti (MM 305).Revenant (MM 259).Troll (MM 291).Werebear (MM 208).Young Remorhaz (MM 258).Manticore (MM 213) .Vampiric Mist (MTF  246).Winter Wolf (MM 340).Yeti (MM 305).Revenant (MM 259).Troll (MM 291).Werebear (MM 208).Young Remorhaz (MM 258).Manticore (MM 213) .Vampiric Mist (MTF  246).Winter Wolf (MM 340).Yeti (MM 305).Revenant (MM 259).Troll (MM 291).Werebear (MM 208).Young Remorhaz (MM 258).Manticore (MM 213) .Vampiric Mist (MTF  246).Winter Wolf (MM 340).Yeti (MM 305).Revenant (MM 259).Troll (MM 291).Werebear (MM 208).Young Remorhaz (MM 258).Owl (MM 333).Blood Hawk (MM 319).Kobold (MM 195).Giant Owl (MM 327).Gnoll Witherling (VGM 155).Winged Kobold (MM 195).Gnoll Hunter (VGM 154).Ice Mephit (MM 215).Orc (MM 246).Brown Bear (MM 319).Gnoll Flesh Gnawer (VGM 154).Half-ogre (MM 238).Griffon (MM 174).Guard Drake (VGM 158).Ogre (MM 237).Orc Eye of Gruumsh (MM 247).Orog (MM 247).Polar Bear (MM 334).Saber-toothed Tiger (MM 336).Owl (MM 333).Blood Hawk (MM 319).Kobold (MM 195).Giant Owl (MM 327).Gnoll Witherling (VGM 155).Winged Kobold (MM 195).Gnoll Hunter (VGM 154).Ice Mephit (MM 215).Orc (MM 246).Brown Bear (MM 319).Gnoll Flesh Gnawer (VGM 154).Half-ogre (MM 238).Griffon (MM 174).Guard Drake (VGM 158).Ogre (MM 237).Orc Eye of Gruumsh (MM 247).Orog (MM 247).Polar Bear (MM 334).Saber-toothed Tiger (MM 336).Owl (MM 333).Blood Hawk (MM 319).Kobold (MM 195).Giant Owl (MM 327).Gnoll Witherling (VGM 155).Winged Kobold (MM 195).Gnoll Hunter (VGM 154).Ice Mephit (MM 215).Orc (MM 246).Brown Bear (MM 319).Gnoll Flesh Gnawer (VGM 154).Half-ogre (MM 238).Griffon (MM 174).Guard Drake (VGM 158).Ogre (MM 237).Orc Eye of Gruumsh (MM 247).Orog (MM 247).Polar Bear (MM 334).Saber-toothed Tiger (MM 336).Owl (MM 333).Blood Hawk (MM 319).Kobold (MM 195).Giant Owl (MM 327).Gnoll Witherling (VGM 155).Winged Kobold (MM 195).Gnoll Hunter (VGM 154).Ice Mephit (MM 215).Orc (MM 246).Brown Bear (MM 319).Gnoll Flesh Gnawer (VGM 154).Half-ogre (MM 238).Griffon (MM 174).Guard Drake (VGM 158).Ogre (MM 237).Orc Eye of Gruumsh (MM 247).Orog (MM 247).Polar Bear (MM 334).Saber-toothed Tiger (MM 336).Owl (MM 333).Blood Hawk (MM 319).Kobold (MM 195).Giant Owl (MM 327).Gnoll Witherling (VGM 155).Winged Kobold (MM 195).Gnoll Hunter (VGM 154).Ice Mephit (MM 215).Orc (MM 246).Brown Bear (MM 319).Gnoll Flesh Gnawer (VGM 154).Half-ogre (MM 238).Griffon (MM 174).Guard Drake (VGM 158).Ogre (MM 237).Orc Eye of Gruumsh (MM 247).Orog (MM 247).Polar Bear (MM 334).Saber-toothed Tiger (MM 336).Owl (MM 333).Blood Hawk (MM 319).Kobold (MM 195).Giant Owl (MM 327).Gnoll Witherling (VGM 155).Winged Kobold (MM 195).Gnoll Hunter (VGM 154).Ice Mephit (MM 215).Orc (MM 246).Brown Bear (MM 319).Gnoll Flesh Gnawer (VGM 154).Half-ogre (MM 238).Griffon (MM 174).Guard Drake (VGM 158).Ogre (MM 237).Orc Eye of Gruumsh (MM 247).Orog (MM 247).Polar Bear (MM 334).Saber-toothed Tiger (MM 336)."
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                avgTempW = -30
                avgTempSA = 8
                avgTempS = 46
                weatherGen(avgTempW,avgTempSA,avgTempS)
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### COASTAL ##############################################
                
        elif biome == 2:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Crab (MM 322).Blood Hawk (MM 319).Dolphin (VGM 208).Giant Crab (MM 324).Kobold (MM 195).Merfolk (MM 218).Poisonous Snake (MM 334).Stirge (MM 284).Dimetrodon (VGM 139).Giant Lizard (MM 326).Giant Wolf Spider (MM 330).Pseudodragon (MM 254).Pteranodon (MM 80).Winged Kobold (MM 195).Sahuagin (MM 263).Skulk (MTF 227).Giant Eagle (MM 324).Giant Toad (MM 329).Harpy (MM 181).Sea Spawn (VGM 189).Griffon (MM 174).Merrow (MM 219).Ogre (MM 237).Plesiosaurus (MM 80).Quetzalcoatlus (VGM 140).Sahuagin Priestess (MM 264).Sea Hag (MM 179).Deep Scion (VGM 135).Manticore (MM 213).Merrenoloth (MTF 250).Vampiric Mist (MTF 246).Banshee (MM 23).Sahuagin Baron (MM 264).Water Elemental (MM 125).Cyclops (MM 45).Canoloth (MTF 247).Young Bronze Dragon (MM 108).Lonely Sorrowsworn (MTF 232).Young Blue Dragon (MM 91).Stone Giant Dreamwalker	 (VGM 150).Balhannoth (MTF 118).Djinni (MM 144).Marid (MM 146).Morkoth (VGM 178).Roc (MM 260).Spirit Troll (MTF 244).Eidolon (MTF 194).Frost Giant Everlasting One (VGM 148).Ki-rin (VGM 163).Morkoth(in lair)(VGM 178).Storm Giant (MM 156).Wastrilith (MTF 139).Adult Bronze Dragon (MM 108).Adult Blue Dragon (MM 91).Storm Giant Quintessent (VGM 151).Blue Abishai (MTF 161).Dragon Turtle (MM 119).Nagpa (MTF 215).Leviathan (MTF 198).Ancient Bronze Dragon (MM 107).Ancient Blue Dragon (MM 90).Elder Tempest (MTF 200)"
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                avgTempW = 35
                avgTempSA = 60
                avgTempS = 85
                weatherGen(avgTempW,avgTempSA,avgTempS)
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### DESERT ###############################################
                
        elif biome == 3:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Cat (MM 320).Hyena (MM 331).Jackal (MM 331).Scorpion (MM 337).Vulture (MM 339).Camel (MM 320).Flying Snake (MM 322).Kobold (MM 195).Mule (MM 333).Poisonous Snake (MM 334).Stirge (MM 284).Young Kruthik (MTF 211).Constrictor Snake (MM 320).Giant Lizard (MM 326).Giant Poisonous Snake (MM 327).Giant Wolf Spider (MM 330).Pseudodragon (MM 254).Winged Kobold (MM 195).Dust Mephit (MM 215).Firenewt Warrior (VGM 142).Gnoll (MM 163).Hobgoblin (MM 186).Jackalwere (MM 193).Swarm of Insects (MM 338).Death Dog (MM 321).Firenewt Warlock of Imix	 (VGM 143).Giant Hyena (MM 326).Giant Spider (MM 328).Giant Toad (MM 329).Giant Vulture (MM 329).Half-ogre (MM 238).Lion (MM 331).Meazel (MTF 214).Stone Cursed (MTF 240).Thri-kreen (MM 288).Vargouille (VGM 195).Yuan-ti Pureblood (MM 310).Adult Kruthik (MTF 212).Berbalang (MTF 120).Giant Constrictor Snake (MM 324).Gnoll Pack Lord (MM 163).Guard Drake (VGM 158).Ogre (MM 237).Yuan-ti Broodguard (VGM 203).Giant Scorpion (MM 327).Hobgoblin Captain (MM 186).Leucrotta (VGM 169).Mummy (MM 228).Phase Spider (MM 334).Wight (MM 300).Yuan-ti Malison (MM 309).Couatl (MM 43).Dybbuk (MTF 132).Gnoll Fang of Yeenoghu (MM 163).Lamia (MM 201).Weretiger (MM 210).Yuan-ti Mind Whisperer (VGM 204).Yuan-ti Nightmare Speaker (VGM 205).Air Elemental (MM 124).Fire Elemental (MM 125).Kruthik Hive Lord (MTF 212).Revenant (MM 259).Spawn of Kyuss (VGM 192).Tlincalli (VGM 193).Yuan-ti Pit Master (VGM 206).Cyclops (MM 45).Hobgoblin Warlord (MM 187).Medusa (MM 214).Young Brass Dragon (MM 105).Lost Sorrowsworn (MTF 233).Yuan-ti Abomination (MM 308).Howler (MTF 210).Lonely Sorrowsworn (MTF 232).Rot Troll (MTF 244).Young Blue Dragon (MM 91).Githyanki Gish (MTF 205).Githzerai Enlightened (MTF 208).Guardian Naga (MM 234).Orthon (MTF 169).Summer Eladrin (MTF 196).Efreeti (MM 145).Gynosphinx (MM 282).Roc (MM 260).Boneclaw (MTF 121).Eidolon (MTF 194).Githyanki Kith'rak (MTF 205).Ki-rin (VGM 163).Oinoloth (MTF 251).Yuan-ti Anathema (VGM 202).Adult Brass Dragon (MM 105).Githyanki Supreme Commander (MTF 206).Retriever (MTF 222).Mummy Lord (MM 229).Purple Worm (MM 255).Skull Lord (MTF 230).Adult Blue Dragon (MM 91).Phoenix (MTF 199).Storm Giant Quintessent	Giant (VGM 151).Adult Blue Dragon Dracolich (MM 84).Androsphinx (MM 281).Nagpa (MTF 215).Ancient Brass Dragon (MM 104).Nightwalker (MTF 216).Zaratan (MTF 201).Ancient Blue Dragon (MM 90).."
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                avgTempD = 100
                avgTempN = 25
                dWeatherGen(avgTempD,avgTempN)
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### FOREST ###############################################
                
        elif biome == 4:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Awakened Shrub (MM 317).Baboon (MM 318).Badger (MM 318).Cat (MM 320).Deer (MM 321).Hyena (MM 331).Owl (MM 333).Blood Hawk (MM 319).Boggle (VGM 128).Flying Snake (MM 322).Giant Rat (MM 327).Giant Weasel (MM 329).Kobold (MM 195).Mastiff (MM 332).Poisonous Snake (MM 334).Stirge (MM 284).Twig Blight (MM 32).Blink Dog (MM 318).Boar (MM 319).Constrictor Snake (MM 320).Elk (MM 322).Giant Badger (MM 323).Giant Bat (MM 323).Giant Frog (MM 325).Giant Lizard (MM 326).Giant Owl (MM 327).Giant Poisonous Snake (MM 327).Giant Wolf Spider (MM 330).Gnoll Witherling (VGM 155).Goblin (MM 166).Grung (VGM 156).Kenku (MM 194).Kobold Inventor (VGM 166).Needle Blight (MM 32).Panther (MM 333).Pixie (MM 253).Pseudodragon (MM 254).Sprite (MM 283).Swarm of Ravens (MM 339).Vegepygmy (VGM 196).Velociraptor (VGM 140).Winged Kobold (MM 195).Wolf (MM 341).Ape (MM 317).Black Bear (MM 318).Darkling (VGM 134).Giant Wasp (MM 329).Gnoll (MM 163).Gnoll Hunter (VGM 154).Hobgoblin (MM 186).Lizardfolk (MM 204).Orc (MM 246).Orc Nurtured One of Yurtrus (VGM 184).Satyr (MM 267).Skulk (MTF 227).Swarm of Insects (MM 338).Vine Blight (MM 32).Worg (MM 341).Bronze Scout (MTF 125).Brown Bear (MM 319).Bugbear (MM 33).Choker (MTF 123).Deinonychus (VGM 139).Dire Wolf (MM 321).Dryad (MM 121).Giant Hyena (MM 326).Giant Spider (MM 328).Giant Toad (MM 329).Gnoll Flesh Gnawer (VGM 154).Goblin Boss (MM 166).Grung Wildling (VGM 157).Half-ogre (MM 238).Harpy (MM 181).Kobold Dragonshield (VGM 165).Kobold Scale Sorcerer (VGM 167).Meazel (MTF 214).Nilbog (VGM 182).Quickling (VGM 187).Thorny (VGM 197).Tiger (MM 339).Young Faerie Dragon (MM 133).Yuan-ti Pureblood (MM 310).Adult Faerie Dragon (MM 133).Ankheg (MM 21).Awakened Tree (MM 317).Centaur (MM 38).Darkling Elder (VGM 134).Ettercap (MM 131).Giant Boar (MM 323).Giant Constrictor Snake (MM 324).Giant Elk (MM 325).Gnoll Pack Lord (MM 163).Grick (MM 173).Grung Elite Warrior (VGM 157).Guard Drake (VGM 158).Hobgoblin Iron Shadow (VGM 162).Lizardfolk Shaman (MM 205).Meenlock (VGM 170).Ogre (MM 237).Orc Eye of Gruumsh (MM 247).Orc Hand of Yurtrus (VGM 184).Orog (MM 247).Pegasus (MM 250).Shadow Mastiff (VGM 190).Swarm of Poisonous Snakes (MM 338).Vegepygmy Chief (VGM 197).Wererat (MM 209).Will-o-wisp (MM 301).Yuan-ti Broodguard (VGM 203).Displacer Beast (MM 81).Flail Snail (VGM 144).Green Hag (MM 177).Hobgoblin Captain (MM 186).Orc Red Fang of Shargaas (VGM 185).Owlbear (MM 249).Phase Spider (MM 334).Redcap (VGM 188).Vampiric Mist (MTF 246).Werewolf (MM 211).Yuan-ti Malison (MM 309).Banshee (MM 23).Barghest (VGM 123).Couatl (MM 43).Girallon (VGM 152).Gnoll Fang of Yeenoghu (MM 163).Hobgoblin Devastator (VGM 161).Iron Cobra (MTF 125).Orc Blade of Ilneval (VGM 183).Stegosaurus (VGM 140).Stone Defender (MTF 126).Wereboar (MM 209).Weretiger (MM 210).Yeth Hound (VGM 201).Yuan-ti Mind Whisperer (VGM 204).Yuan-ti Nightmare Speaker (VGM 205).Brontosaurus (VGM 139).Gorgon (MM 171).Oaken Bolter (MTF 126).Revenant (MM 259).Shambling Mound (MM 270).Troll (MM 291).Unicorn (MM 294).Werebear (MM 208).Wood Woad (VGM 198).Yuan-ti Pit Master (VGM 206).Hobgoblin Warlord (MM 187).Giant Ape (MM 323).Grick Alpha (MM 173).Korred (VGM 168).Lost Sorrowsworn (MTF 233).Oni (MM 239).Venom Troll (MTF 245).Yuan-ti Abomination (MM 308).Corpse Flower (MTF 127).Shoosuva (VGM 137).Young Green Dragon (MM 94).Flind (VGM 153).Rot Troll (MTF 244).Treant (MM 289).Autumn Eladrin (MTF 195).Guardian Naga (MM 234).Spring Eladrin (MTF 196).Summer Eladrin (MTF 196).Winter Eladrin (MTF 197).Young Gold Dragon (MM 115).Hungry Sorrowsworn (MTF 232).Spirit Troll (MTF 244).Eidolon (MTF 194).Gray Render (MTF 209).Yuan-ti Anathema (VGM 202).Dire Troll (MTF 243).Retriever (MTF 222).Adult Green Dragon (MM 94).Adult Gold Dragon (MM 114).Nagpa (MTF 215).Ancient Green Dragon (MM 93).Zaratan (MTF 201).Ancient Gold Dragon (MM 113)"
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                avgTempW = 30
                avgTempSA = 50
                avgTempS = 70
                weatherGen(avgTempW,avgTempSA,avgTempS)
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### GRASSLAND ############################################
                
        elif biome == 5:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Cat (MM 320).Deer (MM 321).Eagle (MM 322).Goat (MM 330).Hyena (MM 331).Jackal (MM 331).Vulture (MM 339).Blood Hawk (MM 319).Flying Snake (MM 322).Giant Weasel (MM 329).Poisonous Snake (MM 334).Stirge (MM 284).Axe Beak (MM 317).Boar (MM 319).Elk (MM 322).Giant Poisonous Snake (MM 327).Giant Wolf Spider (MM 330).Gnoll Witherling (VGM 155).Goblin (MM 166).Hadrosaurus (VGM 140).Panther (MM 333).Pteranodon (MM 80).Riding Horse (MM 336).Rothe (VGM 207).Velociraptor (VGM 140).Wolf (MM 341).Cockatrice (MM 42).Giant Goat (MM 326).Giant Wasp (MM 329).Gnoll (MM 163).Gnoll Hunter (VGM 154).Hobgoblin (MM 186).Jackalwere (MM 193).Orc (MM 246).Orc Nurtured One of Yurtrus (VGM 184).Swarm of Insects (MM 338).Worg (MM 341).Bronze Scout (MTF 125).Bugbear (MM 33).Deinonychus (VGM 139).Giant Eagle (MM 324).Giant Hyena (MM 326).Giant Vulture (MM 329).Gnoll Flesh Gnawer (VGM 154).Goblin Boss (MM 166).Hippogriff (MM 184).Lion (MM 331).Meazel (MTF 214).Scarecrow (MM 268).Thri-kreen (MM 288).Tiger (MM 339).Allosaurus (MM 79).Ankheg (MM 21).Aurochs (VGM 207).Centaur (MM 38).Giant Boar (MM 323).Giant Elk (MM 325).Gnoll Pack Lord (MM 163).Griffon (MM 174).Hobgoblin Iron Shadow (VGM 162).Ogre (MM 237).Ogre Bolt Launcher (MTF 220).Ogre Howdah (MTF 221).Orc Eye of Gruumsh (MM 247).Orc Hand of Yurtrus (VGM 184).Orog (MM 247).Pegasus (MM 250).Rhinoceros (MM 336).Ankylosaurus (MM 79).Hobgoblin Captain (MM 186).Leucrotta (VGM 169).Manticore (MM 213).Ogre Chain Brute (MTF 221).Phase Spider (MM 334).Sword Wraith Warrior (MTF 241).Vampiric Mist (MTF 246).Barghest (VGM 123).Couatl (MM 43).Elephant (MM 322).Gnoll Fang of Yeenoghu (MM 163).Hobgoblin Devastator (VGM 161).Iron Cobra (MTF 125).Ogre Battering Ram (MTF 220).Orc Blade of Ilneval (VGM 183).Stegosaurus (VGM 140).Stone Defender (MTF 126).Wereboar (MM 209).Weretiger (MM 210).Yeth Hound (VGM 201).Brontosaurus (VGM 139).Bulette (MM 34).Gorgon (MM 171).Oaken Bolter (MTF 126).Triceratops (MM 80).Chimera (MM 39).Cyclops (MM 45).Hobgoblin Warlord (MM 187).Mouth of Grolantor (VGM 149).Howler (MTF 210).Shoosuva (VGM 137).Sword Wraith Commander (MTF 241).Tyrannosaurus Rex (MM 80).Flind (VGM 153).Spring Eladrin (MTF 196).Young Gold Dragon (MM 115).Eidolon (MTF 194).Ki-rin (VGM 163).Cadaver Collector (MTF 122).Adult Gold Dragon (MM 114).Zaratan (MTF 201).Elder Tempest (MTF 200).Ancient Gold Dragon (MM 113)"
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                avgTempW = -40
                avgTempSA = 30
                avgTempS = 100
                weatherGen(avgTempW,avgTempSA,avgTempS)
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### HILL #################################################
                
        elif biome == 6:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Baboon (MM 318).Eagle (MM 322).Goat (MM 330).Hyena (MM 331).Raven (MM 335).Vulture (MM 339).Blood Hawk (MM 319).Boggle (VGM 128).Giant Weasel (MM 329).Kobold (MM 195).Mastiff (MM 332).Mule (MM 333).Neogi Hatchling (VGM 179).Poisonous Snake (MM 334).Stirge (MM 284).Xvart (VGM 200).Axe Beak (MM 317).Boar (MM 319).Elk (MM 322).Giant Owl (MM 327).Giant Wolf Spider (MM 330).Gnoll Witherling (VGM 155).Goblin (MM 166).Kobold Inventor (VGM 166).Panther (MM 333).Pseudodragon (MM 254).Swarm of Bats (MM 337).Swarm of Ravens (MM 339).Winged Kobold (MM 195).Wolf (MM 341).Firenewt Warrior (VGM 142).Giant Goat (MM 326).Gnoll (MM 163).Gnoll Hunter (VGM 154).Hobgoblin (MM 186).Orc (MM 246).Orc Nurtured One of Yurtrus (VGM 184).Swarm of Insects (MM 338).Worg (MM 341).Bronze Scout (MTF 125).Brown Bear (MM 319).Deinonychus (VGM 139).Dire Wolf (MM 321).Firenewt Warlock of Imix	 (VGM 143).Giant Eagle (MM 324).Giant Hyena (MM 326).Giant Strider (VGM 143).Gnoll Flesh Gnawer (VGM 154).Goblin Boss (MM 166).Half-ogre (MM 238).Harpy (MM 181).Hippogriff (MM 184).Kobold Dragonshield (VGM 165).Kobold Scale Sorcerer (VGM 167).Lion (MM 331).Meazel (MTF 214).Nilbog (VGM 182).Xvart Warlock of Raxivort (VGM 200).Aurochs (VGM 207).Giant Boar (MM 323).Giant Elk (MM 325).Gnoll Pack Lord (MM 163).Griffon (MM 174).Hobgoblin Iron Shadow (VGM 162).Ogre (MM 237).Ogre Bolt Launcher (MTF 220).Ogre Howdah (MTF 221).Orc Eye of Gruumsh (MM 247).Orc Hand of Yurtrus (VGM 184).Orog (MM 247).Pegasus (MM 250).Peryton (MM 251).Quetzalcoatlus (VGM 140).Shadow Mastiff (VGM 190).Green Hag (MM 177).Hobgoblin Captain (MM 186).Manticore (MM 213).Neogi (VGM 180).Ogre Chain Brute (MTF 221).Orc Red Fang of Shargaas (VGM 185).Phase Spider (MM 334).Redcap (VGM 188).Werewolf (MM 211).Barghest (VGM 123).Ettin (MM 132).Gnoll Fang of Yeenoghu (MM 163).Hobgoblin Devastator (VGM 161).Iron Cobra (MTF 125).Neogi Master (VGM 180).Ogre Battering Ram (MTF 220).Orc Blade of Ilneval (VGM 183).Stone Defender (MTF 126).Wereboar (MM 209).Yeth Hound (VGM 201).Bulette (MM 34).Gorgon (MM 171).Hill Giant (MM 155).Oaken Bolter (MTF 126).Revenant (MM 259).Tanarukk (VGM 186).Troll (MM 291).Werebear (MM 208).Annis Hag (VGM 159).Chimera (MM 39).Cyclops (MM 45).Galeb Duhr (MM 139).Hobgoblin Warlord (MM 187).Mouth of Grolantor (VGM 149).Wyvern (MM 303).Stone Giant (MM 156).Young Copper Dragon (MM 111).Howler (MTF 210).Shoosuva (VGM 137).Flind (VGM 153).Stone Giant Dreamwalker (VGM 150).Young Red Dragon (MM 98).Roc (MM 260).Gray Render (MTF 209).Dire Troll (MTF 243).Adult Copper Dragon (MM 111).Adult Red Dragon (MM 98).Ancient Copper Dragon (MM 110).Zaratan (MTF 201).Elder Tempest (MTF 200).Ancient Red Dragon (MM 97)"
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                avgTempW = 0
                avgTempSA = 45
                avgTempS = 90
                weatherGen(avgTempW,avgTempSA,avgTempS)
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### MOUNTAIN #############################################
                
        elif biome == 7:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Eagle (MM 322).Goat MM 330).Blood Hawk (MM 319).Kobold (MM 195).Stirge (MM 284).Tribal Warrior (MM 350).Young Kruthik (MTF 211).Aarakocra (MM 12).Derro (MTF 158).Kobold Inventor (VGM 166).Pseudodragon (MM 254).Pteranodon (MM 80).Star Spawn Grue (MTF 234).Swarm of Bats (MM 337).Winged Kobold (MM 195).Firenewt Warrior (VGM 142).Giant Goat (MM 326).Orc (MM 246).Orc Nurtured One of Yurtrus (VGM 184).Bronze Scout (MTF 125).Choker (MTF 123).Duergar Soulblade (MTF 190).Firenewt Warlock of Imix (VGM 143).Giant Eagle (MM 324).Half-ogre (MM 238).Harpy (MM 181).Hippogriff (MM 184).Kobold Dragonshield (VGM 165).Kobold Scale Sorcerer (VGM 167).Lion (MM 331).Meazel (MTF 214).Stone Cursed (MTF 240).Adult Kruthik (MTF 212).Aurochs (VGM 207).Berserker (MM 344).Duergar Hammerer (MTF 188).Duergar Kavalrachni (MTF 189).Duergar Mind Master (MTF 189).Duergar Stone Guard (MTF 191).Duergar Xarrorn (MTF 193).Giant Elk (MM 325).Griffon (MM 174).Guard Drake (VGM 158).Ogre (MM 237).Ogre Bolt Launcher (MTF 220).Ogre Howdah (MTF 221).Orc Claw of Luthic (VGM 183).Orc Eye of Gruumsh (MM 247).Orc Hand of Yurtrus (VGM 184).Orog (MM 247).Peryton (MM 251).Quetzalcoatlus (VGM 140).Saber-toothed Tiger (MM 336).Basilisk (MM 24).Duergar Screamer (MTF 190).Hell Hound (MM 182).Manticore (MM 213).Ogre Chain Brute (MTF 221).Orc Red Fang of Shargaas (VGM 185).Vampiric Mist (MTF 246).Barghest (VGM 123).Ettin (MM 132).Iron Cobra (MTF 125).Ogre Battering Ram (MTF 220).Orc Blade of Ilneval (VGM 183).Stone Defender (MTF 126).Air Elemental (MM 124).Bulette (MM 34).Kruthik Hive Lord (MTF 212).Oaken Bolter (MTF 126).Tanarukk (VGM 186).Troll (MM 291).Annis Hag (VGM 159).Chimera (MM 39).Cyclops (MM 45).Duergar Warlord (MTF 192).Galeb Duhr (MM 139).Wyvern (MM 303).Lost Sorrowsworn (MTF 233).Stone Giant (MM 156).Frost Giant (MM 155).Cloud Giant (MM 154).Fire Giant (MM 154).Lonely Sorrowsworn (MTF 232).Young Silver Dragon (MM 118).Githyanki Gish (MTF 205).Githzerai Enlightened (MTF 208).Stone Giant Dreamwalker (VGM 150).Young Red Dragon (MM 98).Balhannoth (MTF 118).Cloud Giant Smiling One (VGM 146).Roc (MM 260).Duergar Despot (MTF 188).Eidolon (MTF 194).Githyanki Kith'rak (MTF 205).Ki-rin (VGM 163).Dire Troll (MTF 243).Star Spawn Seer Medium (MTF 236).Fire Giant Dreadnought (VGM 147).Githyanki Supreme Commander (MTF 206).Adult Silver Dragon (MM 117).Phoenix (MTF 199).Star Spawn Larva Mage (MTF 235).Storm Giant Quintessent (VGM 151).Adult Red Dragon (MM 98).Red Abishai (MTF 162).Zaratan (MTF 201).Ancient Silver Dragon (MM 116).Elder Tempest (MTF 200).Ancient Red Dragon (MM 97)"
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                avgTempW = 52
                avgTempSA = 60
                avgTempS = 68
                weatherGen(avgTempW,avgTempSA,avgTempS)
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### SWAMP ################################################
                
        elif biome == 8:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Rat (MM 335).Raven (MM 335).Giant Rat (MM 327).Kobold (MM 195).Poisonous Snake (MM 334).Stirge (MM 284).Bullywug (MM 35).Constrictor Snake (MM 320).Dimetrodon (VGM 139).Giant Frog (MM 325).Giant Lizard (MM 326).Giant Poisonous Snake (MM 327).Hadrosaurus (VGM 140).Mud Mephit (MM 216).Oblex Spawn (MTF 217).Star Spawn Grue (MTF 234).Swarm of Rats (MM 339).Swarm of Ravens (MM 339).Vegepygmy (VGM 196).Winged Kobold (MM 195).Wretched Sorrowsworn (MTF 233).Crocodile (MM 320).Darkling (VGM 134).Lizardfolk (MM 204).Orc (MM 246).Skulk (MTF 227).Swarm of Insects (MM 338).Swarm of Rot Grubs (VGM 208).Ghoul (MM 148).Giant Spider (MM 328).Giant Toad (MM 329).Meazel (MTF 214).Thorny (VGM 197).Vargouille (VGM 195).Yuan-ti Pureblood (MM 310).Darkling Elder (VGM 134).Ghast (MM 148).Giant Constrictor Snake (MM 324).Guard Drake (VGM 158).Lizardfolk Shaman (MM 205).Meenlock (VGM 170).Ogre (MM 237).Orc Eye of Gruumsh (MM 247).Shadow Mastiff (VGM 190).Swarm of Poisonous Snakes (MM 338).Vegepygmy Chief (VGM 197).Will-o-wisp (MM 301).Flail Snail (VGM 144).Green Hag (MM 177).Redcap (VGM 188).Sword Wraith Warrior (MTF 241).Vampiric Mist (MTF 246).Wight (MM 300).Yuan-ti Malison (MM 309).Adult Oblex (MTF 218).Allip (MTF 116).Catoblepas (VGM 129).Giant Crocodile (MM 324).Revenant (MM 259).Shambling Mound (MM 270).Troll (MM 291).Water Elemental (MM 125).Bodak (VGM 127).Lost Sorrowsworn (MTF 233).Maurezhi (MTF 133).Venom Troll (MTF 245).Young Black Dragon (MM 88).Yuan-ti Abomination (MM 308).Corpse Flower (MTF 127).Hydra (MM 190).Sword Wraith Commander (MTF 241).Rot Troll (MTF 244).Elder Oblex (MTF 219).Froghemoth (VGM 145).Spirit Troll (MTF 244).Star Spawn Seer (MTF 236).Wastrilith (MTF 139).Adult Black Dragon (MM 88).Nabassu (MTF 135).Skull Lord (MTF 230).Nagpa (MTF 215).Nightwalker (MTF 216).Ancient Black Dragon (MM 87)"
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                avgTempW = 30
                avgTempSA = 50
                avgTempS = 70
                weatherGen(avgTempW,avgTempSA,avgTempS)
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### URBAN ################################################
                
        elif biome == 9:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = ""
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                print("The temperature depends on the biome it is located within.")
                precipGen()
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### UNDERDARK ############################################
                
        elif biome == 10:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Cranium Rat (VGM 133).Giant Fire Beetle (MM 325).Myconid Sprout (MM 230).Shrieker (MM 138).Boggle (VGM 128).Flumph (MM 135).Giant Rat (MM 327).Kobold (MM 195).Neogi Hatchling (VGM 179).Stirge (MM 284).Xvart (VGM 200).Young Kruthik (MTF 211).Deep Rothe (VGM 207).Derro (MTF 158).Drow (MM 128).Giant Bat (MM 323).Giant Centipede (MM 323).Giant Lizard (MM 326).Giant Poisonous SnakeMedium (MM 327).Goblin (MM 166).Grimlock (MM 175).Kobold Inventor (VGM 166).Kuo-toa (MM 199).Male Steeder (MTF 238).Oblex Spawn (MTF 217).Swarm of Bats (MM 337).Troglodyte (MM 290).Violet Fungus (MM 138).Winged Kobold (MM 195).Wretched Sorrowsworn (MTF 233).Chitine (VGM 131).Darkling (VGM 134).Darkmantle (MM 46).Firenewt Warrior (VGM 142).Gas Spore (MM 138).Gazer (VGM 126).Gray Ooze (MM 243).Hobgoblin (MM 186).Magma Mephit (MM 216).Myconid Adult (MM 232).Orc (MM 246).Orc Nurtured One of Yurtrus (VGM 184).Piercer (MM 252).Rust Monster (MM 262).Scout (MM 349).Shadow (MM 269).Skulk (MTF 227).Swarm of Insects (MM 338).Swarm of Rot Grubs (VGM 208).Bugbear (MM 33).Choker (MTF 123).Duergar (MM 122).Duergar Soulblade (MTF 190).Female Steeder (MTF 238).Fire Snake (MM 265).Firenewt Warlock of Imix(VGM 143).Ghoul (MM 148).Giant Spider (MM 328).Giant Strider (VGM 143).Giant Toad (MM 329).Goblin Boss (MM 166).Half-ogre (MM 2380.Kobold Dragonshield (VGM 165).Kobold Scale Sorcerer (VGM 167).Kuo-toa Whip (MM 200).Maw Demon (VGM 137).Meazel (MTF 214).Nilbog (VGM 182).Quaggoth Spore Servant(MM 230).Specter (MM 279).Vargouille (VGM 195).Xvart Warlock of Raxivort (VGM 200).Adult Kruthik (MTF 212).Carrion Crawler (MM 37).Darkling Elder (VGM 134).Duergar Hammerer (MTF 188).Duergar Kavalrachni (MTF 189).Duergar Mind Master (MTF 189).Duergar Stone Guard (MTF 191).Duergar Xarrorn (MTF 193).Gargoyle (MM 140).Gelatinous Cube (MM 242).Ghast (MM 148).Giant Constrictor Snake (MM 324).Gibbering Mouther (MM 157).Grick (MM 173).Guard Drake (VGM 158).Intellect Devourer (MM 191).Mimic (MM 220).Minotaur Skeleton (MM 273).Nothic (MM 236).Ochre Jelly (MM 243).Ogre (MM 237).Orc Claw of Luthic (VGM 183).Orc Eye of Gruumsh (MM 247).Orc Hand of Yurtrus (VGM 184).Orog (MM 247).Polar Bear (MM 334).Quaggoth (MM 256).Yuan-ti Broodguard (VGM 203).Cave Fisher (VGM 130).Choldrith (VGM 132).Derro Savant (MTF 159).Doppelganger (MM 82).Duergar Screamer (MTF 190).Flail Snail (VGM 144).Grell (MM 172).Hell Hound (MM 182).Hobgoblin Captain (MM 186).Hook Horror (MM 189).Minotaur (MM 223).Neogi (VGM 180).Orc Red Fang of Shargaas (VGM 185).Phase Spider (MM 334).Quaggoth Thonot (MM 256).Slithering Tracker (VGM 191).Spectator (MM 30).Trapper (VGM 194).Vampiric Mist (MTF 246).Water Weird (MM 299).Wight (MM 300).Babau (VGM 136).Barghest (VGM 123).Black Pudding (MM 241).Bone Naga (MM 233).Chuul (MM 40).Ettin (MM 132).Flameskull (MM 134).Ghost (MM 147).Neogi Master (VGM 180).Orc Blade of Ilneval (VGM 183).Yuan-ti Mind Whisperer (VGM 204).Yuan-ti Nightmare Speaker (VGM 205).Adult Oblex (MTF 218).Beholder Zombie (MM 316).Drow Elite Warrior (MM 128).Earth Elemental (MM 124).Kruthik Hive Lord (MTF 212).Mindwitness (VGM 176).Otyugh (MM 248).Roper (MM 261).Salamander (MM 266).Spawn of Kyuss (VGM 192).Swarm of Cranium Rats (VGM 133).Tanarukk (VGM 186).Troll (MM 291).Umber Hulk (MM 292).Vampire Spawn (MM 298).Wraith (MM 302).Xorn (MM 304).Yuan-ti Pit Master (VGM 206).Bodak (VGM 127).Chimera (MM 39).Cyclops (MM 45).Drider (MM 120).Duergar Warlord (MTF 192).Gauth (VGM 125).Hobgoblin Warlord (MM 187).Kuo-toa Archpriest (MM 200).Armanite (MTF 131).Dhergoloth (MTF 248).Draegloth (VGM 141).Drow Mage (MM 129).Grick Alpha (MM 173).Lost Sorrowsworn (MTF 233).Mind Flayer (MM 222).Stone Giant (MM 156).Venom Troll (MTF 245).Canoloth (MTF 247).Cloaker (MM 41).Fomorian (MM 136).Howler (MTF 210).Mind Flayer Arcanist (MM 222).Spirit Naga (MM 234).Drow House Captain (MTF 184).Fire Giant (MM 154).Lonely Sorrowsworn (MTF 232).Rot Troll (MTF 244).Ulitharid (VGM 175).Aboleth (MM 13).Alhoon (VGM 172).Death Kiss (VGM 124).Elder Oblex (MTF 219).Froghemoth (VGM 145).Orthon (MTF 169).Alkilith (MTF 130).Balhannoth (MTF 118).Behir (MM 25).Dao (MM 143).Drow Shadowblade (MTF 187).Hungry Sorrowsworn (MTF 232).Spirit Troll (MTF 244).Duergar Despot (MTF 188).Oinoloth (MTF 251).Yuan-ti Anathema (VGM 202).Angry Sorrowsworn (MTF 231).Beholder (MM 28).Devourer (VGM 138).Dire Troll (MTF 243).Drow Arachnomancer (MTF 182).Neothelid (VGM 181).Wastrilith (MTF 139).Young Red Shadow Dragon (MM 85).Death Tyrant (MM 29).Drow Inquisitor (MTF 184).Elder Brain (VGM 174).Fire Giant Dreadnought (VGM 147).Retriever (MTF 222).Nabassu (MTF 135).Purple Worm (MM 255).Skull Lord (MTF 230).Nagpa (MTF 215).Drow Favored Consort (MTF 183).Sibriex (MTF 137).Drow Matron Mother (MTF 186).Nightwalker (MTF 216).Mind Flayer Lich (VGM 172).Zaratan (MTF 201)"
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                print("The temperature depends on the biome of the surface.")
                precipGen()
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### UNDERWATER ###########################################
                
        elif biome == 11:
            gen = genType()
            if gen == 0:
                print()
            elif gen == 1:
                rawCreatures = "Quipper (MM 335).Dolphin (VGM 208).Merfolk (MM 218).Constrictor Snake (MM 320).Steam Mephit (MM 217).Giant Sea Horse (MM 328).Reef Shark (MM 336).Sahuagin (MM 263).Giant Octopus (MM 326).Sea Spawn (VGM 189).Swarm of Quippers (MM 338).Giant Constrictor Snake (MM 324).Hunter Shark (MM 330).Merrow (MM 219).Plesiosaurus (MM 80).Sahuagin Priestess (MM 264).Sea Hag (MM 179).Deep Scion (VGM 135).Killer Whale (MM 331).Giant Shark (MM 328).Sahuagin Baron (MM 264).Water Elemental (MM 125).Marid (MM 146).Morkoth (VGM 178).Morkoth (in lair)(VGM 178).Wastrilith (MTF 139).Storm Giant Quintessent (VGM 151).Dragon Turtle (MM 119).Leviathan (MTF 198).Kraken (MM 197)"
                creaturesList = rawCreatures.split(".")
                creatureGen(creaturesList)
            elif gen == 2:
                avgTempS = 63
                avgTempD = 35
                wWeatherGen(avgTempS,avgTempD)
            elif gen == 3:
                locationList = ["Location 1","Location 2","Location 3"]
                locationGen(locationList)

    ### DICE ROLLING #########################################
        elif biome == 12:
            repeat = 1
            while repeat == 1:
                print("Dice Options:")
                print("1. d2")
                print("2. d4")
                print("3. d6")
                print("4. d8")
                print("5. d10")
                print("6. d12")
                print("7. d20")
                print("8. d100")
                print()
                diceType = int(input("Which dice (Enter the number) do you want to roll? "))
                print()
                numDice = int(input("How many dice would you like to roll? "))
                print()
                modYN = input("Is there a modifier on the roll? ").lower()
                print()
                while modYN != "yes" and modYN != "no":
                        print()
                        print("Please enter yes or no.")
                        modYN = input("Is there a modifier on the roll? ").lower()
                if modYN == "yes":
                    modX = input("Is the modifier on every roll (yes) or on the sum (no)? ")
                    print()
                    while modX != "yes" and modX != "no":
                        print()
                        print("Please enter yes or no.")
                        modX = input("Is the modifier on every roll (yes) or on the sum (no)? ").lower()
                    if modX == "yes":
                        xMod = int(input("What is the modifier (enter the value)? "))
                        sumMod = 0
                    elif modX == "no":
                        xMod = 0
                        sumMod = int(input("What is the modifier (enter the value)? "))
                elif modYN == "no":
                    xMod = 0
                    sumMod = 0
                diceSum = 0
                if diceType == 1:
                    for i in range(numDice):
                        i = random.randrange(1,3) + xMod
                        print(i)
                        diceSum = diceSum + i
                    print("Sum: ", diceSum + sumMod)
                    print()
                elif diceType == 2:
                    for i in range(numDice):
                        i = random.randrange(1,5) + xMod
                        print(i)
                        diceSum = diceSum + i
                    print("Sum: ", diceSum + sumMod)
                    print()
                elif diceType == 3:
                    for i in range(numDice):
                        i = random.randrange(1,7) + xMod
                        print(i)
                        diceSum = diceSum + i
                    print("Sum: ", diceSum + sumMod)
                    print()
                elif diceType == 4:
                    for i in range(numDice):
                        i = random.randrange(1,9) + xMod
                        print(i)
                        diceSum = diceSum + i
                    print("Sum: ", diceSum + sumMod)
                    print()
                elif diceType == 5:
                    for i in range(numDice):
                        i = random.randrange(1,11) + xMod
                        print(i)
                        diceSum = diceSum + i
                    print("Sum: ", diceSum + sumMod)
                    print()
                elif diceType == 6:
                    for i in range(numDice):
                        i = random.randrange(1,13) + xMod
                        print(i)
                        diceSum = diceSum + i
                    print("Sum: ", diceSum + sumMod)
                    print()
                elif diceType == 7:
                    for i in range(numDice):
                        i = random.randrange(1,21) + xMod
                        print(i)
                        diceSum = diceSum + i
                    print("Sum: ", diceSum + sumMod)
                    print()
                elif diceType == 8:
                    for i in range(numDice):
                        i = random.randrange(1,101) + xMod
                        print(i)
                        diceSum = diceSum + i
                    print("Sum: ", diceSum + sumMod)
                    print()
                yn = input("Do you want to roll more dice? ").lower()
                if yn == "yes":
                    print()
                if yn == "no":
                    print()
                    repeat = 0
            

    ### TRACKING #############################################
        elif biome == 13:
            print("Tracking Options:")
            print("1. Tarrasque")
            print("2. Demogorgon")
            print("3. Baphomet")
            print("4. Fraz-Urb'Luu")
            print("5. Jubilex")
            print("6. Orcus")
            print("7. Yeenoghu")
            print("8. Zuggtomy")
            print("9. Graz'zt")
            print("10. All")
            print()
            trackNum = int(input("Which tracker (Input the Number) do you want to run? "))
            print()
            if trackNum == 1:
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("The Tarrasque has moved",distance,unit,direction,sep=" ")
                print()
            elif trackNum == 2:
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Demogorgon has moved",distance,unit,direction,sep=" ")
                print()
            elif trackNum == 3:
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Baphomet has moved",distance,unit,direction,sep=" ")
                print()
            elif trackNum == 4:
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Fraz-Urb'Luu has moved",distance,unit,direction,sep=" ")
                print()
            elif trackNum == 5:
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Jubilex has moved",distance,unit,direction,sep=" ")
                print()
            elif trackNum == 6:
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Orcus has moved",distance,unit,direction,sep=" ")
                print()
            elif trackNum == 7:
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Yeenoghu has moved",distance,unit,direction,sep=" ")
                print()
            elif trackNum == 8:
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Zuggtomy has moved",distance,unit,direction,sep=" ")
                print()
            elif trackNum == 9:
                town = random.randrange(0,16)
                if town == 0:
                    print("Graz'zt is in a town.")
                else:
                    print("Graz'zt is not in a town.")
                print()
            elif trackNum == 10:
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("The Tarrasque has moved",distance,unit,direction,sep=" ")
                print()
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Demogorgon has moved",distance,unit,direction,sep=" ")
                print()
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Baphomet has moved",distance,unit,direction,sep=" ")
                print()
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Fraz-Urb'Luu has moved",distance,unit,direction,sep=" ")
                print()
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Jubilex has moved",distance,unit,direction,sep=" ")
                print()
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Orcus has moved",distance,unit,direction,sep=" ")
                print()
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Yeenoghu has moved",distance,unit,direction,sep=" ")
                print()
                direction = trackingGen()
                distance = random.randrange(0,51)
                if distance == 1:
                    unit = "mile"
                else:
                    unit = "miles"
                print("Zuggtomy has moved",distance,unit,direction,sep=" ")
                print()
                town = random.randrange(0,16)
                if town == 0:
                    print("Graz'zt is in a town.")
                else:
                    print("Graz'zt is not in a town.")
                print()
                
    ### LOOT #################################################
        elif biome == 14:
            loot()
        
main()
