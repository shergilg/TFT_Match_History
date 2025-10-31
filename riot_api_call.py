
import time, requests as rq


# Custom class for Riot API errors
class RiotAPIError(Exception):
    """Custom exception for Riot API errors."""
    pass



class MakeRiotAPIRequest:
    """Class to handle Riot API requests with rate limiting and error handling."""

    # Constructor
    def __init__(self, api_key: str):
        self.s = rq.Session() # starting a session so don't have to keep re-authenticating
        self.s.headers.update({"X-Riot-Token": api_key}) # Adding the API key to the headers for authentication( listed on Riot API docs as X-Riot-Token)
    
    # Method to get response status with rate limit handling
    def get_status(self, url: str) -> rq.Response:
        response = self.s.get(url)
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 1))
            time.sleep(retry_after)
            response = self.s.get(url)
        # Can add other status code checks here as needed later
        if response.status_code != 200:
            raise RiotAPIError(f"Riot API returned status code {response.status_code}: {response.text}")
        return response
    
    # Method to get JSON data from the response
    def get_json(self, url: str) -> dict:
        response = self.get_status(url)
        return response.json()