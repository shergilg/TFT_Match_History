# -*- coding: utf-8 -*-

from reading_riot_info import load_settings
import requests as rq


# loading settings:
s = load_settings()

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






