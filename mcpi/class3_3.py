from mcpi.minecraft import Minecraft

omega=Minecraft.create()

x,y,z=omega.player.getTilePos()

count=0
while count<255:
    omega.setBlock(x,count,z,0)

    count=count+1