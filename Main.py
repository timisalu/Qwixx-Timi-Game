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
One score sheet and pencil per player
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

import climage

# is_unicode=True gives higher resolution blocks; is_truecolor=True enables full RGB colors
#output = climage.convert(r"C:\Users\timisalu\Downloads\qUIXX.jpg", is_unicode=True, width=180)
#print(output)
yes_responses = {"yes", "y", "yeah", "yep", "yup", "sure", "ok","okay","ready","ya"}
no_responses = {"no", "na", "n"}
person_yes = {"person", "people"}
ai_response = {"ai", "bot" }
answer = input("Ready to play Qwixx: Yes or No").strip().lower()
person_yes = {"person", "people", ""}
if answer in yes_responses:
    rules = input("Do you want the rules")
    if rules in yes_responses:
        print(ruless)
    start = input("Start Game: Yes or No")
    if start in  yes_responses:
        person_ai = input("Do you want to play with AI or with people").strip().lower()
        if person_ai in "ai":
            print(""" 
                        red │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 10 │ 11 │ 12 🔒 │
                     yellow │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 10 │ 11 │ 12 🔒 │
                       blue │ 12│ 11│ 10│ 9 │ 8 │ 7 │ 6 │ 5 │ 4  │ 3  │ 2  🔒 │
                      green │ 12│ 11│ 10│ 9 │ 8 │ 7 │ 6 │ 5 │ 4  │ 3  │ 2  🔒 │""")
        if person_ai in person_yes:
            print(""" 
            red │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 10 │ 11 │ 12 🔒 │
         yellow │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 10 │ 11 │ 12 🔒 │
           blue │ 12│ 11│ 10│ 9 │ 8 │ 7 │ 6 │ 5 │ 4  │ 3  │ 2  🔒 │
          green │ 12│ 11│ 10│ 9 │ 8 │ 7 │ 6 │ 5 │ 4  │ 3  │ 2  🔒 │""")
            #replace code above t
            roll = input("")
    if start in no_responses:
        print("Ok. see you soon")
if answer in no_responses:
    print("OK. See you next time")
#while answer not in no_responses or yes_responses:
    #print("Please enter an actual answer please")
    # Make this loop to the start game after this is show

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
yellow2 = Spaces(2, "yellow", "no")
yellow3 = Spaces(2, "yellow", "no")
yellow4 = Spaces(2, "yellow", "no")
yellow5 = Spaces(2, "yellow", "no")
yellow6 = Spaces(2, "yellow", "no")
yellow7 = Spaces(2, "yellow", "no")
yellow8 = Spaces(2, "yellow", "no")
yellow9 = Spaces(2, "yellow", "no")
yellow10 = Spaces(2, "yellow", "no")
yellow11= Spaces(2, "yellow", "no")
yellow12= Spaces(2, "yellow", "no")
green2 = Spaces(2, "green", "no")
green2 = Spaces(2, "green", "no")
green3 = Spaces(2, "green", "no")
green4 = Spaces(2, "green", "no")
green5 = Spaces(2, "green", "no")
green6 = Spaces(2, "green", "no")
green7 = Spaces(2, "green", "no")
green8 = Spaces(2, "green", "no")
green9 = Spaces(2, "green", "no")
green10 = Spaces(2, "green", "no")
green11= Spaces(2, "green", "no")
green12= Spaces(2, "green", "no")






