#!/usr/bin/python
import unittest
from simulator import Process, FCFS_scheduling

class SimulatorTest(unittest.TestCase):

    def test_FCFS(self):
        '''test First Come First Served outputs process switching events'''
        process_list = [
          # id, arrive_time, burst_time
          Process(0, 0, 4),
          Process(1, 2, 3),
          Process(2, 5, 1)
        ]

        (actual, FCFS_avg_waiting_time) = FCFS_scheduling(process_list)

        self.assertListEqual([(0, 0), (4, 1), (7, 2)], actual)

if __name__ == '__main__':
    unittest.main()
