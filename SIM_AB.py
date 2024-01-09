from SIM_FUNCTIONS import *
from SIM_BOXSCORE import *
from SIM_INN import *
from SIM_ROSTERS import *

### PITCHER VS BATTER OUTCOME PROBABILITY FORMULA
def calculate_probability_based_on_your_formula(batter_attr, pitcher_attr, league_avg):
    GR = (1+math.sqrt(5))/2
    E = math.e
    b = 2 - GR/7
    BISMO_Ei = ((1/E+math.sqrt((1/E)**2+4))/2-1)**b
    RN = random.randint(880000,1040000)/1000000

    probability = (((((((batter_attr-league_avg)/math.sqrt(league_avg*math.sqrt(1-league_avg)))+((pitcher_attr-league_avg)/math.sqrt(league_avg*math.sqrt(1-league_avg)))+(((batter_attr/league_avg-1)+(pitcher_attr/league_avg-1))*BISMO_Ei))/GR)*math.sqrt(league_avg*math.sqrt(1-league_avg)))+league_avg)*RN)

    return probability

def update_batter_probabilities(batter, pitcher, league_averages):
    for outcome in batter['attributes'].keys():
        batter_attr = batter['attributes'][outcome]
        pitcher_attr = pitcher['attributes'][outcome]
        league_avg = league_averages[outcome]

        # Calculate new probability using your complex formula
        new_probability = calculate_probability_based_on_your_formula(batter_attr, pitcher_attr, league_avg)
        batter['attributes'][outcome] = new_probability
    return batter

def simulate_at_bat(batter, pitcher):
    # Add the logic to simulate an at-bat using the updated probabilities here
    outcome = np.random.choice(list(batter['attributes'].keys()), p=list(batter['attributes'].values()))
    return outcome

def simulate_pitch_count(outcome):
    if outcome == "STRIKEOUT":
        return np.random.randint(3, 7)  # At least 3 pitches, could be more
    elif outcome == "WALK":
        return np.random.randint(4, 7)  # At least 4 pitches, could be more
    elif outcome in ["SINGLE", "DOUBLE", "TRIPLE", "HOMERUN"]:
        return np.random.randint(1, 7)  # Assume 1-3 pitches for a hit
    else:
        return np.random.randint(1, 7)  # Assume 1-3 pitches for an out