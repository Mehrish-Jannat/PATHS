import os
import shutil
#print(os.system("date"))
#os.mkdir("/Users/JANNAT/Desktop/Fish")
#print(os.getcwd())
#print (os.path.exists("/Users/JANNAT/Desktop/water"))
#x = os.path.splitext("/Users/JANNAT/Desktop/Python/fly.py")
#print(x[1])

src = input("Enter source path: ")
dest = input("Enter destination path: ")
src = src+"/"
dest = dest+"/"
f = os.listdir(src)
for i in f :
    shutil.copy((src+i),dest)
