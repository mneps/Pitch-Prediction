import random
from GlobalVars import *
from FrequencyTable import *

class Predictor():

    def __init__(self, freqTable, testData):
        self.freqTable = freqTable
        self.testData = list(filter(lambda x: len(x) > LINK_LENGTH, testData))
        self.accuracy = self.predictPitches()


    def predictPitches(self):
        correctPredictions = 0
        totalPitches = 0

        for atBat in self.testData:
            for i in range(LINK_LENGTH, len(atBat)):
                prevPitches = tuple(atBat[i-LINK_LENGTH:i])
                averages = self.freqTable.lookup(prevPitches)
                max_avg = 0
                pitchType = None
                for j in range(len(averages)):
                    (pitch, weight) = averages[j]
                    if weight > max_avg:
                        max_avg = weight
                        pitchType = pitch

                if pitchType == atBat[i]:
                    correctPredictions += 1

                totalPitches += 1

        return correctPredictions / totalPitches






