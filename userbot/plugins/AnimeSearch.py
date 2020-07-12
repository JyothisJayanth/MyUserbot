"""
Anilist Search Plugin for Userbot
Usage : .anilist animeName
By :- @Zero_cool7870

"""

import requests
import json
import asyncio
from uniborg.util import admin_cmd

async def callAPI(search_str):
    query = '''
    query ($id: Int,$search: String) { 
      Media (id: $id, type: ANIME,search: $search) { 
        id
        title {
          romaji
          english
        }
        description (asHtml: false)
        startDate{
            year
          }
          episodes
          chapters
          volumes
          season
          type
          format
          status
          duration
          averageScore
          genres
          bannerImage
      }
    }
    '''
    variables = {
        'search' : search_str
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})
    return response.text

async def formatJSON(outData):
    msg = ""
    jsonData = json.loads(outData)
    res = list(jsonData.keys())
    if "errors" in res:
        msg += f"**Error** : `{jsonData['errors'][0]['message']}`"
        return msg
    else:
        jsonData = jsonData['data']['Media']
        if "bannerImage" in jsonData.keys():
            msg += f"[〽️]({jsonData['bannerImage']})"
        else:
            msg += "〽️"
        title = jsonData['title']['romaji']
        link = f"https://anilist.co/anime/{jsonData['id']}"
        msg += f"[{title}]({link})"
        msg += f"\n\n**Type** : {jsonData['format']}"
        msg += f"\n**Genres** : "
        for g in jsonData['genres']:
            msg += g+" "
        msg += f"\n**Status** : {jsonData['status']}"
        msg += f"\n**Episode** : {jsonData['episodes']}"
        msg += f"\n**Year** : {jsonData['startDate']['year']}"
        msg += f"\n**Score** : {jsonData['averageScore']}"
        msg += f"\n**Duration** : {jsonData['duration']} min"
        msg += f"\n\n __{jsonData['description']}__"
        return msg

@borg.on(admin_cmd(pattern="anilist ?(.*)", allow_sudo=True))
async def anilist(event):
	if event.fwd_from:
		return
	input_str = event.pattern_match.group(1)
	result = await callAPI(input_str)
	msg = await formatJSON(result)
	await event.edit(msg,link_preview=True)

	
import nekos
import os
import json
import aiohttp
import asyncio
import random
from jikanpy import Jikan
from jikanpy.exceptions import APIException
from urllib.parse import quote as urlencode
from telethon import events
from userbot.events import register
from userbot import CMD_HELP, bot
from asyncio import sleep


_pats = []
jikan = Jikan()



@register(outgoing=True, pattern=r"^.anime (.*)")
async def asearch(event):
    msg = event.pattern_match.group(1)
    res = ""
    try:
        res = jikan.search("anime", msg)
    except APIException:
        await event.edit("Error connecting to the API. Please try again!")
        return ""
    try:
        res = res.get("results")[0].get("mal_id") # Grab first result
    except APIException:
        await event.edit("Error connecting to the API. Please try again!")
        return ""
    if res:
        anime = jikan.anime(res)
        title = anime.get("title")
        japanese = anime.get("title_japanese")
        type = anime.get("type")
        duration = anime.get("duration")
        synopsis = anime.get("synopsis")
        source = anime.get("source")
        status = anime.get("status")
        episodes = anime.get("episodes")
        score = anime.get("score")
        rating = anime.get("rating")
        genre_lst = anime.get("genres")
        genres = ""
        for genre in genre_lst:
            genres += genre.get("name") + ", "
        genres = genres[:-2]
        studios = ""
        studio_lst = anime.get("studios")
        for studio in studio_lst:
            studios += studio.get("name") + ", "
        studios = studios[:-2]
        duration = anime.get("duration")
        premiered = anime.get("premiered")
        image_url = anime.get("image_url")
        url = anime.get("url")
        trailer = anime.get("trailer_url")
    else:
        await event.edit("No results found!")
        return
    rep = f"<b>{title} ({japanese})</b>\n"
    rep += f"<b>Type:</b> <code>{type}</code>\n"
    rep += f"<b>Source:</b> <code>{source}</code>\n"
    rep += f"<b>Status:</b> <code>{status}</code>\n"
    rep += f"<b>Genres:</b> <code>{genres}</code>\n"
    rep += f"<b>Episodes:</b> <code>{episodes}</code>\n"
    rep += f"<b>Duration:</b> <code>{duration}</code>\n"
    rep += f"<b>Score:</b> <code>{score}</code>\n"
    rep += f"<b>Studio(s):</b> <code>{studios}</code>\n"
    rep += f"<b>Premiered:</b> <code>{premiered}</code>\n"
    rep += f"<b>Rating:</b> <code>{rating}</code>\n\n"
    rep += f"<a href='{image_url}'>\u200c</a>"
    rep += f"<i>{synopsis}</i>\n"
    await event.edit(rep, parse_mode='html', link_preview = True)
    
