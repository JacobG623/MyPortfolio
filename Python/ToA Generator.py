import random

def weatherGen():
    td20 = random.randrange (1,21)
    if td20 <= 14:
        print("It is the normal temperature of 95 degrees")
    elif td20 <= 17:
        td4 = random.randrange (1,5)
        d4 = td4 * 10
        temp = 95 - d4
        print("It is colder than usual at ",temp," degrees")
    else:
        print("It is extremely hot at over 100 degrees. Characters must make a DC5 CON save which increases by 1 every hour for each hour spent in the heat or gain one level of exhaustion. Additionally, insect salve gets sweated off more rapidly, reuiring twice as much to work for a full day.")
    wd20 = random.randrange (1,21)
    if wd20 <= 12:
        print("It isn't windy today")
    elif wd20 <= 17:
        print("The wind is light today")
    else:
        print("The wind is strong today. Boat speed is halved and chracaters must roll a d4 and on a 3 or 4 they make no headway. In addition attacks suffer from disadvantage due to the strong wind.")
    pd20 =  random.randrange (1,21)
    if pd20 <= 12:
        print("There is no precipitation today")
    elif pd20 <= 17:
        print("There is light precipitation today")
    else:
        wd4 = random.randrange (1,5)
        if wd4 < 4:
            print("There is heavy rain today. Visibility is limited to 50 yards, only Huge or larger creatures can be distinguished beyond that. Boat speed is halved. Navigation checks are made with disadvantage.")
        else:
            print("There is a tropical storm today. Travel by boat is impossible and travel on foot automatically causes 1 level of exhaustion as well as a DC10 CON save to avoid gaining another. Navigation checks are made with disadvantage. Characters must roll a d4 and on a 3 or 4 they make no progress on foot. Attacks suffer from disadvantage.")
    print()

def aarakocra():
    d4 = random.randrange(1,5)
    total = d4 + 1;
    print("Any character with a passive Wisdom (Perception) score of 15 or higher spots ",total," aarakocra flying overhead. These creatures are scouts from Kir Sabal or another aerie. They observe the party from a safe distance but don't approach unless the characters demonstrate peaceful intentions. The bird folk are friendly and can point characters in the direction of nearby landmarks.")
    print()

def albinoDwarves():
    d4 = random.randrange(1,5)
    total = d4 + 3
    print("The characters are ambushed by ",total," albino dwarf warriors (see appendix D) that attack from hidden burrows. Any character with a passive Wisdom (Perception) score of 13 or higher spots the dwarves, but all others are surprised. The dwarves knock characters out rather than killing them, stealing food, water, and gear from those rendered unconscious. They break off their attack if any character speaks Dwarvish to them or demonstrates peaceful intentions.")
    print()

def aldani():
    d4 = random.randrange(1,5)
    print("The characters are shadowed by ",d4," aldani (see appendix D), which are noticed by any character with a passive Wisdom (Perception) score of 12 or higher. The aldani don't communicate with others unless they must, and they won't fight unless the characters refuse to take a bribe to leave the area. The aldani will aid the characters only if they're offered something of great value in return- for example, an offer to drive off a pack of predatory dinosaurs encroaching on their territory.")
    print()

def almiraj():
    d6 = random.randrange(1,7)
    print("Any character with a passive Wisdom (Perception) score of 12 or higher spots ",d6," almiraj (see appendix D) 60 feet away. The almiraj run from any creature that they can see within 30 feet of them. Any character who successfully traps an almiraj can use an actio n to make a DC 14 Wisdom (Animal Handling) check. If the check succeeds, the almiraj becomes calm and doesn't attack the character or run away unless it feels threatened or is harmed.")
    print()

def apes():
    ad4 = random.randrange(1,5)
    bd4 = random.randrange(1,5)
    d4 = ad4 + bd4
    print("The characters stumble upon ",d4," apes enjoying some excellent fruit. The apes feel threatened and show signs of defending their food. If the characters immediately back away slowly, the apes do nothing but make threatening displays. Otherwise, they attack.")
    print()

def artusCimber():
    print("Artus Cimber (with or without his saurial traveling companion, Dragonbait) can be encountered almost anywhere. See appendix D for more information on these NPCs. The characters might stumble into Artus's camp in the evening, or he might walk into theirs. They could find him at the camp of another group of explorers, or telling a story to Dragonbait. He could appear out of nowhere and use the powers of the Ring of Winter to help characters caught up in a tough encounter.")
    print()

def assassinVines():
    d3 = random.randrange(1,4)
    print("The characters unwittingly enter the hunting grounds of ",d3," assassin vines (see appendix D). The vines are indistinguishable from normal plants and can't be spotted with Wisdom (Perception) checks. However, they draw carrion to their roots, so characters might smell a dead body nearby. Because assassin vines can move, an encounter in the evening or at night might involve the vines creeping into the characters' camp and strangling them as they sleep.")
    print()

def axeBeaks():
    d6 = random.randrange(1,7)
    total = d6 + 3
    print("A flock of ",total," axe beaks stampede through the characters. The characters can hear the birds charging toward them but can't see anything through the thick undergrowth until the axe beaks burst forth and attack, slashing at anyone they can reach.")
    print()

def baboons():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    cd6 = random.randrange(1,7)
    d6 = ad6 + bd6 + cd6
    print("A pack of ",d6," baboons take umbrage at the characters' intrusion. The baboons can be distracted by tossing each of them a day's supply of food. Otherwise, they attack.")
    print()

def cache():
    d20 = random.randrange(1,21)
    print("The party finds a cache of supplies left behind by other explorers. There's no way to tell from the cache whether those who left it are still alive and coming back for it, or dead.")
    print()
    if d20 == 1:
        print("Item: rain catcher (see chapter 1) and mess kit")
    elif d20 == 2:
        print("Item: 10-day supply of preserved rations")
    elif d20 == 3:
        print("Item: 20-day supply of preserved rations")
    elif d20 == 4:
        print("Item: 50-day supply of preserved rations")
    elif d20 == 5:
        d4 = random.randrange(1,5)
        print("Item: ",d4," casks of water holding 5 gallons each")
    elif d20 == 6:
        d4 = random.randrange(1,5)
        print("Item: ",d4," casks of tej (see chapter 1)")
    elif d20 == 7:
        d4 = random.randrange(1,5)
        print("Item: ",d4," climber's kits")
    elif d20 == 8:
        ad4 = random.randrange(1,5)
        bd4 = random.randrange(1,5)
        d4 = ad4 + bd4
        print("Item: coffer containing ",d4," vials of antitoxin")
    elif d20 == 9:
        print("Item: 20-day supply of insect repellent salve (see chapter 1) in a leather tube)")
    elif d20 == 10:
        d4 = random.randrange(1,5)
        d20 = random.randrange(1,21)
        print("Item: ",d4," quivers, each containing",d20," arrows")
    elif d20 == 11:
        print("Item: canoe with 6 paddles")
    elif d20 == 12:
        print("Item: 2 hooded lanterns and 10 flasks of oil")
    elif d20 == 13:
        d4 = random.randrange(1,5)
        print("Item: two-person tent and",d4," explorer's packs")
    elif d20 == 14:
        ad10 = random.randrange(1,11)
        bd10 = random.randrange(1,11)
        d10 = ad10 + bd10
        print("Item: wooden box containing ",d10," daggers(low quality, of the type used as trade goods)")
    elif d20 == 15:
        print("Item: set of navigator's tools")
    elif d20 == 16:
        d10 = random.randrange(1,11)
        print("Item: ",d10," changes of woolen clothing")
    elif d20 == 17:
        print("Item: set of cartographer's tools")
    elif d20 == 18:
        d4 = random.randrange(1,5)
        print("Item: two-person tent and ",d4," healer's kits")
    elif d20 == 19:
        print("Item: 2 two-person tents, folding camp table, and 4 folding stools")
    else:
        ad4 = random.randrange(1,5)
        bd4 = random.randrange(1,5)
        d4 = ad4 + bd4
        print("Item: wooden box containing ",d4," potions of healing")
    print()

def cannibals():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    cd6 = random.randrange(1,7)
    d6 = ad6 + bd6 + cd6
    print("Chultan cannibals prowl the jungles in small groups, killing and eating zombies while avoiding faster, more dangerous undead. Abandoned by their gods, the cannibals have turned to the worship of Dendar the Night Serpent and pay tribute to Ras Nsi in exchange for his favor and protection. They paint a blue triangle (Ras Nsi's symbol) on their foreheads as proof of their devotion and are known to venture into Omu to hunt and deliver tribute.")
    print("If this encounter occurs during the day, the characters spot ",d6," tribal warriors feeding on the rotting remains of a dismembered zombie. If the characters remain quiet and keep their distance, they can move away without being noticed by the cannibals.")
    print("If this encounter occurs at night, ",d6," tribal warriors try to sneak into the adventurers' camp and murder them. Any character on guard is warned of the attack with a successful DC 10 Wisdom (Perception) check.")
    print()

def chwinga():
    print("A chwinga (see appendix D) takes an interest in the characters. It attempts to steal something valuable from an unguarded pack or canoe, but is noticed by any character with a passive Wisdom (Perception) score of 17 or higher. The chwinga always leaves something else in exchange: a pretty shell, a handful of nuts, or an uncut gemstone (10 gp).")
    print()

