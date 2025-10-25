# TFT_Match_History
 This will fetch the data from recent TFT matches and clean/organize it nicely
 
 
You'll need the API_KEY for this to work. To obtain the API_KEY, go to https://developer.riotgames.com/ and request an API_KEY :) 


Current Python version: 3.12.11
IDE: Sypder 6.1.0

Files:
- riot_info - Example.json
-- [An Example]This stores the local information like API_Key and other variables. May add the webaddresses here than declaring variables in the code...
- reading_riot_info.py
-- We're just reading info from a local json file that contains information to make an api call to the riot servers
- riot_data_fetch.py
-- This fetches the data from the riot servers. I am unsure yet, if I want this to be general and then later use to make any type of call for different datasets but this is what it is right now.


Info on Type hints:
- annotations to describe the expected types of variables. Very helpful for type checkers with catching bugs early and give better autocompletion :) 
- need 'from __future__ import annotations' currently in the reading_riot_info.py

--------------------------------------------------------------------------------------------------------
I'll slowly keep adding to this as my repo gets filled. For now, above is true for what I've done so far
--------------------------------------------------------------------------------------------------------