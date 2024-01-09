import os

from SIM_FUNCTIONS import *
from SIM_BOXSCORE import *
from SIM_INN import *
from SIM_AB import *
from SIM_ROSTERS import *
from SIM_LBRY import *

def simulate_game(team1_csv, team2_csv):
    #############################################################
    team1_abbr = os.path.splitext(os.path.basename(team1_csv))[0]
    team1 = load_away_roster(team1_csv)
    team1_score_by_inning = []
    team1_hits_inning = []
    team1_pitches_by_inning = []
    team1_pitcher = team1[next(iter(team1))]
    team1_batting_order = list(team1.values())[1:10]
    #############################################################
    team2_abbr = os.path.splitext(os.path.basename(team2_csv))[0]
    team2 = load_home_roster(team2_csv)
    team2_score_by_inning = []
    team2_hits_inning = []
    team2_pitches_by_inning = []
    team2_pitcher = team2[next(iter(team2))]
    team2_batting_order = list(team2.values())[1:10]
    #############################################################
    inning = 1
    top_or_bottom = "TOP"
    current_score = [0, 0]

    #play_intro()
    long_wait()
    print("WELCOME TO BASEBALL'S FINEST!")
    print(f"TODAYS MATCHUP IS BETWEEN {team1_abbr} -VS- {team2_abbr}!")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    long_wait()
    print()
    display_away_roster(team1)
    long_wait()
    print()
    display_home_roster(team2)
    long_wait()
    print()

    print("XXXXXXXXXXXXX")
    print("PLAY BALL!")
    print("XXXXXXXXXXXXX")
    long_wait()
    print()

    while True:  # Continue indefinitely, we'll break out of the loop when the game ends
        short_wait()
        message = f'| START OF THE {ordinal(inning):2} INN |'
        print(colored('=' * len(message), 'white', attrs=['bold']))
        print(colored(message, 'yellow', attrs=['bold']))
        print(colored('=' * len(message), 'white', attrs=['bold']))
        print()
        short_wait()
        
        # Simulate the top half of the inning
        top_or_bottom = "TOP"
        current_score, hits_top, total_pitches_top = simulate_half_inning(team1_batting_order, team1_pitcher, team1_abbr, team2_abbr, current_score, inning, top_or_bottom)

        # Update the score for team1
        team1_score_by_inning.append(current_score[0] - sum(team1_score_by_inning))
        team1_hits_inning.append(hits_top)
        team1_pitches_by_inning.append(total_pitches_top)

        # Check for walk-off condition in the bottom of the 9th or later
        if inning >= 9 and sum(team2_score_by_inning) > sum(team1_score_by_inning):
            break  # Home team wins in bottom of the inning (9th or later)
        
        short_wait()
        message = f'| MID OF THE {ordinal(inning):2} INN |'
        print(colored('=' * len(message), 'white', attrs=['bold']))
        print(colored(message, 'yellow', attrs=['bold']))
        print(colored('=' * len(message), 'white', attrs=['bold']))
        print()
        short_wait()

        # Simulate the bottom half of the inning
        top_or_bottom = "BOT"
        current_score, hits_bot, total_pitches_bot = simulate_half_inning(team2_batting_order, team2_pitcher, team1_abbr, team2_abbr, current_score, inning, top_or_bottom)

        # Update the score for team2
        team2_score_by_inning.append(current_score[1] - sum(team2_score_by_inning))
        team2_hits_inning.append(hits_bot)
        team2_pitches_by_inning.append(total_pitches_bot)
        short_wait()

        # Check for walk-off condition in the bottom of the 9th or later
        if inning >= 9 and sum(team2_score_by_inning) > sum(team1_score_by_inning):
            print()
            print(f"{team2_abbr} WALKS IT OFF FOR THE WIN!!!")
            print()
            short_wait()
            break  # Home team wins in bottom of the inning (9th or later)

        short_wait()
        message = f'| END OF THE {ordinal(inning):2} INN | {team1_abbr}: {sum(team1_score_by_inning)} - {team2_abbr}: {sum(team2_score_by_inning)} |'
        print(colored('=' * len(message), 'white', attrs=['bold']))
        print(colored(message, 'yellow', attrs=['bold']))
        print(colored('=' * len(message), 'white', attrs=['bold']))
        print()
        short_wait()

        # Check for game-ending conditions
        if inning >= 9 and sum(team1_score_by_inning) != sum(team2_score_by_inning):
            break  # Game is decided in 9 innings, no need for extra innings

        inning += 1  # Proceed to the next inning

    # Ensure score lists have same length
    while len(team1_score_by_inning) > len(team2_score_by_inning):
        team2_score_by_inning.append(0)
    while len(team1_score_by_inning) < len(team2_score_by_inning):
        team1_score_by_inning.append(0)
    
    team1_pitches = sum(team1_pitches_by_inning)
    team2_pitches = sum(team2_pitches_by_inning)

    team1_hits = sum(team1_hits_inning)
    team2_hits = sum(team2_hits_inning)

    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(f"| FINAL: | {colored(team1_abbr, 'white', attrs=['bold'])}: {colored(current_score[0], 'yellow', attrs=['bold'])} | {colored(team2_abbr, 'white', attrs=['bold'])}: {colored(current_score[1], 'yellow', attrs=['bold'])} |")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print()
    
    print()
    print("======= BOXSCORE =======")
    print_boxscore([team1_score_by_inning, team2_score_by_inning], team1_hits, team2_hits, team1_pitches, team2_pitches, team1_abbr, team2_abbr)  # Also print the pitches

    return current_score

def initialize_team(file_name):
    team = load_roster(file_name)
    team_pitcher = team[next(iter(team))]
        
    for batter in list(team.values())[1:]:
        update_batter_probabilities(batter, team_pitcher, league_averages)

    return team

def initialize_and_simulate_game(team1_abbr, team2_abbr):
    file_path = # Replace with your file path 

    team1_filename = f'{file_path}\{team1_abbr}.csv'
    team2_filename = f'{file_path}\{team2_abbr}.csv'

    # Load the rosters
    team1_roster = load_away_roster(team1_filename)
    team2_roster = load_home_roster(team2_filename)

    simulate_game(team1_filename, team2_filename)

def main():
    # Initialize and simulate game between two teams
    AWAY = 'WAS'
    HOME = 'CHR'
    initialize_and_simulate_game(AWAY, HOME)

if __name__ == "__main__":
    main()
















