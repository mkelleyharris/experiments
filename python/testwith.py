# With Statement



# open a file

import time

def output(info):
    with open("someFileName.txt", 'w') as f:
        f.write("info")

class Timer(object):
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end = self.start


if __name__ == "__main__":
    
    with Timer() as t:
	    output("some output info")
	
    print "Iterval: " + str(t.interval)



	