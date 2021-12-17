from PIL import Image
from sense_hat import SenseHat




im = Image.open("img")
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im,im)

bg = bg.resize((8,8))
bg.save("img.jpg")


sh = SenseHat()

sh.clear()

sh.load_image("img.jpg")
