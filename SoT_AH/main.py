from datetime import date, datetime
from multiprocessing.sharedctypes import Value
from pickle import FALSE, TRUE
from sqlite3 import Time
from ssl import SSLSession
from Ship_Inputs.sloop_input import *
from Ship_Inputs.brig_input import *
from Ship_Inputs.galleon_input import *
from pynput.keyboard import Key, Controller
from pyglet.text import Label
from pyglet.gl import Config
from helpers import SOT_WINDOW, SOT_WINDOW_H, SOT_WINDOW_W, main_batch, \
version, logger
from sot_hack import SoTMemoryReader
import logging
import threading
import time
import datetime
import json
import base64
import pyglet

# numHops definition
global numberofHops
numberofHops = 0

# runOnce for pyglet.clock interval
global runOnce
runOnce = True



# Define shipType as a global variable and takes input for the type of ship you are hopping with
global shipType
print("\nWhat ship would you like to hop with: ")
shipType = input("\n(1) Sloop\n(2) Brig\n(3) Galleon\n\n")



# See explanation in Main, toggle for a non-graphical debug
DEBUG = False

# Pyglet clock used to track time via FPS
clock = pyglet.clock.Clock()

# Controller for input macro
keyboard = Controller()


# Macro for joining a game on a sloop
def sloopInput(self):
    
    #on_draw()
    
    global smr
    global SoTMemoryReader
    global numberofHops
    
    coords = smr.my_coords
    #parser = json.loads(coords)
    print("My Cooardinate X =" + str(coords["x"]))
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": Starting Sloop Hop: 0%" + " complete")
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ":  Number of hops 🐇 : " + str(numberofHops)) 
    
    #print(smr.my_coords)
    
    print(smr.my_coords)
    
    time.sleep(10)
    time.sleep(10)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    #SoTMemoryReader()
    
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": 25%" + " complete")
    
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    #MENU LEFT. WAITING FOR LOADING SCREEN TO MAIN MENU

    
    time.sleep(11)
    #smr = SoTMemoryReader()
    #print(smr.my_coords)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    #LOADING INTO FIRST OPTION SCREEN. 25s FOR UNEXPECTED DELAY
    
    time.sleep(25)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": 50%" + " complete")
    
    #print(smr.my_coords)
    #if smr.server_players == 0: 
        #print("not in a game")
    
    #SoTMemoryReader()
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)

    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.12)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.12)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)

    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": 75%" + " complete")
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(45)
    
    #SoTMemoryReader()
    #print(smr.my_coords)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": Hop 100%" + " completed ✔️ . Reading players:\n")
    numberofHops += 1

 
# Macro for joining a game on a brig
def brigInput(self):
    global numberofHops
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": Starting Brig Hop: 0%" + " complete")
      
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": Number of hops 🐇 : " + str(numberofHops)) 
    
    time.sleep(10)
    time.sleep(10)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    #Down Arrow
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": 25%" + " complete")
    
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
        
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)

    #Enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(11)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(25)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": 50%" + " complete")
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)

    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.12)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.12)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)

    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": 75%" + " complete")
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(45)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": Hop 100%" + " completed ✔️ . Reading players:\n")
    numberofHops += 1


# Macro for joining a game on a galleon
def galleonInput(self):
    
    global numberofHops
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": Starting Galleon Hop: 0%" + " complete")
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": Number of hops 🐇 : " + str(numberofHops)) 
    
    time.sleep(10)
    time.sleep(10)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    #Down Arrow
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": 25%" + " complete")
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    #Enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(11)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(25)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": 50%" + " complete")
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)

    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.12)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.12)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": 75%" + " complete")
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(45)
    
    now = datetime.datetime.now()
    print(now.strftime("\n%H:%M:%S") + ": Hop 100%" + " completed ✔️ . Reading players:\n")
    numberofHops += 1

# Loading graphics and updating them
def update_all(_):
    """
    Triggers an entire read_actors call in our SoT Memory Reader. Will
    re-populate all of the display objects if something entered the screen
    or render distance.
    """
    smr.read_actors()
   


def load_graphics(_):
    """
    Our main graphical loop which updates all of our "interesting" items.
    During a "full run" (update_all()), a list of the objects near us and we
    care about is generated. Each of those objects has a ".update()" method
    we use to re-poll data for that item (required per display_object.py)
    """
    # Update our players coordinate information
    smr.update_my_coords()

    # Initialize a list of items which are no longer valid in this loop
    to_remove = []

    # For each actor that is stored from the most recent run of read_actors
    for actor in smr.display_objects:
        # Call the update function within the actor object
        actor.update(smr.my_coords)

        # If the actor isn't the actor we expect (per .update), prepare to nuke
        if actor.to_delete:
            to_remove.append(actor)

    # Clean up any items which arent valid anymore
    for removable in to_remove:
        smr.display_objects.remove(removable)


