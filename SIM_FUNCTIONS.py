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
    time.sleep(0)

def long_wait():
    # 2 SECOND
    time.sleep(0)

### LOADING FUNCTION #######################################################################################################################################################
def print_loading_dots(duration=0, interval=0):
    end_time = time.time() + duration
    sys.stdout.write("SIMULATING PLAY")
    while time.time() < end_time:
        sys.stdout.write(".")
        sys.stdout.flush()  # Make sure the dot is immediately printed to the terminal
        time.sleep(interval)
    print()  # Print a newline character to move to the next line


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
    inning = colored(ordinal(inning), 'red', attrs=['bold'])
    outs = colored((outs), 'yellow', attrs=['bold'])
    home_abb = colored(team1_abbr, 'white', attrs=['bold'])
    home_score = colored(f'{score[0]:2}', 'yellow', attrs=['bold'])
    away_abb = colored(team2_abbr, 'white', attrs=['bold'])
    away_score = colored(f'{score[1]:2}', 'yellow', attrs=['bold'])
    base_status = [
        "██" if bases[base] else "░░" for base in ['1ST', '2ND', '3RD']
    ]
    first = colored(base_status[0], 'red', 'on_white', attrs=['bold'])
    second = colored(base_status[1], 'red', 'on_white', attrs=['bold'])
    third = colored(base_status[2], 'red', 'on_white', attrs=['bold'])

    scoreboard = f"""

{colored(f'╔══════════╦═════════╗', 'white', attrs=['bold'])}
{colored(f'║', 'white', attrs=['bold'])} {colored(inning_indicator, 'red', attrs=['bold'])} {inning} {colored(f' ║', 'white', attrs=['bold'])} {outs} OUTS {colored(f' ║', 'white', attrs=['bold'])}
{colored(f'╠══════════╬═════════╣', 'white', attrs=['bold'])}
{colored(f'║', 'white', attrs=['bold'])} {home_abb}  {home_score} {colored(f' ║', 'white', attrs=['bold'])}    {second}  {colored(f' ║', 'white', attrs=['bold'])}
{colored(f'╟──────────╢         ║', 'white', attrs=['bold'])}
{colored(f'║', 'white', attrs=['bold'])} {away_abb}  {away_score} {colored(f' ║', 'white', attrs=['bold'])}  {third}  {first}{colored(f' ║', 'white', attrs=['bold'])}
{colored(f'╚══════════╩═════════╝', 'white', attrs=['bold'])}

    """
    print(scoreboard)
    short_wait()


### SOUNDBOARD #############################################################################################################################################################
pygame.mixer.init()

def play_sound(event):
    sound_map = {
        "WALK": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\catch_ball6.ogg",
        "SINGLE": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\hit_normal1.ogg",
        "DOUBLE": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\hit_normal6.ogg",
        "TRIPLE": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\hit_hard3.ogg",
        "SOLO HOMERUN!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\horn.ogg",
        "TWO-RUN HOMERUN!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\horn.ogg",
        "THREE-RUN HOMERUN!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\horn.ogg",
        "GRAND SLAM!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\horn.ogg",
        "GROUNDOUT": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\out2.ogg",
        "LINEOUT": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\out2.ogg",
        "FLYOUT": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\out2.ogg",
        "STRUCK HIM OUT!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\strike_three1.ogg",
        "HEE YAHH!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\strike_three2.ogg",
        "STRIKE THREE!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\strike_three1.ogg",
        "SUNG JOOKY BOUY!!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\strike_three2.ogg",
        "HEE GONE!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\strike_three1.ogg",
        "CYA LATER!": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\strike_three2.ogg",
        "STRIKEOUT": "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\SOUNDS\\strike_three1.ogg"
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



# ┌───┬───┬───┐
# │   │   │   │  
# └─


# ┌─────────────┐
# │             │
# │             │
# │             │
# │ 
# │ 
# │ 
# │ 
# └─────────────┘











# # #         ┌────────────┐
# # # │                                                                                             │
# # # └───────────┘
