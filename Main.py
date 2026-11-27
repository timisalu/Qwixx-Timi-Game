import random
from operator import truediv


class Spaces:
    def __init__(self, number, colour, occupied):
        self.number = number
        self.colour = colour
        self.occupied = occupied


red2 = Spaces(2, "red", "no")
red3 = Spaces(3,"red","no")
red4 = Spaces(4,"red","no")
red5 = Spaces(5,"red","no")
red6 = Spaces(6,"red","no")
red7 = Spaces(7,"red","no")
red8 = Spaces(8,"red","no")
red9 = Spaces(9,"red","no")
red10 = Spaces(10,"red","no")
red11= Spaces(11,"red","no")
red12= Spaces(12,"red","no")
redrow = [red2, red3, red4, red5, red6, red7, red8, red9, red10, red11, red12]
blue2 = Spaces(2, "blue", "no")
blue3 = Spaces(3,"blue","no")
blue4 = Spaces(4,"blue","no")
blue5 = Spaces(5,"blue","no")
blue6 = Spaces(6,"blue","no")
blue7 = Spaces(7,"blue","no")
blue8 = Spaces(8,"blue","no")
blue9 = Spaces(9,"blue","no")
blue10 = Spaces(10,"blue","no")
blue11= Spaces(11,"blue","no")
blue12= Spaces(12,"blue","no")
bluerow = [blue2, blue3, blue4, blue5, blue6, blue7, blue8, blue9, blue10, blue11, blue12]
yellow2 = Spaces(2, "yellow", "no")
yellow3 = Spaces(3, "yellow", "no")
yellow4 = Spaces(4, "yellow", "no")
yellow5 = Spaces(5, "yellow", "no")
yellow6 = Spaces(6, "yellow", "no")
yellow7 = Spaces(7, "yellow", "no")
yellow8 = Spaces(8, "yellow", "no")
yellow9 = Spaces(9, "yellow", "no")
yellow10 = Spaces(10, "yellow", "no")
yellow11= Spaces(11, "yellow", "no")
yellow12= Spaces(12, "yellow", "no")
yellowrow = [yellow2, yellow3, yellow4, yellow5, yellow6, yellow7, yellow8, yellow10, yellow11, yellow12]
green2 = Spaces(2, "green", "no")
green3 = Spaces(3, "green", "no")
green4 = Spaces(4, "green", "no")
green5 = Spaces(5, "green", "no")
green6 = Spaces(6, "green", "no")
green7 = Spaces(7, "green", "no")
green8 = Spaces(8, "green", "no")
green9 = Spaces(9, "green", "no")
green10 = Spaces(10, "green", "no")
green11 = Spaces(11, "green", "no")
green12= Spaces(12, "green", "no")
greenrow = [green2, green3, green4, green5, green6, green7, green8, green9, green10, green11, green12]

ruless = ("""QWIXX – HOW TO PLAY
Simple Game Instructions
1. OBJECTIVE

Get the highest score by crossing off numbers in the four coloured rows on your score sheet.

2. WHAT YOU NEED
2–5 players
2 white dice
1 red die
1 yellow die
1 green die
1 blue die

3. UNDERSTANDING THE SCORE SHEET

There are four coloured rows:

Red: Numbers go from 2 to 12.
Yellow: Numbers go from 2 to 12.
Green: Numbers go from 12 down to 2.
Blue: Numbers go from 12 down to 2.

Important: You must always cross off numbers from left to right. You can skip numbers, but you cannot go back and cross them off later.

4. HOW TO PLAY A TURN

The player whose turn it is rolls all six dice.

There are TWO steps:

STEP 1 – THE WHITE DICE

Add the two white dice together.

Example:

White die 1 = 3
White die 2 = 4
Total = 7

EVERY player may choose to cross off the number 7 in any one coloured row.

Players can also choose not to cross anything off.

STEP 2 – WHITE DIE + COLOURED DIE

The player who rolled may choose one white die and add it to one coloured die.

Example:

White die = 5
Red die = 2
Total = 7

The player who rolled may cross off 7 in the red row, provided it follows the left-to-right rule.

Remember: Only the player who rolled gets to use this second step.

5. PENALTY BOXES

If the player who rolled does not cross off ANY number during either step, they must mark one penalty box.

Each penalty costs 5 points at the end of the game.

Other players do not receive penalties for choosing not to cross off a number.

6. LOCKING A COLOURED ROW

To lock a row:

You must already have at least 5 numbers crossed off in that row.
You must cross off the final number in that row.
Cross off the lock symbol.

The final numbers are:

Red: 12
Yellow: 12
Green: 2
Blue: 2

Once a row is locked, nobody can cross off numbers in that colour anymore. Remove that coloured die from the game.

7. WHEN DOES THE GAME END?

The game ends when either:

Two coloured rows have been locked.
A player receives their fourth penalty.
8. HOW TO SCORE

Count the number of crosses in each coloured row.

Number of Crosses	Points
1	1
2	3
3	6
4	10
5	15
6	21
7	28
8	36
9	45
10	55
11	66
12	78

Subtract 5 points for every penalty.

The player with the highest total score wins!

9. QUICK EXAMPLE

The player rolls:

White dice: 3 and 4
Red die: 2

Step 1: Everyone can cross off 7 in any coloured row.

Step 2: The player who rolled can add 3 + 2 to make 5 and cross off 5 in the red row.

Then the next player takes their turn.

IMPORTANT RULES TO REMEMBER
Everyone gets to participate during the white-dice step.
Only the roller gets to participate during the second step.
Always cross off numbers from left to right.
Skipped numbers can never be crossed off later.
Four penalties end the game.     
Two locked rows end the game.

HAVE FUN AND GOOD LUCK!""")

