import os

from SIM_FUNCTIONS import *
from SIM_AB import *
from SIM_ROSTERS import *
from SIM_LBRY import *
from SIM_AB import simulate_pitch_count
from SIM_AB import simulate_at_bat

###############################################################################################################
def simulate_half_inning(batting_order, pitcher, team1_abbr, team2_abbr, current_score, inning, top_or_bottom):
    outs = 0
    hits = 0
    runs_scored = 0
    total_pitches = 0
    bases = {'1ST': 0, '2ND': 0, '3RD': 0}
    
    # Print the scoreboard at the beginning of the inning or when state changes
    print_scoreboard(inning, top_or_bottom, current_score, outs, bases, team1_abbr, team2_abbr)

    while outs < 3:
        batter = batting_order[0]  # get the first batter
        batting_order.append(batting_order.pop(0))  # move the first batter to the end

        outcome = simulate_at_bat(batter, pitcher)
        total_pitches += simulate_pitch_count(outcome)

#########################################################################################################
        if outcome == "WALK":
            if bases['1ST'] == 1 and bases['2ND'] == 1 and bases['3RD'] == 1:
                runs_scored += 1  # Runner on 3RD scores
                outcome = "WALK"
                outcomex = "(RUNS SCORES!)"

            elif bases['1ST'] == 1 and bases['2ND'] == 1: 
                bases['2ND'] = 1 
                bases['3RD'] = 1
                outcome = "WALK"
                outcomex = "(RUNNERS MOVE UP 90FT!)"

            elif bases['1ST'] == 1 and bases['3RD'] == 1:
                bases['2ND'] = 1
                outcome = "WALK"
                outcomex = "(RUNNER TO FIRST!)"

            elif bases['2ND'] == 1 and bases['3RD'] == 1:
                bases['1ST'] = 1 
                outcome = "WALK"
                outcomex = "(RUNNER TO FIRST!)"

            elif bases['1ST'] == 1: 
                bases['2ND'] = 1 
                outcome = "WALK"
                outcomex = "(RUNNER TO FIRST!)"

            elif bases['2ND'] == 1:
                bases['1ST'] = 1 
                outcome = "WALK"
                outcomex = "(RUNNER TO FIRST!)"

            elif bases['3RD'] == 1:
                bases['1ST'] = 1 
                outcome = "WALK"
                outcomex = "(RUNNER TO FIRST!)"

            if bases['1ST'] == 0 and bases['2ND'] == 0 and bases['3RD'] == 0:
                bases['1ST'] = 1
                outcome = "WALK"
                outcomex = "(RUNNER TO FIRST!)"

