from mcpi.minecraft import Minecraft

omega=Minecraft.create()

block=input("Plese enter a code:")
try:
    block=int(block)
    x,y,z=omega.player.getTilePos()
    omega.setBlock(x,y,z,block)
except:
    print("please enter a code")
finally:
    print("exit")