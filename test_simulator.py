#!/usr/bin/env python
import unittest
from simulator import *

class SimulatorTest(unittest.TestCase):

    def setUp(self):
        self.process_list = [
            # id, arrive_time, burst_time
            Process(0, 0, 4),
            Process(1, 2, 3),
            Process(2, 5, 1),
            Process(3, 15, 3)
        ]

    def test_FCFS(self):
        '''test First Come First Served outputs process switching events'''

        (schedule, avg_waiting_time) = FCFS_scheduling(self.process_list)

        self.assertListEqual([(0, 0), (4, 1), (7, 2), (15, 3)], schedule)

    def test_average_waiting_time(self):
        '''waiting_time of each process / num of processes'''

        (schedule, avg_waiting_time) = FCFS_scheduling(self.process_list)

        self.assertEquals(1.0, avg_waiting_time)

    def test_RR_without_preemption(self):
        '''Round Robin with time_quantum > max burst_time has the same output as FCFS'''

        (schedule, avg_waiting_time) = RR_scheduling(self.process_list, 4)

        self.assertListEqual([(0, 0), (4, 1), (7, 2), (15, 3)], schedule)

    def test_RR_with_preemption(self):
        '''Round Robin with time_quantum < max burst_time pre-empts long running processes'''

        (schedule, avg_waiting_time) = RR_scheduling(self.process_list, 3)

        self.assertListEqual([(0, 0), (3, 1), (6, 2), (7, 0), (15, 3)], schedule)

    def test_average_waiting_time_RR(self):
        '''waiting_time of each process / num of processes'''

        (schedule, avg_waiting_time) = RR_scheduling(self.process_list, 3)

        self.assertEquals(1.5, avg_waiting_time)

    def test_SRTF(self):
        '''Shortest Remaining Time First (basically SJF with pre-emption)'''

        (schedule, avg_waiting_time) = SRTF_scheduling(self.process_list)

        self.assertListEqual([(0, 0), (4, 1), (5, 2), (6, 1), (15, 3)], schedule)

    def test_average_waiting_time_SRTF(self):
        '''avg waiting time for SRTF'''

        (schedule, avg_waiting_time) = SRTF_scheduling(self.process_list)

        self.assertEquals(0.75, avg_waiting_time)

    def test_SJF(self):
        '''Shortest Job First has no pre-emption (i.e. runs jobs to completion)'''
        self.process_list = [
        # id, arrive_time, burst_time
        Process(0, 0, 3),
        Process(1, 1, 2),
        Process(2, 2, 1),
        Process(3, 30, 5)
        ]

        (schedule, avg_waiting_time) = SJF_scheduling(self.process_list, 1.0)

        self.assertListEqual([(0, 0), (3, 2), (4, 1), (30, 3)], schedule)

    def test_average_waiting_time_SJF(self):
        '''avg waiting time for SJF'''
        self.process_list = [
        # id, arrive_time, burst_time
        Process(0, 0, 3),
        Process(1, 1, 2),
        Process(2, 2, 1)
        ]

        (schedule, avg_waiting_time) = SJF_scheduling(self.process_list, 1.0)

        self.assertEquals(1.3333333333333333, avg_waiting_time)

if __name__ == '__main__':
    unittest.main()
