# implementation of card game - Memory

import simplegui
import random

exposed = [False]*16

# helper function to initialize globals
def new_game():
    global card_list,exposed, state, counter
    l1 = [0, 1, 2, 3, 4, 5, 6, 7]
    card_list = l1+l1
    random.shuffle(card_list)
    exposed = [False]*16
    state = 0
    counter = 0
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global counter,first_card, second_card, state, first_card_number, second_card_number
    if state == 0:
        for i in range(0,16):
            if pos[0] >= (50*i) and pos[0] <= (50*i+50) and exposed[i] == False:
                first_card = card_list[i]
                first_card_number = i
                exposed[i] = True
                state = 1
                return
            
    elif state == 1:
        for i in range(0,16):
            if pos[0] >= (50*i) and pos[0] <= (50*i+50) and exposed[i] == False:
                second_card = card_list[i]
                second_card_number = i
                exposed[i] = True
                state = 2
                counter += 1
                return
            
    elif state == 2:
        for i in range(0,16):
            if pos[0] >= (50*i) and pos[0] <= (50*i+50) and exposed[i] == False:
                if first_card != second_card:
                    exposed[first_card_number] = False
                    exposed[second_card_number] = False
                first_card = card_list[i]
                first_card_number = i
                exposed[i] = True
                state = 1
                return  
      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = " + str(counter))
    for i in range(0,16):
        if exposed[i] == True:
            canvas.draw_line((50*i+25, 0), (50*i+25, 100), 48, 'White')
            canvas.draw_text(str(card_list[i]), (50*i+15, 60) , 36, 'Black')
        else:
            canvas.draw_line((50*i+25, 0), (50*i+25, 100), 48, 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
