# Rock-Paper-Scissors
# freeCodeCamp: Rock Paper Scissors (Machine Learning)

This repository contains my solution for the **Rock Paper Scissors** project, which is part of the **Machine Learning with Python** certification curriculum on freeCodeCamp.

The objective of this challenge is to build a program that plays Rock, Paper, Scissors against four different automated bots, achieving a winning rate of **at least 60%** across a 1,000-game match against each opponent.

---

## 🚀 The Strategy: N-Gram Pattern Matching

A completely random strategy only yields a 50% win rate. To defeat all four specialized bots (Quincy, Abbey, Kris, and Mrugesh), this program implements a **Markov Chain / N-Gram Frequency Tracking** algorithm.

### How It Works:
* **State Persistence:** Python's mutable default arguments are used to remember the sequence of plays across multiple function calls.
* **Frequency Mapping:** The algorithm tracks strings of consecutive moves (e.g., sequences of 3 moves like `"RRP"`). It logs how often the opponent plays `"R"`, `"P"`, or `"S"` immediately following that specific sequence.
* **Predictive Counter-play:** When a known sequence occurs again, the program looks up the historical data, predicts the opponent's most probable next move based on maximum frequency, and plays the exact winning counter-move.

---

## 📂 Project Structure

* `RPS.py`: Contains the main `player()` function logic implementing the frequency-tracking algorithm.
* `main.py`: The entry point script used to run matches and trigger tests.
* `RPS_game.py`: The game engine provided by freeCodeCamp containing the implementation of the 4 opponent bots.
* `test_module.py`: The unit testing suite that verifies the 60%+ win rate criteria.

---

## 🛠️ How to Run Locally

If you want to clone this repository and test the code on your local environment (or via mobile apps like Pydroid 3):

1. Clone this repository:
   ```bash
   https://github.com/siddikiranmayi-cloud/Rock-Paper-Scissors
   
