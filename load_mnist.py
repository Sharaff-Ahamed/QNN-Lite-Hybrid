import idx2numpy

train_images = idx2numpy.convert_from_file('Data/train-images.idx3-ubyte')
train_labels = idx2numpy.convert_from_file('Data/train-labels.idx1-ubyte')
test_images = idx2numpy.convert_from_file('Data/t10k-images.idx3-ubyte')
test_labels = idx2numpy.convert_from_file('Data/t10k-labels.idx1-ubyte')

print("Train Images Shape:", train_images.shape)
print("Test Images Shape:", test_images.shape)