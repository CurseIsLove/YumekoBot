import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://images3.alphacoders.com/115/1156277.png"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  YUMEKO = "**Holla I'm Izumi!** \n\n"
  YUMEKO += "×**I'm Working Properly** \n\n"
  YUMEKO += "×**My Owner : [Zeref](https://t.me/FringesBright)**× \n\n"
  YUMEKO += f"×**Telethon Version : {tlhver}** \n\n"
  YUMEKO += f"×**Pyrogram Version : {pyrover}** \n\n"
  YUMEKO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/YumekoProBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/izumibotsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  YUMEKO = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/izumibotsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)
