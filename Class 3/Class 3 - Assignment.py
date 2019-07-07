#1.
if if __name__ == '__main__':
    try:
        a = 1 / 0

#2.
if if __name__ == '__main__':
    try:
        a = 1 / 0
    except:
        print("Avoid Exception")

#3.
Yes, we can combine try with except and finally.

#4.
All types of exceptions.

#5.
It's almost always better to specify an explicit exception type.
this can hide bugs or make it harder to debug programs when they aren't doing what you expect.

#6.
Except IOError : handles input/otuput exceptions:
Except ZeroDivisionError : the next argument of a division is zero.

#7-9.

f = open("/Users/yishaihalpert/Desktop/words.txt", "a")
f.write("Yishai Halpert")
f = open("/Users/yishaihalpert/Desktop/words.txt", "r")
print(f.read())

#10.

f = open("/Users/yishaihalpert/Desktop/hebrew.txt" ,'a' ,encoding='utf-8')
f.write("ישי הלפרט")
f = open("/Users/yishaihalpert/Desktop/hebrew.txt", "r")
print(f.read())

#11,
from PIL import Image, ImageDraw
img = Image.new('RGB', (100, 30), color=(73, 109, 137))
d = ImageDraw.Draw(img)
d.text((10, 10), "My Image File", fill=(255, 255, 0))
img.save('/Users/yishaihalpert/Desktop/pil_text.png')