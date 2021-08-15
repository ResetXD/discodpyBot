from PIL import Image
import aiohttp
import aiofiles

class face():
    def __init__(self) -> None:
        pass

    async def get_face(self,imgLink):
        img = Image.open('mask.jpg')
        async with aiohttp.ClientSession() as session:
            async with session.get(imgLink) as resp:
                if resp.status == 200:
                    f = await aiofiles.open('ewtest.png', mode='wb')
                    await f.write(await resp.read())
                    await f.close()
        img1 = Image.open("ewtest.png")
        a = img1.resize(size=(138,144))
        img.paste(a,(138,640))
        img.show()
        img.save("ewtest.png")
