# N-armed-bandito
A repository for n-armed bandit simulations. The simulation is rather simple right now.

## The problem
A wonderful discussion of the n-armed bandit problem can be found in [Barto and Sutton, 1998]. The environment is a test bed for classical ideas in reinforcement learning. The bandit initially has access to N slot machines and has no knowledge about the distribution of rewards from any machine. Beginning with a fixed wallet, the goal of the bandit is to simultaneously determine the expected value and standard deviation of the rewards from each machine as well as maximize the utility return. Utility is a fancy name for expected value of reward over many successive gambles. The question is: what sort of strategy (policy) should the bandit employ? He needs to explore as well as exploit.
