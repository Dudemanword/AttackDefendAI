from actions import Action
from result import Result
class Determinator():
    def DetermineResult(self, enemyAction) -> Action:
        if(enemyAction == Action.ATTACK):
            return Result.DEATH
        elif(enemyAction == Action.DEFEND):
            return Result.LIVE