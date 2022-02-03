from gameInfoRequests import *
import re
import classModule

def messageHandler(message):
    print(f'[INFO] New Message {message}')
    returnText = 'Woah'
    if message.startswith("\clash:"):
        summonerName = message.split('\clash:', 1)[1].strip()
        returnText = getClashTeam(summonerName)
    return returnText


def getClashTeam(summonerName):
    id = getApiInfo(summonerName, 'summonerByName', 'EUW')['id']
    teamId = getApiInfo(id, 'clashPlayer', 'EUW')[0]['teamId']
    clashTeam = getApiInfo(teamId, 'clashTeam', 'EUW')
    team = classModule.clashTeam()
    team.setClashTeamInfo(clashTeam)
    players = []
    for i, player in enumerate(team.players):
        summonerInfo = getApiInfo(player['summonerId'], 'summonerByEncryptedSummonerId', 'EUW')
        summoner = classModule.summoner("summonerName")
        summoner.setSummonerInfo(summonerInfo)
        players.append(summoner)
    team.playerClasses = players
    print("------")
    returnText = ''
    opggUrl = 'https://euw.op.gg/multi/query='
    for player in team.playerClasses:
        text = f'{player.name} {player.summonerLevel}'
        opggUrl += quote(f'{player.name},')
        print(text)
    opggUrl = opggUrl
    return opggUrl