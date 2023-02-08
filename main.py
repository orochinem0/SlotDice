def cls():
    import os as _os
    _os.system('cls' if _os.name=='nt' else 'clear')

class Die:
    def __init__(self, sides=['1', '2', '3', '4', '5', '6']):
        self.sides = sides
        self.length = len(self.sides)

    def roll(self):
        import random as _random
        return self.sides[_random.randint(0, self.length-1)]

    def __str__(self):
        return self.roll()

class Slots:
    def __init__(self,drums):
        self.drums = drums

    def score(self):
        from collections import Counter as _Counter
        drumList = self.drums
        score = _Counter(drumList)

        extraBars = 0
        total = 0

        if score['Cherry'] == 2: # Cherry totals are 200 / 250 / 300
            total += 200
        if score['Cherry'] == 3:
            total += 250
        if score['Cherry'] == 4:
            total += 300

        if score['Orange'] == 2: # Orange totals are 100 / 250 / 500 / 2000
            total += 100
        if score['Orange'] == 3:
            total += 250
        if score['Orange'] == 4:
            total += 500
        if score['Orange'] == 5:
            total += 2000

        if score['Lemon'] == 2: # Lemon totals are 100 / 250 / 500 / 2000
            total += 100
        if score['Lemon'] == 3:
            total += 250
        if score['Lemon'] == 4:
            total += 500
        if score['Lemon'] == 5:
            total += 2000

        if score['1BAR'] == 2: # 1BAR totals are 100 / 250 / 1000
            total += 100
        if score['1BAR'] == 3:
            total += 250
        if score['1BAR'] == 4:
            total += 1000

        if score['2BAR'] == 2: # 2BAR totals are 150 / 300 / 1000
            total += 150
        if score['2BAR'] == 3:
            total += 300
        if score['2BAR'] == 4:
            total += 1000

        if score['3BAR'] == 2: # 3BAR totals are 200 / 350 / 1000
            total += 200
        if score['3BAR'] == 3:
            total += 350
        if score['3BAR'] == 4:
            total += 1000

        if (score['Cherry'] == 3 or score['Orange'] == 3 or score['Lemon'] == 3 or score['1BAR'] == 3 or score['2BAR'] == 3 or score['3BAR'] == 3):
            extraBars = score['1BAR'] + score['2BAR'] + score['3BAR']
        if (extraBars == 1): # 3 of a kind plus 1x BAR of any value is +50 points
            total += 50
        if (extraBars == 2): # 3 of a kind plus 2x BARs of any value are +100 points
            total += 100

        if score['Pass'] == 1: # move to next player
            pass
        if score['Pass'] == 2: # reverse order and move to next player
            pass

        if score['Lose'] == 1: # no score, move to next player
            pass
        if score['Lose'] == 2: # on rolling 2x Lose sides, score is reduced to zero
            total = 0

        return total

    def __str__(self):
        output = '| '
        output += ' | '.join(map(str, self.drums))
        output += ' |'
        return output

class Player:
    pass

# Clear console
cls()

# Build slot dice
p1 = Die(['1BAR','3BAR','Orange','2BAR','Lose',  'Lemon'])
p2 = Die(['1BAR','3BAR','Orange','2BAR','Cherry','Lemon'])
p3 = Die(['1BAR','3BAR','Orange','Lose','Cherry','Lemon'])
p4 = Die(['2BAR','3BAR','Orange','Pass','Cherry','Lemon'])
p5 = Die(['1BAR','2BAR','Orange','Pass','Cherry','Lemon'])

# Roll them bones or drums or whatever
machine = Slots([p1.roll(),p2.roll(),p3.roll(),p4.roll(),p5.roll()])

# Show the slot drums and the total score
print(machine)
print("Score: {}".format(machine.score()))