import unittest
from entity import *
from random_walk import *


class RandomWalkTestCase(unittest.TestCase):
    def test_init_instance(self):
        # a = Drunk("a")
        # a.take_steps()
        # print(a)
        b = UsualDrunk("jack")
        print(b.take_steps())
        print(b)

    def test_walk(self):
        start_loc = Location(0.0, 0.0)
        usual_drunk = UsualDrunk("a")
        south_drunk = SouthDrunk("b")
        only_x_drunk = OnlyXDrunk("c")
        field = Field()
        field.add_drunk(usual_drunk, start_loc)
        field.add_drunk(south_drunk, start_loc)
        field.add_drunk(only_x_drunk, start_loc)

        num_steps = 100

        usual_drunk_distance = walk(usual_drunk, field, num_steps)
        print(usual_drunk_distance)
        south_drunk_distance = walk(south_drunk, field, num_steps)
        print(south_drunk_distance)
        only_x_drunk_distance = walk(only_x_drunk, field, num_steps)
        print(only_x_drunk_distance)

    def test_sim_walk(self):
        num_steps = 100
        num_trials = 100

        usual_drunk_distance_list = sim_walk(num_steps, num_trials, UsualDrunk)
        south_drunk_distance_list = sim_walk(num_steps, num_trials, SouthDrunk)
        only_x_drunk_distance_list = sim_walk(num_steps, num_trials, OnlyXDrunk)
        print("Mean dist for Usual Drunk:", sum(usual_drunk_distance_list) / len(usual_drunk_distance_list))
        print("Mean dist for South Drunk:", sum(south_drunk_distance_list) / len(south_drunk_distance_list))
        print("Mean dist for OnlyX Drunk:", sum(only_x_drunk_distance_list) / len(only_x_drunk_distance_list))

    def test_drunk_test(self):
        walk_length = (10, 100, 1000)
        num_trials = 1000
        print("################Usual Drunk #######################")
        drunk_test(walk_length, num_trials, UsualDrunk)
        print("################Usual Drunk #######################")
        print("################South Drunk #######################")
        drunk_test(walk_length, num_trials, SouthDrunk)
        print("################South Drunk #######################")
        print("################OnlyX Drunk #######################")
        drunk_test(walk_length, num_trials, OnlyXDrunk)
        print("################OnlyX Drunk #######################")

    def test_drunk_test_with_graph(self):
        walk_length = (10, 100, 1000)
        num_trials = 1000
        drunk_type = [UsualDrunk,SouthDrunk,OnlyXDrunk]
        drunk_test_with_graph(walk_length,num_trials,drunk_type)

    def test_plot_locs(self):
        drunk_type = [UsualDrunk, SouthDrunk, OnlyXDrunk]
        num_steps = 100
        num_trials = 100
        plot_locs(drunk_type,num_steps,num_trials)

    def test_trace_walk(self):
        drunk_type = [UsualDrunk, SouthDrunk, OnlyXDrunk,WestDrunk]
        num_steps = 100
        trace_walk(drunk_type,num_steps)

    def test_trace_walk(self):
        drunk_type = [UsualDrunk, SouthDrunk, OnlyXDrunk,WestDrunk]
        num_steps = 100
        trace_walk(drunk_type,num_steps)


if __name__ == '__main__':
    unittest.main()
