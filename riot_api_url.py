
from __future__ import annotations
from reading_riot_info import Settings, load_settings


#-----------------------------------------------------------------------------------------------------------------------
# Helper functions to build URLs for Riot API endpoints
def platform_host(settings: Settings) -> str:
    return f"https://{settings.region_summoner}.api.riotgames.com"

print(platform_host(load_settings()))  # Example usage; remove or comment out in production code

def regional_host(settings: Settings) -> str:
    return f"https://{settings.region_match}.api.riotgames.com"

#-----------------------------------------------------------------------------------------------------------------------
# URL builders for specific Riot API endpoints

# URL builder for account by Riot ID endpoint
def account_by_riot_id_url(settings: Settings, game_name: str, tag_line: str) -> str:
    region = regional_host(settings)
    return f"{region}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"

# URL builder for match IDs by PUUID endpoint
def match_ids_by_puuid_url(settings: Settings, puuid: str, *, # this is to that count, startTime, endTime are keyword only
                           start: int = 0, count: int = 20,
                  startTime: int | None = None, endTime: int | None = None, queue: int | None = None) -> str:
    region = regional_host(settings) # settings the region from helper function
    filters = [f"start={start}", f"count={count}"] # list to hold the filters

    # startTime in epoch seconds(we get this from match details)
    # endTime in epoch seconds(we get this from match details)
    # eg. in the natch details, within info, there's "game_datetime": 1761342218414 <--this is in epoch seconds
    if startTime is not None: 
        filters.append(f"startTime={int(startTime)}")
    if endTime   is not None: 
        filters.append(f"endTime={int(endTime)}")
    if queue     is not None: 
        filters.append(f"queue={int(queue)}")
    return f"{region}/tft/match/v1/matches/by-puuid/{puuid}/ids?{'&'.join(filters)}"

# URL builder for match details endpoint
def match_details_url(settings: Settings, match_id: str) -> str:
    region = regional_host(settings)
    return f"{region}/tft/match/v1/matches/{match_id}"
