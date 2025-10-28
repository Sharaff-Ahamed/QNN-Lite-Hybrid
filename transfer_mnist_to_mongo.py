import idx2numpy
from pymongo import MongoClient

# Load MNIST data
train_images = idx2numpy.convert_from_file('Data/train-images.idx3-ubyte')
train_labels = idx2numpy.convert_from_file('Data/train-labels.idx1-ubyte')
test_images = idx2numpy.convert_from_file('Data/t10k-images.idx3-ubyte')
test_labels = idx2numpy.convert_from_file('Data/t10k-labels.idx1-ubyte')

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['mnist_db']

# Collections for train and test
train_collection = db['train_images']
test_collection = db['test_images']

# Helper function to insert data in batches (safe for memory)
def insert_images(collection, images, labels, batch_size=1000):
    total = images.shape[0]
    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        batch = []
        for i in range(start, end):
            img_doc = {
                "index": i,
                "label": int(labels[i]),
                "pixels": images[i].tolist()  # Convert numpy array to list
            }
            batch.append(img_doc)
        collection.insert_many(batch)
        print(f"Inserted images {start} to {end-1}")

# Store training images
insert_images(train_collection, train_images, train_labels)

# Store test images
insert_images(test_collection, test_images, test_labels)

print("All MNIST images stored in MongoDB successfully!")