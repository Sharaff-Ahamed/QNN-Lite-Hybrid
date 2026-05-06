import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import config
import os


def visualize():
    # 1. Load the dataset
    # We use download=False because you have the Kaggle files in the data folder
    try:
        dataset = datasets.MNIST(
            root=config.DATA_PATH,
            train=True,
            download=False,
            transform=transforms.ToTensor()
        )

        # 2. Setup the plot (2 rows, 5 columns)
        fig, axes = plt.subplots(2, 5, figsize=(10, 5))
        fig.suptitle('MNIST Kaggle Dataset Preview', fontsize=16)
        axes = axes.flatten()

        for i in range(10):
            image, label = dataset[i]

            # Convert tensor to a viewable 28x28 grayscale image
            # Squeeze removes the channel dimension (1, 28, 28) -> (28, 28)
            axes[i].imshow(image.squeeze(), cmap='gray')
            axes[i].set_title(f"Digit: {label}")
            axes[i].axis('off')

        plt.tight_layout()
        print("✅ Success! Displaying images...")
        plt.show()

    except Exception as e:
        print(f"❌ Error: Could not load images.")
        print(f"Make sure your .idx-ubyte files are in: {config.DATA_PATH}")
        print(f"\nDetails: {e}")


if __name__ == "__main__":
    visualize()