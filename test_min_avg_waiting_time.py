#!/usr/bin/env python
import unittest
from simulator import *

class AverageWaitingTimeTest(unittest.TestCase):

    def setUp(self):
        self.process_list = read_input('input.txt')

    def test_RR_min_avg_waiting_time(self):
        '''Find the time quantum which produces the minimum average waiting time for RR.'''
        results = []

        for quantum in range(1, 20):
            (schedule, avg_waiting_time) = RR_scheduling(self.process_list, quantum)
            results.append((quantum, avg_waiting_time, schedule))

        quantum, avg_waiting_time, schedule = min(results, key=lambda r: r[1])

        print self._testMethodDoc
        print "quantum: ", quantum,
        print ", avg_waiting_time: ", avg_waiting_time
        print "schedule: ", schedule
        print "-"*80
        self.assertEquals(6.4375, avg_waiting_time)

    def test_SJF_min_avg_waiting_time(self):
        '''Find the historical predicted burst_time weighting (alpha) which produces the minimum average waiting time for SJF.'''
        results = []
        for alpha in [x/100.0 for x in range(0,100)]:
            (schedule, avg_waiting_time) = SJF_scheduling(self.process_list, alpha)
            results.append((alpha, avg_waiting_time, schedule))

        alpha, min_avg_waiting_time, schedule = min(results, key=lambda r: r[1])

        print self._testMethodDoc
        print "alpha:", alpha,
        print "min_avg_waiting_time:", min_avg_waiting_time
        print "schedule:", schedule

        self.assertEquals(6.375, avg_waiting_time)

if __name__ == '__main__':
    unittest.main()
