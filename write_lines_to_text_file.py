# MrNetTek
# eddiejackson.net/blog
# 10/14/2019
# free for public use 
# free to claim as your own

import os.path
  
textFile = "c:\\Users\\Shared\\TextFile.txt"
doesFileExist=os.path.isfile(textFile)
if doesFileExist == True:
    file = open(textFile,"w+")#w+ w, a+, r
    file.write('Write to textfile 1\n')
    file.write('Write to textfile 2\n')
    file.write('Write to textfile 3\n')
    file.close()