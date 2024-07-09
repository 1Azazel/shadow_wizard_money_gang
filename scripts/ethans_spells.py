import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN, K_RETURN
#THIS PROGRAM WILL TAKE A USER INPUTTED 3 DIGIT CODE, CHECKS IF IT IS VALID, AND THEN DISPLAYS THE CORRESPONDING SPELL NAME. PRESS ENTER OR LEFT CLICK TO SUBMIT THE CODE.
pygame.init()

# Spell class. Barebones, but it's a start. im assuming we will have me def for spells here
class Spell(object):
    def __init__(self, name, combo, distance):
        self.name = name
        self.combo = combo 
        self.distance = distance

# Creating spell objects for water spells
waterspell1 = Spell("water missile", 411, 20)
waterspell2 = Spell("water scythe", 412, 10)
waterspell3 = Spell("water illusion", 413, 20)
waterspell4 = Spell("wall of ice", 421, 10)
waterspell5 = Spell("whirlpool", 422, 20)
waterspell6 = Spell("lucky duck", 423, 10)
waterspell7 = Spell("water shield", 431, 20)
waterspell8 = Spell("air bubble", 432, 10)
waterspell9 = Spell("water regen", 433, 10)

# Creating spell objects for fire spells
firespell1 = Spell("fire missile", 511, 20)
firespell2 = Spell("fire scythe", 512, 10)
firespell3 = Spell("fire illusion", 513, 20)
firespell4 = Spell("wall of fire", 521, 10)
firespell5 = Spell("firepool", 522, 20)
firespell6 = Spell("fire duck", 523, 10)
firespell7 = Spell("fire shield", 531, 20)
firespell8 = Spell("fire bubble", 532, 10)
firespell9 = Spell("fire regen", 533, 10)

# Creating dictionaries for water and fire spells
water_spell_dict = {
    waterspell1.combo: waterspell1.name,
    waterspell2.combo: waterspell2.name,
    waterspell3.combo: waterspell3.name,
    waterspell4.combo: waterspell4.name,
    waterspell5.combo: waterspell5.name,
    waterspell6.combo: waterspell6.name,
    waterspell7.combo: waterspell7.name,
    waterspell8.combo: waterspell8.name,
    waterspell9.combo: waterspell9.name
}

fire_spell_dict = {
    firespell1.combo: firespell1.name,
    firespell2.combo: firespell2.name,
    firespell3.combo: firespell3.name,
    firespell4.combo: firespell4.name,
    firespell5.combo: firespell5.name,
    firespell6.combo: firespell6.name,
    firespell7.combo: firespell7.name,
    firespell8.combo: firespell8.name,
    firespell9.combo: firespell9.name
}

# Initialize Pygame display
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Spell Combo")

# Font for displaying text
font = pygame.font.Font(None, 74)

# List to store the spell combo
combo = []
# Variable to store the current spell. converts to int
def process_combo(combo):
    combo_number = int("".join(map(str, combo)))
#checks the first digit of the combo to look in the proper dictionary.
    first_digit = int(str(combo_number)[0])
    if first_digit == 4:
        #searches thru the dictionary and returns the spell name
        if combo_number in water_spell_dict:
            return water_spell_dict[combo_number]
        else:
            return "Error: No such water spell exists"
    elif first_digit == 5:
        if combo_number in fire_spell_dict:
            return fire_spell_dict[combo_number]
        else:
            return "Error: No such fire spell exists"
    else:
        return "Error: No such spell exists"

# Main loop to run the program
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                # When Enter is pressed, processes the combo
                if combo:
                    spell_name = process_combo(combo)
                    pygame.display.set_caption(spell_name)
                    #resets the combo list to 0 after each time here
                    combo = []
            elif event.unicode.isdigit():
                # Append the digit to the combo if a number is pressed
                combo.append(int(event.unicode))
                if len(combo) > 3:
                    combo.pop(0)
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # When left mouse button is clicked, process the combo. Another way vs enter
                if combo:
                    spell_name = process_combo(combo)
                    pygame.display.set_caption(spell_name)
                    combo = []

    # Clear the screen
    DISPLAYSURF.fill((0, 0, 0))

    # Render the combo on the screen
    combo_text = "".join(map(str, combo))
    text = font.render(combo_text, True, (255, 255, 255))
    text_rect = text.get_rect(center=(200, 150))
    DISPLAYSURF.blit(text, text_rect)

    pygame.display.update()
