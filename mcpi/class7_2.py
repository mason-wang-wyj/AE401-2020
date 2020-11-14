from mcpi.minecraft import Minecraft
omega=Minecraft.create()

x,y,z=omega.player.getPos()
for k in range(20):
     for j in range(20):
        for i in range(20):
            omega.setBlock(x+k,y+j,z+i,46)