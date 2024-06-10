import random

class MazeRats:
    def __init__(self):

        # Character Creation
        self.character_starting_items = ["animal scent", "bear trap", "bedroll", "caltrops", "chain (10 ft.)", "chalk", "chisel", "crowbar", "fishingnet", "glass marbles", "glue", "grappling hook", "grease", "hacksaw", "hammer", "hand drill", "horn", "iron spikes", "iron tongs", "lantern and oil", "large sack", "lockpicks (3)", "manacles", "medicine (3)", "metal file", "rations (3)", "rope (50 ft.)", "steel wire", "shovel", "steel mirror", "ten foot pole", "tinderbox", "torch", "vial of acid", "vial of poison", "waterskin"]
        self.character_creation_appearances = ["aquiline", "athletic", "barrel-chested", "boney", "brawny", "brutish", "bullnecked", "chiseled", "coltish", "corpulent", "craggy", "delicate", "furrowed", "gaunt", "gorgeus", "grizzled", "haggard", "hamdsome", "hideous", "lanky", "pudgy", "ripped", "rosy", "scrawny", "sinewy", "slender", "slumped", "solid", "square-jawed", "statuesque", "towering", "trim", "weathered", "willowy", "wiry", "wrinkled"]
        self.character_creation_physical_details = ["acid scars", "battle scars", "birthmark", "braided hair", "brand mark", "broken nose", "bronze skinned", "burn scars", "bushy eyebrows", "curly hair", "dark skinned", "dreadlocks", "exotic accent", "flogging scars", "freckles", "gold tooth", "hoarse voice", "huge beard", "long hair", "matted hair", "missing ear", "missing teeth", "mustache", "muttonchops", "nine fingers", "oiled hair", "one-eyed", "pale skinned", "piercings", "ritual scars", "sallow skin", "shaved head", "sunburned", "tangled hair", "tattoos", "topknot"]
        self.character_creation_backgrounds = ["alchemist", "beggar-prince", "blackmailer", "bounty-hunter", "chimney sweep", "coin-clipper", "contortionist", "counterfeiter", "cultist", "cutpurpse", "debt-collector", "deserter", "fence", "fortuneteller", "galley slave", "gambler", "gravedigger", "headsman", "hedge knight", "highwayman", "housebreaker", "kidnapper", "mad prophet", "mountebank", "peddler", "pit-fighter", "poisoner", "rat-catcher", "scrivener", "sellsword", "slave", "smuggler", "street performer", "tattoosit", "urchin", "usurer"]
        self.character_creation_clothing = ["antique", "battle-torn", "bedraggled", "blood-stained", "ceremonial", "dated", "decaying", "eccentric", "elegant", "embroidered", "exotic", "fashionable", "flamboyant", "food-stained", "formatl", "frayed", "frumpy", "garish", "grimy", "haute couture", "lacey", "livery", "mud-stained", "ostentatious", "oversized", "patched", "patterned", "perfumed", "practical", "rumpled", "sigils", "singed", "tasteless", "undersized", "wine-stained", "worn out"]
        self.character_creation_personalities = ["bitter", "brave", "cautious", "chipper", "contrary", "cowardly", "cunning", "driven", "entitled", "gregarious", "grumpy", "heartless", "honor-bound", "hotheaded", "inquisitive", "irascible", "jolly", "know-it-all", "lazy", "loyal", "menacing", "mopey", "nervous", "protective", "righteous", "rude", "sarcastic", "savage", "scheming", "seren", "spacey", "stoic", "stubborn", "stuck-up", "suspicious", "wisecracking"]
        self.character_creation_mannerisms = ["anecdotes", "breathy", "chuckles", "clipped", "cryptic", "deep voice", "drawl", "enunciates", "flowery speech", "gravelly voice", "highly formal", "hypnotic", "interrupts", "laconic", "laughs", "long pauses", "melodious", "monotone", "mumbles", "narrates", "overly casual", "quaint sayings", "rambles", "random facts", "rapdi-fire", "rhyming", "robotic", "slow speech", "speechifies", "squeaky street slang", "stutters", "talks to self", "trails off", "very loud", "whispers"]

        # Magic
        self.physical_effects = ["animating", "attracting", "binding", "blossoming", "consuming", "creeping", "leitating", "opening", "petrifying", "phasing", "peircing", "pursuing", "crushing", "diminishing", "dividing", "duplicating", "enveloping", "expanding", "reflecting", "regenerating", "rending", "repelling", "resurecting", "screaming", "fusing", "grasping", "hastening", "hindering", "illumiating", "imprisoning", "sealing", "shapeshifting", "sheilding", "spawning", "transmuting", "trasnporting"]
        self.physical_elements = ["acid", "amber", "bark", "blood", "bone", "brine", "clay", "crow", "crystal", "ember", "flesh", "fungus", "glass", "honey", "ice instect", "wood", "lava", "moss", "obsidian", "oil", "poison", "rat", "salt", "sand", "sap", "serpent", "slime", "stone", "tar", "thorn", "vine", "water", "wine", "wood", "worm"]
        self.physical_forms = ["altar", "armor", "arrow", "beast", "blade", "cauldron", "chain", "chariot", "claw", "cloak", "colossus", "crown", "elemental", "eye", "fountain", "gate", "golem", "hammer", "horn", "key", "mask", "monolith", "pit", "prison", "sentinel", "servant", "sheild", "spear", "steed", "swarm", "tentacle", "throne", "torch", "trap", "wall", "web"]
        self.ethereal_effects = ["avenging", "banishing", "bewildering", "blinding", "charming", "communicating", "compelling", "concealing", "defening", "deciving", "deciphering", "disguising", "dispelling", "emobldening", "encodiing", "energizing", "enlightening", "enraging", "excrutiating", "forseeing", "intoxicating", "maddening", "mesmerising", "mindreading", "nullifying", "paralising", "revealing", "revolting", "scrying", "silencing", "soothing", "summoning", "terrifying", "warding", "wearying", "withering"]
        self.ethereal_elements = ["ash", "chaos", "distortion", "dream", "dust", "echo", "electoplasm", "fire", "fog", "ghost", "harmony", "heat", "light", "lightning", "memory", "mind", "mutation", "negation", "plague", "plasma", "probability", "rain", "rot", "shadow", "smoke", "snow", "soul", "star", "stasis", "steam", "thunder", "time", "void", "warp", "whisper", "wind"]
        self.ethereal_forms = ["aura", "beacon", "beam", "blast", "blog", "bolt", "gaze", "loop", "moment", "nexus", "portal", "pulse", "bubble", "call", "cascade", "circle", "cloud", "coil", "pyramid", "ray", "shard", "sphere", "spray", "storm", "cone", "cube", "dance", "disk", "field", "form", "swarm", "torrent", "touch", "vortex", "wave", "word"]
        self._mutations = ["ages", "attracts birds", "child-form", "corpulence", "covered in hair", "cyclops", "extra arms", "extra eyes", "extra legs", "forked tongue", "gender swap", "hunchback", "long arms", "lose all hair", "lose teeth", "no eyes", "no mouth", "second face", "sheds skin", "shrinks", "shrivels", "skin boils", "slime trail", "transluescent skin", "weeps blood"]
        self._insanities = ["always liesd", "always polited", "cannot countd", "cannot liked", "faceblindd", "fears birdsd", "fears bloodd", "fears booksd", "fears darkenssd", "fears fired", "fears goldd", "fears horsesd", "fears irond", "fears musicd", "fears own handd", "fears PCd", "fears raind", "fears riversd", "fears silenced", "fears sleepd", "fears sunlightd", "fears the moond", "fears treesd", "'genius'd", "'gorgeous'd", "hates violenced", "'invisible'd", "'invulnerable'd",  "must singd", "says thoughts", "sees dead people"]
        self._omens_and_catastrophes = ["all iron rusts", "animals die", "birds attack", "city appears", "deadly fog", "dream plague", "endless night", "endless rain", "endless storm", "endless twilight", "endless winter", "fae return", "forest appears", "forgetfulness", "graves open", "lamentations", "maggots", "mass slumber", "meteor strike", "mirrors speak", "no stars", "outsider enters", "people shrink", "people vanish", "plants wither", "portal opens", "rifts open", "shadows speak", "space distorts", "stones speak", "total silence", "tower appears", "water to blood"]

        # Monsters & Animals
        self.monster_bases = ["aerial", "terrestrial", "aquatic"]
        self.aerial_animal_bases = ["albatross", "bat", "beetle", "bird of paradise", "butterfly", "condor", "crane", "crow", "dragonfly", "eagle", "falcon", "firefly", "flamingo", "fly", "flying squirrel", "goose", "gull", "hummingbird", "kingfisher", "locust", "magpie", "mantis", "mockingbird", "mosquito", "moth", "owl", "parrot", "peacock", "pelican", "pteranodon", "rooster", "sparrow", "swan", "vulture", "wasp", "woodpecker"]
        self.terrestrial_animal_bases = ["ant", "ape", "armadillo", "badger", "bear", "boar", "caterpillar", "centipede", "chameleon", "cockroach", "deer", "elephant", "ferret", "fox", "giraffe", "goat", "horse", "human", "mole", "ostrich", "ox", "porcupine", "rabbit", "racoon", "rat", "rhinoceros", "scorpion", "sheep", "slug", "snail", "snake", "spider", "squirrel", "tiger", "wolf", "wolverine"]
        self.aquatic_animal_bases = ["alligator", "amoeba", "anglerfish", "beaver", "clam", "crab", "dolphin", "eel", "frog", "hippopotamus", "jellyfish", "leech", "lobster", "manatee", "manta ray", "muskrat", "narwhal", "newt", "octopus", "otter", "penguin", "platypus", "pufferfish", "salamander", "sea anemone", "sea urchin", "seahorse", "seal", "shark", "shrimp", "squid", "swordfish", "tadpole", "turtle", "walrus", "whale"]
        self.monster_features = ["antlers", "beak carapace", "claws", "compound eyes", "eye stalks", "fangs", "fins", "fur", "gills", "hooves", "horns", "legless", "long tongue", "many-eyed", "many-limbed", "mucus", "pncers", "plates", "plumage", "probiscus", "scales", "segments", "shaggy hair", "shell", "spikes", "spinnerets", "spines", "stinger", "suction cups", "tail", "talons", "tentacles", "trunk", "tusks", "wings"]
        self._monster_traits = ["amphibious", "bloated", "brittle", "cannibal", "clay-like", "colossal", "crystalline", "decaying", "ethereal", "ever-young", "eyeless", "fearless", "fluffy", "fungal", "gelatinous", "geometric", "hardened", "illusory", "intelligent", "iridescent", "luminous", "many-headed", "mechanical",  "planar", "reflective", "rubbery", "shadowy", "sharp", "skeletal", "slimy", "sticky", "stinking", "tiny", "transluscent"]
        self._monster_abilities = ["absorbing", "acid blood", "anti-magic", "blinding", "breath weapon", "camouflaging", "duplicating", "electric", "entangling",  "exploding", "flying", "gaze weapon", "hypnotizing", "impervious", "invisible", "life-draining", "magnetic", "mimicking", "mind-reading", "paralyzing", "phasing", "poisonous", "radioactive", "reflective", "regenerating", "shapeshifting", "spell-casting", "stealthy", "strangling", "super-strength", "telekinetic", "vampiric", "wall-crawling"]
        self.monster_tactics = ["ambush", "call for support", "capture", "charge", "climb foes", "compel worship", "create barrier", "decieve", "demand duel", "disorient", "encircle", "evade", "gang up", "gather strength", "go berserk", "harry", "hurl foes", "immobilize", "manipulate", "mock", "monologue", "order minion", "protect leader", "protect self", "scatter foes", "stalk", "steal from", "swarm", "target insolent", "target leader", "target nearest", "target richest", "target strongest", "target weakest", "toy with", "use terrain"]
        self.monster_personality = ["alien", "aloof", "bored", "cautious", "cowardly", "curios", "devious", "distractible", "educated", "embittered", "envious", "erudite", "fanatical", "forgetful", "generous", "hateful", "honorable", "humble", "jaded", "jobial", "legalistic", "manipulative", "megalomaniac", "melancholy", "meticulous", "mystical", "obsessive", "outof touch", "paranoid", "polite", "psychopathic", "sophisticated", "touchy", "unimpressed", "vain", "xenophobic"]
        self._monster_weaknesses = ["bells", "birdsong", "children", "cold", "cold iron", "competition", "conversation", "deformity", "flattery", "flowers", "gifts", "gold", "heat", "holy icon", "holy water", "home cooking", "mirrors", "mistletoe", "moonlight", "music", "phylactery", "puzzles", "riddles", "rituals", "silver", "sunlight", "tears", "true names", "weak spot", "wine", "wormwood"]

        # Characters
        self.civilized_npcs = ["acolyte", "actor", "apothecary", "baker", "barber", "blacksmith", "brewer", "bureaucrat", "butcher", "carpenter", "clockmaker", "courier", "courtier", "diplomat", "fishmonger", "guard", "haberdasher", "innkeeper", "item-seller", "jeweler", "knight", "locksmith", "mason", "miller", "musician", "noble", "painter", "priest", "scholar", "scribe", "sculptor", "shipwrithgt", "soldier", "tailor", "taxidermist", "wigmaker"]
        self.underworld_npcs = ["alchemist", "beggar-prince", "blackmailer", "bounty-hunter", "chimney sweep", "coin-clipper", "contortiounsit", "counterfieter", "cultist", "cutpurse", "debt-collector", "deserter", "fence", "fortuneteller", "galley slave", "gambler", "gravedigger", "headsman", "hedge nkight", "highwayman", "housebreaker", "kidnapper", "mad prohet", "mountebank", "peddler", "pit-fighter", "poisoner", "rat-catcher", "scrivener", "sellsword", "slave", "smuggler", "street performer", "tattooist", "urchin", "usurer"]
        self.wilderness_npcs = ["apiarist", "bandit", "caravan guard", "caravaneer", "druid", "exile", "explorer", "farmer", "fisherman", "forager", "fugitive", "hedge wizard", "hermit", "hunter", "messenger", "minstrel", "monk", "monster hunter", "outlander", "tinker", "pilgrim", "poacher", "raider", "ranger", "sage", "scavenger", "scout", "shepherd", "seer", "surveyor", "tinker", "tomb raider", "trader", "trapper", "witch", "woodcutter"]
        self.female_names = ["Adelaide", "Alma", "Barsaba", "Beatrix", "Bianca", "Cleopha", "Clover", "Constance", "Damaris", "Daphne", "Demona", "Elsbeth", "Esme", "Fern", "Hester", "Hippolyta", "Jessamine", "Jilly", "Morgot", "Minerva", "Nerissa", "Odette", "Olga", "Orchid", "Pepper", "Phoebe", "Piety", "Poppy", "Silence", "Sybil", "Trillby", "Tuesday", "Ursula", "Vivian", "Wendy", "Zora"]
        self.male_names = ["Balthazard", "Basil", "Bertram", "Blaxton", "Chadwick", "Clovis", "Destrain", "Ellis", "Erasmus", "Faustus", "Finn", "Fitzhugh", "Florian", "Fox", "Godwin", "Hannibal", "Jasper", "Jiles", "Jules", "Leopold", "Merrick", "Mortimer", "Ogden", "Orion", "Oswald", "Percival", "Peregrine", "Quentin", "Redmaine", "Reinhold", "Silas", "Stilton", "Stratford", "Tenpiece", "Waverly", "Webster"]
        self.upper_class_surnames = ["Belverderer", "Bithesea", "Calaver", "Carvolo", "Rippe", "Droll", "Dunlow", "Edevane", "Erelong", "Febland", "Fernsby", "Fisk", "Gastrell", "Girdwood", "Gorgon", "Grimeson", "Gruger", "Hitheryon", "Marque", "Malmora", "Miter", "Oblington", "Onymous", "Philleifent", "Portendorfer", "Romatet", "Rothery", "Skorbeck", "Slora", "Southwark", "Stavish", "Vandermeer", "Wellbelove", "Westergren", "Wexley", "Wilberforce"]
        self.lower_class_surnames = ["Barrow", "Beetleman", "Berrycloth", "Birdwhistle", "Bobich", "Chips", "Coffin", "Crunmpling", "Culpepper", "Dankworth", "Digsworthy", "Dreggs", "Gimble", "Graveworm", "Greelish", "Hardwick", "Hatman", "Hovel", "Knibbs", "Midnighter", "Needle", "Nethercoat", "Pestle", "Relish", "Rumbold", "Rummage", "Sallow", "Saltmarsh", "Silverless", "Skitter", "Slee", "Slitherly", "Stoker", "Tarwater", "Tumbler", "Villin"]
        self._assets = ["authority", "avoids detection", "calls in favors", "charming", "cooks the books", "erases evidence", "excellent liar", "extremly rich", "feared", "fortified base", "gorgeous", "hears rumors", "huge family", "huge library", "impersonator", "interrogator", "knows a guy", "knowsa a way in", "launders money", "learned", "local celebrity", "local knowledge", "loyal henchmen", "middling oracle", "nothing to lose", "owns the guards", "powerful spouse", "procures gear", "pulls the strings", "secret lab", "sells contraband", "smuggles goods", "spy netowrk", "war hero"]
        self._liabilities = ["addiction", "alcholic", "corrupt ally", "coward", "decadent", "forbidden love", "gambler", "glutton", "greedy", "heretic", "huge debts", "imposter", "jealous", "leaves evidence", "many enemies", "misinformed", "money trail", "narcissist", "needs medicine", "OCD", "paranoid", "partyer", "poor equipment", "protective", "scandalous", "softhearted", "scrit routines", "superstitious", "suspicious", "temper", "trusting", "vulnerable base", "wanted", "weak-willed", "widley despised"]
        self._npc_goals = ["a better life", "acceptance", "enlightment", "fame", "freedom", "glory", "infamy", "justice",  "learning", "love", "mastery", "power", "reach location",  "resolve dispute",  "revenge",  "serve a diety", "serve evil",  "serve ideology", "serve leader", "serve the needy", "wealth"]
        self.misfortunes = ["abandoned", "addicted", "arrested", "blackmailed", "burgled", "challenged", "condemned", "crippled", "cursed", "defrauded", "demoted", "depressed", "discredited", "dismissed", "disowned", "exiled", "famished", "forgotten", "framed", "haunted", "humiliated", "impovershed", "kidnapped", "lost", "mobbed", "mutilated", "overworked", "poisoned", "pursued", "rejected", "replaced", "robbed", "sick", "sued", "suspected", "transformed"]
        self.missions = ["apprehend", "assassinate", "blackmail", "burgle", "chart", "convince", "deface", "defraud", "deliver", "destroy", "discredit", "escort", "exfiltrate", "extort", "follow", "frame", "impersonate", "impress", "infiltrate", "interrogate", "investigate", "kidnap", "locate", "plant", "protect", "raid", "replace", "retrieve", "rob", "ruin", "sabotage", "smuggle", "surveil", "take over", "terrorize", "threaten"]
        self.character_methods = ["alchemy", "blackmail", "bluster", "bribery", "bullying", "bureaucracy", "charm", "commerce", "cronies", "debate", "deciet", "deduction", "eloquence", "espionage", "fast-talking", "favors", "hard work", "humor", "investigation", "legal maneurvers", "manipulation", "misdirection", "money", "nagging", "negotiation", "persistence", "piety", "preperation", "quick wit", "research", "rumors", "sabotage", "teamwork", "theft", "threats", "violence"]
        self.character_appearances = ["aquiline", "athletic", "barrel-chested", "boney", "brawny", "brutish", "bullnecked", "chiseled", "coltish", "corpulent", "craggy", "delicate", "furrowed", "gaunt", "gorgeus", "grizzled", "haggard", "hamdsome", "hideous", "lanky", "pudgy", "ripped", "rosy", "scrawny", "sinewy", "slender", "slumped", "solid", "square-jawed", "statuesque", "towering", "trim", "weathered", "willowy", "wiry", "wrinkled"]
        self.character_physical_details = ["acid scars", "battle scars", "birthmark", "braided hair", "brand mark", "broken nose", "bronze skinned", "burn scars", "bushy eyebrows", "curly hair", "dark skinned", "dreadlocks", "exotic accent", "flogging scars", "freckles", "gold tooth", "hoarse voice", "huge beard", "long hair", "matted hair", "missing ear", "missing teeth", "mustache", "muttonchops", "nine fingers", "oiled hair", "one-eyed", "pale skinned", "piercings", "ritual scars", "sallow skin", "shaved head", "sunburned", "tangled hair", "tattoos", "topknot"]
        self.character_clothing = ["antique", "battle-torn", "bedraggled", "blood-stained", "ceremonial", "dated", "decaying", "eccentric", "elegant", "embroidered", "exotic", "fashionable", "flamboyant", "food-stained", "formatl", "frayed", "frumpy", "garish", "grimy", "haute couture", "lacey", "livery", "mud-stained", "ostentatious", "oversized", "patched", "patterned", "perfumed", "practical", "rumpled", "sigils", "singed", "tasteless", "undersized", "wine-stained", "worn out"]
        self.character_personalities = ["bitter", "brave", "cautious", "chipper", "contrary", "cowardly", "cunning", "driven", "entitled", "gregarious", "grumpy", "heartless", "honor-bound", "hotheaded", "inquisitive", "irascible", "jolly", "know-it-all", "lazy", "loyal", "menacing", "mopey", "nervous", "protective", "righteous", "rude", "sarcastic", "savage", "scheming", "seren", "spacey", "stoic", "stubborn", "stuck-up", "suspicious", "wisecracking"]
        self.character_mannerisms = ["anecdotes", "breathy", "chuckles", "clipped", "cryptic", "deep voice", "drawl", "enunciates", "flowery speech", "gravelly voice", "highly formal", "hypnotic", "interrupts", "laconic", "laughs", "long pauses", "melodious", "monotone", "mumbles", "narrates", "overly casual", "quaint sayings", "rambles", "random facts", "rapdi-fire", "rhyming", "robotic", "slow speech", "speechifies", "squeaky street slang", "stutters", "talks to self", "trails off", "very loud", "whispers"]
        self._character_secrets = ["addicted", "artificial", "assassin", "bankrupt", "beholden", "counterspy", "cultist", "demigod", "evil lineage", "exile", "fence", "fugitive", "ghost", "has a child", "heretic", "high born", "huge fortune", "illusion", "insurrectionist", "low born", "married", "mind-controlled", "monster hunter", "non-human", "polygamist", "protects relic", "scanalous birth", "secret police", "serial killer", "smuggler", "spy", "time traveler", "transformed", "war criminal"]
        self.character_reputations = ["ambitious", "authoritative", "boor", "borrower", "celebrity", "charitable", "cheat", "dangerous", "entertainer", "gossip", "hardworking", "holy", "honest", "hypochondriac", "idiot", "influential", "layabout", "leader", "misanthrope", "miser", "neighborly", "nutjob", "obnoxious", "overeducated", "partier", "pious", "proper", "prophet of doom", "repulsive", "respected", "riffraff", "scandalous", "slime ball", "terrifying", "weirdo", "wise"]
        self.chracter_hobbies = ["archeaeology", "art collecting", "bad fiction", "calligraphy", "card games", "clockwork", "collecting cats", "cuisine", "dark lore", "dog breeding", "embroidery", "exercise", "falconry", "fashion", "fishing", "foreign cultures", "gardening", "history", "horseracing", "hunting", "instrument", "knitting", "lawn games", "mountaineering", "opera", "painting", "poetry", "puzzle-solving", "riddling", "science", "sculpture", "sketching", "smoking", "theater", "weaving", "whiskey"]
        self.character_relationships = ["adviser", "blackmailer", "business partner", "business rival", "buyer", "captor", "client", "confidant", "debtor", "disciple", "guardian", "henchman", "idol", "informant", "master", "mentor", "nemesis", "offspring", "parent", "patron", "political rival", "prisoner", "protege", "quarry", "right hand", "romantic rival", "servant", "sibling", "social rival", "spouse", "stalker", "suitor", "supplicant", "supplier", "sweetheart", "unrequited love"]
        self._divine_domains = ["Balance", "Betrayal", "Chance", "Chaos", "Conquest", "Cycles", "Death", "Destiny", "Dreams", "Gateways", "Judgement", "Loe", "Memory", "Monsters", "Moon", "Motherhood", "Oaths", "Order", "Plague", "Purification", "Reason", "Schemes", "Secrets", "Storms", "Summer", "Sun", "The Forge", "The Sea", "The Wild", "Time", "Underworld", "Wealth", "Winter"]
        self._characters_after_the_party = ["absurd boasts", "adopted a child", "awarded medal", "bought the inn", "cursed", "duel scheduled", "elected to office", "given a quest", "got married", "in a coffin", "in love", "in the stocks", "inconvenient pet", "insulted a noble",  "joined a cult", "letter of thanks", "lost", "lost at gambling", "lost reputation", "new identity", "new tattoo", "poisoned", "recruited", "robbed", "roof on fire", "shanghaied", "sick", "signed contract", "someone died", "spilled secrets", "started a cult", "swindled", "thrown in jail", "unruly mob", "wrong clothes"]

        # Treasure & Equipment
        self.miscellaneous_items = ["bowl", "brass bell", "brooch", "carved figurine", "cup", "deck of cards", "long fork", "numbered key", "oil lamp", "old doll", "paint pot", "pencil", "drawing", "foreign coin", "game piece", "glass eye", "glass jar", "hair comb", "purse", "quill pen", "salve", "scissors", "scroll", "sealed letter", "handkerchief", "hinged box", "hourglass", "human tooth", "hunting horn", "loaded dice", "sewing needle", "shaving razor", "silver button", "skull", "tobacco pipe", "wine bottle"]
        self.worn_items = ["belt", "blouse", "boots", "bracelet", "breastplate", "brigandine", "leather armor", "locket", "mail shirt", "mask", "necklace", "padded armor", "cincture", "cloak", "coat", "dress", "earing", "eyepatch", "plate mail", "ring", "robe", "sandals", "scarf", "shirt", "gauntlets", "glove", "gown", "hat", "helmet", "hose", "shoes", "skirt", "slippers", "socks", "trousers", "veil"]
        self.weapon_items = ["arming sword", "backsword", "battleaxe", "blowpipe", "claymore", "club", "longbow", "longsword", "mace", "maul", "morningstar", "pike", "crossbow", "cutlass", "dagger", "flail", "flanged mace", "glaive", "scimitar", "shortbow", "sickle", "sling", "spear", "staff", "halberd", "hammer", "hatchet", "horsebow", "hunting knife", "lance", "stake", "stiletto", "throwing axe", "warhammer", "warpick", "whip"]
        self.book_subjects = ["alchemy", "art", "astrology", "blackmail", "charts & maps", "conspiracies", "cookbook", "criminals", "divination", "etiquette", "fashion", "genealogy", "hagiography", "history", "journal", "language", "laws", "letters", "lost empires", "lost places", "love poems", "monsters", "mythology", "odd customs", "oratory", "propaganda", "prophecies", "siegecraft", "songs", "state secrets", "sword fighting", "theology", "treasures", "war chronicle", "who's who", "witch-hunting"]
        self.tool_items = ["acid flask", "bear trap", "bellows", "bolt cutters", "chain", "chisel", "lens", "lock & key", "lockpicks", "manacles", "metal file", "mortar & pestle", "crowbar", "door ram", "ear trumpet", "fire oil", "fishing hook", "goggles", "needle", "pickaxe", "pitchfork", "pliers", "pole", "pulleys", "grappling hook", "grease", "hacksaw", "hammer", "hand drill", "lantern", "rope", "scissors", "shovel", "spikes", "steel wire", "tongs"]
        self._potions = ["body swap", "camouflage", "control animals", "cure affliction", "detect evil", "detect gold", "detect hidden", "direction sense", "extra arm", "flight", "ghost-speech", "heat vision", "invulnerable", "magic immunity", "mirror image", "night vision",  "restore health", "speed", "stretchy", "super-jump", "super-strength", "telekinesis", "tongues", "water-breathing", "water-walking"]
        self._magical_ingredients = ["ancient liquor",  "blind eye", "boiled cat",  "bottled fog", "coffin nail", "corpse's hair", "crossroad dust", "cultist entrails", "exotic spice", "killer's hand", "king's tooth", "last breath", "liar's tongue", "lightning bolt", "lodestone", "monk's vow", "newborn's cry", "oil portrait", "pyre ember", "queen bee", "queen's blood", "ship's barnacle", "star-metal", "thief's finger", "tomb flower", "wedding ring", "widow's tears", "wizard skull"]
        self.treasure_items = ["alchemy recipe", "amulet", "astrolabe", "blueprints", "calligraphy", "carpet", "orrery", "painting", "perfume", "prayer book", "printing block", "rare textile", "compass", "contract", "crown", "crystal", "deed", "embroidery", "royal robes", "saint's relic", "scrimshaw", "sextant", "sheet music", "signet ring", "fine china", "fine liquor", "instrument", "magical book", "microscope", "music box", "silverware", "spices", "spyglass", "tapestry", "telescope", "treasure map"]
        self._treasure_traits = ["altered", "ancient", "blessed", "bulky", "compact", "consumable", "cultural value", "cursed", "damaged", "disguised", "draws enemies",  "embellished", "encoded", "exotic", "extra-planar", "famous", "forbidden", "fragile", "heavy", "immovable", "impracticable", "indestructible", "intelligent", "masterwork", "military value", "non-human", "owned", "partial", "political value", "religious value", "repaired", "royal", "toxic", "vile"]
        self.valuable_materials = ["alabaster", "amber", "aquamarine", "azurite", "beryl", "black pearl", "bloodstone", "bone china", "chalcedony", "cinnabar", "coral", "diamond", "ebony", "emerald", "fire agate", "garnet", "gold", "ivory", "jade", "jasper", "jet", "lapis lazuli", "malachite", "moonstone", "onyx", "opal", "pearl", "platinum", "porcelain", "ruby", "sapphire", "serpentine", "silver", "star iron", "topaz", "turquoise"]

        # The City
        self._city_themes = ["aristocracy", "art", "bureaucracy", "castes", "catacombs", "crime families", "cruelty", "festivals", "feuds", "intrigue",  "martial law", "meritocracy", "opulence",  "pilgrimages", "piracy", "plutocracy", "poverty", "rituals", "slavery", "spices", "theocracy", "theivery", "trade", "tyranny", "xenophobia"]
        self._city_events = ["assassination", "carvinval", "conscription", "coronation", "coup", "cult activity", "curfew", "discovery", "earthquake", "fashion trend", "fire", "flood", "heavy fog", "heavy taxes", "holy day", "hysteria", "inquisition", "insurrection", "invasion", "jailbreak", "mass eviction", "mass pardon", "negotiations", "plague", "proclamation", "prohibition", "public games", "refugees", "rioting", "roundup", "scandal", "serial killer", "shortage", "tournament", "trial"]
        self._district_themes = ["catacombs", "construction", "crafts", "criminality", "culture", "dining", "education", "entertainment", "finance", "foreigners", "ghettoes", "government", "graveyards", "green space", "industrialization", "judgement", "livestock", "marketplace", "memorials", "military", "opulence", "pollution", "poverty", "punishment", "religion", "science", "trade", "trash", "vices", "wizardry", "wonders"]
        self.upper_class_buildings = ["academy", "alchemist", "archive", "art dealer", "barber", "bookbinder", "bookseller", "castle", "clockmaker", "clotheir", "courthouse", "furrier", "gallery", "garden", "haberdashery", "jeweler", "law office", "locksmith", "lounge", "manor", "museum", "observatory", "opera house", "park", "physician", "printer", "public baths", "restaurant", "salon", "stables", "taxidermist", "temple", "tobacconist", "townhouse", "winery", "zoo"]
        self.lower_class_buildings = ["apothecary", "asylum", "baker", "brewery", "butcher", "candlemaker", "catacombs", "cheesemaker", "criminal den", "curiosity shop", "dock", "fighting pit", "forge", "fortuneteller", "gambling hall", "leatherworks", "marketplace", "mason", "mill", "moneylender", "orphanage", "outfitter", "prison", "sewers", "shipyards", "shrine", "stockyard", "stonecarver", "tattooist", "tavern", "theater", "veternarian", "warehouse", "watchtower", "weaver", "workshop"]
        self._city_activities = ["abduct", "beg", "brawl", "burgle", "celebrate", "chase", "construct", "cook", "dance", "deul", "execute", "extinguish", "extort", "follow", "gamble", "haul", "interrogate", "marry", "mourn", "party", "patrol", "perform", "play", "preach", "process", "proclaim", "protest", "release", "repair", "riot", "rob", "search", "sell"]
        self._building_rooms = ["arboretum", "atrium", "attic", "aviary", "ballroom", "baths", "bed chamber", "cabinet", "chapel", "cloakroom", "dining room", "dressing room", "garden", "garret", "greenhouse", "junk room", "kitchen", "larder", "library", "map room", "menagerie", "mews", "nursery", "pantry", "parlor", "privy", "root cellar", "saucery", "scullery", "smoking room", "spicery", "still room", "study", "trophy room", "wardrobe"]
        self._tactical_street_features = ["arcade", "awnings", "balconies", "barricades", "bridge", "canal", "carriages", "catwalks",
         "climbable walls", "clotheslines", "crowd", "dead end", "dense fog", "downpour", "flooding", "food stalls", "fountain", "gates", "ladders", "livestock", "muddy", "overgrown", "roof access", "roof gardens", "sweer access", "sinkhole", "slick", "steep roofs", "steep streets", "steps", "torn up street", "vermin swarms", "well"]
        self._tactical_building_features = ["balconies", "basement access", "brightly lit", "broken furniture", "broken glass", "cabinets", "carpeted floors", "chandeliers", "crawlspaces", "drain pipes", "dumbwaiters", "echoing marble", "hanging chains", "huge fireplace", "narrow ledges", "open windows", "ornate weapons", "overgrown", "patrols", "piles of trash", "illars", "rotting ceiling", "rotting floors", "rotting walls", "screens", "servant passages", "sweer access", "shadowy alcoves", "skylights", "spyholes", "staircases", "tall bookshelves", "unlit", "watchdogs", "window drapes"]
        self.factions = ["art movement", "beggar's guild", "black market", "brotherhood", "city guard", "conspiracy", "craft guild", "crime family", "crime ring", "dark cult", "explorer's club", "free company", "gourmand club", "heist crew", "heretical sect", "high council", "hired killers", "local militia", "national church", "noble house", "outlander clan", "outlaw gang", "political party", "religious order", "religious sect", "resistance", "royal army", "royal house", "scholar's circle", "secret society", "spy netowrk", "street artists", "street gang", "street musicians", "theater troupe", "trade company"]
        self.faction_traits = ["bankrupt", "bureaucratic", "charitable", "confused", "connected", "corrupt", "decadent", "decayhing", "delusional", "swindling", "efficient", "esoteric", "expanding", "hunted", "incompetent", "incorruptib le", "insane", "insular", "manipulative", "martial", "pious", "popular", "righteous", "ruthless", "secret", "subversive", "suppressed", "threatened", "thriving", "unpopular", "up-and-comming", "wealthy", "well-prepared", "xenophobic"]
        self._faction_goals = ["advise leader", "avoid detection", "awaken being", "collect artifacts", "construct base",  "control politics", "create artifact",  "defend borders", "defend leader", "detroy artifacts", "destroy being", "destroy villain", "enforce law", "encrich members", "entertain", "exchange goods", "hear rumors", "indulge tastes", "map the wild", "overthrow order", "preserve lineage", "preserve lore", "produce goods", "promote arts", "promote craft", "purge traitors", "sell services", "share knowledge", "spread beliefs", "summon evil", "survive", "transport goods"]

        #The Wild
        self.wilderness_regions = ["ashy", "badlands", "bay", "beach", "delta", "desert", "jungle", "lowlands", "mesas", "moor", "mountains", "petrified forest", "dry lands", "dune sea", "dust bowl", "fjords", "flood lands", "foothills", "plains", "rainforest", "riverlands", "salt pan", "savanna", "steppe", "forest", "glaciers", "heath", "highlands", "hills", "ice fields", "tiaga", "thickets", "tundra", "volcanic plain", "wetlands", "woodlands"]
        self.wilderness_landmarks = ["bog", "boulder field", "butte", "cave", "cliff", "crag", "lakebed", "marsh", "mesa", "moor", "pass", "pit", "crater", "creek", "crossing", "ditch", "field", "forest", "pond", "rapids", "ravine", "ridge", "rise", "river", "grove", "hill", "hollow", "hot springs", "lair", "lake", "rockslide", "spring", "swamp", "thickets", "valley", "waterfall"]
        self.wilderness_structures = ["altar", "aquadeuct", "bandit's camp", "battleifeld", "bonfire", "bridge", "cairn", "crossroads", "crypt", "dam", "dungeon", "farm", "ford", "fortress", "gallows", "graveyard", "hedge", "hunter's camp", "inn", "lumber camp", "mine", "monastery", "monument", "orchard", "outpost", "pasture", "ruin", "seclusion", "shack", "shrine", "standing stone", "temple", "village", "wall", "watchtower", "waystone"]
        self._wilderness_region_traits = ["ashen", "blasted", "blighted", "broken", "consuming", "corrupted", "creeping", "desolate", "eternal", "foresaken", "frozen", "haunted", "howling", "jagged", "lonely", "misty", "perilous", "petrified", "phantasmal", "ravenous", "savage", "shadowy", "shifting", "shivering", "sinister", "sinking", "smoldering", "sweltering", "frozen", "huanted", "howling", "jagged", "loneyly", "misty", "thorny", "thundering", "torrential", "wandering", "withered"]
        self._wilderness_discoveries = ["bloodstains", "bones", "broken weapons", "burrow", "cut ropes", "dead animal", "food scraps", "grave marker", "human corpse", "map", "message", "migration", "nest", "portal", "resources", "rift", "strange plant", "supplies", "torn flag", "tracks", "trap", "treasure cache", "wizard fight"]
        self._wilderness_activities = ["ambush", "argue", "birth", "build", "bury", "capture",  "convene", "demolish", "die", "duel",  "eat", "excavate", "feast", "felling", "fish", "flee", "forage", "hunt", "march", "raid", "rescue", "rest", "sacrifice", "scout", "sing", "skin", "skirmish", "slay", "sleep", "swim", "track", "trap", "wander", "worship"]
        self.wilderness_hazards = ["avalanche", "blizzard", "brushfire", "cloudburst", "cyclone", "dense fog", "downpour", "drizzle", "dust storm", "earthquake", "eruption", "flooding", "forest fire", "hail", "heatwave", "hurricane", "ice storm", "light mist", "locust swarm", "magma flow", "meteor strike", "monsoon", "mudflow", "mudslide", "predator", "quicksand", "rain of frogs", "rockslide", "sandstorm", "sleet", "snow", "stampede", "thunderstorm", "tsunami", "whirlpool", "windstorm"]
        self.edible_plants = ["acorns", "apples", "asparagus", "blackberries", "blueberries", "carrots", "cattail", "cherries", "chickweed", "chicory", "clover", "dandelion", "dead-nettle", "elderberries", "fireweed", "gooseberries", "hazelenuts", "henbit", "hickorynuts", "honeysuckle", "leeks", "milkthisle", "mint", "mulberries", "mushrooms", "mustard", "onion", "pecans", "persimmons", "raspberries", "strawberries", "walnuts", "watercress", "wild garlic", "wild grapes", "wood sorrel"]
        self.poisonous_plants = ["angel's trumpet", "baneberry", "belladona", "blacktruffle", "bleedingheart", "celandine", "cocklebur", "columbine", "crowncup", "deathcap", "dumbcane", "foxglove", "hemlock", "hogweed", "holly", "horse chestnut", "hyacinth", "ivy", "jessamine", "kudu", "larkspur", "mandrake", "mangrove", "mistletoe", "moonflower", "nightshadeoleander", "ragwort", "reindeer lichen", "snakeweed", "spindle", "stinkhorn", "waxcap", "wine-cap", "woflsbane", "wormswood"]
        self.inn_adjectives = ["bellowing", "blazing", "bleak", "blessed", "bloody", "crimson", "cunning", "copper", "dancing", "dead", "drunken", "flying", "ghastly", "golden", "helpful", "hideous", "howling", "hungry", "moldy", "muttering", "nimble", "oozing", "petrified", "prancing", "romantic", "salty", "singing", "shivering", "shrieking", "silver", "smoking", "thirsty", "wicked", "tipsy", "whistling", "wanton"]
        self.inn_nouns = ["axe", "barrel", "bear", "bell", "boot", "bowl", "bucket", "candle", "cock", "cow", "dragon", "egg", "elephant", "flea", "fork", "giant", "griffin", "hart", "hog", "hound", "lamb", "lion", "mackerel", "maid", "monk", "moon", "pipe", "prince", "rat", "skull", "spoon", "star", "swan", "sword", "whale", "wife"]
        self._inn_quirks = ["100 years in past", "always night", "animal fights", "bard duels", "bigger inside", "black market", "brand new", "cannibals",  "constant party", "dancing contest", "dead drop",  "expensive",  "famous chef", "fey patrons", "fight club", "five floors", "ghost staff", "haunted", "hideout",  "magic sword", "magically moves", "mercs for hire",  "preaching", "secure storage", "staff at kids", "talking painting", "underground", "VIP lounge", "voice in well", "women only"]

        # The Maze
        self.dungeon_entrances = ["all libraries", "beaver dam", "behind waterfall", "chalk rectangle", "chest bottom", "chimney", "cupboard", "dolmen shadow", "down a well", "fiery pit", "fog road", "forest spring", "giant book", "gypsy wagon", "hollow tree", "huge keyhole", "iron maiden", "living tattoo", "magic painting", "man-shape hole", "maze potion", "mirror", "monster mouth", "monster wound", "narrow alley", "rain door", "sewer grate", "sudden rift", "tidal cave", "tower top", "tree roots", "under the bed", "unfolded map", "up a tree", "whirlpool", "wine barrel"]
        self._dungeon_forms = ["arena", "asylum", "aviary", "bank", "baths", "body",  "casino", "catacombs", "cave", "court",  "forge", "garden", "hideout", "hotel", "laboratory", "library", "market", "mine", "monastery", "museum", "nursery", "orphanage", "palace", "prison", "sewer", "ship", "slave pit", "temple", "theater",  "university", "vault", "zoo"]
        self.dungeon_layout = ["ant colony", "central hub", "claustrophobic", "crisscrossing", "curved", "disorienting", "galleria", "geometric", "gonzo", "haphazard", "highly regular", "honeycomb", "intertwined", "isolated wings", "layered", "linear", "loops", "many corridors", "mazes", "mix of layouts", "multiple hubs", "no corridors", "open plan", "open voids", "organic", "oversized", "recursive", "repetitive", "sprawling", "suspended", "symbol shape", "tall and narrow", "themed zones", "vertical", "winding", "ziggurat"]
        self._dungeon_ruinations = ["arcane disaster", "army invasion", "cannibalism", "civil war", "collapse", "crystal growth", "curse", "degeneration", "earthquake", "eruption", "evil unearthed", "experiments", "explosion", "famine", "fire", "flooding", "fungus", "haunting", "ice",  "lava flow", "magical sleep", "melted", "monster attack", "outsider attack", "overgrowth", "petrification", "plague", "planar overlay", "poison gas", "resources gone", "revolt", "risen dead", "too many traps", "war"]
        self._dungeon_rewards = ["ancient lore", "animal ally", "army", "blessing", "blueprints", "cultural artifact", "enemy weakness",  "forewarning", "guide", "holy relic", "influential ally", "instructions", "jewels", "key", "lost formula", "machine",  "magical ally", "map", "martial ally", "masterpiece", "oracle", "piles of loot", "planar portal", "prohecy", "renown", "spell", "transformation", "transport",  "uncovererd plot",  "vision", "weapon"]
        self._dungeon_activities = ["besiege", "capture", "collect", "construct", "ontrol", "deliver", "demolish", "escape", "feed", "fortify", "gaurd", "hide", "hunt", "loot", "map", "mine",  "negotiate", "patrol", "perform ritual", "purge", "question", "raid", "repair", "rescue", "research", "revive", "riddle", "scavenge", "seize", "tunnel", "unearth", "vandalize", "worship"]
        self._dungeon_rooms = ["armory", "banquet hall", "barracks",  "catacombs", "cavern", "chasm", "courtyard", "crypt", "dormitory", "fighting pit", "forge", "fountain", "gatehouse", "guard room", "kennel", "lower class building", "laboratory", "mess hall", "mine shaft", "museum", "oubliette", "pool", "prison", "record room", "shrine", "slaughterhouse", "stables", "storeroom", "throne room", "torture room", "treasury", "vault", "well", "workshop"]
        self.dungeon_room_details = ["bas-relief", "blood trail", "bones", "chains", "chalk marks", "claw marks", "corpses", "cracked beams", "crumbling walls", "decaying food", "decaying nest", "dripping water", "fading murals", "faint breeze", "faint footsteps", "fallen pillars", "fungus", "furniture", "graffiti", "mosaics", "recent repairs", "rotting books", "rubble", "shed skin", "slime trails", "spider webs", "stalactites", "stench", "smoke stains", "thug dust", "torn clothes", "tree roots", "unusual smell", "vibrations", "vines", "whispers"]
        self._dungeon_tricks = ["absorption", "activation", "animation", "blessings", "communication", "confusion", "consumption", "creation", "curses", "deception", "duplication", "exchange", "imprisonment", "instructions", "interrogation", "mind-control", "mission", "mood-alteration", "nullification", "planeshift", "protection", "rejuvenation", "release", "reversal", "rotation", "scrying", "size-alteration", "summoning", "theft", "time-alteration", "transformation", "transmutation", "transportation", "wonder"]
        self.dungeon_hazards = ["acid drip", "bloodsuckers", "cave-in", "choking dust", "crude oil", "crystal shards", "deafening noise", "dense fog", "ensnaring vines", "fallen floor", "flooding", "freezing", "geysers", "magma", "magnetic field", "mud flow", "narrow ledge", "narrow passage", "poison goo", "poison plants", "precipice", "quicksand", "radiation", "rockslide", "rotten ceiling", "rotten floor", "sinkhole", "slippery slope", "spider webs", "spores", "steam vents", "strong winds", "tar pit", "tight passage", "toppling object", "toxic fumes"]
        self.trap_effects = ["acid pool", "adhesive", "alarm", "armor melts", "bear trap", "blinding spray", "blunt pendulum", "boiling tar", "collapsing floor", "crocodile pit", "crushing walls", "deep pit", "falling cage", "falling ceiling", "fills with sand", "flooding", "giant magnet", "hard vacuum", "lava flow", "lighting", "living statues", "missile fire", "net trap", "pendulum blade", "poison gas", "poison needle", "quicksand", "rage gas", "rolling boulder", "room freezes", "room on fire", "sleeping gas", "spike pit", "tombs open", "wall spikes"]
        self.trap_trigers = ["blow", "break", "burn", "choice", "countdown", "darkness", "drain", "eat", "insert", "kill", "knock", "light", "magic", "melody", "noise", "open", "phrase", "pour", "press", "proximity", "pull", "read", "reflect", "release", "remove", "retrieve", "rudeness", "shut", "sit", "sleep", "slide", "touch", "turn", "unbalance", "unearth", "write"]


    # Magic
    @property
    def elements(self):
        return self.physical_elements + self.ethereal_elements
    
    @property
    def effects(self):
        return self.physical_effects + self.ethereal_effects

    @property
    def mutations(self):
        
        __mutations = self._mutations.copy()
        __mutations.append(f"{random.choice(self.animals)} arms")
        __mutations.append(f"{random.choice(self.animals)} eyes")
        __mutations.append(f"{random.choice(self.animals)} head")
        __mutations.append(f"{random.choice(self.animals)} legs")
        __mutations.append(f"{random.choice(self.animals)} mouth")
        __mutations.append(f"{random.choice(self.animals)} skin")
        __mutations.append(f"{random.choice(self.items)}-form")
        __mutations.append(f"{random.choice(self.animals)} feature")
        __mutations.append(f"{random.choice(self.animals)} trait")
        __mutations.append(f"{random.choice(self.physical_elements)} skin")
        __mutations.append(f"{random.choice(self.animals)} form")
        return __mutations
    
    @property
    def insanities(self):
        
        __insanities = self._insanities.copy()
        __insanities.append(f"'{random.choice(self.animals)}-form'")
        __insanities.append(f"'{random.choice(self._monster_abilities)}'")
        __insanities.append(f"'{random.choice(self.monster_features)}'")
        __insanities.append(f"'{random.choice(self.monster_traits)}'")
        __insanities.append(f"{random.choice(self.character_creation_personalities)}")
        return __insanities
    
    def generate_spell(self, as_string=True):
        first_part = random.choice(self.physical_effects + self.ethereal_effects + self.physical_elements + self.ethereal_elements)
        second_part = random.choice(self.physical_forms + self.ethereal_forms + self.physical_elements + self.ethereal_elements)
        
        if as_string == False:
            return first_part, second_part
        else:
            return f"{first_part} {second_part}"

    # Monsters & Animals
    @property
    def monster_traits(self):
        __monster_traits = self._monster_traits.copy()
        __monster_traits.append(f"{random.choice(self.ethereal_elements)}")
        __monster_traits.append(f"{random.choice(self.physical_elements)}")
        return __monster_traits
    
    @property
    def monster_abilities(self):
        __monster_abilities = self._monster_abilities.copy()
        __monster_abilities.append(f"{random.choice(self.ethereal_effects)}")
        __monster_abilities.append(f"{random.choice(self.physical_effects)}")
        return __monster_abilities

    @property
    def monster_weaknesses(self):
        __monster_weaknesses = self._monster_weaknesses.copy()
        __monster_weaknesses.append(f"{random.choice(self.insanities)}")
        __monster_weaknesses.append(f"{random.choice(self.character_methods)}")
        __monster_weaknesses.append(f"{random.choice(self.physical_elements)}")
        __monster_weaknesses.append(f"{random.choice(self.valuable_materials)}")
        __monster_weaknesses.append(f"{random.choice(self.weapon_items)}")
        return __monster_weaknesses

    @property
    def animals(self):
        return self.aerial_animal_bases + self.terrestrial_animal_bases + self.aquatic_animal_bases


    # Characters
    @property
    def assets(self):
        __assets = self._assets.copy()
        __assets.append(f"{random.choice(self.factions)}-leader")
        __assets.append(f"{random.choice(self.factions)}-member")
        return __assets
    
    @property
    def liabilities(self):
        __liabilities = self._liabilities.copy()
        __liabilities.append(f"{random.choice(self.insanities)}")
        return __liabilities

    @property
    def npc_goals(self):
        __npc_goals = self._npc_goals.copy()
        __npc_goals.append(f"acquire {random.choice(self.items)}")
        __npc_goals.append(f"craft {random.choice(self.items)}")
        __npc_goals.append(f"destroy {random.choice(self.factions)}")
        __npc_goals.append(f"found {random.choice(self.factions)}")
        __npc_goals.append(f"impress {random.choice(self.npcs)}")
        __npc_goals.append(f"infiltrate {random.choice(self.factions)}")
        __npc_goals.append(f"kidnap {random.choice(self.npcs)}")
        __npc_goals.append(f"locate {random.choice(self.npcs)}")
        __npc_goals.append(f"rescue {random.choice(self.npcs)}")
        __npc_goals.append(f"restore {random.choice(self.factions)}")
        __npc_goals.append(f"sabatoge {random.choice(self.factions)}")
        __npc_goals.append(f"serve {random.choice(self.factions)}")
        return __npc_goals
    
    @property
    def character_secrets(self):
        __secrets = self._character_secrets.copy()
        __secrets.append(random.choice(self.npcs))
        __secrets.append(random.choice(self.misfortunes))
        return __secrets
    
    @property
    def divine_domains(self):
        __domains = self._divine_domains.copy()
        __domains.append(f"{random.choice(self.animals)}s")
        __domains.append(f"{random.choice(self.physical_elements + self.ethereal_elements)}")
        __domains.append(f"{random.choice(self.npcs)}s")
        return __domains

    @property
    def after_the_party(self):
        __after = self._characters_after_the_party.copy()
        __after.append(f"insulted {random.choice(self.factions)}")
        return __after

    @property
    def npcs(self):
        return self.civilized_npcs + self.underworld_npcs + self.wilderness_npcs


    # Treasure & Equipment
    @property
    def items(self):
        return self.miscellaneous_items + self.worn_items + self.weapon_items + self.tool_items + self.treasure_items
    
    @property
    def potions(self):
        __potions = self._potions.copy()
        __potions.append(f"{random.choice(self.animals)}-form")
        __potions.append(f"control {random.choice(self.elements)}")
        __potions.append(f"{random.choice(self.elements)}-form")
        __potions.append(f"{random.choice(self.elements)}-skin")
        __potions.append(f"{self.insanities}")
        __potions.append(f"{random.choice(self.items)}-form")
        __potions.append(random.choice(self.monster_abilities))
        __potions.append(random.choice(self.monster_features))
        __potions.append(random.choice(self.monster_traits))
        __potions.append(random.choice(self.mutations))
        __potions.append(f"{random.choice(self.generate_spell())}")
        return __potions
    
    @property
    def magical_ingredients(self):
        __ingredients = self._magical_ingredients.copy()
        __ingredients.append(random.choice(self.animals))
        __ingredients.append(f"{random.choice(self.book_subjects)} page")
        __ingredients.append(random.choice(self.edible_plants))
        __ingredients.append(random.choice(self.monster_features))
        __ingredients.append(random.choice(self.physical_effects))
        __ingredients.append(random.choice(self.poisonous_plants))
        __ingredients.append(random.choice(self.potions))
        __ingredients.append(random.choice(self.valuable_materials))
        return __ingredients

    @property
    def treasure_traits(self):
        __traits = self._treasure_traits.copy()
        __traits.append(random.choice(self.effects))
        __traits.append(random.choice(self.elements))
        return __traits



    # The City
    @property
    def city_themes(self):
        __themes = self._city_themes.copy()
        __themes.append(random.choice(self.animals))
        __themes.append(random.choice(self.city_activities))
        __themes.append(random.choice(self.city_events))
        __themes.append(random.choice(self.district_themes))
        __themes.append(random.choice(self.divine_domains))
        __themes.append(random.choice(self.factions))
        __themes.append(random.choice(self.lower_class_buildings))
        __themes.append(random.choice(self.npcs))
        __themes.append(random.choice(self.physical_elements))
        __themes.append(random.choice(self.upper_class_buildings))
        return __themes

    @property
    def city_events(self):
        __events = self._city_events.copy()
        __events.append(f"{random.choice(self.factions)} war")
        return __events
    
    @property
    def district_themes(self):
        __themes = self._district_themes.copy()
        __themes.append(f"{random.choice(self.civilized_npcs)}s")
        __themes.append(f"{random.choice(self.lower_class_buildings)}s")
        __themes.append(f"{random.choice(self.underworld_npcs)}s")
        __themes.append(f"{random.choice(self.upper_class_buildings)}s")
        __themes.append(f"{random.choice(self.wilderness_npcs)}s")
        return __themes

    @property
    def city_activities(self):
        __city_activites = self._city_activities.copy()
        __city_activites.append(random.choice(self._dungeon_activities))
        __city_activites.append(f"{random.choice(self.missions)}")
        __city_activites.append(random.choice(self.wilderness_activities))
        return __city_activites
    
    @property
    def building_rooms(self):
        __rooms = self._building_rooms.copy()
        # __rooms.append(random.choice(self.dungeon_rooms))
        return __rooms
    
    @property
    def tactical_street_features(self):
        __features = self._tactical_street_features.copy()
        __features.append(random.choice(self.city_activities))
        __features.append(random.choice(self.dungeon_activities))
        __features.append(random.choice(self.wilderness_activities))
        return __features
    
    @property
    def tactical_building_features(self):
        __features = self._tactical_building_features.copy()
        __features.append(f"{random.choice(self.animals)} nest")
        return __features
    
    @property
    def faction_goals(self):
        __goals = self._faction_goals.copy()
        __goals.append(f"control {random.choice(self.factions)}")
        # __goals.append(f"create {random.choice(self.generate_monster())}")
        __goals.append(f"create monster")
        __goals.append(f"defeat {random.choice(self.factions)}")
        __goals.append(f"infiltrate {random.choice(self.factions)}")
        return __goals

    # The Wild
    @property
    def wilderness_region_traits(self):
        __wilderness_region_traits = self._wilderness_region_traits.copy()
        __wilderness_region_traits.append(random.choice(self.dungeon_tricks))
        __wilderness_region_traits.append(random.choice(self.ethereal_effects))
        __wilderness_region_traits.append(random.choice(self.physical_effects))
        return __wilderness_region_traits
    
    @property
    def wilderness_discoveries(self):
        __wilderness_discoveries = self._wilderness_discoveries
        __wilderness_discoveries.append(random.choice(self.city_activities))
        __wilderness_discoveries.append(f"{random.choice(self.civilized_npcs)}")
        __wilderness_discoveries.append(random.choice(self.dungeon_activities))
        __wilderness_discoveries.append(random.choice(self.items))
        __wilderness_discoveries.append(f"lost {random.choice(self.npcs)}")
        __wilderness_discoveries.append(self.generate_spell())
        __wilderness_discoveries.append(random.choice(self.mutations))
        __wilderness_discoveries.append(f"stunned {random.choice(self.npcs)}")
        __wilderness_discoveries.append(f"{random.choice(self.wilderness_npcs)}")
        __wilderness_discoveries.append(random.choice(self.dungeon_activities))
        __wilderness_discoveries.append(random.choice(self.wilderness_landmarks))
        __wilderness_discoveries.append(random.choice(self.wilderness_npcs))
        return __wilderness_discoveries
    
    @property
    def wilderness_activities(self):
        __wilderness_activities = self._wilderness_activities.copy()
        # __wilderness_activities.append(self.city_activities)
        __wilderness_activities.append(self.dungeon_activities)
        return __wilderness_activities
    
    @property
    def inn_quirks(self):
        __quirks = self._inn_quirks.copy()
        __quirks.append(f"inn/{random.choice(self.lower_class_buildings + self.upper_class_buildings)}")
        __quirks.append(random.choice(self.city_activities))
        __quirks.append(f"{random.choice(self.npcs)} hangout")
        __quirks.append(random.choice(self.dungeon_forms))
        __quirks.append(f"{random.choice(self.factions)} hangout")
        __quirks.append(random.choice(self.faction_traits))
        return __quirks
    
    def generate_inn_name(self):
        if random.choice([True, False]):
            return f"the {random.choice(self.inn_nouns)} & {random.choice(self.inn_nouns)}".title()
        else:
            return f"the {random.choice(self.inn_adjectives)} {random.choice(self.inn_nouns)}".title()
    

    # The Maze
    @property
    def dungeon_forms(self):
        __dungeon_forms = self._dungeon_forms.copy()
        __dungeon_forms.append(random.choice(self._building_rooms))
        __dungeon_forms.append(random.choice(self.dungeon_rooms))
        __dungeon_forms.append(f"{random.choice(self.lower_class_buildings)}")
        __dungeon_forms.append(f"{random.choice(self.upper_class_buildings)}")
        return __dungeon_forms
    
    @property
    def dungeon_ruinations(self):
        __ruinations = self._dungeon_ruinations.copy()
        __ruinations.append(random.choice(self.insanities))
        __ruinations.append(random.choice(self.mutations))
        return __ruinations

    @property
    def dungeon_rewards(self):
        __rewards = self._dungeon_rewards.copy()
        __rewards.append(f"magic {random.choice(self.items)}")
        # __rewards.append(f"{self.generate_monster()} ally")
        __rewards.append(f"monster ally")
        __rewards.append(random.choice(self.treasure_items))
        __rewards.append(random.choice(self.valuable_materials))
        return __rewards

    @property
    def dungeon_activities(self):
        __dungeon_activities = self._dungeon_activities.copy()
        __dungeon_activities.append(random.choice(self._city_activities))
        __dungeon_activities.append(random.choice(self.monster_tactics))
        # __dungeon_activities.append(random.choice(self.wilderness_activities))
        return __dungeon_activities
    
    @property
    def dungeon_rooms(self):
        __rooms = self._dungeon_rooms.copy()
        __rooms.append(random.choice(self.building_rooms))
        __rooms.append(random.choice(self.lower_class_buildings))
        __rooms.append(random.choice(self.upper_class_buildings))
        return __rooms

    @property
    def dungeon_tricks(self):
        __dungeon_tricks = self._dungeon_tricks.copy()
        __dungeon_tricks.append(random.choice(self.ethereal_effects))
        __dungeon_tricks.append(random.choice(self.physical_effects))
        __dungeon_tricks.append(random.choice(self.missions))
        return __dungeon_tricks


    def pick_random_attribute(self):
        properties = [attr for attr in vars(self) if isinstance(getattr(self, attr), list)]
        chosen_property = random.choice(properties)
        chosen_value = random.choice(getattr(self, chosen_property))
        return chosen_value
