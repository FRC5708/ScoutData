import csv

class TeamStats:
    def __init__(self, teamNum):
        self.teamNum = teamNum
        self.best = [0, 0 ,0]
        self.avrg = [0, 0, 0]
        self.matchCount = 0

    def addData(self, row):
        try:
            for i in range(3):
                self.avrg[i] += int(row[i + 1])
                if (self.best[i] < int(row[i + 1])):
                    self.best[i] = int(row[i + 1])
            self.matchCount += 1
        except:
            pass
        
    def printData(self):
        if self.matchCount == 0:
            return
        print(f"High:[best={self.best[0]}; avrg={self.avrg[0] / self.matchCount}] | Low:[best={self.best[1]}; avrg={self.avrg[1] / self.matchCount}] | Bar: 2[best={self.best[2]}; avrg={self.avrg[2] / self.matchCount}]")

def sortCompare0(a, b):
    if ((a.avrg[0] / a.matchCount) > (b.avrg[0] / b.matchCount)):
        return 1
    if ((a.avrg[0] / a.matchCount) < (b.avrg[0] / b.matchCount)):
        return -1
    return 0

teams = {}
teamStats = {} 


with open('5708scouting.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data:
        teamName = row[0]
        if not teamName in teams:
            teams[teamName] = TeamStats(int(teamName))
        teams[teamName].addData(row)

teamData = []

for v in teams.keys():
    teamData.append(teams[v])

choice = input("Enter Sorting Param [high, low, bar]: ").lower()
if "low" in choice:
    choice = 1
elif "bar" in choice:
    choice = 2
else:
    choice = 0


idx = 0
teamData = sorted(teamData, key=lambda x: (x.avrg[choice] / x.matchCount))

for t in teamData:
    print(f"#{t.teamNum} -> ", end="")
    t.printData()

#for teamName in teams.keys():


