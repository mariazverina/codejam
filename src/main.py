'''
Created on Mar 18, 2012

@author: maria
'''

from codejam import * #@UnusedWildImport
import sys #@Reimport
from multiprocessing import Pool


@memoize
def foo(x): 
    if(x == 1):
        return 1
    if(x % 2 == 1):
        return 1 + foo(x/2) + foo(x/2)
    return foo(x/2) + foo(x/2)

def do_case(inputs):
    (a, b) = inputs
    return [foo(a), b]
     

def read_inputs():
    (a, b) = read_ints(2)
    return (a, b)

def print_case(i, result):
    print "Case #%d: %d %d" % tuple([i] + result)
    
    
#-- end of user serviceable parts

def run_case((i, inputs)):
    return(i, do_case(inputs))

def run_single(num_problems):
    for i in range(1, num_problems+1):
        inputs = read_inputs()
        (i, result) = run_case((i, inputs))
        print_case(i, result)

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
        print_case(i, result)

def main():
    num_problems = read_int()
    if "multi" in sys.argv:
        debug('using multiple cores')
        run_multi(num_problems)
    else:
        run_single(num_problems)
        
    
if __name__ == '__main__':
    if not "script" in sys.argv:
        set_input_file('sample.in')     # use sample file if we're in IDE
    main()