#########################################################################################################
        if outcome == "SINGLE":
            hits += 1
            if bases['1ST'] == 1 and bases['2ND'] == 1 and bases['3RD'] == 1:
                if random.random() < 0.64:  # 70% chance of runner on second scoring
                    runs_scored += 2
                    bases['2ND'] = 1
                    bases['3RD'] = 0
                    outcome = "SINGLE"
                    outcomex = "(3RD SCORES, 2ND SCORES!)"

                elif random.random() < 0.91:  # 25% chance of runner advancing to third
                    runs_scored += 1
                    bases['3RD'] = 1
                    bases['2ND'] = 1
                    outcome = "SINGLE"
                    outcomex = "(3RD SCORES, RUNNER HELD AT 3RD!)"

                else:  # 5% chance of runner thrown out at home
                    runs_scored += 1
                    outs += 1
                    bases['2ND'] = 1
                    outcome = "SINGLE"
                    outcomex = "(3RD SCORES, 2ND THROWN OUT!)"

            elif bases['1ST'] == 1 and bases['2ND'] == 1:
                if random.random() < 0.7:
                    runs_scored += 1
                    bases['2ND'] = 1
                    outcome = "SINGLE"
                    outcomex = "(RUNNER SCORES FROM 2ND!)"

                elif random.random() < 0.93:
                    bases['3RD'] = 1
                    bases['2ND'] = 1
                    outcome = "SINGLE"
                    outcomex = "(RUNNER HELD AT 3RD!)"

                else:  # % chance of being thrown out at home
                    outs += 1
                    bases['2ND'] = 1
                    outcome = "SINGLE"
                    outcomex = "(OUT AT HOME!)"

            elif bases['1ST'] == 1 and bases['3RD'] == 1: # Runner on first has a chance to go to third
                if random.random() < 0.24:  # 20% chance of being thrown out at third
                    outs += 1
                    bases['3RD'] = 0
                    runs_scored += 1
                    outcome = "SINGLE"
                    outcomex = "(RUN SCORED, OUT AT 3RD!)"

                elif random.random() < 0.37:
                    bases['3RD'] = 1
                    runs_scored += 1
                    outcome = "SINGLE"
                    outcomex = "(RUN SCORED, RUNNER ADVANCES TO 3RD!)"

                else:
                    bases['2ND'] = 1
                    bases['3RD'] = 0
                    runs_scored += 1
                    outcome = "SINGLE"
                    outcomex = "(RUN SCORED!)"

            elif bases['2ND'] == 1 and bases['3RD'] == 1:
                if random.random() < 0.7:  # 70% chance of runner on second scoring
                    runs_scored += 2
                    bases['1ST'] = 1
                    bases['2ND'] = 0
                    bases['3RD'] = 0
                    outcome = "SINGLE"
                    outcomex = "(2 RUNS SCORED! 3RD SCORES, 2ND SCORES!)"

                elif random.random() < 0.95:  # 25% chance of runner advancing to third
                    runs_scored += 1
                    bases['3RD'] = 1
                    bases['2ND'] = 0
                    bases['1ST'] = 1
                    outcome = "SINGLE"
                    outcomex = "(1 RUNS SCORED! 3RD SCORES, 2ND HELD AT 3RD!)"

                else:  # 5% chance of runner thrown out at home
                    runs_scored += 1
                    outs += 1
                    bases['1ST'] = 1
                    bases['2ND'] = 0
                    bases['3RD'] = 0
                    outcome = "SINGLE"
                    outcomex = "(1 RUN SCORED! 3RD SCORES, 2ND THROWN OUT!)"

            elif bases['3RD'] == 1:
                bases['1ST'] = 1
                bases['3RD'] = 0
                runs_scored += 1  # Runner on third scores
                outcome = "SINGLE"
                outcomex = "(RUNNER SCORES FROM 3RD!)"

            elif bases['2ND'] == 1: # Runner on second has a chance to score
                if random.random() < 0.7:
                    runs_scored += 1
                    bases['1ST'] = 1
                    bases['2ND'] = 0
                    outcome = "SINGLE"
                    outcomex = "(RUNNER SCORES FROM 2ND!)"

                elif random.random() < 0.93:
                    bases['3RD'] = 1
                    bases['2ND'] = 0
                    bases['1ST'] = 1
                    outcome = "SINGLE"
                    outcomex = "(RUNNER HELD AT 3RD!)"

                else:  # % chance of being thrown out at home
                    outs += 1
                    bases['1ST'] = 1
                    bases['2ND'] = 0
                    outcome = "SINGLE"
                    outcomex = "(OUT AT HOME!)"

            elif bases['1ST'] == 1: # Runner on first has a chance to go to third
                if random.random() < 0.14:  # 20% chance of being thrown out at third
                    outs += 1
                    bases['1ST'] = 1
                    bases['3RD'] = 0
                    outcome = "SINGLE"
                    outcomex = "(RUNNER OUT AT 3RD!)"

                elif random.random() < 0.33:
                    bases['1ST'] = 1
                    bases['3RD'] = 1
                    outcome = "SINGLE"
                    outcomex = "(RUNNER ADVANCES TO 3RD!)"

                else:
                    bases['2ND'] = 1
                    outcome = "SINGLE"
                    outcomex = "(RUNNERS MOVE UP 90FT!)"

            elif bases['1ST'] == 0 and bases['2ND'] == 0 and bases['3RD'] == 0:
                bases['1ST'] = 1  # Batter takes first
                outcome = "SINGLE"
                outcomex = "(RUNNER TO FIRST!)"

