from mcpi.minecraft import Minecraft

omega=Minecraft.create()

user=input("Enter your name")
while True:
     message=input("Enter a message")
     omega.postToChat("<"+user+"> "+message)