def crocodile():
    d4 = random.randrange(1,5)
    total = d4 + 1
    print("Any character with a passive Wisdom (Perception) score of 12 or higher sees and hears ",total," crocodiles moments before they attack; all other characters are surprised. A crocodile can capsize a canoe and throw its occupants into the water by using its action and succeeding on a DC 15 Strength (Athletics) check.")
    print()

def cyclops():
    print("A cyclops is journeying toward its home near Snapping Turtle Bay. It isn't looking for a fight, but any sudden moves or hostility from the characters might trigger one. The cyclops knows the region around Lake Luo and the western end of the Valley of Dread quite well, and it's never seen anything like Omu in those areas. Roll twice on the Treasure Drops table to see what treasure, if any, the cyclops has.")
    print()

def allosaurus():
    d3 = random.randrange(1,4)
    print("The party's scent attracts ",d3," allosauruses, which appear 100 yards away when the characters first notice them. Any character who succeeds on a DC 15 Wisdom (Survival) check can find a safe refuge (a high branch, a small crevice, a hollow log, and so forth) that the predators can't reach or enter.")
    print()

def ankylosaurus():
    print("An ornery ankylosaurus is gorging on plants, but it attacks any characters who disturb it.")
    print()

def brontosaurus():
    print("A lone brontosaurus (see appendix D) lumbers toward the characters, oblivious to their presence. Though it might step on characters who don't get out of its way, it fights only in self-defense.")
    print()

def deinonychus():
    d4 = random.randrange(1,5)
    total = d4 + 1
    print("A wild boar races across the party's path, followed closely by a hunting pack of ",total," deinonychuses (see appendix D). The predators decide the characters are more interesting prey.")
    print()

def dimetrodon():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    print("A pack of ",d6," dimetrodons (see appendix D) are spotted along a sunny riverbank or on rocks above the water. Roll any die. On an odd result, the dimetrodons take no notice of the characters; on an even result, they're hungry and attack at the slightest provocation, or if the characters approach within 100 feet of them.")
    print()

def hadrosaurus():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    cd6 = random.randrange(1,7)
    d6 = ad6 + bd6 + cd6
    yd6 = random.randrange(1,7)
    print("A herd of ",d6," hadrosauruses (see appendix D) are grazing nearby, with ",yd6," noncombatant young among them. The adults don't attack unless they're attacked or antagonized. The young are Small beasts that can be sold to Ifan Talro'a in Port Nyanzaru for 50 gp each, or for 100 gp if a character succeeds on a DC 15 Charisma (Persuasion) check to negotiate the price. The young dinosaurs are easy to handle if separated from their parents, but the adults fight if their young are captured.")
    print()

def plesiosaurus():
    print("Two plesiosauruses are fighting over a dead giant octopus. If the characters are on a river, the creatures are spotted at a distance of 300 feet. whereupon they bellow menacingly and move to attack the party. To paddle a canoe to a safe spot along the riverbank, one character in the canoe must succeed on a DC 13 Strength (Athletics) check, with other characters in the canoe using the Help action. Canoes that don't reach the bank are flipped and demolished by the reptiles, which then attack swimmers in the water.")
    print()

def pteranodon():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    print("A flock of ",d6," pteranodons is spotted overhead. They keep their distance and attack only if threatened.")
    print()

def quetzalcoatlus():
    d4 = random.randrange(1,5)
    total = d4 + 1
    print("A flight of ",total," quetzalcoatluses (see appendix D) is spotted overhead. They keep their distance and attack only if threatened.")
    print()

def stegosaurus():
    print("This lone stegosaurus (see appendix D) is in a genial mood. It approaches the characters out of curiosity, but anyone who touches it triggers a swipe from its tail.")
    print()

def triceratops():
    print("A triceratops that appears to be grazing alone is actually a mother with a nearby nest containing one noncombatant hatchling and two unhatched eggs. The mother eyes the characters suspiciously but doesn't attack unless they position themselves between her and the nest. Ifan Talro'a in Port Nyanzaru offers 50 gp for an intact triceratops egg or hatchling, or a character can talk him up to 150 gp with a successful DC 15 Charisma (Persuasion) check..")
    print()

def tyrannosaurus():
    print("The characters spot a tyrannosaurus rex 300 yards away. There's a 50 percent chance that the hungry behemoth is fighting either a stegosaurus, a triceratops, a pair of giant constrictor snakes, a giant ape, or a mob of ghouls and zombies. None of these creatures will voluntarily team up with the party, but their presence might weaken the tyrannosaurus to the point where the characters have a chance of slaying it. Characters can avoid an encounter with the tyrannosaurus if they keep their distance and succeed on a DC 15 group Dexterity (Stealth) check. If any character is trained in the Survival skill, all the characters' checks are made with advantage.")
    print()

def velociraptor():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    cd6 = random.randrange(1,7)
    d6 = ad6 + bd6 + cd6
    print("A pack of ",d6," velociraptors (see appendix D) burst out from behind cover and attack. Make a single Dexterity (Stealth) check for the dinosaurs, with advantage. Any character whose passive Wisdom (Perception) score equals or exceeds the velociraptors' check result is not surprised.")
    print()

def faerieDragon():
    print("An invisible green faerie dragon takes an interest in the adventurers and follows them for a while. If the characters are in good spirits, the tiny dragon plays harmless pranks on them during the party's next short or long rest. lf the characters are not angered by this trickery, the dragon appears and truthfully answers three of their questions before bidding the party farewell. If the characters seem dour or mean, or if the faerie dragon's pranks sour them, it flutters off without providing any sort of aid.")
    print("The faerie dragon visited Omu recently and knows about the evil gargoyles and \"snake people\" that watch over the city. It also knows things about other nearby landmarks or locations, as you determine.")
    print()

def redDragon():
    print("lf the characters are within 50 miles of Wyrmheart Mine (see chapter 2), they see the young red dragon known as Tzindelor or Tinder circling over that location. If they're farther away, they see her flying in the direction of the mine. The dragon ignores the characters unless they do something to attract her attention.")
    print()

def eblis():
    d4 = random.randrange(1,5)
    total = d4 + 1
    print("lf the characters are on the move when this encounter occurs, they stumble across ",total," eblis (see appendix D) living in reed huts built on stilts above a swampy marsh or pond. The eblis attack wounded or weak-looking characters but offer to trade information for precious gemstones if faced with a strong, well-armed group. For 50 gp worth of gems, they point the adventurers in the direction of nearby landmarks. If the characters follow these directions, they have advantage on checks made to reach those landmarks (see \"Navigation,\" page 38). If the characters defeat the eblis and search the huts, roll three times on the Treasure Drops table to determine what, if anything, the eblis have stashed in their homes. If this encounter occurs while the party is camped, the eblis sneak into the camp and try to drag one character away.")
    print()

def emeraldEnclave():
    d4 = random.randrange(1,5)
    total = d4 + 1
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    d6total = d6 * 5
    print("The characters encounter a band of Emerald Enclave scouts or stumble upon one of their outposts. Choose whichever encounter works best for the circumstances and location.")
    print("Enclave Scouts. The party meets ",total," members of the Emerald Enclave working to rid the jungle of its undead menace. The group works with a priest of Mielikki, but all other members are scouts. If one of the adventurers has died recently, you can use this encounter to introduce a new character-either a member of the Emerald Enclave, someone the scouts have rescued, or a character who hired the scouts as guides. The scouts are willing to trade information on an equal basis with a non-evil party. Characters can also convince the scouts to join their party for up to 3 days by succeeding on a DC 12 group Charisma (Persuasion) check. The Emerald Enclave scouts have enough food and water to nourish themselves, and each scout has an explorer's pack. The priest carries a priest's pack.")
    print("Enclave Outpost. Any character with a passive Wisdom (Perception) score of 13 or higher spots a wooden platform in a tree. The platform is ",d6total," feet above ground, and a successful DC 12 Strength (Athletics) check is required to climb the tree. The platform is 10 feet square and sturdy enough to support six characters and their gear.")
    print()

