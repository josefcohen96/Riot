# from riotwatcher import LolWatcher, ApiError
# import pandas as pd
# import requests
#
#
# # golbal variables
# api_key = 'RGAPI-4b2b5b37-648a-4905-8a8b-551568c0a423'
# watcher = LolWatcher(api_key)
# my_region = 'euw1'
#
# me = watcher.summoner.by_name(my_region, 'VirtualLeizLeiz')
# print(me)
# my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
# print(my_ranked_stats)
#
# my_matches = watcher.match.matchlist_by_puuid(region=my_region, puuid=me['puuid'])  # my_matches id_match for last 20 games
# # my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
#
# # fetch last match detail
# last_match = my_matches[0]  #
# # match_detail = watcher.match.by_id(my_region, last_match)
# try:
#     url = "https://europe.api.riotgames.com/lol/match/v5/matches/EUW1_6311372578" + last_match + "?api_key=" + api_key
#     participants = []
#     match_detail = watcher.match.by_id(my_region, last_match)
#     for row in match_detail['info']['participants']:
#         participants_row = {}
#         participants_row['champion'] = row['championId']
#         participants_row['win'] = row['win']
#         participants_row['kills'] = row['kills']
#         participants_row['deaths'] = row['deaths']
#         participants_row['assists'] = row['assists']
#         participants_row['totalDamageDealt'] = row['totalDamageDealt']
#         participants_row['goldEarned'] = row['goldEarned']
#         participants_row['champLevel'] = row['champLevel']
#         participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
#         participants_row['item0'] = row['item0']
#         participants_row['item1'] = row['item1']
#         participants.append(participants_row)
#         print(participants_row)
#
# except Exception as e:
#     print(e)
# # df = pd.DataFrame(participants)
# print(participants)

import riotwatcher

# Replace "YOUR_API_KEY" with your actual API key
api_key = "RGAPI-4b2b5b37-648a-4905-8a8b-551568c0a423"
watcher = riotwatcher.LolWatcher(api_key)

# Replace "SUMMONER_NAME" with the summoner name of the player you want to rate
summoner_name = "VirtualLeizLeiz"

# Retrieve the summoner ID for the specified summoner name
summoner = watcher.summoner.by_name("EUW1", summoner_name)

# Retrieve the match history for the specified summoner ID
# match_history = watcher.match.matchlist_by_account("EUW1", summoner['accountId'])
match_history = watcher.match.matchlist_by_puuid("EUW1", summoner['puuid'])

# Calculate the win rate for the last 10 matches
num_matches = 10
num_wins = 0
for i in range(num_matches):
    match_id = match_history['matches']
    match = watcher.match.by_id("EUW1", match_id)
    participant_id = None
    for participant in match['participantIdentities']:
        if participant['player']['accountId'] == summoner['accountId']:
            participant_id = participant['participantId']
            break
    if participant_id is not None:
        participant = match['participants'][participant_id - 1]
        if participant['stats']['win']:
            num_wins += 1
    print(participant)

win_rate = num_wins / num_matches
print(f"{summoner_name}'s win rate in the last {num_matches} matches is {win_rate:.2%}")


class RiotApi:


    def __init__(self):
        pass