#########################################################################################################
        elif outcome == "DOUBLE":
            hits += 1
            if bases['1ST'] == 1 and bases['2ND'] == 1 and bases['3RD'] == 1 and outs <= 2:
                if random.random() < .08:
                    runs_scored += 3
                    bases['1ST'] = 0
                    bases['3RD'] = 0
                    outcome = "DOUBLE"
                    outcomex = "(BASES CLEARED! 3 RUNS SCORED!)"

                elif random.random() < .93:
                    runs_scored += 2
                    bases['1ST'] = 0
                    bases['3RD'] = 1
                    outcome = "DOUBLE"
                    outcomex = "(2 RUNS SCORED, TRAIL RUNNER HELD AT 3RD!)"

                else:
                    outs += 1
                    runs_scored += 2
                    bases['1ST'] = 0
                    bases['3RD'] = 0
                    outcome = "DOUBLE"
                    outcomex = "(2 RUNS SCORED, TRAIL RUNNER THROWN OUT AT HOME!)"

            elif bases['2ND'] == 1 and bases['3RD'] == 1 and outs <= 2:
                runs_scored += 2  
                bases['3RD'] = 0  
                bases['2ND'] = 0  
                outcome = "DOUBLE"
                outcomex = "(2 RUNS SCORED!)"

            elif bases['1ST'] == 1 and bases['3RD'] == 1 and outs <= 2: # Runner on first has a chance to go to third
                if random.random() < 0.24:  # 20% chance of being thrown out at third
                    outs += 1
                    runs_scored += 1
                    bases['1ST'] = 0
                    bases['3RD'] = 0
                    outcome = "DOUBLE"
                    outcomex = "(RUN SCORED, OUT AT HOME!)"

                elif random.random() < 0.32:
                    bases['3RD'] = 0
                    bases['1ST'] = 0
                    runs_scored += 2
                    outcome = "DOUBLE"
                    outcomex = "(TWO RUNS SCORED!)"

                else:
                    bases['3RD'] = 1
                    bases['1ST'] = 0
                    runs_scored += 1
                    outcome = "DOUBLE"
                    outcomex = "(RUN SCORED, RUNNER HELD AT 3RD)"

            elif bases['1ST'] == 1 and bases['2ND'] == 1 and outs < 2: # Runner on first has a chance to go to third
                if random.random() < 0.09:  # chance of being thrown out at third
                    runs_scored += 2
                    bases['1ST'] = 0
                    bases['2ND'] = 1
                    outcome = "DOUBLE"
                    outcomex = "(2 RUNS SCORED!)"

                elif random.random() < 0.17:
                    bases['3RD'] = 0
                    bases['2ND'] = 1
                    bases['1ST'] = 0
                    runs_scored += 1
                    outs += 1
                    outcome = "DOUBLE"
                    outcomex = "(RUN SCORES, TRAIL RUNNER OUT AT HOME!)"

                else:
                    bases['3RD'] = 1
                    bases['2ND'] = 1
                    bases['1ST'] = 0
                    runs_scored += 1
                    outcome = "DOUBLE"
                    outcomex = "(RUN SCORED, RUNNER MOVES TO 3RD!)"

            # If there's a runner on first, they have a chance to score or be thrown out
            elif bases['1ST'] == 1 and outs <= 2:
                if random.random() < 0.08:  # 15% chance of scoring from first on a double
                    runs_scored += 1
                    bases['1ST'] = 0
                    bases['2ND'] = 1
                    outcome = "DOUBLE"
                    outcomex = "(RUNNER SCORES FROM 1ST!)"

                elif random.random() < 0.88:  # 70% chance of being held at third
                    bases['3RD'] = 1
                    bases['2ND'] = 1
                    bases['1ST'] = 0
                    outcome = "DOUBLE"
                    outcomex = "(RUNNER HELD AT 3RD!)"

                else:  # % chance of an out at home
                    outs += 1
                    bases['1ST'] = 0
                    bases['2ND'] = 1
                    bases['3RD'] = 0
                    outcome = "DOUBLE"
                    outcomex = "(RUNNER OUT AT HOME!)"

            # If there's a runner on third, they will score
            elif bases['3RD'] == 1 and outs <= 2:
                runs_scored += 1
                bases['3RD'] = 0
                bases['2ND'] = 1
                outcome = "DOUBLE"
                outcomex = "(RUNNER SCORES FROM 3RD!)"

            elif bases['2ND'] == 1 and outs <= 2:
                runs_scored += 1
                bases['2ND'] = 1
                outcome = "DOUBLE"
                outcomex = "(RUNNER SCORES FROM 2ND!)"

            elif bases['1ST'] == 0 and bases['2ND'] == 0 and bases['3RD'] == 0:
                bases['2ND'] = 1  # Batter takes first
                outcome = "DOUBLE"
                outcomex = "(RUNNER TO SECOND!)"

