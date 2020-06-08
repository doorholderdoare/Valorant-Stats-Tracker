import time
from colored import fg
from random import choice
import datetime

# Leaderboard fixer
posts = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th'}

def positional(number):
    if number % 100 >= 10 and number % 100 <= 20:
        post = 'th'
    else:
        post = posts.get(number % 10, 'th')

    return str(number) + post

print(fg("red") + "Valorant Stat Logger" + fg("white") + " - " + fg("green") + "Re-programmed\n\n" + fg("white"))
time.sleep(1.3)

# Limits
klimit = 70
dlimit = 35
alimit = 35
llimit = 5
rlimit = 13

# Character Dict
agents = {"Breach", "Brimstone", "Cypher", "Jett", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Sova", "Viper", "breach", "brimstone", "cypher", "jett", "omen", "phoenix", "raze", "reyna", "sage", "sova", "viper"}

# Questions
while True:
    yourkills = int(input("How many kills did you get?\n[-] "))
    while True:
        if yourkills > klimit:
            print(fg("red") + "[ERROR] " + fg("white") + f"Current input [{yourkills}] goes over the current limit ({klimit})")
            time.sleep(1)
            yourkills = int(input("How many kills did you get?\n[-] "))
        else:
            break
            
    yourdeaths = int(input("How many deaths did you get?\n[-] "))
    while True:
        if yourdeaths > dlimit:
            print(fg("red") + "[ERROR] " + fg("white") + f"Current input [{yourdeaths}] goes over the current limit ({dlimit})")
            time.sleep(1)
            yourdeaths = int(input("How many deaths did you get?\n[-] "))
        else: 
            break

    yourassists = int(input("How many assists did you get?\n[-] "))
    while True:
        if yourassists > alimit:
            print(fg("red") + "[ERROR] " + fg("white") + f"Current input [{yourassists}] goes over the current limit ({alimit})")
            time.sleep(1)
            yourassists = int(input("How many assists did you get?\n[-] "))
        else:
            break

    yourchar = input("What character did you play?\n[-] ").casefold()
    while True:
        if yourchar in agents:
            break
        else:
            print(fg("red") + "[ERROR] " + fg("white") + f"{yourchar} is not a currently an agent in Valorant")
            time.sleep(1)
            yourchar = input("What character did you play?\n[-] ").casefold()

    yourscore = int(input("How many rounds did your team win?\n[-] "))
    while True:
        if yourscore > rlimit:
            print(fg("red") + "[ERROR] " + fg("white") + f"Amount of rounds given exceeds current limit (13)")
            time.sleep(1)
            yourscore = int(input("How many rounds did your team win?\n[-] "))
        else:
            break

    enemyscore = int(input("How many rounds did the enemy team win?\n[-] "))
    while True:
        if enemyscore > rlimit:
            print(fg("red") + "[ERROR] " + fg("white") + f"Amount of rounds given exceeds current limit (13)")
            time.sleep(1)
            enemyscore = int(input("How many rounds did the enemy team win?\n[-] "))
        if enemyscore == yourscore:
            print(fg("red") + "[ERROR] " + fg("white") + f"Variable [YourScore] already meets the limit (13)")
            time.sleep(1)
            enemyscore = int(input("How many rounds did the enemy team win?\n[-] "))
        if yourscore < rlimit:
            print(fg("red") + "[ERROR] " + fg("white") + f"{yourscore} is lower than the round limit, making it impossible for no teams to win")
        else:
            break

    leaderboard = int(input("What place did you get on the leaderboard?\n[-] "))
    while True:
        if leaderboard > llimit:
            print(fg("red") + "[ERROR] " + fg("white") + f"Input given exceeds the current leaderboard placement (5)")
            time.sleep(1)
            leaderboard = int(input("What place did you get on the leaderboard?\n[-] "))
        else:
            break
    
    lpl = positional(leaderboard)
    kd = yourkills / yourdeaths
    kda = yourkills / yourdeaths / yourassists
    ka = yourkills / yourassists
    da = yourdeaths / yourassists
    
    f = datetime.datetime.now()
    date = f.strftime("%x")
    time = f.strftime("%X")
    

    file = open("Valorant Stat Logger.txt", "a")
    file.write(f"""
======================
Valorant Stat Logger - Re-programmed
======================
Time Logged
======================
Date - {date}
Time - {time}
======================
Game Info -
======================
Character - {yourchar.capitalize()}
Kills - {yourkills}
Deaths - {yourdeaths}
Assists - {yourassists}
------------------------------
Rounds won - {yourscore}
Rounds lost - {enemyscore}
------------------------------
Leaderboard Placement - {lpl}
======================
K/D/A Info -
======================
K/D - {round(kd, 2)}
K/D/A - {round(kda, 2)}
K/A - {round(ka, 2)}
D/A - {round(da, 2)}
======================

""")
    file.close()

    exit()
