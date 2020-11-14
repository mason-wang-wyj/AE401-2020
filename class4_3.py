from mcpi.minecraft import Minecraft
omega=Minecraft.create()
x,y,z=omega.player.getTilePos()
weight=1000
height=1000
lenght=1000
omega.setBlocks(x,y,z,x+weight,y+height,z+lenght,20)
omega.setBlocks(x+1,y+1,z+1,x+weight-1,y+height-1,z+lenght-1,0)
omega.player.setTilePos(x+2,y+2,z+2)