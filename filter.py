from scraper import build_track_list
import collections

def find_dups(playlist_id):    
    list = build_track_list(playlist_id)

    dup = [item for item, count in collections.Counter(list).items() if count > 1]
    return dup