def deadExplorer():
    print("Chult is strewn with the corpses and bones of those who have fallen victim to its terrors. When the characters discover one such victim, roll a d20 and consult the Dead Explorers table to determine what they find. Then roll once on the Treasure Drops table to see what, if anything, can be found on or near the remains.")
    d20 = random.randrange(1,21)
    if d20 == 1:
        print("The bloated corpse of a dead halfling, riddled with tiny arrows and dangling from a tree vine. (The halfling trespassed on grung sacred ground, and the corpse was hung here as a warning.)")
    if d20 == 2:
        print("The bones of an unarmored humanoid, lashed to a tree by vines. (This explorer was captured by Batiri goblins, doused in honey, and left to be devoured by hungry insects.)")
    if d20 == 3:
        print("The crushed remains of an unarmored dwarf, showing signs that she was stomped to death by a rampaging dinosaur.")
    if d20 == 4:
        print("The gnawed and charred bones of a humanoid. (This unfortunate was murdered and cannibalized by his starving, fever-crazed companions.)")
    if d20 == 5:
        print("The mangled body of a half-elf, seemingly bludgeoned to death. (She was dropped from high altitude by pterafolk.)")
    if d20 == 6:
        print("The scattered bones of a dwarf, torn to pieces before being devoured. (A hunting pack of velociraptors did the dwarf in.)")
    if d20 == 7:
        print("The swollen, purple corpse of an elf, dead only a few days ago from the bite of a poisonous snake.")
    if d20 == 8:
        print("A fresh human corpse stuffed into a hollow tree. (Girallons plan to return and devour it later.)")
    if d20 == 9:
        print("The skeleton of a humanoid seated on a folding camp stool, clutching a knife and fork in its bony hands .")
    if d20 == 10:
        print("The desiccated husk of a gnome, cocooned in giant spider webs.")
    if d20 == 11:
        print("The body of a human - from the waist up. Signs show that the explorer crawled a considerable distance after being bitten in half by a tyrannosaurus. (A Flaming Fist charter found on the corpse identifies it as Lord Onovan IV, of the Dales.)")
    if d20 == 12:
        print("A charred elf's skeleton inside a charred constrictor snake's skeleton. (Both were killed by a lightning bolt spell.)")
    if d20 == 13:
        print("The rotting body of a giant frog with the blade of a shorts word poking out its back. (If the frog is cut open, the partially digested body of a halfing is found inside.)")
    if d20 == 14:
        print("A tabaxi spread-eagled on the ground, but with its limbs and head severed from its torso and crudely stitched back on in the wrong arrangement.")
    if d20 == 15:
        print("A half-ore spiked to an enormo us tree by the broken-off horn of a triceratops.")
    if d20 == 16:
        print("A gnome, spitted over a burned-out fire pit and thoroughly overcooked, but not eaten. (Goblin weapons and tools are scattered around amid velociraptor tracks.)")
    if d20 == 17:
        print("A headless humanoid, hung upside down from a tree and with six Batiri goblin spears thrust symmetrically through the body. (It was a Red Wizard, judging by the robes. The head is nowhere to be found.)")
    if d20 == 18:
        print("An elf, balanced on a tree branch 40 feet ab ove the ground, arms and legs dangling downward. (A note pressed between the body and the branch explains that the elf climbed the tree to get away from a prowling allosaurus and was too terrified to come down.)")
    if d20 == 19:
        print("The moldering remains of a human wearing a Flaming Fist-style helmet, his legs broken. (He succumbed to a faerie dragon's euphoria breath weapon and stepped off a cliff. A companion tried to carry him back to Fort Beluarian, but the warrior died en route.)")
    if d20 == 20:
        print("A dwarf with six large holes piercing her armor and chest. (A stegosaurus caught her squarely with a swipe of its tail.)")
    print()
    
def explorers():
    td6 = random.randrange(1,7)
    ed6 = random.randrange(1,7)
    print("The party runs into another band of explorers, consisting of a mage, a priest, a scout, and ",td6," tribal warriors.")
    if ed6 <= 2:
        print("The explorers are lost and hungry.")
    elif ed6 <= 4:
        print("The explorers are in good shape but are actively hunted by firenewts, ghouls, goblins, or grungs (see the appropriate entry in this appendix).")
    elif ed6 == 5:
        print("The explorers are healthy and headed toward the nearest landmark, intent on exploring it.")
    else:
        print("The explorers are healthy and heading back to Port Nyanzaru for rest and supplies.")
    print()

def firenewts():
    ld4 = random.randrange(1,5)
    ad4 = random.randrange(1,5)
    bd4 = random.randrange(1,5)
    hd4 = ad4 + bd4
    print("A light firenewt patrol consists of ",ld4," firenewt warriors mounted on giant striders. A heavy patrol consists of ",hd4," firenewt warriors and a firenewt warlock of Imix, all mounted on giant striders. Statistics for all these creatures appear in appendix D. The firenewts always strike their final blows with the intention of knocking out enemies, who are then taken back to the creatures' cave lair to be tortured and eaten.")
    print()

def flailSnail():
    print("Characters spot the slimy trail of a flail snail (see appendix D). If they wish to follow it, a successful DC 10 Wisdom (Survival) check correctly deduces which direction the snail was traveling.")
    print()

def flamingFist():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    d4 = random.randrange(1,5)
    print("The soldiers of the Flaming Fist know the dangers of Chult better than most, and they don't take the wilderness lightly. A typical patrol is made up of a knight or veteran leading an acolyte, a scout, and ",d6," guards and is sometimes accompanied by ",d4," deinonychuses (see a ppendix D) trained to fight and hunt alongside their handlers. The Flaming Fist is friendly and helpful toward adventurers possessing a charter of exploration issued by Commander Liara Portyr of Port Beluarian. If the party has no such document, the patrol tries to confiscate the adventurers' critical gear and advises them to replace it at Fort Beluarian-and co obcain a proper charter while they're at it.")
    print()

def flyingMonkeys():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    cd6 = random.randrange(1,7)
    d6 = ad6 + bd6 + cd6
    print("The sound of wings heralds the arrival of ",d6," flying monkeys (see appendix D), which swoop through the adventurers in a wave of grasping hands and feet. Each character must succeed on a DC 12 Dexterity saving throw or lose a useful piece of gear to the furry thieves. If this encounter occurs near Mbala (see chapter 2), the monkeys are servants of the green hag Nanny Pu'pu.")
    print("These sociable creatures are curious about humanoids and have little fear of them. A flying monkey that is successfully grappled, caught in a net, or otherwise prevented from escaping can be trained to perform simple tricks by a character with proficiency in Animal Handling who spends a few hours a day working with the monkey. At the end of 1 week, the character makes a DC 10 Wisdom (Animal Handling) check. On a success, the flying monkey learns to perform a simple trick on command (such as fetching a specific object or dancing to music). An individual monkey can learn a maximum of ld6 tricks and can be taught one trick per week.")
    print()

def flyingSnakes():
    d2 = random.randrange(1,3)
    if d2 == 1:
        print("The party encounters 1 flying snake.")
    else:
        ad6 = random.randrange(1,7)
        bd6 = random.randrange(1,7)
        d6 = ad6 + bd6
        print("The party encounters ",d6," flying snakes.")
    print("These snakes attack only when threatened. A flying snake that is successfully grappled can be stuffed in a sack or other soft container. After 1 hour of confinement, the snake settles down. A character who succeeds on a DC 13 Wisdom (Animal Handling) check can remove a calm snake from the container without causing it to attack or fly away. Characters can sell captured flying snakes to Ifan Talro'a in Port Nyanzaru. He offers 25 gp for each snake, but a character who succeeds on a DC 15 Charisma (Persuasion) check can talk him up to 50 gp.")
    print()

def frostGiants():
    d2 = random.randrange(1,3)
    d5 = random.randrange(1,6)
    print("The characters hear the sound of huge creatures stomping through the wilderness. If they follow the noise, they encounter a search party of three frost giants accompanied by ",d2," winter wolves.")
    if d5 == 4:
        print("This is Drufi's search party (see \"Hvalspyd,\" page 64).")
    print("The frost giants are concerned chiefiy with locating the Ring of Winter, and they might help characters who can provide useful information. They immediately attack characters who withhold information, or who threaten to reveal the giants' presence to the Flaming Fist. The frost giants carry no treasure with them while they hunt.")
    print()

def giantBoars():
    d4 = random.randrange(1,5)
    total = d4 + 1
    print("The characters see and hear ",total," giant boars foraging ahead of them. Skirting around the boars to prevent them from charging requires a successful DC 12 group Dexterity (Stealth) check.")
    print()

def giantCrocodile():
    print("Before it rises out of the water, make a Dexterity (Stealth) check for the giant crocodile. Any character with a passive Wisdom (Perception) score less than the check result is surprised when the monstrous creature attacks.")
    print()

def giantFrogs():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    print("These ",d6," giant frogs have come together in hunger and try to eat everything that crosses their path. The characters have plenty of warning as the amphibians hop noisily toward them.")
    print()

def giantLizards():
    d6 = random.randrange(1,7)
    print("The characters encounter ",d6," giant lizards sunning themselves on warm rocks. The lizards pose no threat unless they're attacked, and they're too set in their ways to be trained as pack animals.")
    print()

def giantScorpions():
    d3 = random.randrange(1,4)
    print("Any character with a passive Wisdom (Perception) score of 11 or higher spots ",d3," giant scorpions moments before they emerge from hiding and attack. At the end of the encounter, any character damaged by a giant scorpion must succeed on a DC 11 Constitution saving throw or become infected with shivering sickness (see \"Diseases,\" page 40).")
    print()

def giantSnappingTurtle():
    print("The characters spot a giant snapping turtle (see appendix D) sunning itself on the shore. The turtle attacks any character it can see within 30 feet of it.")
    print()

def giantWasps():
    d6 = random.randrange(1,7)
    print("A droning sound announces the presence of ",d6," giant wasps before the characters see them. The wasps attack at once, ignoring heavily armored targets in favor of those with little or no defensive protection. At the end of the encounter, any character damaged by a giant wasp must succeed on a DC 11 Constitution saving throw or become infected with shivering sickness (see \"Diseases,\" page 40).")
    print()

