import sys
from itertools import permutations

class FrequencyTable(object):
    def __init__(self, list):
        self.list = list
        self.PITCH_TYPES = self.__findPitchTypes()
        self.convertPitches = self.__initPitchMap()
        self.freqTable = [ [0 for _ in range(len(self.PITCH_TYPES))] for _ in range(len(self.PITCH_TYPES) ** 2)]
        self.__populate()
        
    def __findPitchTypes(self):
        pitches = [item for sublist in self.list for item in sublist]
        return list(set(pitches))

    def __initPitchMap(self):
        perm = permutations(self.PITCH_TYPES, 2)
        convertPitches = list(perm)
        return convertPitches
    
    def __populate(self):
        for atBat in self.list:
            if len(atBat) < 3:
                continue
            prePitches = (atBat[0], atBat[1])
            col = self.convertPitches.index(prePitches)
            row = self.PITCH_TYPES.index(atBat[2])
            self.freqTable[col][row] += 1
            
            
    
        
