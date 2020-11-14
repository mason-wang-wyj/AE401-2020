from mcpi.minecraft import Minecraft
import time
omega=Minecraft.create()
while True:
    x,y,z=omega.player.getTilePos()
    a=omega.getBlock(x+1,y-1,z)
    b=omega.getBlock(x-1,y-1,z)
    c=omega.getBlock(x,y-1,z-1)
    d=omega.getBlock(x,y-1,z+1)
    if a== 8 or b == 8 or c == 8 or d ==9:
        omega.setBlocks(x+1,y-1,z+1,x - 1,y-1,z - 1,20)
