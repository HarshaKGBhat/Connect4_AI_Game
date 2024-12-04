# Connect4_AI_Game
This is an Academic Project of DSCI-6612 . Contributors are Aldric Pinto and Harsha Keladi Ganapathi


### README for Connect Four AI Agents  

---

## **Overview**  
This project implements two different AI agents, **MiniMax Agent** and **Q-Learning Agent**, to play the classic Connect Four game. These agents showcase two distinct approaches to decision-making in games: a deterministic tree search algorithm (MiniMax) and a reinforcement learning-based adaptive model (Q-Learning).  

---

## **Table of Contents**  
1. [Features](#features)  
2. [Getting Started](#getting-started)  
3. [Game Rules](#game-rules)  
4. [AI Agents](#ai-agents)  
   - [MiniMax Agent](#minimax-agent)  
   - [Q-Learning Agent](#q-learning-agent)  
5. [How to Run](#how-to-run)  
6. [Results](#results)  
7. [Future Enhancements](#future-enhancements)  

---

## **Features**  
- Interactive **Connect Four** game with AI agents.  
- Two AI agents:
  - **MiniMax Agent:** Uses tree search and heuristics.  
  - **Q-Learning Agent:** Learns optimal strategies over multiple training episodes.  
- Supports human vs. AI or AI vs. AI gameplay.  
- Configurable training episodes and agent parameters.  

---

## **Getting Started**  
### **Requirements**  
- Python 3.7+  
- Libraries:
  - `numpy`
  - `matplotlib` (optional, for visualizing results)  

### **Installation**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-repo/connect-four-ai.git
   cd connect-four-ai
   ```  
2. Install the required libraries:  
   ```bash
   pip install -r requirements.txt
   ```  

---

## **Game Rules**  
Connect Four is a two-player game played on a 6x7 grid. Players take turns dropping discs into columns. The goal is to connect four discs in a row, column, or diagonal before the opponent.  

---

## **AI Agents**  
### **MiniMax Agent**  
- **Description:**  
  Uses the MiniMax algorithm to evaluate the game tree up to a specified depth.  
- **Features:**  
  - Explores all possible moves within the depth limit.  
  - Uses a heuristic scoring function to evaluate board states.  
- **Parameters in Code:**  
  - `depth`: Controls how many moves ahead the agent looks.  (depth limitation =4)

---

### **Q-Learning Agent**  
- **Description:**  
  A reinforcement learning agent that learns optimal moves by playing multiple games and updating a Q-table.  
- **Features:**  
  - Learns through trial and error.  
  - Adapts to new strategies over time.  
- **Key Parameters in Code:**  
  - `alpha`: Learning rate (0.1  
  - `gamma`: Discount factor for future rewards.(0.9) 
  - `epsilon`: Exploration rate during training.  (0.1)
  - `episodes`: Number of games the agent plays during training. (1000) 

---

## How to Run 
1. # Train the Q-Learning Agent: 
   Run the script to train the agent. Adjust parameters like `alpha`, `gamma`, and `episodes` in the code if needed.  
   ```bash
   **python main.py** 
   ```  

2. **Play the Game:**  
   Run the main script to start the game. You can choose to play against the MiniMax agent, Q-Learning agent, or watch them compete.  
   ```bash
   python main.py
   ```  
   During the game:
   - Enter a column number (1-7) to drop your disc.  



---

## Results  
1. # MiniMax Agent Performance:  
   - Performs consistently well within the depth limit.  
   - Strong against predictable or less-experienced players.  

2. # Q-Learning Agent Performance: 
   - Improves with training.  
   - Learns to counter predictable strategies after sufficient training.  


## Future Enhancements  
- Improve Q-Learning by implementing **Deep Q-Learning (DQL)** for better scalability.  
- Add more heuristic options for the MiniMax agent to refine decision-making.  
- Incorporate visualization tools for game playback and Q-table exploration.  
- Support multiplayer games over a network.  

----------------------------------------------------------------------------------------------------