def girallons():
    print("Two girallons (see appendix D) hang in the trees, perch atop rocks, or lumber between crumbling, vine-covered ruins. The characters spot them automatically and can avoid a hostile encounter if they withdraw and succeed on a DC 13 group Dexterity (Stealth) check.")
    print("If the characters defeat the girallons or frighten them away, a search of the area reveals a hidden cache, determined by rolling on the Caches table. The girallons might also have some treasure hidden near the cache; roll once on the Treasure Drops table to determine what, if anything, is found after a search of the area.")
    print()

def goblins():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    total = ad6 + bd6 + 3
    print("A typical Batiri patrol or hunting party consists of a goblin boss leading ",total," goblins, all wearing painted wooden masks. They move quietly through familiar areas and seldom range outside their home territory. Batiri prefer to hunt at night and lay low in ambush positions during the day.")
    print("A night encounter with Batiri goblins involves an attack on the characters' camp. Each party member standing watch must attempt a DC 16 Wisdom (Perception) check, made with disadvantage because of the noise of the jungle at night. On a success, a character detects the goblins moving into attack positions and can rouse the rest of the parry. If no one on watch succeeds on the check, all the characters are surprised.")
    print("If this encounter occurs while the characters are traveling during the day, have each party member make a DC 16 Wisdom (Perception or Survival) check to spot the telltale signs of an ambush: disadvantageous terrain coupled with an eerie silence not normal for the jungle.")
    print("Goblins bargain for their lives if captured. If the characters can force or coerce a vow of cooperation £rom goblin prisoners, the Batiri wi ll serve as guides. They have the following additional skill: Survival +l.")
    print()

def grungs():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    print("A grung hunting party consists of ",d6," grungs led by a grung elite warrior (see appendix D for both). If this encounter occurs while the characters are traveling, the grungs have set up an ambush in the trees. Any character with a passive Wisdom (Perception) score of 14 or higher spots them just in time. All other characters are surprised.")
    print("If this encounter occurs while the party is camped, the grungs spotted the characters earlier in the day and have shadowed them unseen. Each character standing watch must succeed on a DC 14 Wisdom (Perception) check, made with disadvantage because of the noise of the jungle at night. On a success, a character detects the encroaching grungs and can rouse the rest of the party. If no one on watch succeeds on the check, all the characters are surprised.")
    print("If the character s capture one or more grungs, the frogfolk offer to lead the characters to treasure in exchange for a promise of freedom. The \"treasure\" is a half-mile away from the party's present location and consists of a cache, which you can randomly determine by rolling on the Caches table.")
    print()

def jaculis():
    d6 = random.randrange(1,7)
    print("Without warning, ",d6," jaculis (see appendix D) launch themselves at the party from the trees. Any character with a passive Wisdom (Perception) score of 14 or higher is able to react, but all others are surprised.")
    print()

def kamadans():
    d2 = random.randrange(1,3)
    d4 = random.randrange(1,5)
    print("The party is ambushed by ",d2," kamadans (see appendix D). Any character with a passive Wisdom (Perception) score of 16 or higher gets a warning of the attack, but all others are surprised. Characters who prevail against the kamadans can search the area for their lair, finding it with a successful DC 15 Wisdom (Survival) check.")
    if d4 == 2:
        d3 = random.randrange(1,4)
        print("The kamadan lair contains ",d3," noncombatant young the s ize of house cats. With their snakes not yet grown out, they look like leopard cubs. Ifan Talro'a in Port Nyanzaru will pay 150 gp for a live kamadan cub, but a successful DC 15 Charisma (Persuasion) check talks him up to 300 gp.")
    print()

def lizardfolk():
    ad4 = random.randrange(1,5)
    bd4 = random.randrange(1,5)
    d4 = ad4 + bd4
    print("The characters encounter ",d4," lizardfolk and a lizardfolk shaman. These lizard folk belong to a tribe or kingdom in the Valley of Dread and can be appeased with food (one day's supply per lizard folk in the group). Otherwise they attack.")
    print()

def madMonkeyMist():
    print("A bank of blue mist drifts toward the party, covering an area of ld6 20-foot squares. Any character with a passive Wisdom (Perception) score of 13 or higher notices the mist and can warn others of its approach. If the encounter occurs while the party is camped, the mist drifts through the camp at a speed of 5 feet per round. Characters who come into contact with the mist are exposed to mad monkey fever (see \"Diseases\" page 40).")
    print()

def magmins():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    print("The characters are attacked by ",d6," magmins, which flee if reduced to fewer than half their starting number.")
    print()

def mantraps():
    d4 = random.randrange(1,5)
    total = d4 + 1
    print("The characters blunder into a patch of ",total," mantraps (see appendix D), which are undetectable until they attack. The plants are 10 feet apart, so that only one plant attacks on the first round. The others must wait until characters maneuver within 5 feet of them.")
    print()

def mephits():
    d4 = random.randrange(1,5)
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    if d4 == 1:
        print("The party encounters ",d6," magma mephits. The mephits don't attack unless they outnumber the characters two to one, but they're reluctant to be helpful unless they themselves are outnumbered.")
    elif d4 == 2:
        print("The party encounters ",d6," mud mephits. The mephits don't attack unless they outnumber the characters two to one, but they're reluctant to be helpful unless they themselves are outnumbered.")
    elif d4 == 3:
        print("The party encounters ",d6," smoke mephits. The mephits don't attack unless they outnumber the characters two to one, but they're reluctant to be helpful unless they themselves are outnumbered.")
    else:
        print("The party encounters ",d6," steam mephits. The mephits don't attack unless they outnumber the characters two to one, but they're reluctant to be helpful unless they themselves are outnumbered.")
    print()

def nightHag():
    print("One of the Sewn Sisters (see chapter 5 ) shadows the party while staying in the Border Ethereal. During the party's next long rest, the night hag materializes and snatches some blood or hair from a random character before returning to the Ethereal Plane.")
    print()

def pterafolk():
    d4 = random.randrange(1,5)
    total = d4 + 2
    print("Looming in the sky, ",total," pterafolk (see appendix D) watch the characters' every move and wait until they blunder into danger. The next time a random encounter occurs, the pterafolk take advantage of the distraction and attack from the air, launching javelin attacks at wounded characters while staying out of melee. If they meet firm resistance, the pterafolk fly away, but they might regroup for a follow-up attack at your discretion.")
    print()

def rarePlants():
    d6 = random.randrange(1,7)
    if d6 == 1:
        ad6 = random.randrange(1,7)
        bd6 = random.randrange(1,7)
        total = ad6 + bd6
        print("The characters find ",total," dancing monkey fruit (see Appendix C) growing on a tree")
    elif d6 == 2:
        ad6 = random.randrange(1,7)
        bd6 = random.randrange(1,7)
        total = ad6 + bd6
        print("The characters find a menga bush with ",total," ounces of leaves")
    elif d6 == 3:
        d4 = random.randrange(1,5)
        print("The characters find ",d4," ryath roots growing in the ground")
    elif d6 == 4:
        ad6 = random.randrange(1,7)
        bd6 = random.randrange(1,7)
        cd6 = random.randrange(1,7)
        dd6 = random.randrange(1,7)
        total = ad6 + bd6 + cd6 + dd6
        print("The characters find ",total," sinda berries growing on a bush")
    elif d6 == 5:
        ad6 = random.randrange(1,7)
        bd6 = random.randrange(1,7)
        total = ad6 + bd6
        print("The characters find a wukka tree with ",total," wukka nuts")
    else:
        ad6 = random.randrange(1,7)
        print("The characters find ",ad6," zabou growing on a dead tree")
    print()
    
def redWizard():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    print("This group consists of a Red Wizard (LE male or female Thayan human mage), ",ad6,", guards , and ",bd6," skeletons, all answerable to Valindra Shadowmantle (see \"Heart of Ubtao.\" page 58). If this encounter occurs outside of Omu, these reinforcements are on their way to the city. If the encounter takes place in Omu, the Red Wizard is searching the city for shrines (see chapter 3). The Thayans aren't spoiling for a fight; if defeat seems inevitable, the Red Wizard surrenders and offers a crude map of Chult marking the regions occupied by undead (see map 2.1). The characters can use the map to steer clear of these regions.")
    print()

def salamander():
    d6 = random.randrange(1,7)
    print("The characters see a salamander tending a nest of ",d6," fire snakes. The salamander has no interest in fighting and attacks only to protect itself and the snakes.")
    print()

def seaHags():
    print("The characters encounter 3 sea hags that comprise a coven. Their favorite trick is to pull a damaged or abandoned canoe onto a riverbank and pretend to be stranded or wounded explorers in need of rescue.")
    print("If the characters defeat the sea hags and search the area, roll three times on the Treasure Drops table to determine what, if anything, they find. Whatever treasure the hags have is stowed inside a rotted wooden chest.")
    print()

def shamblingMound():
    print("Roll any die when a shambling mound encounter occurs. On an even result, the characters hear the creature trudging through the muck before it attacks them. On an odd result, the shambling mound lurks within a mass of vegetation, where it can be noticed by any character with a passive Wisdom (Perception) score of 15 or higher.")
    print()

def constrictorSnake():
    print("A constrictor snake attacks a random party member from hiding. The character targeted by the snake is surprised unless he or she has a passive Wisdom (Perception) score of 12 or higher.")
    print()

