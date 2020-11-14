from mcpi.minecraft import Minecraft
stephanie=Minecraft.create()

import time

x = 10
y = 100
z = 1000

time.sleep(3)
stephanie.player.setTilePos(x,y,z)

y = y + 10
time.sleep(1)
stephanie.player.setTilePos(x,y,z)

y = y + 10
time.sleep(1)
stephanie.player.setTilePos(x,y,z)