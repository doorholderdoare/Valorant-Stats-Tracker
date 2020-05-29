import time
import datetime
import random

posts = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th'}

def positonal(number):
    if number % 100 >= 10 and number % 100 <= 20:
        post = 'th'
    else:
        post = posts.get(number % 10, 'th')

    return str(number) + post

print("""  
,------.                                                   ,--.                ,---.         ,--.    
|  .--. ',--.--. ,---.  ,---. ,--.--. ,--,--.,--,--,--.    |  |-.,--. ,--.    '   .-'  ,---. |  |-.  
|  '--' ||  .--'| .-. || .-. ||  .--'' ,-.  ||        |    | .-. '\  '  /     `.  `-. | .-. :| .-. ' 
|  | --' |  |   ' '-' '' '-' '|  |   \ '-'  ||  |  |  |    | `-' | \   '      .-'    |\   --.| `-' | 
`--'     `--'    `---' .`-  / `--'    `--`--'`--`--`--'     `---'.-'  /       `-----'  `----' `---'  
                       `---'                                     `---'                                               
""")
time.sleep(2)
print("Valorant Stat Tracker [Keep track of your stats.]")
time.sleep(3)

limit = 70

assist_responses = ["Damn bro, people seem to be scared of you be more friendly.",
"Bro you are really good if people don't be stealing your kills like that",
"Holy jebuz lord. Well played don't let them steal your kills like that!"]

death_responses = ["Damn bro, you're not very good, you'll improve the longer you play",
"Holy cow, you aren't doing very well, try watching some videos to improve?",
"Seems like you're getting better to me, your stats are improving"]

while True:
    your_score = int(input("How many rounds did your team win?\n"))
    while True:
        if your_score > 13:
            print(f"Sorry, current round limit is 13. {your_score} is invialid")
            time.sleep(2)
            your_score = int(input("How many rounds did your team win?\n"))
        else:
            break
    
    enemy_score = int(input("How many rounds did the enemy win?\n"))
    while True:
        if your_score == 13:
            if enemy_score >= 13:
                print(f"Sorry, you can't draw with enemy team. {enemy_score} is invalid must be 12 or lower")
                time.sleep(2)
                enemy_score = int(input("How many rounds did the enemy win?\n"))
            elif enemy_score <= 12:
                break
            
        if your_score < 13:
            if enemy_score < 13:
                print(f"Sorry, it seems you have lost the game. {enemy_score} is invalid, must be 13.")
                time.sleep(2)
                enemy_score = int(input("How many rounds did the enemy win?\n"))
            elif enemy_score == 13:
                break
            elif enemy_score > 13:
                print(f"The enemy team can't exceed Valorant's round limit of 13. {enemy_score} is invalid, must be 13 or lower.")
                time.sleep(2)
                enemy_score = int(input("How many rounds did the enemy win?\n"))

    kills = int(input("How many kills did you get?\n"))
    while True:
        if kills > limit:
            print("That is basically impossible. You'd have to get 6 kills or more a round for that...")
            time.sleep(2)
            kills = int(input("How many kills did you get?\n"))
            if kills >= 25:
                print("you're pro man, damn..")
                time.sleep(2)
                break
            elif kills <= 15:
                print(f"{random.choice(death_responses)}")
                time.sleep(2)
                break
        else:
            break


    deaths = int(input("How many deaths did you have?\n"))
    while True:
        if deaths > 30:
            print("Wow, that's nearly impossible due to there being only 25 rounds in a game including Sage's Ultimate.")
            time.sleep(2)
            deaths = int(input("How many deaths did you have?\n"))
            if deaths >= 20:
                print(f"{random.choice(death_responses)}")
                break
            elif deaths <= 5:
                print("You are pro men")
            
                break
        else:
            break

    assists = int(input("How many assists did you have\n"))
    while True:
        if assists > 10:
            print("Damn bro tell them to stop your stealing your kills...")
            break
        elif assists < 10:
            print(f"{random.choice(assist_responses)}")
            break

    leaderboard_placement = int(input("What place were you on the leaderboard?\n"))
    while True:
        if leaderboard_placement > 5:
            print(f"Sorry, but there are only 5 spots on the leaderboard. {leaderboard_placement} is invalid")
            time.sleep(2)
            leaderboard_placement = int(input("What place were you on the leaderboard?\n"))
        else: 
            break

    nn = positonal(leaderboard_placement)        
    kd = kills / deaths
    kda = kills / deaths / assists
    ka = kills / assists
    da = deaths / assists

    f = datetime.datetime.now()
    time = f.strftime("%x")
    dayt = f.strftime("%X")

    x = open("Valorant Games.txt", "a")
    x.write(f"""
=======================================
|          Date/Time of save          
=======================================
| Date - {time}         
| Time Recorded - {dayt}
=======================================
|             Game Info               
=======================================
| Rounds Won - {your_score}
| Rounds Lost - {enemy_score}
=======================================
|            Personal Info            
=======================================
| Kils - {kills}
| Deaths - {deaths}
| Assists - {assists}
| Leaderboard Placement - {nn}
=======================================
|            In-depth Info            
=======================================
| K/D - {round(kd, 2)}
| K/D/A - {round(kda, 2)}
| K/A - {round(ka, 2)}
| D/A - {round(da, 2)}
=======================================


    """)
    x.close()

    print("Everything has been written in a file")

    end = input("Press enter to exit the program")
    exit()