from random import randrange

failNum = 4
skill = 4


def dieMaker(sides):
    """return a die roller function"""
    def die():
        return randrange(1, sides+1)
    return die


def roll(numDice, die):
    """
    Run game mechanic roll.

    Roll a number of dice then check to see if any are
    below the suceess threshold. The Skill value allows
    a number of dice equal ot below the Skill to be re-rolled.
    """
    rolls = [die() for x in range(numDice)]
    fails = [x for x in rolls if x <= failNum]
    if (len(fails) > skill):
        return False
    rerolls = [die() for x in fails]
    fails = [x for x in rerolls if x <= failNum]
    return len(fails) == 0


def test(min, max, die, trials=100):
    """
    Run trials for different pool sizes, since I suck at prob-stat.
    """
    results = dict()
    for pool in range(min, max):
        results[pool] = dict()
        for trial in range(trials):
            res = roll(pool, die)
            results[pool][res] = results[pool].get(res, 0) + 1
    return results


if __name__ == '__main__':
    n = 10000
    trials = test(1, 13, dieMaker(12), n)
    prob_success = [float(x[True])/n for x in trials.values()]
    print('d12:')
    print([x for x in enumerate(prob_success, 1)])

    trials = test(1, 13, dieMaker(10), n)
    prob_success = [float(x[True])/n for x in trials.values()]
    print('d10:')
    print([x for x in enumerate(prob_success, 1)])
