from GenerateTrainingData import GenerateTrainingData
from GenerateTestData import GenerateTestData
from typing import List,Tuple
from actions import Action
from result import Result

import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

trainingData: List[Tuple[Action, Action, Result]] = GenerateTrainingData()
trainingPlayerActions = []
trainingEnemyResponse = []
trainingResults = []

testPlayerActions = []
testEnemyResponse = []
testResults = []

for res in trainingData:
    trainingPlayerActions.append(res[0].value)
    trainingEnemyResponse.append(res[1].value)
    trainingResults.append(res[2].value)

testData:List[Tuple[Action, Action, Result]] = GenerateTestData(60000)
for res in testData:
    testPlayerActions.append(res[0].value)
    testEnemyResponse.append(res[1].value)
    testResults.append(res[2].value)

model = keras.Sequential([
    keras.layers.Dense(2, activation=tf.nn.relu, input_shape=(1,)),
    keras.layers.Dense(2, activation='softmax')
])
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
q = np.array(trainingPlayerActions)
z = np.array(testResults)

model.fit(np.array(trainingPlayerActions), np.array(trainingResults), epochs=10, steps_per_epoch=1000)
test_loss, test_acc = model.evaluate(np.array(testPlayerActions), np.array(testResults))
print('Test accuracy:', test_acc)