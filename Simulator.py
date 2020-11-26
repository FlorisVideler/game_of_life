from World import *
import copy


class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world=None, rule=None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world


    def parse_rule(self) -> dict:
        return {}

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1
        next_world = self.next_gen()
        self.world = next_world
        # TODO: Do something to evolve the generation

        return next_world

    def next_gen(self) -> World:
        next_world = copy.deepcopy(self.world)

        for x in range(next_world.width):
            for y in range(next_world.height):
                neighbours = self.world.get_neighbours(x, y)

                if neighbours.count(0) > 6 or neighbours.count(0) < 5:
                    # Dead
                    next_world.set(x, y, 0)
                elif neighbours.count(0) == 5 and self.world.get(x, y) == 0:
                    # birth
                    next_world.set(x, y, 1)
                # There is no else, the other option is to do nothing (survive)

        return next_world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world
