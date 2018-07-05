
from SlotMachine import SlotMachine
import numpy as np
import time

# A knowledge-base. The shaky, drunken memory of our gambler. #

class KnowledgeBase:

    def __init__(self,SlotMachine):
        self.totalNumSlots = SlotMachine.totalNumSlots
        self.memory = []
        self.slotRollNumbers = [0 for j in range(SlotMachine.totalNumSlots)]
        self.slotRewardList = [0 for j in range(SlotMachine.totalNumSlots)]

    def update(self):
        self.slotRewardList = [sum([i if list.index(i) == j else 0 for list in self.memory for i in list]) for j in range(self.totalNumSlots)]

        for i in range(len(self.slotRollNumbers)):
            self.slotRollNumbers[i] = sum([1 if (reward > 0 and event.index(reward) == i) else 0 for event in self.memory for reward in event])

# A machine-learning, gunslinging, rough gambler type. #

class Gambler:

    def __init__(self, SlotMachine, Wallet, Epsilon):

        self.Casino = SlotMachine
        self.actions = SlotMachine.actionSpace
        self.Wallet = Wallet
        self.Epsilon = Epsilon
        self.KnowledgeBase = KnowledgeBase(SlotMachine)

    def action(self):

        generateMeanKnowledge = [0 for i in range(self.Casino.totalNumSlots)]
        for i in range(self.Casino.totalNumSlots):
            try:
                generateMeanKnowledge[i] = self.KnowledgeBase.slotRewardList[i]/self.KnowledgeBase.slotRollNumbers[i]
            except ZeroDivisionError:
                generateMeanKnowledge[i] = 0

        print("Here's the current roll list: " + str(self.KnowledgeBase.slotRollNumbers))
        print("Current estimators of the mean for each slot: " + str(generateMeanKnowledge))

        bestKnown = generateMeanKnowledge.index(max(generateMeanKnowledge))
        print("The best known slot is slot (" + str(bestKnown) + ").")

        #Here is the famous 1-|epsilon| policy
        if max(generateMeanKnowledge) < 50:
            action = np.random.randint(0,self.Casino.totalNumSlots)
            print("The gunslinger is actually going for slot (" + str(action) + ").")
            reward = self.Casino.action(action)

        elif np.random.rand(1)<(1-(self.Epsilon/(1+sum(self.KnowledgeBase.slotRollNumbers)))):
            reward = self.Casino.action(bestKnown)

        else:
            action = np.random.randint(0,self.Casino.totalNumSlots)
            print("The gunslinger is actually going for slot (" + str(action) + ").")
            reward = self.Casino.action(action)

        self.Wallet += sum(reward)
        self.KnowledgeBase.memory.append(reward)
        self.KnowledgeBase.update()

# Happy gambling! #

def main():
    Casino = SlotMachine(int(input("How many slots do you you want to the gunslinger to play with?: ")))
    Wallet = int(input("How much money is the gunslinger rolling with? "))
    GambleCost = 50
    print("The cost to roll is 50 big ones.")
    Gunslinger = Gambler(Casino, Wallet, 0.9)

    while Gunslinger.Wallet > 50:
        Gunslinger.action()
        Gunslinger.Wallet -= GambleCost
        print(Gunslinger.Wallet)
        time.sleep(2)

    print("The Gunslinger is out of cash!")

main()