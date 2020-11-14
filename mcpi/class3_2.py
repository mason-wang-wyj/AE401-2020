from mcpi.minecraft import Minecraft
omega=Minecraft.create()
import time

count=0

while count<10:
    x,y,z=omega.player.getTilePos()
    omega.postToChat("Position:"+str(x)+","+str(y)+","+str(z))

    count=count+1
    time.sleep(1)