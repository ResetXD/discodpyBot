from user import User
from init import Init
import asyncio
from beatmap import Beatmap

async def main():
    token = Init(key= "93356998b70d759b28c97b5ac1a4276f8e747d47")
    user = User(token=token)
    map = Beatmap(token=token)
    a = await user.get_user_best_one(username="ResetXD")
    beat = await map.get_beatmap(beatmapID=a["beatmap_id"])
    print(beat["title"])
asyncio.run(main())