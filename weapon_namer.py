import os
import random
from namegen import lc, new_word

#    singular    possesive     "of"...
targets = (
    ('ancient', 'ancient\'s', 'the ancients',),
    ('bandit',  'bandit\'s',  'the bandits',),
    ('beast',   'beast\'s',   'beasts',),
    ('chaos',   'chaos\'',    'chaos',),
    ('death',   'death\'s',   'death',),
    ('demon',   'demon\'s',   'demons',),
    ('dragon',  'dragon\'s',  'the dragon',),
    ('dream',   'dream\'s',   'dreams',),
    ('doom',    'doom\'s',    'doom',),
    ('dwarf',   'dwarves',    'the dwarves',),
    ('elf',     'elves',      'the elves',),
    ('fairy',   'fae\'s',     'the fae',),
    ('foe',     'foe\'s',     'the foe',),
    ('gnome',   'gnome\'s',   'the gnomes',),
    ('goblin',  'goblin\'s',  'the goblins',),
    ('god',     'god\'s',     'gods',),
    ('heart',   'heart\'s',   'hearts',),
    ('king',    'king\'s',    'kings',),
    ('law',     'law\'s',     'law',),
    ('mage',    'mage\'s',    'the mage',),
    ('mist',    'mist\'s',    'the mists',),
    ('night',   'night\'s',   'the night',),
    ('ogre',    'ogre\'s',    'the ogres',),
    ('orc',     'orc\'s',     'the orcs',),
    ('serpent', 'serpent\'s', 'the serpent',),
    ('soul',    'soul\'s',    'souls',),
    ('spirit',  'spirit\'s',  'spirits',),
    ('storm',   'storm\'s',   'the storm',),
    ('sun',     'sun\'s',     'the sun',),
    ('truth',   'truth\'s',   'truth',),
    ('thunder', 'thunder\'s', 'thunder',),
    ('world',   'world\'s',   'the world',),
    
)

titles = (
    '{0} breaker',
    '{0} crusher',
    '{0} cutter',
    '{0} edge',
    '{0} killer',
    '{0} knife',
    '{0} piercer',
    '{0} poker',
    '{0} reaper',
    '{0} slayer',
    '{0} smasher',
    '{0} splitter',
    '{0} stabber',
    '{1} bane',
    '{1} blade',
    '{1} end',
    '{1} glory',
    '{1} heart',
    '{1} knife',
    '{1} might',
    'bane of {2}',
    'blade of {2}',
    'breath of {2}',
    'defender of {2}',
    'glory of {2}',
    'hammer of {2}',
    'knife of {2}',
    'might of {2}',
    'spirit of {2}',
    'soul of {2}',
    'tear of {2}',
    'wind of {2}',
)

def generate_title():
    return random.choice(titles).format(*random.choice(targets))

def named_title():
    langfiles = os.listdir('name_files')
    (hash, start) = lc(os.path.join('name_files',random.choice(langfiles)))
    name1 = new_word(hash, start, 3, 5)
    name2 = new_word(hash, start, 6, 10)

    return ' '.join((name1, name2, 'the', generate_title()))
    
if __name__ == '__main__':
    print(named_title())
    #print (generate_title())
