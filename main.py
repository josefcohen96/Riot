import requests


def get_api_key(*args, **kwargs):
    return "RGAPI-272a652d-180b-42f6-9861-bc5af2f4975f"


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
    print(1)
    print(match_data.keys())