def giantConstrictorSnake():
    print("A giant constrictor snake attacks a random party member from hiding. The character targeted by the snake is surprised unless he or she has a passive Wisdom (Perception) score of 12 or higher.")
    print()

def giantPoisonousSnake():
    print("A giant poisonous snake shoots out from the undergrowth to attack a random character. The character targeted by the snake is surprised unless he or she has a passive Wisdom (Perception) score of 14 or higher.")
    print()

def spiders():
    d6 = random.randrange(1,7)
    print("Giant spider webs are easily concealed in Chult's dense jungles and swamps. Any character with a passive Wisdom (Perception) score of 13 or higher spots the webs in time to alert the other characters to an encounter with ",d6," giant spiders. Otherwise, the spiders attack with surprise when the lead party member blunders into a sticky web and becomes grappled by it (escape DC 12). Hundreds of baby giant spiders crawl through the webs, but they are harmless.")
    print()

def statueOfUbtao():
    d4 = random.randrange(1,5)
    print("Any character with a passive Wisdom (Perception) score of 12 or higher spots a 10-foot-tall statue overgrown with vines. The statue depicts a stylized Chultan king-a representation of Ubtao.")
    if d4 == 1:
        print("Treasure lies at the foot of the statue, left there as tribute by some jungle creature. Roll once on the Treasure Drops table to determine what treasure is found. If the roll indicates no treasure, the characters find worthless pieces of bone jewelry instead.")
    elif d4 == 2:
        print("Goblin, grung, and su-monster skulls are piled around the statue's base.")
    elif d4 == 3:
        pd4 = random.randrange(1,5)
        if pd4 == 4:
            print("A glyph of warding is inscribed on the statue. To spot the glyph, a character searching the statue must succeed on a DC 15 Intelligence (Investigation) check. If any creature touches the statue, the glyph erupts with magical energy in a 20-foot-radius sphere centered on the statue. Each creature in the area must succeed on a DC 14 Dexterity saving throw, taking 22 (5d8) thunder damage on a failed save, or half as much damage on a successful one.")
        else:
            ad6 = random.randrange(1,7)
            bd6 = random.randrange(1,7)
            d6 = ad6 + bd6
            print("A glyph of warding is inscribed on the statue. To spot the glyph, a character searching the statue must succeed on a DC 15 Intelligence (Investigation) check. If any creature touches the statue, the glyph erupts with magical energy in a 20-foot-radius sphere centered on the statue. Each creature in the area must succeed on a DC 14 Dexterity saving throw, taking 22 (5d8) thunder damage on a failed save, or half as much damage on a successful one. The thunderous noise attracts ",d6," stirges or a troll lurking nearby.")
    else:
        print("The statue has grooves carved into its stomach that form a maze. Any character who studies the grooves and succeeds on a DC 10 Intelligence check sees a clear pathway through the labyrinth. That character is then bestowed with the power to cast the find the path spell as an action, no components required, by tracing the same path with his or her finger. Once used, this ability goes away. Once che statue has granted this benefit, it can't do so again until the next dawn.")
    print()

def stirges():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    print("Chult is rich in caves, ruins, and hollow logs in which stirges can hide. By day, the characters disturb ",d6," stirges as they move through the jungle. At night, the same number of stirges descend on the party's camp.")
    print()

def suMonsters():
    d4 = random.randrange(1,5)
    total = d4 + 1
    print("The party comes across ",total," su-monsters (see appendix D). The su-monsters approach cautiously, feigning curiosity. If allowed to get close, each su-monster uses its Psychic Crush in the hope of stunning an adventurer before attacking with its bite and claws. The su-monsters flee to their treetop lairs if the fight goes against them.")
    print("The su-monsters might have treasure stashed in one of their trees; roll once on the Treasure Drops table to determine what, if anything, a search of the tree yields.")
    print()

def swarmsOfBats():
    d4 = random.randrange(1,5)
    print("Ruins, hollow trees, and hidden caverns can all be homes to bats. This encounter sees the characters disturb ",d4," swarms of bats that have become unnaturally aggressive from feeding on undead flesh.")
    print()

def swarmsOfInsects():
    d4 = random.randrange(1,5)
    print("The characters are beset by ",d4," swarms of insects (centipedes). At the end of the encounter, any character damaged by a swarm must succeed on a DC 11 Constitution saving throw or become infected with shivering sickness (see \"Diseases,\" page 40).")
    print()

def swarmsOfQuippers():
    d4 = random.randrange(1,5)
    print("This encounter indicates that ",d4," swarms of quippers catch sight of the party, but these creatures are dangerous only if the characters are in the water with them. Creatures on the shore or in canoes are safe, but in both cases, the swarms follow the characters until they're out of sight and away from the water.")
    print()

def tabaxiHunter():
    print("Any character with a passive Wisdom (Perception) score of 15 or higher spots a tabaxi hunter (see appendix D) watching the party from a vantage point 300 feet away. If the tabaxi goes unseen, it might shadow the characters for a while, then suddenly appear to help them fight off a tough encounter or warn them of danger in the vicinity.")
    print("If this encounter takes place in Omu, see chapter 3 for more information on the tabaxi hunters found there.")
    print()

def tiger():
    print("A tiger lies in wait for the party but is noticed by any character whose passive Wisdom (Perception) score is 16 or higher. lf not detected, the tiger pounces at a character who comes within 40 feet of it. The tiger retreats if it loses more than half its hit points.")
    print()

def triFlowerFrond():
    d4 = random.randrange(1,5)
    print("If this encounter occurs while the characters are traveling, they wander into a patch of ",d4," tri-flower fronds (see appendix D) which seem like ordinary plants until they strike. If the encounter occurs while the party is camped, the plants try to infiltrate the camp, anesthetize characters with their orange blossoms, then slay them with their yellow and red blossoms.")
    print()

def troll():
    print("A hungry troll comes crashing out of the jungle, intent on eating the characters.")
    print()

def ghouls():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    print("Any character with a passive Wisdom (Perception) score of 12 or higher hears and smells a ghoul pack approaching, consisting of ",d6," ghouls led by a ghast. The ghast has a blue triangle tattooed on its forehead-an indicator that it once served Ras Nsi.")
    print()

def skeletons():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    cd6 = random.randrange(1,7)
    d6 = ad6 + bd6 + cd6
    print("The characters come across ",d6," skeletons. If the encounter occurs while the party is traveling, the skeletons are either lying on the ground or buried under it, ready to spring up when wayward explorers pass by. If the party is camped, the skeletons wander into the camp and attack.")
    print()

def specter():
    print("The evil remnant of a dead explorer has become a specter that attacks the party. The explorer's body can be found with a successful DC 13 Wisdom (Survival) check. lf the characters locate the body they find:")
    deadExplorer()

def wight():
    print("The characters encounter a wight that has lurked in the Chultan jungle since before the Spellplague. It harbors an eternal hatred for Chultans and everything related to Ubtao. If the party includes any Chultans or any character wearing the holy symbol of Ubtao, the wight attacks those characters in preference to other targets.")
    print()

def zombies():
    d10 = random.randrange(1,11)
    print("Characters catch the scent of death on the air and hear the undead lumbering through the jungle.")
    if d10 <= 3:
        ad6 = random.randrange(1,7)
        bd6 = random.randrange(1,7)
        cd6 = random.randrange(1,7)
        d6 = ad6 + bd6 + cd6 
        print("The party encounters ",d6," zombies")
    elif d10 <= 5:
        print("The party encounters 1 anklyosaurus zombie(see appendix D)")
    elif d10 <= 7:
        d4 = random.randrange(1,5)
        print("The party encounters ",d4," girallon zombies(see appendix D)")
    elif d10 <= 9:
        d4 = random.randrange(1,5)
        print("The party encounters ",d4," ogre zombies")
    else:
        print("The party encounters 1 tyrannosaurus zombie(see appendix D)")
    print()

def vegepygmies():
    d4 = random.randrange(1,5)
    print("The characters cross paths with ",d4," vegepygmies, each one mounted on a thorny (see appendix D for both). These vegepygmy hunters have wandered far from their tribe. They flee if outnumbered; otherwise, they attack.")
    print()

def wereboar():
    print("A wereboar masquerading as a Chultan priest takes a dim view of explorers encroaching on its territory and demands that the characters turn back. Around its neck, it wears a wooden holy symbol of Ubtao (a labyrinthine pattern carved into a circular disk). The wereboar might be guarding a shrine to Ubtao, a grove of wukka trees (see appendix C), or a cave it uses as a lair. The creature might also have treasure in its lair; roll three times on the Treasure Drops table to determine what, if anything, a search of the wereboar's lair yields.")
    print()

def weretiger():
    print("A weretiger in human form offers to escort the party through a particularly dangerous stretch of wilderness. It has no ulterior motive and doesn't ask for payment. If the characters accept its assistance, they have no hostile random encounters while the weretiger is with them. It leaves after accompanying the party for 24 hours or when it reaches a location it does not wish to explore, including Omu, Nangalore, or Orolunga.")
    print()

def winterscape():
    print("The characters stumble into a wondrous sight: a 120-foot-radius sphere of winter weather. To drive off some monsters, Artus Cimber (see appendix D) created the sphere using the Ring of Winter. All plants and surfaces within the sphere are covered with glittering ice and frost, and the temperature within the sphere is a biting -30 degrees Fahrenheit. The effect was created by an artifact and can't be dispelled.")
    print()

