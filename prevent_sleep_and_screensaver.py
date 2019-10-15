# MrNetTek
# eddiejackson.net/blog
# 10/14/2019
# free for public use 
# free to claim as your own

import ctypes
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
input('{Press enter to exit}')
ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)