from PIL import Image
from gtts import gTTS
import os
from pathlib import Path
import time

def set_image(letter):
    print (f"{letter}")
    folder=Path.cwd()
    file=f"{letter}.jpg"
    print(file)
    path=os.path.join(folder,file)
    print(path)

    #path=f"{folder}\{file}"
    #A=Image.open(path)
    with Image.open(path) as img:
        img.show()
      #  A.close()


def converttospeech(letter,word):
    text = f"{letter} for {word}"
    print(text)
    language = 'en'
    speech = gTTS(text=text, lang=language, slow=True)
    speech.save("text.mp3")
    os.system("start text.mp3")

letters=["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
words=["Apple","Ball","Cat","Dog","Elephant","Fox","Goat","Horse","Icecream","Juice","King","Lion","Monkey","Nest","Orange","Parrot","Queen","Rat","Sheep","Tiger","Umbrella","Violine","Wall","Yatch","Zebra"]
#images=["A.jpg","B.jpg","C.jpg","D.jpg","E.jpg","F.jpg","G.jpg","H.jpg","I.jpg","J.jpg","K.jpg","L.jpg","M.jpg","N.jpg","O.jpg","P.jpg","Q.jpg","R.jpg","S.jpg","T.jpg","U.jpg","V.jpg","W.jpg","X.jpg","Y.jpg","Z.jpg"]
for l in letters:
    for w in words:
        if l=='A' and w=="Apple":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='B' and w=="Ball":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='C' and w=="Cat":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='D' and w=="Dog":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='E' and w=="Elephant":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='F' and w=="Fox":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='G' and w=="Goat":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='H' and w=="Horse":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='I' and w=="Icecream":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='J' and w=="Juice":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='K' and w=="King":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='L' and w=="Lion":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='M' and w=="Monkey":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='N' and w=="Nest":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='O' and w=="Orange":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='P' and w=="Parrot":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='Q' and w=="Queen":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='R' and w=="Rat":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='S' and w=="Sheep":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='T' and w=="Tiger":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='U' and w=="Umbrella":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='V' and w=="Violine":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='W' and w=="Wall":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='X' and w=="Xylophone":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='Y' and w=="Yatch":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)
        if l=='Z' and w=="Zebra":
            set_image(l)
            time.sleep(1)
            converttospeech(l, w)














