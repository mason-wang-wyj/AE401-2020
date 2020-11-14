from mcpi.minecraft import Minecraft
omega=Minecraft.create()

x,y,z=omega.player.getTilePos()

w=10
h=8
l=20

omega.setBlocks(x,y,z, x+w,y+h,z+l, 7)
