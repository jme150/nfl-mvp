"""
    NFL MVP Tracker -- Constants/Set-Up
    Judah Ellison
    December 2023/January 2024
"""
# Imports
import turtle
import datetime

# Constant variables
player_list = ["allen", "burrow", "herbert", "hurts", "jackson", "mahomes", 
            "mccaffrey", "prescott", "purdy", "tagovailoa"]
weeks = {1: [datetime.date(2023, 9, 7), datetime.date(2023, 9, 11)], 
         2: [datetime.date(2023, 9, 14), datetime.date(2023, 9, 18)], 
         3: [datetime.date(2023, 9, 21), datetime.date(2023, 9, 25)], 
         4: [datetime.date(2023, 9, 28), datetime.date(2023, 10, 2)], 
         5: [datetime.date(2023, 10, 5), datetime.date(2023, 10, 9)], 
         6: [datetime.date(2023, 10, 12), datetime.date(2023, 10, 16)], 
         7: [datetime.date(2023, 10, 19), datetime.date(2023, 10, 23)], 
         8: [datetime.date(2023, 10, 26), datetime.date(2023, 10, 30)], 
         9: [datetime.date(2023, 11, 2), datetime.date(2023, 11, 6)], 
         10: [datetime.date(2023, 11, 9), datetime.date(2023, 11, 13)], 
         11: [datetime.date(2023, 11, 16), datetime.date(2023, 11, 20)], 
         12: [datetime.date(2023, 11, 23), datetime.date(2023, 11, 27)], 
         13: [datetime.date(2023, 11, 30), datetime.date(2023, 12, 4)], 
         14: [datetime.date(2023, 12, 7), datetime.date(2023, 12, 11)], 
         15: [datetime.date(2023, 12, 14), datetime.date(2023, 12, 18)], 
         16: [datetime.date(2023, 12, 21), datetime.date(2023, 12, 25)], 
         17: [datetime.date(2023, 12, 28), datetime.date(2023, 12, 31)], 
         18: [datetime.date(2024, 1, 6), datetime.date(2024, 1, 7)]}

# Index constants for weeks dictionary (defined in settings.py)
YEAR = 0
MONTH = 1
DAY = 2

WEEK_START = 0
WEEK_END = 1

# Index constants for statistics
STATS_DATE = 0

# Turtle screen setup
screen = turtle.Screen()
screen.setup(1400, 800)
screen.title("NFL MVP Tracker")