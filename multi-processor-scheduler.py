#!/usr/bin/env python
from multiprocessing import Pool
from simulator import *

if __name__ == '__main__':
    input_file = 'input.txt'
    process_list = read_input(input_file)
    num = 4
    p = Pool(processes=num)
    results = p.map(FCFS_scheduling, [process_list[i::num] for i in range(num)])
    print "average_waiting_time:", sum([r[1] for r in results])
    print "schedule:", sorted([item for sublist in [r[0] for r in results] for item in sublist], key=lambda cs: cs[0])
