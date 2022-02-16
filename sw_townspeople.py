import random

tool = (
    'axe',
    'flail',
    'pitchfork',
    'rake',
    'scythe',
    'shears',
    'sickle',
    'spade',
    'chisel',
    'hammer',
    'rope and tackle',
    'auger',
    'saw',
    'knife'
)

stuff = (
    'A folded piece of leather containing several pieces of blank parchment',
    'A diary/journal',
    'A bag of various pretty stones and small coins',
    'A key',
    'A half eaten piece of cheese',
    'A silver ring',
    'A fishing hook',
    'A love poem',
    'A brass signet ring',
    'A sea shell',
    'A small piece of parchment',
    'A small bone knife carved with runes',
    'A palm-sized brass coin from a distant Fire Giant city',
    'A paper napkin with a few stanzas of poetry or a partial diagram of a machine scrawled on it',
    'A piece of chalk',
    'A small crystal',
    'A deck of cards',
    'A leather bag full of seeds',
    'A roughly scribbled map on a piece of parchment folded up three times',
    'A feather',
    'An old love letter neatly but repeated folded and worn from age',
    'A simple pen knife',
    'A poorly made rope doll with button eyes and frayed yellow cloth for hair',
    'A tiny nugget of fool\'s gold',
    'A tinder box',
    'A handkerchief',
    'A bottle cork with a small blue star inked on the bottom',
    'A wrapped sandwich',
    'A lovenote',
    'A half eaten ham sandwich',
    'The perfect skipping stone',
    'A small pouch of nuts and dried meats',
    'A charm of antlers',
    'A small wooden figurine carved into the shape of an owlbear',
    'A small brass bell',
    'A brooch',
    'A game piece',
    'A nice shell comb',
    'An oil lamp',
    'A sewing needle and thread',
    'A tobacco pipe',
    'A wooden flute',
    'A small steel mirror',
    'A pouch of marbles',
    'A tin of sulfur',
    'A tuning fork',
    'A small first aid kit',
    'A ball of twine',
    'A small metal flask',
    'Flint and Steel',
    'A copper ring etched with runes',
    'A quartz crystal'    
)

produce = (
    'potato', 
    'wheat', 
    'turnip', 
    'corn', 
    'rice', 
    'parsnip', 
    'radish', 
    'rutabaga' 
)

animal = (
    'chicken',
    'cow',
    'dog',
    'duck',
    'goat',
    'goose',
    'mule',
    'ox',
    'pony',
    'pig',
    'sheep',
)

