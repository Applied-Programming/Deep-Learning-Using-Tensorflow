# train_model.py

import numpy as np

print("Loading Alexnet...")
from alexnet import alexnet
WIDTH = 250
HEIGHT = 60
LR = 1e-3
EPOCHS = 5
MODEL_NAME = 'pydinoai-{}-{}-{}-epochs-2k-data.model'.format(LR, 'alexnetv2',EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)
print("Loaded Alexnet.")

for i in range(EPOCHS):
    final_train_data = np.load('final_training_data.npy')
    print(len(final_train_data))

    train = final_train_data[:-6000]
    test = final_train_data[-6000:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
        snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

    model.save(MODEL_NAME)

# tensorboard --logdir=foo:C:/path/to/log
# tensorboard --logdir=foo:C:\Users\HP\Desktop\PyDinoAI\log
