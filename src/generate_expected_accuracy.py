
import sys
from load_data import *
from random import random
import numpy as np

TRAILS = 10000

def predict_pitch(pitch_prob):
    # print(pitch_prob)
    rand = random()
    # print("rand: %f" %rand)
    for (pitch, prob) in pitch_prob:
        if rand < prob:
            # print(pitch)
            return pitch


def main(train_fp, test_fp):

    pitches = [item for sublist in get_data(train_fp) for item in sublist]

    set_pitches = set(pitches)

    pitch_prob = []

    cum_prob = 0

    for p in set_pitches:
        count = pitches.count(p)

        prob = count/len(pitches)

        cum_prob += prob

        pitch_prob.append((p, cum_prob))



    test_pitches = [item for sublist in get_data(test_fp) for item in sublist]

    accuracy_list = []

    for _ in range(TRAILS):

        correct = 0

        for t_p in test_pitches:
            p_p = predict_pitch(pitch_prob)
            if t_p == p_p:
                correct += 1

        accuracy = correct / len(test_pitches)

        print(accuracy)

        accuracy_list.append(accuracy)

    print("Mean:   %f" %(np.mean(accuracy_list)))
    print("Stdev:  %f" %(np.std(accuracy_list)))
    print(pitch_prob)





if __name__ == '__main__':
    assert (len(sys.argv) == 3)
    assert(os.path.isfile(sys.argv[1]))
    assert(os.path.splitext(sys.argv[1])[1] == ".csv")
    assert(os.path.splitext(sys.argv[2])[1] == ".csv")
    main(sys.argv[1], sys.argv[2])