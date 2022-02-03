import requests
import os
from urllib.parse import quote

riotApiKey = os.environ['riotAPIKey']
print("riotAPIKey: {}".format(riotApiKey))
servers = {"BR": "https://br1.api.riotgames.com",
           "EUN": "https://eun1.api.riotgames.com",
           "EUW": "https://euw1.api.riotgames.com",
           "JP": "https://jp1.api.riotgames.com",
           "KR": "https://kr.api.riotgames.com",
           "LA1": "https://la1.api.riotgames.com",
           "LA2": "https://la2.api.riotgames.com",
           "NA": "https://na1.api.riotgames.com",
           "OC": "https://oc1.api.riotgames.com",
           "TR": "https://tr1.api.riotgames.com",
           "RU": "https://ru.api.riotgames.com"
           }

urlType = {"summonerByName": "/lol/summoner/v4/summoners/by-name/",
           "summonerByEncryptedSummonerId": "/lol/summoner/v4/summoners/",
           "rank": "/lol/league/v4/entries/by-summoner/",
           "activeGame": "/lol/spectator/v4/active-games/by-summoner/",
           "masteryInfo": "/lol/champion-mastery/v4/champion-masteries/by-summoner/",
           "championInfo": "https://ddragon.leagueoflegends.com/cdn/11.15.1/data/en_US/champion.json", #Get Update here https://developer.riotgames.com/docs/lol
           "avatar": "http://avatar.leagueoflegends.com/",
           "avatarDragon": "https://cdn.communitydragon.org/latest/profile-icon/",
           "clashPlayer": "/lol/clash/v1/players/by-summoner/",
           "clashTeam": "/lol/clash/v1/teams/",
           "clashTournament": "/lol/clash/v1/tournaments/"
           }



def getApiInfo(parameter, type, server):
    #print(f"[INFO API] {type} RequestToAPI!")
    requestUrl = f"{servers[server]}{urlType[type]}{parameter}?api_key={riotApiKey}"
    print(f"[INFO API] REQUESTURL {type}: {requestUrl}")
    requestData = requests.get(requestUrl).json()
    if requestData == []:
        return None
    return requestData

def getChampionInformation(): #Get Update here https://developer.riotgames.com/docs/lol
    requestUrl = urlType['championInfo']
    requestData = requests.get(requestUrl).json()
    return requestData

def getSummonerIconURL(server, summonerName):
    requestUrl = urlType['avatar'] + quote(f"{server}/{summonerName}.png")
    print("[INFO API] AVATAR ICON REQUEST: {}".format(url))
    return url

def getSummonerIconURL_withID(ID):
    type = 'avatarDragon'
    url = f"{urlType[type]}{ID}"
    print("[INFO API] AVATAR ICON REQUEST: {}".format(url))
    return url