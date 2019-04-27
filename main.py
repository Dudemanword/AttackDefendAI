from GenerateTrainingData import GenerateTrainingData
from GenerateTestData import GenerateTestData
from typing import List,Tuple
from actions import Action
from result import Result

trainingData: List[Tuple[Action, Action, Result]] = GenerateTrainingData()
testData = GenerateTestData(60000)
print(testData[0])