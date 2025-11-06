import idx2numpy
import matplotlib.pyplot as plt

# Load MNIST
train_images = idx2numpy.convert_from_file('Data/train-images.idx3-ubyte')

# Function to display images from start index
def show_images(start_index):
    plt.figure(figsize=(10,10))
    for i in range(25):  # 5x5 grid
        plt.subplot(5,5,i+1)
        idx = start_index + i
        if idx < train_images.shape[0]:
            plt.imshow(train_images[idx], cmap='gray')
        plt.axis('off')
    plt.show()

# Example: show first 25
show_images(0)

# You can change start_index to see the next batch
# show_images(25), show_images(50), etc.