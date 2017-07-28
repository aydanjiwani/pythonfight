
import random

class Unit:
    def __init__(self, n, hp, s, d, a, s1, s2, s3, s4, d1, d2, d3, d4, h, sc, sr):
        self.name = n
        self.maxHP = hp
        self.curHP = hp
        self.strength = s
        self.defence = d
        self.agility = a
        self.strength1 = s1
        self.strength2 = s2
        self.strength3 = s3
        self.strength4 = s4
        self.defence1 = d1
        self.defence2 = d2
        self.defence3 = d3
        self.defence4 = d4
        self.hero = h
        self.statchance = sc
        self.statresist = sr

def battle( a, b ):
    turn = 1

    if a.agility > b.agility:
        attacker = a
        defender = b
    else:
        attacker = b
        defender = a

    doBattle = True
    while (doBattle):
        print "\n ---  Turn " , turn , ": " , attacker.name , " ---"
        print attacker.name , ": " , attacker.curHP
        print defender.name , ": " , defender.curHP , "\n"

        if defender.agility > attacker.agility and random.randint(1,4) == 4:
            print attacker.name , " missed."
        else:

            if attacker.hero == 1:
                movechoice = raw_input("Pick a move 1-4 ")
            else:
                movechoice = str (random.randint(1,4))
            if movechoice == "1":
                attacker.strength += attacker.strength1
                defender.defence += defender.defence1
            if movechoice == "2":
                attacker.strength += attacker.strength2
                defender.defence += defender.defence2
            if movechoice == "3":
                attacker.strength += attacker.strength3
                defender.defence += defender.defence3
            if movechoice == "4":
                attacker.strength += attacker.strength4
                defender.defence += defender.defence4

            stathit = attacker.statchance - defender.statresist
            if stathit >= 50:
                print "same"
                if movechoice == "1":
                    attacker.strength += 2
                    print "bonus damage"
                if movechoice == "2":
                    print "attempting crit"
                    if random.randint(1,2) == 2:
                        attacker.strength *= 2
                        print "CRIT!"
                if movechoice == "3":
                    attacker.statchance += 5
                    print "statchance increased to", attacker.statchance

                if movechoice == "4":
                    print "armor pen"
                    defender.defence = 0


            attackDamage = attacker.strength - defender.defence
            if attackDamage < 0:
                attackDamage = 0
            defender.curHP -= attackDamage

            print attacker.name , " did " , attackDamage , " damage to " , defender.name , "using move", movechoice, "."



        if defender.curHP <= 0:
            doBattle = False
            print "\n\n" , attacker.name , " won the battle!"
        else:
            temp = defender
            defender = attacker
            attacker = temp
            turn = turn + 1


name = raw_input("What is your name?\nName: ")

character = Unit(name, random.randint(10,30), random.randint(2,5), random.randint(1,3), random.randint(1,5), 1,1,1,1,1,1,1,1,1,100,100)
while raw_input("Fight? [y/n]: ") == "y":
    character.curHP = character.maxHP
    enemy = Unit("Monster", random.randint(10,30), random.randint(2,5), random.randint(1,3), random.randint(1,5) , 1,1,1,1,1,1,1,1,0,0,0)
    battle( character, enemy )
