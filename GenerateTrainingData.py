from player import Player
import random
from enemy import Enemy
from result import Result
from determinator import Determinator
from typing import Dict, List, Tuple
from actions import Action

#Generate random list of attack/defend from a player
#Get response from enemy
#Classify result as good or bad
def GenerateTrainingData() -> List[Tuple[Action, Action, Result]] :
    classificationData = []
    
    badGuy: Enemy = Enemy()
    combatResultDeterminator: Determinator = Determinator()
    for trainingData in range(10000):
        playerAction: Action = GetPlayerAction()
        enemyResponse: Action = badGuy.Response(playerAction)
        result: Result = combatResultDeterminator.DetermineResult(enemyResponse)
        classificationData.append(
            (playerAction, enemyResponse, result)
        )

    return classificationData

def GetPlayerAction() -> Action:
    mainPlayer: Player = Player()
    randomValue: int = random.randrange(0, 2)
    if(randomValue == 0):
        return mainPlayer.Attack()
    elif(randomValue == 1):
        return mainPlayer.Defend()