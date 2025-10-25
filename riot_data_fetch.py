# -*- coding: utf-8 -*-

from reading_riot_info import load_settings # Just loading my settings from the reading_riot_info.py
import requests as rq # to send request to the Riot API
import time # time to create delays


# loading settings:
s = load_settings()

class RateLimit(Exception): # this is so I don't run into ratelimit...
    pass




def platform_host() -> str:
    return f"https://{s.region_summoner}.api.riotgames.com"

def regional_host() -> str:
    return f"https://{s.region_match}.api.riotgames.com"

    
def riot_acc_url(game_name: str, tag_line: str) -> str:
    region = regional_host()
    api_key = s.api_key
    return f"{region}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={api_key}"


# will update later, just want to see if I am getting code =200
riot_url_to_get_my_account = riot_acc_url(game_name="Roronoa", tag_line="8728")

request_to_riot_api = rq.get(riot_url_to_get_my_account)
print(request_to_riot_api) # YAAAAASSSSSS...... I AM GETTING HTTP code 200 WOOOHOOOO


if request_to_riot_api.status_code == 200:
    summoner_data_json = request_to_riot_api.json() # Checking if the summoner data is coming through

print(summoner_data_json)






