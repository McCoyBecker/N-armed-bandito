
import numpy as np

# Slot class for rolling high stakes, baby! #

class Slot:
    
    def __init__(self):
        self.mean = np.random.randint(45,55)
        self.variance = np.sqrt(self.mean)

    def roll(self):
        machineReturn = np.random.normal(self.mean,self.variance,1)
        if machineReturn > 0:
            return(machineReturn) 
        else:
            return 0

# Slot machine keeps track of all the slots. #

class SlotMachine:

    def __init__(self, totalNumSlots):
        self.totalNumSlots = totalNumSlots
        self.actionSpace = [i for i in range(totalNumSlots)]
        self.SlotList = [Slot() for _ in range(totalNumSlots)]

    def action(self, slotNumber):
        Choice = self.SlotList[slotNumber]
        instantReward = Choice.roll()
        return([instantReward if i == slotNumber else 0 for i in range(len(self.SlotList))])