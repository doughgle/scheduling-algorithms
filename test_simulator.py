#!/usr/bin/python
import unittest
from simulator import Process, FCFS_scheduling

class SimulatorTest(unittest.TestCase):

    def setUp(self):
        self.process_list = [
        # id, arrive_time, burst_time
        Process(0, 0, 4),
        Process(1, 2, 3),
        Process(2, 5, 1)
        ]

    def test_FCFS(self):
        '''test First Come First Served outputs process switching events'''

        (actual, FCFS_avg_waiting_time) = FCFS_scheduling(self.process_list)

        self.assertListEqual([(0, 0), (4, 1), (7, 2)], actual)

    def test_average_waiting_time(self):
        '''waiting_time of each process / num of processes'''

        (actual, FCFS_avg_waiting_time) = FCFS_scheduling(self.process_list)

        self.assertEquals(1.3333333333333333, FCFS_avg_waiting_time)


if __name__ == '__main__':
    unittest.main()
