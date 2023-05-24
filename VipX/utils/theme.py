## this code is added by the (C) TheTeamKHUSHI on 7th March
# Copyright (C) 2021-2022 by Y0UR_ALEX @ Github, < https://github.com/Khushijha5544/Khushi >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © vc-Bot © Khushi © Yukki


import random
from VipX.utils.database import get_theme

themes = [
    "alexa1",
    "alexa2",
    "alexa3",
    "alexa4",
    "alexa5",
    "alexa6",
    "alexa7",
    "alexa8",
]


async def check_theme(chat_id: int):
    _theme = await get_theme(chat_id, "theme")
    if not _theme:
        theme = random.choice(themes)
    else:
        theme = _theme["theme"]
        if theme == "Random":
            theme = random.choice(themes)
    return theme
