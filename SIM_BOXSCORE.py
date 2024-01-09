from prettytable import PrettyTable
from termcolor import colored

### ORDINAL FOR INNINGS
def ordinal(n):
    return "%d%s" % (n,"TSNRHTDD"[(n//10%10!=1)*(n%10<4)*n%10::4])

### BOXSCORE 
def print_boxscore(score_by_inning, team1_hits, team2_hits, team1_pitches, team2_pitches, team1_abbr, team2_abbr):
    team1_runs = sum(score_by_inning[0])
    team2_runs = sum(score_by_inning[1])
    team1_inning_scores = score_by_inning[0]
    team2_inning_scores = score_by_inning[1]
    
    num_innings = max(len(team1_inning_scores), len(team2_inning_scores))
    if len(team1_inning_scores) < num_innings:
        team1_inning_scores += [0]*(num_innings - len(team1_inning_scores))
    if len(team2_inning_scores) < num_innings:
        team2_inning_scores += [0]*(num_innings - len(team2_inning_scores))

    boxscore = PrettyTable()
    boxscore.field_names = [colored("TEAM", 'red', attrs=['bold'])] + [f"{colored(ordinal(i+1), 'red', attrs=['bold'])}" for i in range(num_innings)] + [colored("RUNS", 'red', attrs=['bold']), colored("HITS", 'red', attrs=['bold']), colored("PITX",'red', attrs=['bold'])]
    boxscore.add_row([team1_abbr] + team1_inning_scores + [team1_runs, team1_hits, team1_pitches])
    boxscore.add_row([team2_abbr] + team2_inning_scores + [team2_runs, team2_hits, team2_pitches])

    boxscore.align = "c"
    print(boxscore)