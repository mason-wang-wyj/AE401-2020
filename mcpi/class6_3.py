from mcpi.minecraft import Minecraft
omega=Minecraft.create()

while True:
    hits=omega.events.pollProjectileHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos
        omega.createExplosion(x,y,z)