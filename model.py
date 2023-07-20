import json
import mysql.connector

HOST = "localhost"
USER = "root"
PASSWD = "mcso@123#@!"
DB = "MYANIMELIST"

Anime_Manga_News = r"/root/son/Anime_Manga_News.json"
Comment_News = r"/root/son/Comment_News.json"
Reviews_Anime = r"/root/son/Reviews_Anime.json"
Reviews_Manga = r"/root/son/Reviews_Manga.json"
Reviews_Top_Anime = r"/root/son/Reviews_Top_Anime.json"
Reviews_Top_Manga = r"/root/son/Reviews_Top_Manga.json"
Top_Anime = "/root/son/Top_Anime.json"
Top_Manga = r"/root/son/Top_Manga.json"



def get_data_json(_LINK_JSON_FILE):
    with open(_LINK_JSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
