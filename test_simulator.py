#!/usr/bin/python
import unittest
from simulator import Process, FCFS_scheduling, RR_scheduling

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

    def test_RR_without_preemption(self):
        '''Round Robin with time_quantum > max burst_time has the same output as FCFS'''

        (actual, FCFS_avg_waiting_time) = RR_scheduling(self.process_list, 4)

        self.assertListEqual([(0, 0), (4, 1), (7, 2)], actual)

    def test_RR_with_preemption(self):
        '''Round Robin with time_quantum < max burst_time pre-empts long running processes'''

        (actual, FCFS_avg_waiting_time) = RR_scheduling(self.process_list, 3)

        self.assertListEqual([(0, 0), (3, 1), (6, 2), (7, 0)], actual)

if __name__ == '__main__':
    unittest.main()
