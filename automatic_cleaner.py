import os
def createIfNotexists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def move_files(folder, files):
    for file in files:
        os.replace(file,f"{folder}/{file}")

createIfNotexists("Images")
createIfNotexists("Docs")
createIfNotexists("Media")
if __name__ == '__main__':

    files=os.listdir()
    files.remove("automatic_cleaner.py")
#print(files)
imgexts=[".png",".jpg",".jpeg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imgexts]
print(images)
docsexts=[".txt",".doc",".pdf"]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docsexts]
mediaexts=[".mp4",".mp3",".flv"]
medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaexts]

others=[] #move all the remaing files to others folder
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if ( ext not in imgexts ) and ( ext not in docsexts ) and ( ext not in mediaexts ) and os.path.isfile(file):
        others.append(file)
move_files("Images",images)
move_files("Docs",docs)
move_files("Media",medias)
