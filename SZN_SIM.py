import csv
from SIM_GAMEDAY import *

file_path = 'C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\FICT_MLB\\ABL_SKED\\ABL_SKED.csv'

def read_schedule(file_path):
    schedule = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            away_team_abbr = row['AWAY']  # Assuming you have a column named 'AWAY' in your CSV
            home_team_abbr = row['HOME']  # Assuming you have a column named 'HOME' in your CSV
            schedule.append((away_team_abbr, home_team_abbr))
    return schedule

def initialize_and_simulate_game(team1_abbr, team2_abbr):
    file_path = "C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\FICT_MLB\\TEAMS\\"
    
    team1_filename = f'{file_path}\{team1_abbr}.csv'
    team2_filename = f'{file_path}\{team2_abbr}.csv'

    # Load the rosters
    team1_roster = load_roster(team1_filename)
    team2_roster = load_roster(team2_filename)

    # Simulate the game
    score1, score2 = simulate_game(f'{file_path}{team1_abbr}.csv', f'{file_path}{team2_abbr}.csv')

    return score1, score2

def simulate_season(file_path):
    schedule = read_schedule(file_path)
    with open('BISMO_SZN.csv', 'w', newline='') as results_file:
        writer = csv.writer(results_file)
        writer.writerow(['GM#', 'AW', 'AWR', 'HM', 'HMR'])  # Write headers

        for game_number, (team1_abbr, team2_abbr) in enumerate(schedule):
            # Call the initialize_and_simulate_game function to get the scores
            score1, score2 = initialize_and_simulate_game(team1_abbr, team2_abbr)
            
            # Write the results to the results CSV file
            writer.writerow([game_number, team1_abbr, score1, team2_abbr, score2])

def main():
    file_path = 'C:\\Users\\herre\\OneDrive\\Documents\\SPORTS\\MLB\\BISMO_BALL\\FICT_MLB\\ABL_SKED\\ABL_SKED.csv'
    simulate_season(file_path)
    # Optionally, include code to summarize the season results

if __name__ == "__main__":
    main()




