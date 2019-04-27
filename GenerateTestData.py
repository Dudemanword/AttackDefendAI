from player import Player
from enemy import Enemy
from actions import Action
from typing import Dict, List, Tuple
import random

def GenerateTestData(iterations: int) -> List[Tuple[Action, Action]]:
    testData: List[Action, Action] = []
    badGuy:Enemy = Enemy()
    for iter in range(iterations):
        playerAction: Action = GeneratePlayerAction()
        testData.append((playerAction, badGuy.Response(playerAction)))
    return testData

def GeneratePlayerAction() -> Action:
    mainPlayer: Player = Player()
    randomValue = random.randrange(0,2)
    if randomValue == 0:
        return mainPlayer.Attack()
    else:
        return mainPlayer.Defend()