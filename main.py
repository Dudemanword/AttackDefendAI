from GenerateTrainingData import GenerateTrainingData
from GenerateTestData import GenerateTestData
from typing import Dict, List
from actions import Action
from result import Result

trainingData: List[Action, Action, Result] = GenerateTrainingData()
testData = GenerateTestData(60000)
print(trainingData[0])