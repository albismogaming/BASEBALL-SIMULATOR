import random
import math
from prettytable import PrettyTable
import numpy as np
import pandas as pd
from termcolor import colored
import time
import os
from SIM_FUNCTIONS import *

roster = {}

def load_home_roster(csv_file):
    return load_roster(csv_file)

def load_away_roster(csv_file):
    return load_roster(csv_file)

def load_roster(csv_file):
    df = pd.read_csv(csv_file)
    roster = {}
    positions_order = ['CF', '2B', '3B', 'DH', '1B', 'RF', 'LF', 'SS', 'C']

    # Only load a random pitcher if one hasn't been loaded yet
    if 'pitcher' not in roster:
        pitcher_df = df[df['POS'] == 'SP']
        random_index = random.randint(0, len(pitcher_df) - 1)
        pitcher_row = pitcher_df.iloc[random_index]
        roster[pitcher_row['NAME']] = {
            'position': pitcher_row['POS'],
            'attributes': pitcher_row.drop(['NAME', 'POS', 'ID']).to_dict()
    }

    # Load batters in the desired order
    for pos in positions_order:
        position_df = df[df['POS'] == pos]
        for _, row in position_df.iterrows():
            roster[row['NAME']] = {
                'position': row['POS'],
                'attributes': row.drop(['NAME', 'POS', 'ID']).to_dict()
            }
    return roster

def display_section(title):
    print(f"\n{title}")
    short_wait()

def display_pitcher(title, roster):
    display_section(title)
    pitcher_name, pitcher_info = next(iter(roster.items()))
    print(f"1. {pitcher_info['position']} - {pitcher_name}")

def display_batters(title, roster):
    display_section(title)
    for idx, (player_name, player_info) in enumerate(list(roster.items())[1:10]):
        print(f"{idx + 1}. {player_info['position']} - {player_name}")

### DISPLAY HOME ROSTER
def display_home_roster(home_roster):
    display_pitcher("======= HOME TEAM: STARTING PITCHER =======", home_roster)
    long_wait()
    display_batters("======= HOME TEAM: BATTING ORDER =======", home_roster)
    long_wait()

### DISPLAY AWAY ROSTER
def display_away_roster(away_roster):
    display_pitcher("======= AWAY TEAM: STARTING PITCHER =======", away_roster)
    long_wait()
    display_batters("======= AWAY TEAM: BATTING ORDER =======", away_roster)
    long_wait()




