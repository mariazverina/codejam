'''
Created on Mar 18, 2012

@author: maria
'''

from codejam import * #@UnusedWildImport
from math import pow
import sys #@Reimport
from multiprocessing import Pool


def do_case(inputs):
    (from_num, to_num) = inputs
    count = 0
    digit_count = len(str(from_num))
    rnumber = int(pow(10, digit_count - 1))
    for x in range(from_num, to_num+1):
        candidate = x
        to_add = set()
        for n in range(digit_count - 1): #@UnusedVariable
            candidate = candidate // 10 + (candidate % 10) * rnumber
            if candidate > x and candidate <= to_num:
                to_add.add(candidate)
                
        count += len(to_add)
            
    return [count]
     

def read_inputs():
    ll = read_ints(2)
    return ll



def run_case((i, inputs)):
    return(i, do_case(inputs))

def run_single(num_problems):
    for i in range(1, num_problems+1):
        inputs = read_inputs()
        (i, result) = run_case((i, inputs))
        print "Case #%d: %d" % tuple([i] + result)

def run_multi(num_problems):
    inputs = []
    for i in range(1, num_problems+1): #@UnusedVariable
        inputs.append(read_inputs())
#    for i in range(1, num_problems+1):
#        run_case(i, inputs.pop(0))
    p = Pool(4)
    results = p.map(run_case, zip(range(1, num_problems+1), inputs))
    for i in range(1, num_problems+1):
        (i, result) = results.pop(0)
        print "Case #%d: %d" % tuple([i] + result)

def main():
    num_problems = read_int()
#    run_single(num_problems)
    run_multi(num_problems)
        
    
if __name__ == '__main__':
    if not "script" in sys.argv:
        set_input_file('sample.in')     # use sample file if we're in IDE
    main()