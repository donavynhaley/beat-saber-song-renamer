import os
import json

for folder in os.listdir():
    # Check for fileRenamer and readme and ds store
    if folder == "fileRenamer.py" or folder == "README.md" or folder == ".DS_Store":
        continue

    # Looks in info.dat file and rename folder to _songName
    for filename in os.listdir(folder):
        if filename != "info.dat":
            continue
        f = open(folder + "/" + filename)
        data = json.load(f)
        if len(data["_songAuthorName"]) != 0:
            songName = data["_songName"] + " by " + data["_songAuthorName"]
        else:
            songName = data["_songName"] + " by " + data["_levelAuthorName"]
        try:
            os.rename(folder, songName)
        except:
            print("Could not change " + folder + " -> " + songName)
            continue