def yellowMuskCreeperAndZombies():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    cd6 = random.randrange(1,7)
    d6 = ad6 + bd6 + cd6
    print("The characters pass close to a ruin inhabited by ",d6," yellow musk zombies (see appendix D). The zombies might be spread across the area or bunched together, depending on the terrain. In the heart of the ruin, a yellow musk creeper (see appendix D) clings to a crumbling archway, statue, or polluted well.")
    print("If this encounter occurs while the party is camped the zombies emerge from a nearby ruin to attack the camp and attempt to knock characters unconscious. They then drag those characters back to the yellow musk creeper.")
    print()

def yuanTi():
    d6 = random.randrange(1,7)
    total = d6 + 1
    d4 = random.randrange(1,5)
    print("Yuan-ti patrols consist of ",total," yuan-ti purebloods, which keep their distance as they try to gather information to take back to Ras Nsi. The yuan-ti are camouflaged, but any character who succeeds on a DC 13 Wisdom (Perception) check made with disadvantage catches sight of the serpent folk as they withdraw.")
    print("If this encounter occurs within 25 miles of Omu, the patrol is instead made up of ",d4," yuan-ti malisons (type 1) and it takes a DC 14 Wisdom (Perception) check to spot them. If the characters chase after the malisons, they transform into snakes and vanish into the jungle.")
    print()

def zhentarim():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    total = ad6 + bd6
    d6 = random.randrange(1,7)
    print("A Zhent a ssassin with a flying snake pet leads a priest, ",total," thugs, and ",d6," tribal war riors through the wilderness in search of Artus Cimber and the Ring of Winter. If Artus is with the characters, the Zhents demand the ring and attack if they don't receive it quickly. Otherwise, they show little interest in the characters.")
    print("Roll once on the Treasure Drops table to determine what treasure, if any, the Zhents carry.")
    print()

def zorbos():
    ad6 = random.randrange(1,7)
    bd6 = random.randrange(1,7)
    d6 = ad6 + bd6
    print("If this encounter occurs while the characters are traveling, they spot ",d6," zorbos (see appendix D) in wukka trees (see appendix C). The creatures growl and bare their teeth if any characters approach them. If the characters act in a threatening manner, the zorbos attack.")
    print("If this encounter occurs while the party is camped, the hungry zorbos drop from the surrounding trees and attack.")
    print()

def gargoyles():
    ad4 = random.randrange(1,5)
    bd4 = random.randrange(1,5)
    d4 = ad4 + bd4
    print("Perched on a cliff are ",d4," gargoyles that swoop down to attack. Two of them carry a net between them. As an action, either gargoyle can use the net to make a melee weapon attack (+4 to hit) against one Small or Medium creature. If the attack hits, the gargoyles hoist the character into the air and fly off with their catch. It takes both gargoyles to lift the net if it has a creature caught in it. The gargoyles flee if reduced to half their number.")
    print()

def giantWolfSpiders():
    d6 = random.randrange(1,7)
    print("The characters are attacked by ",d6," giant wolf spiders living in hidey-holes in the nearby ruins. A search of the spiders' lair might yield treasure; roll once on the Treasure Drops table to determine what, if anything, is found.")
    print()

def kingOfFeathers():
    print("The characters encounter the tyrannosaurus rex known as the King of Feathers. See chapter 3 for more information on this unique beast.")
    print()

def kobolds():
    d4 = random.randrange(1,5)
    total = d4 + 1
    print("Moving through the city or palace ruins are ",total," kobolds led by a kobold inventor (see appendix D). Characters with a passive Wisdom (Perception) score of 12 or higher spot the kobolds, which flee if approached or attacked. The kobolds serve the kobold scale sorcerer Kakarol (see chapter 3). They might be on their way to one of the city's shrines to reset its traps, or they might be returning to their lair with a recently discovered treasure. Roll once on the Treasure Drops table to determine what, if anything, the kobolds found.")
    print()

def beach():
    d100 = random.randrange(1,101)
    if d100 <= 7:
        aarakocra()
    elif d100 == 8:
        artusCimber()
    elif d100 <= 10:
        cache()
    elif d100 <= 12:
        chwinga()
    elif d100 <= 14:
        allosaurus()
    elif d100 <= 16:
        dimetrodon()
    elif d100 <= 21:
        plesiosaurus()
    elif d100 <= 28:
        pteranodon()
    elif d100 <= 31:
        quetzalcoatlus()
    elif d100 <= 37:
        velociraptor()
    elif d100 <= 40:
        redDragon()
    elif d100 <= 42:
        emeraldEnclave()
    elif d100 <= 46:
        explorers()
    elif d100 <= 49:
        flamingFist()
    elif d100 <= 52:
        flyingMonkeys()
    elif d100 <= 55:
        flyingSnakes()
    elif d100 <= 57:
        frostGiants()
    elif d100 <= 63:
        giantLizards()
    elif d100 <= 67:
        giantSnappingTurtle()
    elif d100 <= 71:
        lizardfolk()
    elif d100 <= 74:
        redWizard()
    elif d100 <= 84:
        seaHags()
    elif d100 <= 87:
        stirges()
    elif d100 <= 89:
        swarmsOfBats()
    elif d100 <= 94:
        tabaxiHunter()
    else:
        triFlowerFrond()

def noUndead():
    d100 = random.randrange(1,101)
    if d100 == 1:
        albinoDwarves()
    elif d100 == 2:
        almiraj()
    elif d100 <= 4:
        apes()
    elif d100 == 5:
        artusCimber()
    elif d100 <= 7:
        assassinVines()
    elif d100 == 8:
        axeBeaks()
    elif d100 == 9:
        baboons()
    elif d100 <= 11:
        cache()
    elif d100 <= 13:
        cannibals()
    elif d100 <= 15:
        chwinga()
    elif d100 == 16:
        cyclops()
    elif d100 == 17:
        allosaurus()
    elif d100 == 18:
        anklyosaurus()
    elif d100 == 19:
        brontosaurus()
    elif d100 <= 21:
        deinonychus()
    elif d100 <= 23:
        hadrosaurus()
    elif d100 == 24:
        pteranodon()
    elif d100 <= 26:
        stegosaurus()
    elif d100 <= 28:
        triceratops()
    elif d100 <= 30:
        tyrannosaurus()
    elif d100 <= 35:
        velociraptor()
    elif d100 == 36:
        faerieDragon()
    elif d100 == 37:
        eblis()
    elif d100 <= 42:
        emeraldEnclave()
    elif d100 <= 44:
        deadExplorer()
    elif d100 == 45:
        explorers()
    elif d100 == 46:
        flailSnail()
    elif d100 <= 50:
        flamingFist()
    elif d100 == 51:
        flyingMonkeys()
    elif d100 <= 53:
        flyingSnakes()
    elif d100 <= 55:
        frostGiants()
    elif d100 == 56:
        giantBoars()
    elif d100 == 57:
        giantFrogs()
    elif d100 == 58:
        giantLizards()
    elif d100 == 59:
        giantScorpions()
    elif d100 == 60:
        giantWasps()
    elif d100 <= 62:
        girallons()
    elif d100 <= 64:
        goblins()
    elif d100 <= 66:
        grungs()
    elif d100 == 67:
        jaculis()
    elif d100 == 68:
        kamadans()
    elif d100 <= 70:
        lizardfolk()
    elif d100 <= 72:
        madMonkeyMist()
    elif d100 == 73:
        mantraps()
    elif d100 == 74:
        nightHag()
    elif d100 == 75:
        pterafolk()
    elif d100 == 76:
        rarePlants()
    elif d100 == 77:
        redWizard()
    elif d100 <= 79:
        constrictorSnake()
    elif d100 == 80:
        giantConstrictorSnake()
    elif d100 == 81:
        giantPoisonousSnake()
    elif d100 == 82:
        spiders()
    elif d100 <= 85:
        statueOfUbtao()
    elif d100 == 86:
        stirges()
    elif d100 == 87:
        suMonsters()
    elif d100 == 88:
        swarmsOfBats()
    elif d100 == 89:
        swarmsOfInsects()
    elif d100 == 90:
        tabaxiHunter()
    elif d100 == 91:
        tiger()
    elif d100 == 92:
        triFlowerFrond()
    elif d100 == 93:
        vegepygmies()
    elif d100 == 94:
        wereboar()
    elif d100 == 95:
        weretiger()
    elif d100 == 96:
        winterscape()
    elif d100 == 97:
        yellowMuskCreeperAndZombies()
    elif d100 == 98:
        yuanTi()
    elif d100 == 99:
        zhentarim()
    else:
        zorbos()