if __name__ == '__main__':
    
    
    logger.info(base64.b64decode("RG91Z1RoZURydWlkJ3MgRVNQIEZyYW1ld29yayBTdGFydGluZw==").decode("utf-8"))
    logger.info(f"Hack Version: {version}")
    
    # Initialize our SoT Hack object, and do a first run of reading actors
    smr = SoTMemoryReader()
    smr.read_actors()

        # Custom Debug mode for using a literal python interpreter debugger
        # to validate our fields. Does not generate a GUI.
    if DEBUG:
        while FALSE:
            smr.read_actors()


    config = Config(double_buffer=True, depth_size=24, alpha_size=8)

    # Create an overlay window with Pyglet at the same size as our SoT Window
    window = pyglet.window.Window(SOT_WINDOW_W, SOT_WINDOW_H,
                                vsync=False, style='overlay', config=config,
                                caption="Autohopper")
    window.set_caption('AutoHopper')
    hwnd = window._hwnd  # pylint: disable=protected-access

    # Move our window to the same location that our SoT Window is at
    window.set_location(SOT_WINDOW[0], SOT_WINDOW[1])
    
    
    # Main Loop for reading the players in a server and checking that to our findingplayers.json file as well as drawing to the screen
    @window.event
    def on_draw():
        """
        The event which our window uses to determine what to draw on the
        screen. First clears the screen, then updates our player count, then
        draws both our batch (think of a canvas) & fps display
        """
        window.clear()

        #Update our player count Label & player list
            
        smr = SoTMemoryReader()
        
        # Reading the actors and number of actors
        smr.read_actors()
        player_count.text = f"Player Count: {len(smr.server_players)}"
        player_list.text = "\n".join(smr.server_players)
        
        # {DEBUG} :: print(smr)
        
        # Draw our main batch & FPS counter at the bottom left
        main_batch.draw()
        fps_display.draw()

        # Performs a json.dump to our serverplayers.json that will be checked against our findingplayers.json
        
        # {DEBUG :: Grabs server players and puts them in a json file for debug purposes
        #out_file = open("serverplayers.json", "w") 
        #json.dump(player_list.text, out_file, indent = 4, sort_keys = False) 
        #out_file.close()

        
        # Finding players in game and matching too the server players
        f = open('findingplayers.json')
        data = f.read()
        f.close()
        for x in smr.server_players:
            print("Name = " + x)
            if data.find(x)>0 :
                now = datetime.datetime.now()
                print(now.strftime("%H:%M:%S") + ": Found Player: " + x)
                #Exits program if it finds a player
                quit()
            #{DEBUG} :: Print statement debug
            #else :
                #now = datetime.datetime.now()
                #print(now.strftime("%H:%M:%S") + ": Could not find anyone")

    # We schedule an "update all" to scan all actors every 5seconds
    pyglet.clock.schedule_interval(update_all, 5)


    # We schedule a check to make sure the game is still running every 3 seconds
    pyglet.clock.schedule_interval(smr.rm.check_process_is_active, 3)
    
    # Implemented Later
    #pyglet.clock.schedule_interval(SoTMemoryReader, 30)
    
    

    # Runs through the macro to leave and join servers
    print("ShipType = " + shipType)
    if shipType.find("1") != -1:
        print("pyglet.clock(interval) = " + shipType)
        if runOnce == True : 
            pyglet.clock.schedule_interval(sloopInput,20)
            runOnce = False 
        print("ShipType = " + shipType)

    if shipType.find("2") != -1:
        if runOnce == True : 
            pyglet.clock.schedule_interval(brigInput,20)
            runOnce = False
        print("ShipType = " + shipType)

    if shipType.find("3") != -1:
        if runOnce == True : 
            pyglet.clock.schedule_interval(galleonInput,20)
            runOnce = False
        print("ShipType = " + shipType)
    
    # We schedule an basic graphics load which is responsible for drawing
    # our interesting information to the screen. Max 144fps, can set unlimited
    # pyglet.clock.schedule(load_graphics)
    pyglet.clock.schedule_interval(load_graphics, 1/144)

    # Adds an FPS counter at the bottom left corner of our pyglet window
    # Note: May not translate to actual FPS, but rather FPS of the program
    fps_display = pyglet.window.FPSDisplay(window)
    
    # Our base player_count label in the top-right of our screen. Updated
    player_count = Label("Player Count: {}",
                        x=SOT_WINDOW_W * 0.85,
                        y=SOT_WINDOW_H * 0.9, batch=main_batch)

    # The label for showing all players on the server under the count
    player_list = Label("\n".join(smr.server_players), x=SOT_WINDOW_W * 0.85,
                            y=(SOT_WINDOW_H-25) * 0.89, batch=main_batch, width=300,
                            multiline=True)
    

    #if players.json in player_list:
    #print("Found them")
    #else:
    #print("Not work")
    # Note: The width of 300 is the max pixel width of a single line
    # before auto-wrapping the text to the next line. Updated in on_draw()

    # Runs our application and starts to use our scheduled events to show data
    pyglet.app.run()
    # Note - ***Nothing past here will execute as app.run() is a loop***


