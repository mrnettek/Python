# MrNetTek
# eddiejackson.net/blog
# 10/14/2019
# free for public use 
# free to claim as your own

import os.path
 
textFile = "/Users/Shared/TextFile.txt"
doesFileExist=os.path.isfile(textFile)
if doesFileExist == True:
    file = open(textFile,"r")
    lines=file.read().splitlines()
    global line1
    global line2
    line1 = lines[0]
    line2 = lines[1]
    file.close()