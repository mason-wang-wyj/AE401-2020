from mcpi.minecraft import Minecraft

omega = Minecraft.create()

px, py, pz = omega.player.getTilePos()


def plantTree(x, y, z):
    omega.setBlocks(x - 2, y + 4, z - 2, x + 2, y + 8, z + 2, 18)
    omega.setBlocks(x, y, z, x, y + 5, z, 17)


for i in range(20):
    plantTree(px + i*10, py, pz)
# plantTree(px,py,pz)
