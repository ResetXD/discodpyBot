from PIL import Image
import aiohttp
import aiofiles
from malapipy import anime

class getImage():
    def __init__(self) -> None:
        pass

    async def get_image_byURL(self,imgLink):
        async with aiohttp.ClientSession() as session:
            async with session.get(imgLink) as resp:
                if resp.status == 200:
                    f = await aiofiles.open('imageByUrl.jpg', mode='wb')
                    await f.write(await resp.read())
                    await f.close()
    