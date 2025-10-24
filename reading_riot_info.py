# -*- coding: utf-8 -*-

# Import statements for the data importing using the API key


# Let's use str | Path and -> Settings
# This will help if we define a class later in the code
# we'll strore the annotations as strings until we need to evaluate them(this will avoid NameError :) )
from __future__ import annotations

# Importing dataclass
from dataclasses import dataclass, field

# In case I need to switch between macos and windows, this is helpful so it can automatically 
# replace the operators and other methods depending on the platform
from pathlib import Path

# Our info like API_Key, region and such is stored in json file, to read that info we need to load that json file
# So import statement for json
import json


# creating dictionary to match platforms the summoner is on to appropriate region
# You cannot have na1 playing in europe or asia, we'll need a summoner account in that region.
SUMMONER_MATCH_REGIONS = {
    # Americas regions
    "na1":"americas","br1":"americas","la1":"americas","la2":"americas","oc1":"americas",
    # Europe regions
    "euw1":"europe","eun1":"europe","tr1":"europe","ru":"europe","me1":"europe",
    # Asia regions
    "kr":"asia","jp1":"asia","sg2":"asia","tw2":"asia","vn2":"asia",
}

# All the valid summoner regions:
VALID_SUMMONER_REGIONS = set(SUMMONER_MATCH_REGIONS.keys()) # get the keys from from the dictionary created above

# All the valid summoner regions:
VALID_MATCH_REGIONS = {"americas", "europe", "asia"} # manually entered the 3 possible match regions


@dataclass(frozen=True) # frozen so settings cannot be changed(after we've defined the variables in the settings)
class Settings:
    api_key: str = field(repr=False) # repr = false is need so the key doesn't turn out in any errors/logs accidently
    region_summoner: str
    region_match: str

# We'll first load the settings from our JSON file
def load_settings(path: str | Path = "riot_info.json") -> Settings:
    p = Path(path) # create a path to the file we're reading as 'p'
    try:
        read_info = json.loads(p.read_text(encoding='utf-8')) # adding utf-8 so reading and writing encoding is always this for future use
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not find the file with riot info: {p.resolve()}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in {p.name}: {e}") from e
        
    # grab the info from the Json file
    api_key = read_info.get("api_key")
    region_summoner = read_info.get("region_summoner")
    region_match = read_info.get("region_match")
    
    
    # Ensure the values aren't empty/invalid from the json file
    if not api_key:
        raise ValueError("No 'api_key' in riot_info.json (it's copied from the riot dev portal(google it)')")
    if not region_summoner:
        raise ValueError("No 'region_summoner' in riot_info.json (e.g., NA1)")
    if not region_match:
        if region_summoner in VALID_SUMMONER_REGIONS: 
            # Since we know which summoner regions belong to which match regions, we can just use our VALID_SUMMONER_REGIONS dictionary and give summoner region as a key 
            region_match = SUMMONER_MATCH_REGIONS[region_summoner]
    
    
    # I kept getting errors when there was upper case or mixture of upper and lower case I am adding this to always make it lower case :) 
    region_summoner = region_summoner.lower()
    region_match = region_match.lower()
    
    
    # This is checking for invalid region names
    if region_summoner not in VALID_SUMMONER_REGIONS:
        raise ValueError(f"Unknown Summoner Region [{region_summoner}]. Valid Summoner Regions: {sorted(VALID_SUMMONER_REGIONS)}")
    if region_match not in VALID_MATCH_REGIONS:
        raise ValueError(f"Unknown Match Region [{region_match}]. Valid Match Regions: {sorted(VALID_MATCH_REGIONS)}")
    
    return Settings(api_key=api_key, region_summoner=region_summoner, region_match=region_match)
    
    
    
    