from riotwatcher import LolWatcher, ApiError
import pandas
import re

# Initializing data
api_key = open("./RIOT_API_KEY.txt", "r").read()
watcher = LolWatcher(api_key)
my_region = 'na1'

latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
dataDragonChamps = watcher.data_dragon.champions(latest, False, )
dataDragonItems = watcher.data_dragon.items(latest, 'en_US')
dataDragonSpells = watcher.data_dragon.summoner_spells(latest, 'en_US')
champsDict = itemsDict = spellsDict = {}

for champ in dataDragonChamps["data"]:
    id = dataDragonChamps["data"][champ]["key"]
    name = dataDragonChamps["data"][champ]["name"]
    champsDict[id] = name

for item in dataDragonItems["data"]:
    id = item
    name = dataDragonItems["data"][item]["name"]
    itemsDict[id] = name

for spell in dataDragonSpells["data"]:
    id = dataDragonSpells["data"][spell]["key"]
    name = dataDragonSpells["data"][spell]["name"]
    spellsDict[id] = name

def returnChamp(champId):
    return champsDict[str(champId)]

def returnItem(itemId):
    return itemsDict[str(itemId)]

def returnSpell(spellId):
    return spellsDict[str(spellId)]

# Returns match idfrom an input match history url
def url_split(url):
    url = url[(re.search("/NA1/", url)).end():]
    url = url[:(re.search("/", url)).start()]
    return url

# Put the match Id's into a list to iterate through later
def getMatches():
    with open("urls.txt", "r") as file:
        matchUrls = [line.strip() for line in file]
    return(matchUrls)

def matchDetails(matchId):
    match_detail = watcher.match.by_id(my_region, matchId)
    participants = []
    for row in match_detail['participants']:
        participants_row = {}
        participants_row['champion'] = returnChamp(row['championId'])
        if row["teamId"] == 100:
            side = "Blue"
        elif row["teamId"] == 200:
            side = "Red"
        else:
            side = "Error"
        participants_row['Team'] = side
        participants_row['Spell 1'] = returnSpell(row['spell1Id'])
        participants_row['Spell 2'] = returnSpell(row['spell2Id'])
        if row['stats']['win'] == True:
            outcome = "Win"
        elif row['stats']['win'] == False:
            outcome = "Lose"
        else:
            outcome = "Error"
        participants_row['Win'] = outcome
        participants_row['Kills'] = row['stats']['kills']
        participants_row['Deaths'] = row['stats']['deaths']
        participants_row['Assists'] = row['stats']['assists']
        participants_row['Champ Damage'] = row['stats']['totalDamageDealtToChampions']
        participants_row['Gold'] = row['stats']['goldEarned']
        participants_row['Champ Level'] = row['stats']['champLevel']
        participants_row['CS'] = row['stats']['totalMinionsKilled']
        participants_row['Item 1'] = returnItem(row['stats']['item0'])
        participants_row['Item 2'] = returnItem(row['stats']['item1'])
        participants.append(participants_row)
    return participants

# Grab matches in matchIds.txt
matches = getMatches()

# Grab each match's information
test = []
for match in range(len(matches)):
    test.append({})
    test += matchDetails(url_split(matches[match]))

df = pandas.DataFrame(test)
df.to_csv(r'output.csv', index = False)
print(df)