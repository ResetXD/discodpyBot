from PIL import Image
import aiohttp
import aiofiles

class hellno():
    def __init__(self) -> None:
        pass

    async def get_hell_no(self,imgLink):
        img = Image.open('hellno.jpg')
        async with aiohttp.ClientSession() as session:
            async with session.get(imgLink) as resp:
                if resp.status == 200:
                    f = await aiofiles.open('ewtest.png', mode='wb')
                    await f.write(await resp.read())
                    await f.close()
        img1 = Image.open("ewtest.png")
        a = img1.resize(size=(397,329))
        img.paste(a,(543,161))
        img.show()
        img.save("ewtest.png")
