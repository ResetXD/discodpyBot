from PIL import Image,ImageDraw,ImageFont
import asyncio
asyncio.sleep

class spongebob():
    def __init__(self) -> None:
        pass

    def sp(self,text):
        if len(text) > 13:
            text = text[ : 13] + "\n" + text[13 : ]
        img = Image.open('spongebob.jpg')
        dl = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('Dosis-Bold.ttf', 30)
        dl.text((66, 147), text, fill=(0, 0, 0), font=myFont)
        img.show()
        img.save("sponge.jpg")
