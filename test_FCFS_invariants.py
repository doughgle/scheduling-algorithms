#!/usr/bin/env python
import unittest
from simulator import Process, FCFS_scheduling
from hypothesis import given
from hypothesis.strategies import lists, integers, composite

@composite
def processes(draw):
    pid = draw(integers(min_value=0))
    arrival_time = draw(integers(min_value=0))
    burst_time = draw(integers(min_value=0))
    p = Process(pid, arrival_time, burst_time)
    return p

@composite
def list_of_processes(draw):
    return draw(lists(processes(), min_size=1).map(sorted))

class FCFSInvariants(unittest.TestCase):

    @given(list_of_processes())
    def test_FCFS_process_ids_are_scheduled_in_sorted_order(self, process_list):
        '''process ids are output in ascending sorted order'''
        schedule, avg_waiting_time = FCFS_scheduling(process_list)
        pids = [proc[1] for proc in schedule]
        self.assertEqual(sorted(pids), pids)

if __name__ == '__main__':
    unittest.main()
