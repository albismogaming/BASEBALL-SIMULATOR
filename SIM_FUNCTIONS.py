### STORING THE FUNCTIONS IN A SEPARATE FILE IN ORDER TO KEEP THE SIMULATION CODE CLEANER ##################################################################################
import time
import random
import numpy as np
import pandas as pd
import math
from termcolor import *
import sys
import pygame.mixer
import re

### ORDINAL FOR INNINGS ####################################################################################################################################################
def ordinal(n):
    return "%d%s" % (n,"TSNRHTDD"[(n//10%10!=1)*(n%10<4)*n%10::4])

### WAIT TIME FUNCTIONS ####################################################################################################################################################
def short_wait():
    # 1 SECOND
    time.sleep(2) 

def long_wait():
    # 2 SECOND
    time.sleep(3)

### LOADING FUNCTION #######################################################################################################################################################
def print_loading_dots(duration=1.5, interval=0.5):
    end_time = time.time() + duration
    sys.stdout.write("LOADING")
    while time.time() < end_time:
        sys.stdout.write(".")
        sys.stdout.flush()  # Make sure the dot is immediately printed to the terminal
        time.sleep(interval)
    print()  # Print a newline character to move to the next line

# Use 0 for Wait time and Loading functions to simulate instantly

### STRIKE OUT CALLS #######################################################################################################################################################
def strikeout_call():
    descriptions = [
        "STRUCK HIM OUT!",
        "HEE YAHH!",
        "STRIKE THREE!",
        "SUNG JOOKY BOUY!!",
        "HEE GONE!",
        "CYA LATER!"
    ]
    return random.choice(descriptions)

### SCOREBOARD #############################################################################################################################################################
def print_scoreboard(inning, top_or_bottom, score, outs, bases, team1_abbr, team2_abbr):
    inning_indicator = "TOP" if top_or_bottom == "TOP" else "BOT"
    base_status = [
        "X" if bases[base] else "-" for base in ['1ST', '2ND', '3RD']
    ]
    scoreboard = f"""
{colored(f'====================', 'white', attrs=['bold'])}
{colored(f'|', 'white', attrs=['bold'])} {colored(inning_indicator, 'red', attrs=['bold'])} {colored(ordinal(inning), 'red', attrs=['bold'])} {colored(f'|', 'white', attrs=['bold'])} {colored((outs), 'yellow', attrs=['bold'])} OUTS {colored(f'|', 'white', attrs=['bold'])}
{colored(f'====================', 'white', attrs=['bold'])}
{colored(f'|', 'white', attrs=['bold'])} {colored(team1_abbr, 'white', attrs=['bold'])}: {colored(f'{score[0]:2}', 'yellow', attrs=['bold'])} {colored(f'|', 'white', attrs=['bold'])}   {colored(f'[', 'red', 'on_white', attrs=['bold'])}{colored(base_status[1], 'red', 'on_white', attrs=['bold'])}{colored(f']', 'red', 'on_white', attrs=['bold'])}  {colored(f'|', 'white', attrs=['bold'])}
{colored(f'|', 'white', attrs=['bold'])} {colored(team2_abbr, 'white', attrs=['bold'])}: {colored(f'{score[1]:2}', 'yellow', attrs=['bold'])} {colored(f'|', 'white', attrs=['bold'])} {colored(f'[', 'red', 'on_white', attrs=['bold'])}{colored(base_status[2], 'red', 'on_white', attrs=['bold'])}{colored(f']', 'red', 'on_white', attrs=['bold'])} {colored(f'[', 'red', 'on_white', attrs=['bold'])}{colored(base_status[0], 'red', 'on_white', attrs=['bold'])}{colored(f']', 'red', 'on_white', attrs=['bold'])}{colored(f'|', 'white', attrs=['bold'])}
{colored(f'====================', 'white', attrs=['bold'])}
    """
    print(scoreboard)
    short_wait()


### SOUNDBOARD #############################################################################################################################################################
pygame.mixer.init()

# Create a folder for your sound effects and copy the file path below 
def play_sound(event):
    sound_map = {
        "WALK": "FILE PATH",
        "SINGLE": "FILE PATH",
        "DOUBLE": "FILE PATH",
        "TRIPLE": "FILE PATH",
        "SOLO HOMERUN!": "FILE PATH",
        "TWO-RUN HOMERUN!": "FILE PATH",
        "THREE-RUN HOMERUN!": "FILE PATH",
        "GRAND SLAM!": "FILE PATH",
        "GROUNDOUT": "FILE PATH",
        "LINEOUT": "FILE PATH",
        "FLYOUT": "FILE PATH",
        "STRUCK HIM OUT!": "FILE PATH",
        "HEE YAHH!": "FILE PATH",
        "STRIKE THREE!": "FILE PATH",
        "SUNG JOOKY BOUY!!": "FILE PATH",
        "HEE GONE!": "FILE PATH",
        "CYA LATER!": "FILE PATH",
        "STRIKEOUT": "FILE PATH"
    }

    sound_file = sound_map.get(event)
    if sound_file:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    else:
        print()

def play_intro():
    pygame.mixer.init()
    pygame.mixer.music.load('C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\MLB_FOX_INTRO.mp3')
    pygame.mixer.music.play()






