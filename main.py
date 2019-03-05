
import sys
from load_data import *

def main(filepath):
	pitches = get_data(filepath)



if __name__ == '__main__':
    assert (len(sys.argv) == 2)
    assert(os.path.isfile(sys.argv[1]))
    assert(os.path.splitext(sys.argv[1])[1] == ".csv")
    main(sys.argv[1])