def lesserUndead():
    d100 = random.randrange(1,101)
    if d100 == 1:
        albinoDwarves()
    elif d100 == 2:
        artusCimber()
    elif d100 <= 5:
        assassinVines()
    elif d100 == 6:
        axeBeaks()
    elif d100 <= 8:
        cache()
    elif d100 <= 10:
        cannibals()
    elif d100 == 11:
        allosaurus()
    elif d100 == 12:
        anklyosaurus()
    elif d100 == 13:
        deinonychus()
    elif d100 == 14:
        hadrosaurus()
    elif d100 == 15:
        pteranodon()
    elif d100 == 16:
        stegosaurus()
    elif d100 == 17:
        triceratops()
    elif d100 == 18:
        tyrannosaurus()
    elif d100 <= 20:
        emeraldEnclave()
    elif d100 <= 22:
        deadExplorer()
    elif d100 == 23:
        explorers()
    elif d100 <= 26:
        flamingFist()
    elif d100 == 27:
        flyingSnakes()
    elif d100 == 28:
        giantLizards()
    elif d100 == 29:
        giantWasps()
    elif d100 <= 31:
        girallons()
    elif d100 <= 33:
        goblins()
    elif d100 <= 35:
        grungs()
    elif d100 <= 39:
        madMonkeyMist()
    elif d100 <= 41:
        mantraps()
    elif d100 == 42:
        nightHag()
    elif d100 <= 44:
        pterafolk()
    elif d100 == 45:
        rarePlants()
    elif d100 == 46:
        redWizard()
    elif d100 <= 48:
        constrictorSnake()
    elif d100 == 49:
        giantConstrictorSnake()
    elif d100 == 50:
        giantPoisonousSnake()
    elif d100 <= 52:
        spiders()
    elif d100 <= 55:
        statueOfUbtao()
    elif d100 <= 57:
        stirges()
    elif d100 <= 59:
        suMonsters()
    elif d100 <= 62:
        swarmsOfBats()
    elif d100 <= 65:
        swarmsOfInsects()
    elif d100 == 66:
        triFlowerFrond()
    elif d100 == 67:
        troll()
    elif d100 <= 72:
        ghouls()
    elif d100 <= 77:
        skeletons()
    elif d100 <= 79:
        specter()
    elif d100 == 80:
        wight()
    elif d100 <= 89:
        zombies()
    elif d100 <= 91:
        vegepygmies()
    elif d100 == 92:
        wereboar()
    elif d100 == 93:
        weretiger()
    elif d100 == 94:
        winterscape()
    elif d100 <= 96:
        yellowMuskCreeperAndZombies()
    elif d100 <= 98:
        yuanTi()
    elif d100 == 99:
        zhentarim()
    else:
        zorbos

def greaterUndead():
    d100 = random.randrange(1,101)
    if d100 == 1:
        artusCimber()
    elif d100 == 2:
        assassinVines()
    elif d100 <= 5:
        cache()
    elif d100 == 6:
        allosaurus()
    elif d100 == 7:
        anklyosaurus()
    elif d100 == 8:
        hadrosaurus()
    elif d100 == 9:
        pteranodon()
    elif d100 == 10:
        stegosaurus()
    elif d100 <= 12:
        tyrannosaurus()
    elif d100 <= 14:
        velociraptor()
    elif d100 <= 16:
        emeraldEnclave()
    elif d100 <= 20:
        deadExplorer()
    elif d100 == 21:
        explorers()
    elif d100 <= 23:
        flamingFist()
    elif d100 == 24:
        giantWasps()
    elif d100 == 25:
        mantraps()
    elif d100 == 26:
        pterafolk()
    elif d100 == 27:
        rarePlants()
    elif d100 == 28:
        redWizard()
    elif d100 <= 31:
        constrictorSnake()
    elif d100 == 32:
        giantConstrictorSnake()
    elif d100 == 33:
        giantPoisonousSnake()
    elif d100 <= 36:
        spiders()
    elif d100 <= 40:
        statueOfUbtao()
    elif d100 <= 44:
        stirges()
    elif d100 == 45:
        suMonsters()
    elif d100 == 46:
        swarmsOfBats()
    elif d100 <= 49:
        swarmsOfInsects()
    elif d100 == 50:
        triFlowerFrond()
    elif d100 == 51:
        troll()
    elif d100 <= 63:
        ghouls()
    elif d100 <= 67:
        skeletons()
    elif d100 <= 70:
        specter()
    elif d100 <= 73:
        wight()
    elif d100 <= 85:
        zombies()
    elif d100 <= 87:
        vegepygmies()
    elif d100 <= 89:
        wereboar()
    elif d100 <= 91:
        weretiger()
    elif d100 == 92:
        winterscape()
    elif d100 <= 96:
        yellowMuskCreeperAndZombies()
    elif d100 <= 98:
        yuanTi()
    else:
        zorbos()

def mountains():
    d100 = random.randrange(1,101)
    if d100 <= 11:
        aarakocra()
    elif d100 <= 17:
        albinoDwarves()
    elif d100 <= 20:
        apes()
    elif d100 <= 22:
        baboons()
    elif d100 <= 25:
        cache()
    elif d100 <= 27:
        chwinga()
    elif d100 <= 29:
        cyclops()
    elif d100 <= 38:
        pteranodon()
    elif d100 <= 42:
        quetzalcoatlus()
    elif d100 <= 45:
        redDragon()
    elif d100 <= 47:
        emeraldEnclave()
    elif d100 <= 50:
        deadExplorer()
    elif d100 <= 53:
        explorers()
    elif d100 <= 59:
        flyingMonkeys()
    elif d100 <= 61:
        flyingSnakes()
    elif d100 == 62:
        giantBoars()
    elif d100 == 63:
        giantLizards()
    elif d100 <= 65:
        giantWasps()
    elif d100 <= 70:
        girallons()
    elif d100 <= 73:
        nightHag()
    elif d100 <= 80:
        pteraFolk()
    elif d100 == 81:
        redWizard()
    elif d100 <= 84:
        giantPoisonousSnakes()
    elif d100 <= 87:
        stirges()
    elif d100 <= 90:
        swarmsOfBats()
    elif d100 <= 92:
        tabaxiHunter()
    elif d100 <= 97:
        troll()
    else:
        wereboar()

def rivers():
    d100 = random.randrange(1,101)
    if d100 <= 3:
        aarakocra()
    elif d100 <= 7:
        aldani()
    elif d100 <= 9:
        artusCimber()
    elif d100 == 10:
        assassinVines()
    elif d100 <= 12:
        cache()
    elif d100 <= 15:
        cannibals()
    elif d100 <= 18:
        chwinga()
    elif d100 <= 23:
        crocodiles()
    elif d100 == 24:
        brontosaurus()
    elif d100 <= 26:
        dimetrodon()
    elif d100 <= 28:
        hadrosaurus()
    elif d100 <= 31:
        plesiosaurus()
    elif d100 <= 34:
        pteranodon()
    elif d100 <= 36:
        quetzalcoatlus()
    elif d100 == 37:
        faerieDragon()
    elif d100 <= 40:
        eblis()
    elif d100 <= 43:
        emeraldEnclave()
    elif d100 <= 45:
        deadExplorer()
    elif d100 <= 49:
        explorers()
    elif d100 <= 51:
        flamingFist()
    elif d100 <= 53:
        flyingMonkeys()
    elif d100 <= 55:
        flyingSnakes()
    elif d100 <= 58:
        giantCrocodile()
    elif d100 <= 60:
        giantFrogs()
    elif d100 <= 62:
        giantSnappingTurtle()
    elif d100 == 63:
        giantWasps()
    elif d100 <= 66:
        grungs()
    elif d100 == 67:
        jaculis()
    elif d100 == 68:
        lizardfolk()
    elif d100 <= 70:
        madMonkeyMist()
    elif d100 <= 72:
        pterafolk()
    elif d100 == 73:
        rarePlants()
    elif d100 == 74:
        redWizard()
    elif d100 <= 76:
        seaHags()
    elif d100 <= 79:
        constrictorSnake()
    elif d100 == 80:
        giantConstrictorSnake()
    elif d100 == 81:
        statueOfUbtao()
    elif d100 <= 83:
        stirges()
    elif d100 <= 85:
        swarmsOfInsects()
    elif d100 <= 91:
        swarmsOfQuippers()
    elif d100 <= 93:
        tabaxiHunter()
    elif d100 == 94:
        ghouls()
    elif d100 == 95:
        skeletons()
    elif d100 <= 96:
        zombies()
    elif d100 <= 98:
        yuanTi()
    else:
        zhentarim()