#########################################################################################################
        elif outcome == "TRIPLE":
            hits += 1
            if bases['1ST'] == 1 and bases['2ND'] == 1 and bases['3RD'] == 1:
                runs_scored += 3
                bases['1ST'] = 0
                bases['2ND'] = 0
                bases['3RD'] = 1
                outcome = "TRIPLE"
                outcomex = "(3 RUNS SCORED, BASES CLEARED!)"
                
            elif  bases['1ST'] == 1 and bases['2ND'] == 1:
                runs_scored += 2
                bases['1ST'] = 0
                bases['2ND'] = 0
                bases['3RD'] = 1
                outcome = "TRIPLE"
                outcomex = "(2 RUNS SCORED!)"
                
            elif bases['1ST'] == 1 and bases['3RD'] == 1:
                runs_scored += 2
                bases['1ST'] = 0
                bases['2ND'] = 0
                bases['3RD'] = 1
                outcome = "TRIPLE"
                outcomex = "(2 RUNS SCORED!)"
  
            elif  bases['2ND'] == 1 and bases['3RD'] == 1:
                runs_scored += 2
                bases['1ST'] = 0
                bases['2ND'] = 0
                bases['3RD'] = 1
                outcome = "TRIPLE"
                outcomex = "(2 RUNS SCORED!)"

            elif bases['1ST'] == 1:
                runs_scored += 1
                bases['1ST'] = 0
                bases['2ND'] = 0
                bases['3RD'] = 1
                outcome = "TRIPLE"
                outcomex = "(RUN SCORED FROM 1ST!)"
                
            elif bases['2ND'] == 1:
                runs_scored += 1
                bases['1ST'] = 0
                bases['2ND'] = 0
                bases['3RD'] = 1
                outcome = "TRIPLE"
                outcomex = "(RUN SCORED FROM 2ND!)"
                
            elif bases['3RD'] == 1:
                runs_scored += 1
                bases['1ST'] = 0
                bases['2ND'] = 0
                bases['3RD'] = 1
                outcome = "TRIPLE"
                outcomex = "(RUN SCORED FROM 3RD!)"
                
            elif bases['1ST'] == 0 and bases['2ND'] == 0 and bases['3RD'] == 0:
                bases['3RD'] = 1  # Batter takes first
                outcome = "TRIPLE"
                outcomex = "(RUNNER TO THIRD!)"

#########################################################################################################
        elif outcome == "HOMERUN":
            hits += 1
            # Determine the specific type of home run based on the total runs scored
            if bases['1ST'] == 0 and bases['2ND'] == 0 and bases['3RD'] == 0:
                runs_scored += 1
                outcome = "SOLO HOMERUN!"
                outcomex = "(1 RUNS SCORED)"

            elif bases['1ST'] == 1 and bases['2ND'] == 1 and bases['3RD'] == 1:
                runs_scored += 4
                outcome = "GRAND SLAM!"
                outcomex = "(4 RUNS SCORED)"

            elif bases['1ST'] == 1 and bases['2ND'] == 1:
                runs_scored += 3
                outcome = "THREE-RUN HOMERUN!"
                outcomex = "(3 RUNS SCORED)"

            elif bases['1ST'] == 1 and bases['3RD'] == 1:
                runs_scored += 3
                outcome = "THREE-RUN HOMERUN!"
                outcomex = "(3 RUNS SCORED)"

            elif bases['2ND'] == 1 and bases['3RD'] == 1:
                runs_scored += 3
                outcome = "THREE-RUN HOMERUN!"
                outcomex = "(3 RUNS SCORED)"

            elif bases['3RD'] == 1 or bases['2ND'] == 1 or bases['1ST'] == 1:
                runs_scored += 2
                outcome = "TWO-RUN HOMERUN!"
                outcomex = "(2 RUNS SCORED)"

            bases = {'1ST': 0, '2ND': 0, '3RD': 0}  # Clear the bases
#########################################################################################################
        elif outcome == "STRIKEOUT":
            outs += 1
            outcome = strikeout_call()
            outcomex = "======="
            pass  # No change in bases

