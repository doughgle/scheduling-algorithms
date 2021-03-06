#!/usr/bin/python
'''
Scheduling policies simulator
Forked from Sample skeleton program, Mihn Ho, 2018.
Input file:
    input.txt
Output files:
    FCFS.txt
    RR.txt
    SRTF.txt
    SJF.txt
'''
import sys
from collections import deque
from copy import deepcopy

class Process:
    last_scheduled_time = 0
    def __init__(self, id, arrive_time, burst_time):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time

    def __repr__(self):
        return ('id %d : arrive_time %d,  burst_time %d'%(self.id, self.arrive_time, self.burst_time))

def FCFS_scheduling(process_list):
    #store the (switching time, proccess_id) pair
    schedule = []
    current_time = 0
    waiting_time = 0
    for process in process_list:
        if(current_time < process.arrive_time):
            current_time = process.arrive_time
        schedule.append((current_time,process.id))
        waiting_time = waiting_time + (current_time - process.arrive_time)
        current_time = current_time + process.burst_time

    return schedule, average_waiting_time(waiting_time, process_list)

def average_waiting_time(waiting_time, process_list):
    '''Defined as total waiting_time / num of processes in process_list'''
    return waiting_time / float(len(process_list))

def RR_scheduling(process_list, time_quantum):
    '''
    #Input: process_list, time_quantum (Positive Integer)
    #Output_1 : Schedule list contains pairs of (time_stamp, proccess_id) indicating the time switching to that process_id
    #Output_2 : Average Waiting Time
    '''
    schedule = []
    time = 0
    waiting_time = 0
    quantum = time_quantum
    runningPid = -1
    q = deque(deepcopy(process_list))

    while q:
        # --- Schedule
        #  filter out processes that haven't yet arrived
        arrived = [p for p in q if p.arrive_time <= time]
        if not arrived:
            time += 1
            continue

        arrived.reverse()
        p = arrived.pop()
        q.remove(p)

        # context switch (zero overhead)
        if p.id != runningPid:
            schedule.append((time, p.id))
            runningPid = p.id
            waiting_time = waiting_time + (time - p.arrive_time)

        while quantum > 0 and p.burst_time > 0:
            quantum -= 1
            p.burst_time -= 1
            time += 1

        if(p.burst_time > 0):
            p.arrive_time = time
            q.append(p)

        quantum = time_quantum

    return schedule, average_waiting_time(waiting_time, process_list)

def SRTF_scheduling(process_list):
    '''Shortest Remaining Time First (SRTF) Scheduling'''
    schedule = []
    time = 0
    runningPid = -1
    waiting_time = 0

    q = deque(deepcopy(process_list))

    while q:
        # --- Schedule
        #  filter out processes that haven't yet arrived
        arrived = [p for p in q if p.arrive_time <= time]
        #  sort by burst_time ascending
        sorted_procs = sorted(arrived, key=lambda p: p.burst_time, reverse=True)
        if sorted_procs:
            p = sorted_procs.pop()
            q.remove(p)

            # --- context switch
            if p.id != runningPid:
                schedule.append((time, p.id))
                runningPid = p.id
                waiting_time = waiting_time + (time - p.arrive_time)

            # --- Execute
            p.burst_time -= 1
            time += 1
            if p.burst_time > 0:
                p.arrive_time = time
                q.append(p)

        else:
            time += 1

    return schedule, average_waiting_time(waiting_time, process_list)

def SJF_scheduling(process_list, alpha):
    '''Shortest Job First - no pre-emption, jobs run to completion.
    Burst time predicition is simulated.
    '''
    schedule = []
    waiting_time = 0
    time = 0
    predicted_burst = PredictedBurstTime(alpha)

    q = deque(deepcopy(process_list))

    while q:
        # --- Schedule a process
        arrived = [p for p in q if p.arrive_time <= time]
        sorted_procs = sorted(arrived, key=lambda p: predicted_burst.get(p.id), reverse=True)
        if sorted_procs:
            p = sorted_procs.pop()
            schedule.append((time, p.id))
            waiting_time = waiting_time + (time - p.arrive_time)

            # --- Execute
            time += p.burst_time
            predicted_burst.update(p.id, p.burst_time)
            p.burst_time = 0
            q.remove(p)
        else:
            time += 1

    return schedule, average_waiting_time(waiting_time, process_list)

class PredictedBurstTime:
    INITIAL_PREDICTION = 5

    def __init__(self, alpha):
        self.alpha = alpha
        self.burst_lookup = {}

    def get(self, pid):
        try:
            return self.burst_lookup[pid]
        except KeyError as e:
            return self.INITIAL_PREDICTION

    def update(self, pid, actual_burst_time):
        prediction = self.alpha * actual_burst_time + (1 - self.alpha) * self.get(pid)
        self.burst_lookup[pid] = prediction

def read_input(input_file):
    result = []
    with open(input_file) as f:
        for line in f:
            array = line.split()
            if (len(array)!= 3):
                print ("wrong input format")
                exit()
            result.append(Process(int(array[0]),int(array[1]),int(array[2])))
    return result

def write_output(file_name, schedule, avg_waiting_time):
    with open(file_name,'w') as f:
        for item in schedule:
            f.write(str(item) + '\n')
        f.write('average waiting time %.2f \n'%(avg_waiting_time))

def main(argv):
    input_file = 'input.txt'
    process_list = read_input(input_file)
    print ("printing input ----")
    for process in process_list:
        print (process)
    print ("simulating FCFS ----")
    FCFS_schedule, FCFS_avg_waiting_time =  FCFS_scheduling(process_list)
    write_output('FCFS.txt', FCFS_schedule, FCFS_avg_waiting_time )
    print ("simulating RR ----")
    RR_schedule, RR_avg_waiting_time =  RR_scheduling(process_list,time_quantum = 2)
    write_output('RR.txt', RR_schedule, RR_avg_waiting_time )
    print ("simulating SRTF ----")
    SRTF_schedule, SRTF_avg_waiting_time =  SRTF_scheduling(process_list)
    write_output('SRTF.txt', SRTF_schedule, SRTF_avg_waiting_time )
    print ("simulating SJF ----")
    SJF_schedule, SJF_avg_waiting_time =  SJF_scheduling(process_list, alpha = 0.5)
    write_output('SJF.txt', SJF_schedule, SJF_avg_waiting_time )

if __name__ == '__main__':
    main(sys.argv[1:])
