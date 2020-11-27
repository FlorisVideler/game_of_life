from Visualisation import *
from Simulator import *
import time
import random

# Configuratie
VISUALISATION = True

if __name__ == "__main__":
    w = World(20)
    rule = 'b3s23'
    sim = Simulator(w, rule)

    # quick and dirty start setup
    for x in range(sim.get_world().width):
        for y in range(sim.get_world().height):
            if random.randint(0, 1) == 1:
                sim.get_world().set(x, y, 6)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)
