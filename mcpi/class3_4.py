from mcpi.minecraft import Minecraft

omega=Minecraft.create()

x,y,z=omega.player.getTilePos()

omega.setBlocks(x,y,z,x+3,y+3,z+3,46)