#########################################################################################################
        elif outcome == "OUT":
            out_types = ["GROUNDOUT", "FLYOUT", "LINEOUT"]
            out_type = np.random.choice(out_types, p=[0.44, 0.32, 0.24])

            if out_type == "FLYOUT":
                if bases['3RD'] and outs < 2:
                    if random.random() < 0.82:
                        runs_scored += 1
                        outs += 1
                        bases['3RD'] = 0
                        outcome = "FLYOUT"
                        outcomex = "SAC FLY (RUNNER SCORES!)"

                    elif random.random() < 0.90:
                        outs += 2
                        bases['3RD'] = 0
                        outcome = "FLYOUT"
                        outcomex = "(RUNNER OUT AT HOME!, DOUBLE PLAY!)"

                    else:
                        outs += 1
                        outcome = "FLYOUT"
                        outcomex = "(RUNNER HELD AT 3RD!)"

                elif bases['2ND'] == 1 and outs < 2:
                    if random.random() < 0.64:
                        bases['2ND'] = 0
                        bases['3RD'] = 1
                        outs += 1
                        outcome = "FLYOUT"
                        outcomex = "(RUNNER ADVANCES TO 3RD!)"

                    elif random.random() < 0.87:
                        bases['2ND'] = 0
                        outs += 2
                        outcome = "FLYOUT"
                        outcomex = "(RUNNER THROWN OUT ADVANCING!)"

                    else:
                        bases['2ND'] = 1
                        outs += 1
                        outcome = "FLYOUT"
                        outcomex = "(RUNNERS HOLD!)"

                elif bases['1ST'] == 1 and bases['2ND'] == 1 and outs < 2:
                    if random.random() < 0.64:
                        bases['1ST'] = 1
                        bases['2ND'] = 0
                        bases['3RD'] = 1
                        outs += 1
                        outcome = "FLYOUT"
                        outcomex = "(RUNNER ADVANCES TO 3RD!)"

                    elif random.random() < 0.87:
                        bases['1ST'] = 1
                        bases['2ND'] = 0
                        outs += 2
                        outcome = "FLYOUT"
                        outcomex = "(RUNNER THROWN OUT ADVANCING!)"

                    else:
                        bases['1ST'] = 1
                        bases['2ND'] = 1
                        outs += 1
                        outcome = "FLYOUT"
                        outcomex = "(RUNNERS HOLD!)"


                elif bases['1ST'] == 1 and bases['2ND'] == 1 and bases['3RD'] == 1 and outs < 2:
                    if random.random() < 0.74:
                        runs_scored += 1
                        bases['1ST'] = 1
                        bases['2ND'] = 0
                        bases['3RD'] = 1
                        outs += 1
                        outcome = "FLYOUT"
                        outcomex = "SAC FLY (RUN SCORES AND RUNNER ADVANCES TO 3RD!)"

                    elif random.random() < 0.82:
                        runs_scored += 1
                        bases['1ST'] = 1
                        bases['2ND'] = 0
                        bases['3RD'] = 0
                        outs += 2
                        outcome = "FLYOUT"
                        outcomex = "SAC FLY (RUNNER THROWN OUT ADVANCING TO 3RD!)"

                    elif random.random() < .90:
                        bases['1ST'] = 1
                        bases['2ND'] = 0
                        bases['3RD'] = 1
                        outs += 2
                        outcome = "FLYOUT"
                        outcomex = "(RUNNER THROWN OUT AT HOME! RUNNER ADVANCES TO 3RD!)"

                    else:
                        bases['1ST'] = 1
                        bases['2ND'] = 1
                        bases['3RD'] = 1
                        outs += 1
                        outcome = "FLYOUT"
                        outcomex = "(RUNNERS HOLD!)"
                    
                else:
                    outs += 1
                    outcome = "FLYOUT"
                    outcomex = "======="

