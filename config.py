import os
import torch

# This finds the folder you are currently in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to your MNIST data
DATA_PATH = os.path.join(BASE_DIR, "data")

# Hardware Selection (Optimized for your Mac Air)
DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# Training Settings
BATCH_SIZE = 64
EPOCHS = 5
LEARNING_RATE = 0.001