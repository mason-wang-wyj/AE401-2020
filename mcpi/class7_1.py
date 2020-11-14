from mcpi.minecraft import Minecraft
omega=Minecraft.create()

import random
import time

x,y,z=omega.player.getPos()


while True:
    rx=random.randrange(-10,10)+x
    rz=random.randrange(-10,10)+z
    ry=y+20

    omega.spawnEntity(rx,ry,rz,93)
    time.sleep(0.1)