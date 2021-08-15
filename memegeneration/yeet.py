from PIL import Image
import aiohttp
import aiofiles

class yeet():
    def __init__(self) -> None:
        pass

    async def get_yeet(self,imgLink):
        img = Image.open('yeet.jpg')
        async with aiohttp.ClientSession() as session:
            async with session.get(imgLink) as resp:
                if resp.status == 200:
                    f = await aiofiles.open('ewtest.png', mode='wb')
                    await f.write(await resp.read())
                    await f.close()
        img1 = Image.open("ewtest.png")
        a = img1.resize(size=(170,184))
        mask = Image.new('L', a.size, 255)
        a = a.rotate(20, expand=True)
        mask = mask.rotate(20, expand=True)
        img.paste(a,(745,268),mask)
        img.show()
        img.save("ewtest.png")

