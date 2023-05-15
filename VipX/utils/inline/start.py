from typing import Union
import re
import os
from os import getenv

from dotenv import load_dotenv

from pyrogram import filters


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
load_dotenv()
YOUR_GROUP = getenv("YOUR_GROUP", "")
YOUR_CHANNEL = getenv("YOUR_CHANNEL", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")

def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="αdd mє вαвч",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ϝҽαƚυɾҽ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙ᏕᏋᏖᏖᎥᏁᎶ⚙", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" αdd mє вαвч ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Ꭷ𝒘𝒏𝒆𝒓", url=f"https://t.me/Its_ME_KHUSHI_01",
            ),
            InlineKeyboardButton(
                text="𝒉𝒆𝒍𝒑", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᎶᏒᎧʊք", url=f"https://t.me/Ajanabee_Duniya",
            ),
            InlineKeyboardButton(
                text="ᏦᏂυʂԋι", url=f"https://t.me/ab_krishna_uff",
            )
        ],
        [
            InlineKeyboardButton(
                text="ѕσʋяcɛ",
                url=f"https://t.me/ab_krishna_uff",
            )
        ],
     ]
    return buttons
