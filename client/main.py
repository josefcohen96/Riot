import requests


def get_api_key(*args, **kwargs):
    return "RGAPI-4b2b5b37-648a-4905-8a8b-551568c0a423"


def get_api(*args, **kwargs):
    return "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/VirtualLeizLeiz"


if __name__ == '__main__':
    key = get_api_key()
    api = get_api()
    url = api + "?api_key=" + key
    result = requests.get(url)
    match_data = result.json()
    print(result)
    print(match_data)
    print(match_data.keys())
