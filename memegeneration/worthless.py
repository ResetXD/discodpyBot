from PIL import Image,ImageDraw,ImageFont


class Worthless():
    def __init__(self) -> None:
        pass

    def worthless(self,text):
        if len(text) > 32:
            text = text[ : 32] + "\n" + text[32 : ]
        img = Image.open('worthless.jpg')
        dl = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('Dosis-Bold.ttf', 20)
        dl.text((104, 92), text, fill=(0, 0, 0), font=myFont)
        img.show()
        img.save("worthsend.jpg")
