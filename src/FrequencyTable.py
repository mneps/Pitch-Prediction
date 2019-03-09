from __future__ import division
import sys
from itertools import permutations

class FrequencyTable(object):
    def __init__(self, list):
        self.list = list
        self.PITCH_TYPES = self.__findPitchTypes()
        self.convertPitches = self.__initPitchMap()
        self.freqTable = [ [0 for _ in range(len(self.PITCH_TYPES))] for _ in range(len(self.PITCH_TYPES) ** 2)]
        self.__populate()
        self.__finalizeList()
        
    def __findPitchTypes(self):
        pitches = [item for sublist in self.list for item in sublist]
        return list(set(pitches))

    def __initPitchMap(self):
        perm = permutations(self.PITCH_TYPES, 2)
        convertPitches = list(perm)
        for pitch in self.PITCH_TYPES:
            convertPitches += [(pitch, pitch)]
        return convertPitches
    
    def __populate(self):
        for atBat in self.list:
            if len(atBat) < 3:
                continue
            for i in range(2, len(atBat)):
                prevPitches = (atBat[i-2], atBat[i-1])
                col = self.convertPitches.index(prevPitches)
                row = self.PITCH_TYPES.index(atBat[i])
                self.freqTable[col][row] += 1

    def __finalizeList(self):
        for col in range(len(self.freqTable)):
            pitchComboTotal = sum(self.freqTable[col])
            if pitchComboTotal != 0:
                for row in range(len(self.freqTable[col])):
                    self.freqTable[col][row] = self.freqTable[col][row] / pitchComboTotal

    def lookup(self, prevPitches):
        """ Public method to retrieve probability of all potential future pitches given
            a sequence of previous pitches
        """
        col = self.convertPitches.index(prevPitches)
        pitchList = []
        for pitch in range(len(self.freqTable[col])):
            pitchList.append((self.PITCH_TYPES[pitch], self.freqTable[col][pitch]))
        return pitchList



            
            
    
        
