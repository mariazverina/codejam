import sys

input_stream = sys.stdin
#input_stream = open("sample.in", "rU")

def set_input_file(filename):
    global input_stream
    input_stream = open(filename, "rU")
    
def read_line():
    global input_stream
    return input_stream.readline().strip()

def read_int():
    line = read_line()
    return int(line)

def read_ints(count):
    line = read_line()
    tokens = line.split()
    if(count > 0 and len(tokens) != count):
        print "unexpected number of tokens"
        sys.exit(2)
        #throw Exception
    return [int(x) for x in tokens]

def read_lines(n):
    lines = []
    for i in range(n): #@UnusedVariable
        lines.append(read_line())
    return lines
    
def memoize(f):
    cache= {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf

def debug(foo): 
    print >> sys.stderr, foo