def ruins():
    d100 = random.randrange(1,101)
    if d100 <= 2:
        albinoDwarves()
    elif d100 == 3:
        almiraj()
    elif d100 <= 6:
        apes()
    elif d100 <= 8:
        artusCimber()
    elif d100 <= 12:
        assassinVines()
    elif d100 <= 14:
        baboons()
    elif d100 <= 18:
        cache()
    elif d100 == 19:
        chwinga()
    elif d100 <= 21:
        cyclops()
    elif d100 == 22:
        deinonychus()
    elif d100 == 23:
        velociraptor()
    elif d100 <= 26:
        emeraldEnclave()
    elif d100 <= 28:
        deadExplorer()
    elif d100 <= 31:
        explorers()
    elif d100 <= 33:
        flailSnail()
    elif d100 <= 36:
        flamingFist()
    elif d100 <= 38:
        flyingMonkeys()
    elif d100 == 39:
        flyingSnakes()
    elif d100 <= 41:
        frostGiants()
    elif d100 == 42:
        giantLizards()
    elif d100 <= 45:
        giantScorpions()
    elif d100 <= 48:
        giantWasps()
    elif d100 <= 50:
        girallons()
    elif d100 <= 52:
        goblins()
    elif d100 <= 54:
        jaculis()
    elif d100 <= 57:
        kamadans()
    elif d100 == 58:
        lizardfolk()
    elif d100 <= 60:
        madMonkeyMist()
    elif d100 == 61:
        nightHag()
    elif d100 == 62:
        rarePlants()
    elif d100 == 63:
        redWizard()
    elif d100 <= 66:
        giantPoisonousSnake()
    elif d100 <= 68:
        spiders()
    elif d100 <= 73:
        statueOfUbtao()
    elif d100 <= 75:
        stirges()
    elif d100 <= 77:
        swarmsOfBats()
    elif d100 == 78:
        tabaxiHunter()
    elif d100 <= 80:
        triFlowerFrond()
    elif d100 == 81:
        troll()
    elif d100 <= 84:
        ghouls()
    elif d100 <= 87:
        skeletons()
    elif d100 <= 89:
        specter()
    elif d100 <= 91:
        wight()
    elif d100 <= 93:
        zombies()
    elif d100 == 94:
        weretiger()
    elif d100 == 95:
        winterscape()
    elif d100 == 96:
        yellowMuskCreeperAndZombies()
    elif d100 <= 98:
        yuanTi()
    else:
        zhentarim()

def swamp():
    d100 = random.randrange(1,101)
    if d100 <= 10:
        aldani()
    elif d100 == 11:
        artusCimber()
    elif d100 <= 14:
        assassinVines()
    elif d100 <= 16:
        chwinga()
    elif d100 <= 21:
        crocodiles()
    elif d100 == 22:
        allosaurus()
    elif d100 == 23:
        anklyosaurus()
    elif d100 <= 25:
        brontosaurus()
    elif d100 <= 30:
        dimetrodon()
    elif d100 <= 33:
        hadrosaurus()
    elif d100 <= 35:
        pteranodon()
    elif d100 <= 39:
        eblis()
    elif d100 <= 41:
        deadExplorer()
    elif d100 <= 45:
        explorers()
    elif d100 <= 47:
        flailSnail()
    elif d100 <= 50:
        flyingSnakes()
    elif d100 <= 53:
        giantCrocodile()
    elif d100 <= 56:
        giantFrogs()
    elif d100 <= 58:
        giantLizards()
    elif d100 <= 60:
        giantSnappingTurtle()
    elif d100 <= 62:
        giantWasps()
    elif d100 <= 64:
        grungs()
    elif d100 <= 66:
        lizardfolk()
    elif d100 <= 69:
        madMonkeyMist()
    elif d100 == 70:
        mephits()
    elif d100 == 71:
        nightHag()
    elif d100 == 72:
        rarePlants()
    elif d100 <= 76:
        shamblingMound()
    elif d100 <= 80:
        constrictorSnake()
    elif d100 <= 82:
        giantConstrictorSnake()
    elif d100 <= 85:
        statueOfUbtao()
    elif d100 <= 87:
        stirges()
    elif d100 <= 89:
        swarmsOfBats()
    elif d100 <= 94:
        swarmsOfInsects()
    elif d100 == 95:
        ghouls()
    elif d100 <= 97:
        skeletons()
    elif d100 == 98:
        zombies()
    elif d100 <= 99:
        yellowMuskCreeperAndZombies()
    else:
        yuanTi()

def wasteland():
    d100 = random.randrange(1,101)
    if d100 == 1:
        artusCimber()
    elif d100 <= 5:
        cache()
    elif d100 <= 9:
        redDragon()
    elif d100 <= 18:
        deadExplorer()
    elif d100 == 19:
        explorers()
    elif d100 <= 37:
        firenewts()
    elif d100 <= 45:
        giantScorpions()
    elif d100 <= 54:
        magmins()
    elif d100 <= 71:
        mephits()
    elif d100 <= 78:
        nightHag()
    elif d100 == 79:
        statueOfUbtao()
    elif d100 <= 83:
        troll()
    elif d100 <= 85:
        ghouls()
    elif d100 <= 95:
        skeletons()
    elif d100 <= 97:
        wight()
    elif d100 == 98:
        zombies()
    else:
        zhentarim()

def omuRuins():
    d100 = random.randrange(1,101)
    if d100 <= 5:
        apes()
    elif d100 <= 10:
        baboons()
    elif d100 <= 15:
        cannibals()
    elif d100 <= 20:
        faerieDragon()
    elif d100 <= 25:
        gargoyles()
    elif d100 <= 30:
        giantWasps()
    elif d100 <= 35:
        giantWolfSpiders()
    elif d100 <= 40:
        goblins()
    elif d100 <= 45:
        grungs()
    elif d100 <= 50:
        kingOfFeathers()
    elif d100 <= 55:
        kobolds()
    elif d100 <= 60:
        redWizard()
    elif d100 <= 65:
        shamblingMound()
    elif d100 <= 70:
        suMonsters()
    elif d100 <= 75:
        tabaxiHunter()
    elif d100 <= 80:
        ghouls()
    elif d100 <= 85:
        zombies()
    elif d100 <= 90:
        vegepygmies()
    elif d100 <= 95:
        yellowMuskCreeperAndZombies()
    else:
        yuanTi()

def omuPalace():
    d100 = random.randrange(1,101)
    if d100 <= 10:
        baboons()
    elif d100 <= 15:
        faerieDragon()
    elif d100 <= 25:
        gargoyles()
    elif d100 <= 35:
        giantWolfSpiders()
    elif d100 <= 40:
        goblins()
    elif d100 <= 50:
        kingOfFeathers()
    elif d100 <= 60:
        kobolds()
    elif d100 <= 70:
        redWizard()
    elif d100 <= 75:
        suMonsters()
    elif d100 <= 80:
        tabaxiHunter()
    elif d100 <= 90:
        yellowMuskCreeperAndZombies()
    else:
        yuanTi()

def omuSwamp():
    d100 = random.randrange(1,101)
    if d100 <= 10:
        crocodiles()
    elif d100 <= 15:
        gargoyles()
    elif d100 <= 25:
        giantWasps()
    elif d100 <= 35:
        grungs()
    elif d100 <= 50:
        kingOfFeathers()
    elif d100 <= 60:
        shamblingMound()
    elif d100 <= 65:
        ghouls()
    elif d100 <= 70:
        zombies()
    elif d100 <= 80:
        vegepygmies()
    elif d100 <= 90:
        yellowMuskCreeperAndZombies()
    else:
        yuanTi()
        
def encounterGen():
    stopGen = 2
    while stopGen == 2:
        print("Which environment is the party in?")
        print("0. Close Program")
        print("1. Beach")
        print("2. Jungle (No Undead)")
        print("3. Jungle (Lesser Undead)")
        print("4. Jungle (Greater Undead)")
        print("5. Mountains")
        print("6. Rivers")
        print("7. Ruins")
        print("8. Swamp")
        print("9. Wasteland")
        print ("10. Omu Ruins")
        print("11. Omu Palace")
        print("12. Omu Swamp")
        print()
        env = int(input("Input number: "))
        print()

        ### End ###
        if env == 0:
            stopGen = 0
        
        ### Beach ###
        if env == 1:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                beach()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                beach()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                beach()
            else:
                print("No encounter")
                print()
            
        ### Jungle NU ###
        if env == 2:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                noUndead()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                noUndead()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                noUndead()
            else:
                print("No encounter")
                print()

        ### Jungle LU ###
        if env == 3:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                lesserUndead()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                lesserUndead()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                lesserUndead()
            else:
                print("No encounter")
                print()
                    
        ### Jungle GU ###
        if env == 4:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                greaterUndead()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                greaterUndead()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                greaterUndead()
            else:
                print("No encounter")
                print()
            
        ### Mountains ###
        if env == 5:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                mountains()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                mountains()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                mountains()
            else:
                print("No encounter")
                print()

        ### Rivers ###
        if env == 6:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                rivers()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                rivers()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                rivers()
            else:
                print("No encounter")
                print()

        ### Ruins ###
        if env == 7:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                ruins()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                ruins()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                ruins()
            else:
                print("No encounter")
                print()
            
        ### Swamp ###
        if env == 8:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                swamp()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                swamp()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                swamp()
            else:
                print("No encounter")
                print()

        ### Wasteland ###
        if env == 9:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                wasteland()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                wasteland()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                wasteland()
            else:
                print("No encounter")
                print()

        ### Omu Ruins ###
        if env == 10:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                omuRuins()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                omuRuins()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                omuRuins()
            else:
                print("No encounter")
                print()
            
        ### Omu Palace ###
        if env == 11:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                omuPalace()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                omuPalace()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                omuPalace()
            else:
                print("No encounter")
                print()

        ### Omu Swamp ###
        if env == 12:
            weatherGen()
            print("Morning:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                omuSwamp()
            else:
                print("No encounter")
                print()
            print("Afternoon:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                omuSwamp()
            else:
                print("No encounter")
                print()
            print("Night:")
            d3 = random.randrange(1,4)
            if d3 == 3:
                omuSwamp()
            else:
                print("No encounter")
                print()

def main():
    encounterGen()

main()
