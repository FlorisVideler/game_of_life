from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION = True

if __name__ == "__main__":
    w = World(20)
    sim = Simulator(w, rule='b012345678s012')

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)
