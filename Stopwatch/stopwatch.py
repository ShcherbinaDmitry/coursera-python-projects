# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
win_counter = 0
game_counter = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = 0
    tens_of_seconds = 0
    seconds = 0
    while t//600 > 0:
        minutes += 1
        t -= 600
    while t//100 > 0:
        tens_of_seconds += 1
        t -= 100
    while t//10 >0:
        seconds += 1
        t -= 10
    return str(minutes)+ ':' + str(tens_of_seconds) + str(seconds) + ':' +str(t)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()

def Stop():
    global game_counter, counter, win_counter
    if timer.is_running():
        game_counter += 1
        if str(counter)[-1] == '0':
            win_counter += 1
    timer.stop()
       
def Reset():
    global counter, game_counter, win_counter
    counter = 0
    game_counter = 0
    win_counter = 0
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter),(70,100),25, 'Red')
    canvas.draw_text(str(win_counter) + '/' + str(game_counter),(160,20),25, 'Red')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 200, 200)

                        
# register event handlers
timer = simplegui.create_timer(100, tick)
start = frame.add_button('Start', Start)
stop = frame.add_button('Stop', Stop)
reset = frame.add_button('Reset', Reset)
frame.set_draw_handler(draw_handler)
# start frame
frame.start()