yes_responses = {"yes", "y", "yeah", "yep", "yup", "sure", "ok","okay","ready","ya"}
no_responses = {"no", "na", "n"}
person_yes = {"person", "people"}
ai_response = {"ai", "bot" }
answer = input("Ready to play Qwixx: Yes or No").strip().lower()
game_running = True

while game_running:

def print_board():
    print("\nred   │ " + str(red2.number) + " │ " + str(red3.number) + " │ " + str(red4.number) +" │ " + str(red5.number) +" │ " + str(red6.number) +" │ " + str(red7.number) + " │ " + str(red8.number) + " │ " + str(red9.number) + " │ " + str(red10.number) +" │ " + str(red11.number) + " │ " + str(red12.number) + " 🔒│" )
    print("yellow│ " + str(yellow2.number) + " │ " + str(yellow3.number) + " │ "  + str(yellow4.number) + " │ " + str(yellow5.number) + " │ " + str(yellow6.number) + " │ " + str(yellow7.number) + " │ " + str(yellow8.number) + " │ " + str(yellow9.number) + " │ " + str(yellow10.number) + " │ " + str(yellow11.number) + " │ " + str(yellow12.number) + " 🔒│ ")
    print("blue  │ " + str(blue12.number) + "│ " + str(blue11.number) + "│ " + str(blue10.number) + "│ " + str(blue9.number) + " │ " + str(blue8.number) + " │ " + str(blue7.number) + " │ " + str(blue6.number) + " │ " + str(blue5.number) + " │ " + str(blue4.number) + "  │ " + str(blue3.number) + "  │ " + str(blue2.number) + "  🔒│ ")
    print("green │ " + str(green12.number) + "│ " + str(green11.number) + "│ " + str(green10.number) + "│ " + str(green9.number) + " │ " + str(green8.number) + " │ " + str(green7.number) + " │ " + str(green6.number) + " │ " + str(green5.number) + " │ " + str(green4.number) + "  │ " + str(green3.number) + "  │ " + str(green2.number) + "  🔒│ ")
if answer in yes_responses:
    rules = input("Do you want the rules")
    if rules in yes_responses:
        print(ruless)
    start = input("Start Game: Yes or No")
    if start in  yes_responses:
        print_board()
        white_1 = random.randint(1,6)
        white_2 = random.randint(1,6)
        red = random.randint(1,6)
        yellow = random.randint(1,6)
        blue = random.randint(1,6)
        green = random.randint(1,6)
        whitetogther = white_1 + white_2
        print("White rolled: " + str(whitetogther))
        whichrow = input("Which row do you want? Please input as row,number")
        redcross = 0
        if whichrow == "red,2":
            red2.number = "❌"
            red2.occupied = "yes"
            print_board()
        elif whichrow == "red,3":
            red3.number = "❌"
            red3.occupied = "yes"
            print_board()
        elif whichrow == "red,4":
            red4.number = "❌"
            red4.occupied = "yes"
            print_board()
        elif whichrow == "red,5":
            red5.number = "❌"
            print_board()
            red5.occupied = "yes"
        elif whichrow == "red,6":
            red6.number = "❌"
            red6.occupied = "yes"
            print_board()
        elif whichrow == "red,7":
            red7.number = "❌"
            red7.occupied = "yes"
            print_board()
        elif whichrow == "red,8":
            red8.number = "❌"
            red8.occupied = "yes"
            print_board()
        elif whichrow == "red,9":
            red9.number = "❌"
            red9.occupied = "yes"
            print_board()
        elif whichrow == "red,10":
            red10.number = "❌"
            red10.occupied = "yes"
            print_board()
        elif whichrow == "red,11":
            red11.number = "❌"
            red11.occupied = "yes"
            print_board()
        for space in redrow:
            if space.occupied == "yes":
                redcross += 1
        if redcross == 5 and whitetogther == 12:
            for space in redrow:
                space.number = "❌"
                space.occupied = "yes"
        Rolldie = input("Do you want to roll a die")
        if Rolldie in yes_responses:
            which = input("Which die do you want to roll?").strip().lower()
            if which == "red":
                print("Red rolled: " + str(red))
            if which == "yellow":
                print("Yellow rolled: " + str(yellow))
            if which == "blue":
                print("Blue rolled: " + str(blue))
            if which == "green":
                print("Green rolled: " + str(green))
    if start in no_responses:
        print("Ok. see you soon")
if answer in no_responses:
    print("OK. See you next time")
#while answer not in no_responses or yes_responses:
    #print("Please enter an actual answer please")
    # Make this loop to the start game after this is show

