from player import Player
from enemy import Enemy
from actions import Action
from typing import Dict, List, Tuple
from determinator import Determinator
from result import Result
import random

def GenerateTestData(iterations: int) -> List[Tuple[Action, Action, Result]]:
    testData: List[Action, Action] = []
    badGuy:Enemy = Enemy()
    combatDeterminator: Determinator = Determinator()
    for iter in range(iterations):
        playerAction: Action = GeneratePlayerAction()
        response: Action = badGuy.Response(playerAction)
        testData.append((playerAction, response, combatDeterminator.DetermineResult(response)))
    return testData

def GeneratePlayerAction() -> Action:
    mainPlayer: Player = Player()
    randomValue = random.randrange(0,2)
    if randomValue == 0:
        return mainPlayer.Attack()
    else:
        return mainPlayer.Defend()