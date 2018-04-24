#!/usr/bin/env python
import unittest
from simulator import *

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

        (schedule, avg_waiting_time) = FCFS_scheduling(self.process_list)

        self.assertListEqual([(0, 0), (4, 1), (7, 2)], schedule)

    def test_average_waiting_time(self):
        '''waiting_time of each process / num of processes'''

        (schedule, avg_waiting_time) = FCFS_scheduling(self.process_list)

        self.assertEquals(1.3333333333333333, avg_waiting_time)

    def test_RR_without_preemption(self):
        '''Round Robin with time_quantum > max burst_time has the same output as FCFS'''

        (schedule, avg_waiting_time) = RR_scheduling(self.process_list, 4)

        self.assertListEqual([(0, 0), (4, 1), (7, 2)], schedule)

    def test_RR_with_preemption(self):
        '''Round Robin with time_quantum < max burst_time pre-empts long running processes'''

        (schedule, avg_waiting_time) = RR_scheduling(self.process_list, 3)

        self.assertListEqual([(0, 0), (3, 1), (6, 2), (7, 0)], schedule)

    def test_average_waiting_time_RR(self):
        '''waiting_time of each process / num of processes'''

        (schedule, avg_waiting_time) = RR_scheduling(self.process_list, 3)

        self.assertEquals(2.0, avg_waiting_time)

    def test_SRTF(self):
        '''Shortest remaining time first'''

        (schedule, avg_waiting_time) = SRTF_scheduling(self.process_list)

        self.assertListEqual([(0, 0), (4, 1), (5, 2), (6, 1)], schedule)

if __name__ == '__main__':
    unittest.main()
