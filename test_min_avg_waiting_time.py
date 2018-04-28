#!/usr/bin/env python
import unittest
from simulator import *

class AverageWaitingTimeTest(unittest.TestCase):

    def setUp(self):
        self.process_list = read_input('input.txt')

    def test_RR_min_avg_waiting_time(self):
        '''Find the time quantum which produces the minimum average waiting time for RR.'''

        min_avg_waiting_time = 100000

        for quantum in range(1, 11):
            (schedule, avg_waiting_time) = RR_scheduling(self.process_list, quantum)
            if avg_waiting_time < min_avg_waiting_time:
                min_avg_waiting_time = avg_waiting_time

        print self._testMethodDoc
        print "quantum: ", quantum,
        print ", avg_waiting_time: ", avg_waiting_time
        print "schedule: ", schedule
        print "-"*80
        self.assertEquals(6.4375, min_avg_waiting_time)

if __name__ == '__main__':
    unittest.main()
