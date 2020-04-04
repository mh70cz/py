#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:26:42 2017

https://github.com/fluentpython/example-code/blob/master/16-coroutine/taxi_sim.py

return from coroutine 
"""

import random
import collections
import queue
import argparse
import time

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 20
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')

def taxi_process(ident, trips, start_time = 0):
    """yield to simulator issuing event at each state change"""
    time_on_ride = 0
    time_with_passenger = 0
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time_pickup = time
        time = yield Event(time, ident, 'pick up passenger')
        
        time_with_passenger += (time - time_pickup)
        time = yield Event(time, ident, 'drop off passenger')
    
    time_on_ride = time - start_time
    yield Event(time, ident, 'going home')
    return (time_on_ride, time_with_passenger)

# Begin simulator    
class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)
        
    def run(self, end_time):
        """Schedule and display events until time is up"""
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)
            
        # main loop of the simulation
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
                        
            #print(str(self.events.qsize()) + ">")
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id *  '   ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration as ex:
                del self.procs[proc_id]
                msg = '   Time on ride {}, time with passenger {}, prawling {}'                
                print(msg.format(*ex.value, (ex.value[0] - ex.value[1])))
            else:
                self.events.put(next_event)
                #print(str(self.events.qsize()) + "<" )
        else:
            msg = '*** end od simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))
#end simulator


            
def compute_duration(previous_action):
    """ compute action duration using exponencial distribution """
    if previous_action in ['leave garage', 'drop off passenger']:
        # new state is prowling
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # new state is trip
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknow previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1

def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
         seed=None):
    """ Initialize random generator, build procs and runn simulation"""
    if seed is not None:
        random.seed(seed) # get reproducible results
        
    taxis = {i: taxi_process(i, (i+2), i * DEPARTURE_INTERVAL)
            for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description = 'Taxi fleet simulator.')    
    parser.add_argument('-e', '--end-time', 
                        type=int, default = DEFAULT_END_TIME,
                        help='simulation end time; default = %s'
                        % DEFAULT_END_TIME)
    parser.add_argument('-t', '--taxis', type=int,
                        default= DEFAULT_NUMBER_OF_TAXIS,
                        help='number of taxis running; default = %s'
                        % DEFAULT_NUMBER_OF_TAXIS)    
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='random generator seed (for testing)')
    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)
                    