
import numpy as np
import tensorflow as tf

# A machine-learning, gunslinging, rough gambler type. #

class Gambler:

    def __init__(self, SlotMachine, Wallet):
        self.Casino = SlotMachine
        self.actions = SlotMachine.actionSpace
        self.Wallet = Wallet

        # A couple of shots of whiskey, the gambler bets randomly. #
        self.Policy = [np.random.rand() for _ in range(SlotMachine.totalNumSlots)]
        self.Bias = np.random.rand()


    # Sober the gambler up! #
    def train(self):
