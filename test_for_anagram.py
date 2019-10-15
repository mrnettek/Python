# MrNetTek
# eddiejackson.net/blog
# 10/14/2019
# free for public use 
# free to claim as your own

def is_anagram(input1, input2):
    input1 = input1.lower()
    input2 = input2.lower()
    return sorted(input1) == sorted(input2)
 
print("\x1b[2J")
 
print("iceman cinema")
print(is_anagram("iceman", "cinema"))
print "\n"
 
print("leaf tree")
print(is_anagram("leaf", "tree"))
print "\n"