from PIL import Image
import aiohttp
import aiofiles

class ew():
    def __init__(self) -> None:
        pass

    async def get_ew_img(self,imgLink):
        img = Image.open('ew.png')
        async with aiohttp.ClientSession() as session:
            async with session.get(imgLink) as resp:
                if resp.status == 200:
                    f = await aiofiles.open('ewtest.png', mode='wb')
                    await f.write(await resp.read())
                    await f.close()
        img1 = Image.open("ewtest.png")
        a = img1.resize(size=(1996,1141))
        img.paste(a,(2,1125))
        img.show()
        img.save("ewtest.png")
