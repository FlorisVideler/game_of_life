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

        if rule == None:
            self.rule = {'b': [3], 's': [2, 3]}
        else:
            self.rule = self.parse_rule(rule)

    def parse_rule(self, rule: str) -> dict:
        """
        Parses the string of a simulation.

        :param rule: Rule string to parse
        :return: The rule in dict format
        """
        print('rule', rule)
        try:
            b_split = rule.split('b')
            s_split = b_split[1].split('s')
            b = s_split[0]
            s = s_split[1]
            return {'b': [int(char) for char in b], 's': [int(char) for char in s]}
        except:
            # Return default rule
            return {'b': [3], 's': [2, 3]}

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
        """
        Checks what needs to happen to all the cells based on the rules.

        :return: New state of the new world.
        """
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