jobs = [
    ('Alchemist', 'Staff', 'Oil - 1 flask', 'Arcana'),
    ('Animal trainer', tool, animal, 'Animal Handling'),
    ('Apprentice', tool, stuff, 'Athletics'),
    ('Armorer', 'Hammer', 'Iron helmet', 'Athletics'),
    ('Artisan', 'Staff', 'Clay', 'Perception'),
    ('Astrologer', 'Dagger', 'Spyglass', 'Nature'),
    ('Barber', 'straight razor', 'Bandages', 'Medicine'),
    ('Barkeep', tool, 'bottle of spirits', 'Insight'),
    ('Blacksmith', 'Hammer', 'Steel tongs', 'Athletics'),
    ('Bowyer', 'Longbow', '20 arrows', 'Perception'),
    ('Caravan guard', 'Short sword', 'padded armor', 'Survival'), 
    ('Carpenter', 'Hammer', 'Nails', 'Perception'),
    ('Cobbler', 'Awl', 'Shoehorn', 'Perception'),
    ('Confidence artist', 'Dagger', 'Quality cloak', 'Deception'),
    ('Cook', 'Meat Cleaver', 'Fresh meat', 'Survival'),
    ('Cooper', 'Crowbar', 'Barrel', 'Perception'),
    ('Cutpurse', 'Dagger', stuff, 'Sleight of Hand'),
    ('Ditch digger', 'Shovel', stuff, 'Athletics'),
    ('Drifter', 'Sling', stuff, 'Investigation'),
    ('Farmer', tool,  animal, 'Animal Handling'),
    ('Farrier', 'hammer', 'pliers', 'Animal Handling'),
    ('Forester', 'Staff', 'Herbs', 'Nature'),
    ('Fortune-teller', 'Dagger', 'Tarot deck', 'Performance'),
    ('Gambler', 'Sap', 'Dice', 'Sleight of Hand'),
    ('Gongfarmer', tool, 'Sack of night soil', 'Athletics'),
    ('Grave digger', 'Shovel', stuff, 'Athletics'),
    ('Groom', 'whip', 'saddle horse', 'Animal Handling'),
    ('Guard', 'Spear', 'Shield', 'Intimidation'),
    ('Guild beggar', 'Sling', 'Crutches', 'Deception'),
    ('Healer', 'Club', 'Vial Holy water', 'Medicine'),
    ('Hedge Witch', 'knife', 'healing herbs', 'Nature'),
    ('Herbalist', tool, 'Herbs', 'Nature'),
    ('Herder', 'Staff', 'Herding dog', 'Animal Handling'),
    ('Hunter', 'Shortbow', 'Deer pelt', 'Stealth'),
    ('Indentured servant', 'Staff', stuff, 'Athletics'),
    ('Innkeeper', 'club', stuff, 'Insight'),
    ('Jester', 'Darts', 'Silk clothes', 'Performance'),
    ('Jeweler', 'Fine Dagger', 'Gem worth 20 gp', 'Perception'),
    ('Locksmith', 'Dagger', 'Fine tools', 'Perception'),
    ('Mason', tool, stuff, 'Athletics'),
    ('Mayor', 'Mace', stuff, 'Persuasion'),
    ('Mercenary', 'Longsword', 'Hide armor', 'Survival'),
    ('Merchant', 'Dagger', stuff, 'Persuasion'),
    ('Miller/baker', 'Club (Rolling pin)', 'Flour - 1 lb', 'Athletics'),
    ('Miner', 'Pick', 'Lantern', 'Athletics'),
    ('Minstrel', 'Dagger', 'Lyre', 'Performance'),
    ('Noble', 'Longsword', 'Gold signet ring', 'History'),
    ('Orphan', 'Club', 'Rag doll', 'Stealth'),
    ('Outlaw', 'Short sword', 'leather tunic', 'Deception'),
    ('Rat Catcher', 'Club', 'Small dog', 'Animal Handling'),
    ('Sage', 'Dagger', 'Notebook and pencils', 'History'),
    ('Scribe', 'Darts', 'Parchment, quill pen and ink', 'Investigation'),
    ('Shaman', tool, 'Herbs', 'Religion'),
    ('Smuggler', 'Sling', 'Waterproof sack', 'Stealth'),
    ('Squire', 'Longsword', 'Steel helmet', 'Athletics'),
    ('Tanner', 'knife', 'waterproof bag', 'Athletics'),
    ('Trader', 'Short sword', '20 sp', 'Persuasion'),
    ('Trapper', 'Sling', 'Badger pelt', 'Survival'),
    ('Urchin', 'Stick', 'Begging bowl', 'Stealth'),
    ('Vagrant', 'Club', 'Begging bowl', 'Deception'),
    ('Wainwright', tool, 'Pushcart', 'Athletics'),
    ('Weaver', 'Dagger', 'Fine suit of clothes', 'Perception'),
    ('Wizard’s apprentice', 'Dagger', 'spellbook', 'Arcana'),
    ('Woodcutter', 'Axe', 'Bundle of wood', 'Athletics')
]

skills = (
    'Athletics',
    'Acrobatics',
    'Sleight of Hand',
    'Stealth',
    'Arcana',
    'History',
    'Investigation',
    'Nature',
    'Religion',
    'Animal Handling',
    'Insight',
    'Medicine',
    'Perception',
    'Survival',
    'Deception',
    'Intimidation',
    'Performance',
    'Persuasion'
)

skill_ability = {
    'Athletics': 'str',
    'Acrobatics': 'dex',
    'Sleight of Hand': 'dex',
    'Stealth': 'dex',
    'Arcana' : 'int',
    'History' : 'int',
    'Investigation' : 'int',
    'Nature' : 'int',
    'Religion' : 'int',
    'Animal Handling' : 'wis',
    'Insight' : 'wis',
    'Medicine' : 'wis',
    'Perception' : 'wis',
    'Survival' : 'wis',
    'Deception' : 'cha',
    'Intimidation' : 'cha',
    'Performance' : 'cha',
    'Persuasion' : 'cha',
}

race = (
    'Dragonborn',
    'Dwarf',
    'Elf',
    'Gnome',
    'Half-Elf',
    'Half-Orc',
    'Halfling',
    'Human',
    'Tiefling',
)

def as_thing(wep):
    import re
    return re.findall('\(as (\w+)\)', wep)[0]
    
def statblock():
    labels = ('str', 'dex', 'con', 'int', 'wis', 'cha')
    vals = [round(random.gammavariate(9, .3))+6 for x in range(6)]
    return dict(zip(labels, vals))

proficiency_bonus = 1
score_mod = lambda x: x//2 - 5
# don't forget '{0:+}'.format(value) to get leading +

def character():
    char = {}
    char['abilities'] = statblock()
    (job, weapon, gear, prof) = random.choice(jobs)

    if isinstance(weapon, tuple):
        weapon = random.choice(weapon)
    
    if isinstance(gear, tuple):
        gear = random.choice(gear)

    char['race'] = random.choice(race)
    char['job'] = job
    char['weapon'] = weapon
    char['gear'] = f'{gear}, {random.choice(stuff)}'
    
    char['skills'] = {}
    for skill in skill_ability.keys():
        val = score_mod(char['abilities'][skill_ability[skill]])
        if skill == prof:
            val += proficiency_bonus
        char['skills'][skill] = f'{val:+}{"*" if skill == prof else ""}'

    return char


if __name__ == '__main__':
    print(character())
