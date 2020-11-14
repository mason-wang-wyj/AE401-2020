from mcpi.minecraft import Minecraft
omega=Minecraft.create()

while True:
    hits=omega.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos
        block=omega.getBlock(x,y,z)
        if block == 1:
            omega.setBlock(x,y,z,46)