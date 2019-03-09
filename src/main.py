
import numpy
import sys
from load_data import *
from FrequencyTable import *
from Predictor import *
from split_pitch_data import *
from generate_expected_accuracy import *


def main(filename):
	split_file(filename, 0.75)
	pitches_training = get_data("train_"+filename)
	pitches_testing = get_data("test_"+filename)
	freqTable = FrequencyTable(pitches_training)
	print(Predictor(freqTable, pitches_testing).accuracy)
	generate_accuracy("train_"+filename, "test_"+filename)




if __name__ == '__main__':
    assert (len(sys.argv) == 2)
    assert(os.path.isfile(sys.argv[1]))
    assert(os.path.splitext(sys.argv[1])[1] == ".csv")
    main(sys.argv[1])