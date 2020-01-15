import math
import base64 as b64
from PIL import Image, ImageDraw 

def encode():
	text = b64.b64encode(str.encode(input("Enter text: ")))

	l = []
	for i in text:
		l.append(i)

	wh = math.ceil(math.sqrt(len(text)))
	img = Image.new("RGB", (wh, wh))
	draw = ImageDraw.Draw(img)

	for x in range(img.size[0]):
		for y in range(img.size[1]):

			if len(l) > 0:
				color = l.pop()
			else:
				color = 0
			draw.point((x, y), (color, color, color))

	img.save("result.png", "PNG")
	print("\nSuccess! File \"result.png\" are saved!" )


def decode():
	path = input("Enter path of file: ")
	if (path[-1:] == "\'" and path[:1] == "\'") or (path[-1:] == "\"" and path[:1] == "\""):
		path = path[1:-1]

	l = []
	img = Image.open(path)
	pix = img.load()

	for x in range(img.size[0]):
		for y in range(img.size[1]):

			color = pix[x, y][0]
			l.append(color)

	l.reverse()

	print( "\nResult: "+b64.b64decode(str.encode("".join(map(chr, l)))).decode("utf-8") )



r = input("1 - Encode text;\n2 - Decode text;\n3 - About author;\n-")
if(r == "1"):
	encode()
elif(r == "2"):
	decode()
elif(r == "3"):
	print("© Andrey Ivanov\nEmail: andreie5555@gmail.com\n15.01.2020")
else:
	print("Error")