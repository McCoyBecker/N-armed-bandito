
import numpy as np

# Slot class for rolling high stakes, baby! #

class Slot:
    
    def __init__(self):
        self.mean = np.random.randint(0,100)
        self.variance = np.sqrt(mean)

    def roll(self):
        machineReturn = np.random.normal(self.mean,self.variance,1)
        if machineReturn > 0:
            return(machineReturn) 
        else:
            return 0

# Slot machine keeps track of all the slots #

class SlotMachine:

    def __init__(self, totalNumSlots):
        self.totalNumSlots = totalNumSlots
        self.actionSpace = [i for i in range(totalNumSlots)]
        self.SlotList = [Slot for _ in range(totalNumSlots)]

    def showActionSpace(self):
        print("The action space is " + str(self.actionSpace))

    def action(self, slotNumber):
        instantReward = self.SlotList[slotNumber].roll
        return([instantReward if i == slotNumber else 0 for i in range(len(self.SlotList))])

def main():
    Casino = SlotMachine(int(input("How many slots do you you want to play with?: ")))
    Wallet = int(input("How much money are you rolling with? "))
    print("The cost to roll is 50 big ones.")
    while Wallet > 50:

        print("Here are the slots you can roll at: " + str(Casino.showActionSpace()))
        SlotNumber = int(input("Pick a slot: "))

        try:
            reward = Casino.action(SlotNumber)
            print("Here are your rewards: " + str(reward))
            Wallet += sum(reward)
            print("You now have " + str(Wallet) + "to play with.")
            break

        except IndexError:
            print("You're trying to gamble outside the casino! Pick again partner.")

    print("You're out of cash!")

main()