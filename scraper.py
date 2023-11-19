from requests import get
from spotify_auth import get_auth_header, get_token
import json

def get_playlist_length(token, playlist_id):
    url = "https://api.spotify.com/v1/playlists/" + playlist_id + "?fields=tracks%28total%29"
    headers = get_auth_header(token)
    
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def get_playlist_item(token, playlist_id, offset):
    url = "https://api.spotify.com/v1/playlists/" + playlist_id + '/tracks?fields=items%28track%28name%29%29&limit=100&offset=' + offset
    headers = get_auth_header(token)
    
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def build_track_list(playlist_id):
    token = get_token()
    name_list = []
    
    try:
        total = get_playlist_length(token, playlist_id)
        total = total["tracks"]["total"]
        for n in range((total//100) + 1):
            try:
                items = get_playlist_item(token, playlist_id, str(n * 100))
            except: 
                print("Invalid ID")
            my_list = [[x, y] for x, y in items.items()][0][1]

            for i in range(len(my_list)):
                name_list.append(my_list[i]["track"]["name"])
    except: 
        print("Invalid ID")
    
    return name_list

