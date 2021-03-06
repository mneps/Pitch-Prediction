import sys
import pprint
from GlobalVars import *
from itertools import product

class FrequencyTable(object):
    def __init__(self, list):
        self.list = list
        self.PITCH_TYPES = self.__findPitchTypes()
        self.convertPitches = self.__initPitchMap()
        self.freqTable = \
            [ [0 for _ in range(len(self.PITCH_TYPES))] for _ in range(len(self.PITCH_TYPES) ** LINK_LENGTH)]
        self.__populate()
        self.__finalizeList()
        
    def __findPitchTypes(self):
        pitches = [item for sublist in self.list for item in sublist]
        return list(set(pitches))

    def __initPitchMap(self):
        perm = product(self.PITCH_TYPES, repeat=LINK_LENGTH)
        convertPitches = list(perm)
        # for pitch in self.PITCH_TYPES:
        #     samePitch = tuple()
        #     for _ in range(LINK_LENGTH):
        #         samePitch += (pitch,)
        #     convertPitches.append(samePitch)
        return convertPitches
    
    def __populate(self):
        for atBat in self.list:
            if len(atBat) < (LINK_LENGTH + 1):
                continue
            for i in range(LINK_LENGTH, len(atBat)):
                prevPitches = tuple(atBat[i-LINK_LENGTH:i])
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

    def pprint(self):
        print (self.PITCH_TYPES)
        for pitchCombo in range(len(self.freqTable) - len(self.PITCH_TYPES)):
            print("PITCH COMBO: ", self.convertPitches[pitchCombo], ":", \
                  [ (self.PITCH_TYPES[pitch], self.freqTable[pitchCombo][pitch]) \
                    for pitch in range(len(self.freqTable[pitchCombo]))])
    

            
            
    
        
