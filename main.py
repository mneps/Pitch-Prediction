
import sys
from load_data import *

def main(dir_path):
	pitches = get_data(dir_path)



if __name__ == '__main__':
    assert (len(sys.argv) == 2)
    assert(os.path.isdir(sys.argv[1]))
    main(sys.argv[1])