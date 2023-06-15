# PIC16B - Reinforcement Learning for Blackjack
Members: Aria Huang, Allen Tong, Xiaofu Ding

Report link: file:///C:/Users/huang/OneDrive/Documents/WeChat%20Files/wxid_ar4dnjktpe2m22/FileStorage/File/2023-06/final%20report.pdf
### Project Description

In this project, we will use reinforcement learning to train an AI to play the gambling game BlackJack, with the goal of discovering advanced strategies for winning the game. We plan to compare the performance of two different reinforcement learning algorithms in training an AI to play the gambling game BlackJack. We started by using openAI gym “blackjack” environment but realized that it’s a simpler version where the action space is fixed and player can only “hit” or “stand”.  The goal of the project is to evaluate which algorithm can discover advanced strategies for winning the game more effectively. By comparing the performance of the three agents, we will identify which algorithm is most effective in learning optimal strategies for playing BlackJack. The process involves defining the game's state and action spaces, and then training an agent to take actions that maximize the expected cumulative reward over time. The reinforcement learning algorithm updates the agent's policy or decision-making function based on the feedback received, and over time, the agent improves its decision-making process to maximize its reward.

### Instruction

- [Blackjack_Env_1_Monte_Carlo.ipynb](https://github.com/allensctong/PIC16B/blob/main/Blackjack_Env_1_Monte_Carlo.ipynb) is the Monte-Carlo implementation in our first environment, to run it one needs to download the helper file [BlackJackUtility.py](https://github.com/allensctong/PIC16B/blob/main/BlackJackUtility.py) file and include it in the same folder (if work with Google Colab, one needs to upload the helper file into content to work with it.
    - Addition to this, one game simulation is included in this notebook (using helper functions within the utility helper file). This simulation takes in user input, so one can play around and interact with the environment here.
- [Blackjack_Env_2_Monte_Carlo.ipynb](https://github.com/allensctong/PIC16B/blob/main/Blackjack_Env_2_Monte_Carlo.ipynb) is the Monte-Carlo implementation in our improved (customized) environment, to run it one needs to download the helper file [Strategy.py](https://github.com/allensctong/PIC16B/blob/main/Strategy.py) to be able to compare it with the basic strategy.
- [blackjack-q-learning.ipynb](https://github.com/allensctong/PIC16B/blob/main/blackjack-q-learning.ipynb) ****is the implementation of the Q-learning algorithm. The environment is loaded in the notebook, or one can load the environment through the helper file [BlackJackUtility.py](https://github.com/allensctong/PIC16B/blob/main/BlackJackUtility.py) following a similar procedure as [Blackjack_Env_1_Monte_Carlo.ipynb](https://github.com/allensctong/PIC16B/blob/main/Blackjack_Env_1_Monte_Carlo.ipynb).
- [q-learning-visualization.ipynb](https://github.com/allensctong/PIC16B/blob/main/q-learning-visualization.ipynb) ********contains the visualization of the training process and policy visualization. It should be pasted after the environment is loaded, an agent is defined, and training has been completed. It can be used with [blackjack-q-learning.ipynb](https://github.com/allensctong/PIC16B/blob/main/blackjack-q-learning.ipynb) ****and Monte Carlo with some modifications.
- Default environment code from openAI gym is given by [BlackJackEnv.py](https://github.com/allensctong/PIC16B/blob/main/BlackJackEnv.py), which does not need to be included anywhere because we can use it using syntax “gym.make('Blackjack-v1')”.
- Customized environment code written by us can be found at [costumized environment.ipynb](https://github.com/allensctong/PIC16B/blob/main/costumized%20environment.ipynb), which is included in our implementation of Monte-Carlo in customized environment notebook, due to the need of being able to work in a global environment.

### Contributors

Xiaofu Ding, Aria Huang, Allen Tong (Alphebatical order by last name)
