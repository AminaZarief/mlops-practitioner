# NYC TLC Green Taxi - Baseline Model Pipeline

This repository contains the baseline machine learning pipeline for predicting NYC Green Taxi trip duration using January 2023 trip data.

---

## Setup

Run the following commands in your Ubuntu/WSL terminal to set up the environment and install dependencies:

```bash
sudo apt update
sudo apt install -y python3-full python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install pandas scikit-learn pyarrow jupyter