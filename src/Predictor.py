import random
from FrequencyTable import *

class Predictor():

	def __init__(self, freqTable, testData):
		self.freqTable = freqTable
		self.testData = list(filter(lambda x: len(x) > 2, testData))
		self.accuracy = self.predictPitches()


	def predictPitches(self):
		correctPredictions = 0
		totalPitches = 0

		for atBat in self.testData:
			for i in range(2, len(atBat)):
				prevPitches = (atBat[i-2], atBat[i-1])
				averages = self.freqTable.lookup(prevPitches)
				
				max_avg = 0
				for j in range(len(averages)):
					(pitch, weight) = averages[j]
					if weight > max_avg:
						max_avg = weight
						pitchType = pitch

				if pitchType == atBat[i]:
					correctPredictions += 1

				totalPitches += 1

		return correctPredictions / totalPitches






