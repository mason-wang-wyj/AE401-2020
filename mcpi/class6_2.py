from mcpi.minecraft import Minecraft
omega=Minecraft.create()
x,y,z=omega.player.getTilePos()
omega.setSign(x,y,z,63,0,"我愛","Mincraft","","也愛Python")