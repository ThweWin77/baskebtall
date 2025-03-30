import random

players = ["Player1", "Player2", "Player3", "Player4", "Player5", 
           "Player6", "Player7", "Player8", "Player9", "Player10",
           "Player11", "Player12", "Player13", "Player14", "Player15",
           "Player16", "Player17", "Player18", "Player19", "Player20"]

random.shuffle(players)
team1 = players[:5]
team2 = players[5:10]

print("Team 1:", team1)
print("Team 2:", team2)
