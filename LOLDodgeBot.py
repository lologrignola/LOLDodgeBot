import tweepy
import time
import requests


lolApiKey = 'RGAPI-6997979e-3d28-4ab6-9d9f-7520d46a9418'

consumer_key = 'pOX4t2xNFWGtLc6K0MXrJqMMG'
consumer_secret = 'JD3MNbPuh0Wxxw29vLI4DmzvBh9duMuep24zakZlI801I74OeH'

key = '1445453258932162568-HuRZvBtp60dXHk2PBwcjsvqhB40JYK'
secret = 'LE6vfupOZ3NMn1ruJRELLWiwsqkJa2HO8CBpLRALC5DLn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


api = tweepy.API(auth, wait_on_rate_limit=True)


viejaLista = {}
viejaListaLAS = {}
response = requests.get(
    "https://br1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
usuarios = response.json()
for usuario in usuarios['entries']:
    viejaLista[usuario['summonerName']] = usuario['leaguePoints']
response = requests.get(
    "https://br1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
usuarios = response.json()
for usuario in usuarios['entries']:
    viejaLista[usuario['summonerName']] = usuario['leaguePoints']
response = requests.get(
    "https://br1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
usuarios = response.json()
for usuario in usuarios['entries']:
    viejaLista[usuario['summonerName']] = usuario['leaguePoints']

response = requests.get(
    "https://la2.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
usuarios = response.json()
for usuario in usuarios['entries']:
    viejaListaLAS[usuario['summonerName']] = usuario['leaguePoints']
response = requests.get(
    "https://la2.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
usuarios = response.json()
for usuario in usuarios['entries']:
    viejaListaLAS[usuario['summonerName']] = usuario['leaguePoints']
response = requests.get(
    "https://la2.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
usuarios = response.json()
for usuario in usuarios['entries']:
    viejaListaLAS[usuario['summonerName']] = usuario['leaguePoints']


time.sleep(5)
while 1:
    nuevaLista = {}
    nuevaListaLAS = {}
    response = requests.get(
        "https://br1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
    usuarios = response.json()
    for usuario in usuarios['entries']:
        nuevaLista[usuario['summonerName']] = usuario['leaguePoints']
    response = requests.get(
        "https://br1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
    usuarios = response.json()
    for usuario in usuarios['entries']:
        nuevaLista[usuario['summonerName']] = usuario['leaguePoints']
    response = requests.get(
        "https://br1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
    usuarios = response.json()
    for usuario in usuarios['entries']:
        nuevaLista[usuario['summonerName']] = usuario['leaguePoints']

    for summoner in viejaLista.keys():
        try:
            if viejaLista[summoner]-nuevaLista[summoner] == 3:
                api.update_status("[BR]\n\n"+summoner + " dodgeo por 3 LPs. Sus LPs eran " +
                                  str(viejaLista[summoner])+" y ahora son "+str(nuevaLista[summoner]))
                print('[BR] Nuevo dodge (-3)')
            if viejaLista[summoner]-nuevaLista[summoner] == 10:
                api.update_status("[BR]\n\n"+summoner+" dodgeo por 10 LPs. Sus LPs eran " +
                                  str(viejaLista[summoner])+" y ahora son "+str(nuevaLista[summoner]))
                print('[BR] Nuevo dodge (-10)')
        except:
            print("[BR]"+summoner + 'bajo a diamante o subio a master')

    response = requests.get(
        "https://la2.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
    usuarios = response.json()
    for usuario in usuarios['entries']:
        nuevaListaLAS[usuario['summonerName']] = usuario['leaguePoints']
    response = requests.get(
        "https://la2.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
    usuarios = response.json()
    for usuario in usuarios['entries']:
        nuevaListaLAS[usuario['summonerName']] = usuario['leaguePoints']
    response = requests.get(
        "https://la2.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key="+lolApiKey)
    usuarios = response.json()
    for usuario in usuarios['entries']:
        nuevaListaLAS[usuario['summonerName']] = usuario['leaguePoints']

    for summoner in viejaListaLAS.keys():
        try:
            if viejaListaLAS[summoner]-nuevaListaLAS[summoner] == 3:
                api.update_status("[LAS]\n\n"+summoner + " dodgeo por 3 LPs. Sus LPs eran " +
                                  str(viejaListaLAS[summoner])+" y ahora son "+str(nuevaListaLAS[summoner]))
                print('[LAS] Nuevo dodge (-3)')
            if viejaListaLAS[summoner]-nuevaListaLAS[summoner] == 10:
                api.update_status("[LAS]\n\n"+summoner+" dodgeo por 10 LPs. Sus LPs eran " +
                                  str(viejaListaLAS[summoner])+" y ahora son "+str(nuevaListaLAS[summoner]))
                print('[LAS] Nuevo dodge (-10)')
        except:
            print("[LAS]"+summoner + 'bajo a diamante o subio a master')

    print("Nueva recorrida.")
    viejaLista = nuevaLista.copy()
    viejaListaLAS = nuevaListaLAS.copy()
    time.sleep(60)
