
import numpy
import sys
from load_data import *
from FrequencyTable import *
from Predictor import *


def main(training, testing):
	pitches_training = get_data(training)
	pitches_testing = get_data(testing)
	freqTable = FrequencyTable(pitches_training)
	predictions = []
	for _ in range(1000):
		predictions.append(Predictor(freqTable, pitches_testing).accuracy)
	print(numpy.mean(predictions), numpy.std(predictions))




if __name__ == '__main__':
    assert (len(sys.argv) == 3)
    assert(os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]))
    assert(os.path.splitext(sys.argv[1])[1] == ".csv" and os.path.splitext(sys.argv[2])[1] == ".csv")
    main(sys.argv[1], sys.argv[2])