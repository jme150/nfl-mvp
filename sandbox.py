"""
    Sandbox
"""
import datetime
import settings as s

def main():

    # Initialize weekly data dictionary
    weekly_data = {}

    # Repeat this code for each player
    for player in s.player_list:
        # Initialize list to save player stats
        lines = []

        try:
            # Open player's weekly-stats file
            with open(f'weekly-stats_{player}.txt', 'r') as infile:
                # Append a list containing each line's data
                for each in infile:
                    lines.append(each.strip().split(','))

        # If the file wasn't found, print message
        except FileNotFoundError:
            print(f"Could not find file for this player: {player}")

        else:    
            # For each of the lines corresponding to weekly stats
            for i in range(2, len(lines)):
                # Split the game's date into its components
                lines[i][s.STATS_DATE] = lines[i][s.STATS_DATE].split('-')
                # Convert the date components to integers
                for j in range(len(lines[i][s.STATS_DATE])):
                    lines[i][s.STATS_DATE][j] = int(lines[i][s.STATS_DATE][j])
                
                # Replace each date with the NFL week that it corresponds with 
                for z in range(1, len(s.weeks) + 1):
                    # Define dates for comparison
                    current_date = datetime.date(lines[i][s.STATS_DATE][s.YEAR], 
                                                 lines[i][s.STATS_DATE][s.MONTH], 
                                                 lines[i][s.STATS_DATE][s.DAY])
                    start = s.weeks[z][s.WEEK_START]
                    end = s.weeks[z][s.WEEK_END]

                    # If the current date is within the dates for a given week
                    if start <= current_date <= end:
                        lines[i][s.STATS_DATE] = f"Week {z}"
                        break
            
            # Add player's data to weekly data dictionary
            weekly_data[player] = lines


            
        
    

      

                

    

if __name__ == "__main__":
    main()