#########################################################################################################
            elif out_type == "GROUNDOUT":
                if bases['1ST'] == 1 and bases['2ND'] == 1 and bases['3RD'] == 1 and outs == 0:
                    if random.random() < .44:
                        if random.random() < .88:
                            outs += 2
                            runs_scored += 1
                            bases['1ST'] = 0
                            bases['2ND'] = 0
                            bases['3RD'] = 1
                            outcome = "GROUNDOUT"
                            outcomex = "DOUBLE PLAY! (X-4-3) RUN SCORES!"

                        else:
                            outs += 1
                            runs_scored += 1
                            bases['1ST'] = 1
                            bases['2ND'] = 0
                            bases['3RD'] = 1
                            outcome = "GROUNDOUT"
                            outcomex = "FIELDERS CHOICE! (SAFE AT FIRST!) RUN SCORES!"

                    elif random.random() < .68:
                        if random.random() < .88:
                            outs += 2
                            runs_scored += 0
                            bases['1ST'] = 0
                            bases['2ND'] = 1
                            bases['3RD'] = 1
                            outcome = "GROUNDOUT"
                            outcomex = "DOUBLE PLAY! (X-2-3)"

                        else:
                            outs += 1
                            runs_scored += 0
                            bases['1ST'] = 1
                            bases['2ND'] = 1
                            bases['3RD'] = 1
                            outcome = "GROUNDOUT"
                            outcomex = "FIELDERS CHOICE! (SAFE AT FIRST!)"

                    elif random.random() < .86:
                        if random.random() < .88:
                            outs += 2
                            runs_scored += 1
                            bases['1ST'] = 0
                            bases['2ND'] = 1
                            bases['3RD'] = 0
                            outcome = "GROUNDOUT"
                            outcomex = "DOUBLE PLAY! (X-5-3)"

                        else:
                            outs += 1
                            runs_scored += 1
                            bases['1ST'] = 1
                            bases['2ND'] = 1
                            bases['3RD'] = 0
                            outcome = "GROUNDOUT"
                            outcomex = "FIELDERS CHOICE! (SAFE AT FIRST!)"

                    elif random.random() < .95:
                        if random.random() < .88:
                            outs += 2
                            runs_scored += 1
                            bases['1ST'] = 1
                            bases['2ND'] = 0
                            bases['3RD'] = 0
                            outcome = "GROUNDOUT"
                            outcomex = "DOUBLE PLAY (X-5-4)"

                        else:
                            outs += 1
                            runs_scored += 1
                            bases['1ST'] = 1
                            bases['2ND'] = 1
                            bases['3RD'] = 0
                            outcome = "GROUNDOUT"
                            outcomex = "FIELDERS CHOICE! (SAFE AT SECOND!)"

                    elif random.random() < 1:
                        if random.random() < .88:
                            outs += 2
                            runs_scored += 0
                            bases['1ST'] = 1
                            bases['2ND'] = 1
                            bases['3RD'] = 0
                            outcome = "GROUNDOUT"
                            outcomex = "DOUBLE PLAY (X-2-5)"

                        else:
                            outs += 1
                            runs_scored += 0
                            bases['1ST'] = 1
                            bases['2ND'] = 1
                            bases['3RD'] = 1
                            outcome = "GROUNDOUT"
                            outcomex = "FIELDERS CHOICE! (SAFE AT THIRD!)"

                elif bases['1ST'] == 1 and bases['2ND'] == 1 and outs == 0:
                    if random.random() < 0.88:
                        outs += 2
                        bases['1ST'] = 1 
                        bases['2ND'] = 0
                        bases['3RD'] = 0
                        outcome = "GROUNDOUT"
                        outcomex = "DOUBLE PLAY (X-5-4)!"

                    else:
                        outs += 1
                        bases['1ST'] = 1
                        bases['2ND'] = 1
                        bases['3RD'] = 0
                        outcome = "GROUNDOUT"
                        outcomex = "FIELDERS CHOICE (OUT AT 3RD)!"

                elif bases['1ST'] == 1 and bases['2ND'] == 1 and outs == 1:
                    if random.random() < 0.88:
                        outs += 2
                        bases['1ST'] = 0
                        bases['2ND'] = 0
                        bases['3RD'] = 1
                        outcome = "GROUNDOUT"
                        outcomex = "DOUBLE PLAY (X-4-3)!"

                    else:
                        outs += 1
                        bases['1ST'] = 1
                        bases['2ND'] = 0
                        bases['3RD'] = 1
                        outcome = "GROUNDOUT"
                        outcomex = "FIELDERS CHOICE (OUT AT 2ND!)"

                elif bases['1ST'] == 1 and bases['3RD'] == 1 and outs == 0:
                    if random.random() < 0.88:
                        outs += 2
                        runs_scored += 1
                        bases['1ST'] = 0
                        bases['2ND'] = 0
                        bases['3RD'] = 0
                        outcome = "GROUNDOUT"
                        outcomex = "DOUBLE PLAY (X-4-3)!"

                    else:
                        outs += 1
                        runs_scored += 1
                        bases['1ST'] = 1
                        bases['2ND'] = 0
                        bases['3RD'] = 0
                        outcome = "GROUNDOUT"
                        outcomex = "FIELDERS CHOICE (OUT AT 2ND!)"

                elif bases['1ST'] == 1 and bases['3RD'] == 1 and outs == 1:
                    if random.random() < 0.88:
                        outs += 2
                        bases['1ST'] = 0
                        bases['2ND'] = 0
                        bases['3RD'] = 0
                        outcome = "GROUNDOUT"
                        outcomex = "DOUBLE PLAY (X-4-3)!"

                    else:
                        outs += 1
                        runs_scored += 1
                        bases['1ST'] = 1
                        bases['2ND'] = 0
                        bases['3RD'] = 0
                        outcome = "GROUNDOUT"
                        outcomex = "FIELDERS CHOICE (OUT AT 2ND!)"
                    
                elif bases['1ST'] == 1 and outs == 0:
                    if random.random() < 0.88:
                        outs += 2
                        bases['1ST'] = 0
                        bases['2ND'] = 0
                        outcome = "GROUNDOUT"
                        outcomex = "DOUBLE PLAY (X-4-3)!"

                    else:
                        if random.random() < .57:
                            outs += 1
                            bases['1ST'] = 1
                            bases['2ND'] = 0
                            outcome = "GROUNDOUT"
                            outcomex = "FIELDERS CHOICE (OUT AT 2ND)!"

                        else:
                            outs += 1
                            bases['1ST'] = 0
                            bases['2ND'] = 1
                            outcome = "GROUNDOUT"
                            outcomex = "FIELDERS CHOICE (OUT AT 1ST)!"

                elif bases['1ST'] == 1 and outs == 1:
                    if random.random() < 0.88:
                        outs += 2
                        bases['1ST'] = 0
                        bases['2ND'] = 0
                        outcome = "GROUNDOUT"
                        outcomex = "DOUBLE PLAY (X-4-3)!"

                    else:
                        if random.random() < .57:
                            outs += 1
                            bases['1ST'] = 1
                            bases['2ND'] = 0
                            outcome = "GROUNDOUT"
                            outcomex = "FIELDERS CHOICE (OUT AT 2ND)!"

                        else:
                            outs += 1
                            bases['1ST'] = 0
                            bases['2ND'] = 1
                            outcome = "GROUNDOUT"
                            outcomex = "FIELDERS CHOICE (OUT AT 1ST)!"

                elif bases['3RD'] == 1 and outs < 2:
                    if random.random() < 0.58:
                        outs += 1
                        runs_scored += 1
                        bases['3RD'] = 0
                        outcome = "GROUNDOUT"
                        outcomex = "(RUN SCORES FROM 3RD!)"

                    else:
                        outs += 1
                        runs_scored += 0
                        bases['3RD'] = 1
                        outcome = "GROUNDOUT"
                        outcomex = "(RUNNER HELD AT 3RD!)"

                else:
                    outs += 1
                    outcome = "GROUNDOUT"
                    outcomex = "======="
            else:
                outs += 1
                outcome = out_type
                outcomex = "======="
#########################################################################################################
        colored(print_loading_dots(), 'yellow', attrs=['bold'])
        long_wait()
        #play_sound(outcome)
        print(f"{colored('AT BAT RESULT:', 'yellow', attrs=['bold'])} {colored(outcome, 'white', attrs=['bold'])}")
        short_wait()
        print(f"{colored('RUNNER RESULT:', 'yellow', attrs=['bold'])} {colored(outcomex, 'white', attrs=['bold'])}")
        long_wait()
    

        # Update the score for the appropriate team whenever runs are scored
        if runs_scored > 0:
            if top_or_bottom == "TOP":
                current_score[0] += runs_scored
            else:
                current_score[1] += runs_scored
            runs_scored = 0 # Reset runs_scored for the next play

        # Check for walk-off condition if it's the bottom of the 9th or later
        if inning >= 9 and top_or_bottom == "BOT" and current_score[1] > current_score[0]:
            break  # Home team takes the lead, so end the inning immediately

        # Print the scoreboard at the beginning of the inning or when state changes
        print_scoreboard(inning, top_or_bottom, current_score, outs, bases, team1_abbr, team2_abbr)

    return current_score, hits, total_pitches
