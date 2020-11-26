from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """

    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)

    def reset_sim(self):
        # Reset the sim
        self.setUp()
        world = World(10)
        self.sim.set_world(world)

    # New tests
    def test_next_gen(self):
        """
        Tests functionality of next_gen function. This function checks what needs to happen based on the rules.
        """

        self.reset_sim()

        # Set 1 cell alive and all neighours dead.
        self.sim.get_world().set(1, 1, 1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 0)

        self.reset_sim()

        # Set 1 cell alive and more than 3 alive
        self.sim.get_world().set(1, 1, 1)
        self.sim.get_world().set(0, 0, 1)
        self.sim.get_world().set(1, 0, 1)
        self.sim.get_world().set(2, 0, 1)
        self.sim.get_world().set(2, 1, 1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 0)

        self.reset_sim()

        # Set 2 cells alive (survive)
        self.sim.get_world().set(1, 1, 1)
        self.sim.get_world().set(0, 0, 1)
        self.sim.get_world().set(1, 0, 1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 1)

        self.reset_sim()

        # Set 3 cells alive (birth)
        self.sim.get_world().set(0, 0, 1)
        self.sim.get_world().set(1, 0, 1)
        self.sim.get_world().set(2, 0, 1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 1)

    def test_parse_rule(self):
        sim = Simulator(rule='b3s23')
        self.assertEqual(sim.rule, {'b': [3], 's': [2, 3]})

        sim = Simulator(rule='b012345678s012')
        self.assertEqual(sim.rule, {'b': [0, 1, 2, 3, 4, 5, 6, 7, 8], 's': [0, 1, 2]})

        sim = Simulator(rule='q63535t444')
        self.assertEqual(sim.rule, {'b': [3], 's': [2, 3]})
