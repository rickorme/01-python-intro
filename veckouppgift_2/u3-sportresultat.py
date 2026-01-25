"""
Tottenham are playing Liverpool in the Champions League.
Write a program that asks the user how many goals each team scored, and tells which team won.
Example output:

The match is over, now we will calculate the result!
How many goals did Tottenham score? 2
How many goals did Liverpool score? 1
Tottenham won!

Version 2: the program should tell if it was a draw.

Version 3: now the program should tell how many more goals the team won by. Example:
Tottenham won by 1 goal!
"""
print("\n")
print("⚽"*5,"It's the Champions League tonight!","⚽"*5,"\n")

home_team = input("Who is the home team? (default = Tottenham): ") or "Tottenham"
away_team = input("Who is the away team? (default = Liverpool): ") or "Liverpool"

print("\n")
print("⚽"*5,f"The match between {home_team} and {away_team} is now over!","⚽"*5,"\n")

home_team_score = int(input(f"How many goals did {home_team} score? "))
away_team_score = int(input(f"How many goals did {away_team} score? "))

print(f"\nThe final score was {home_team} {home_team_score} - {away_team_score} {away_team}.\n")

draw = False

if home_team_score == away_team_score:
    draw = True
elif home_team_score > away_team_score:
    winner = home_team
    margin = home_team_score - away_team_score
else:
    winner = away_team
    margin = away_team_score - home_team_score

if draw:
    analysis = "The match was drawn 🥱"
else:
    if margin > 1:
        goal_string = "goals"
    else:
        goal_string = "goal"

    analysis = f"{winner} wom the match by {margin} {goal_string}! 🏆"

print("⚽"*5,analysis,"⚽"*5)

