from actions import Action
class Player:
    def Attack(self) -> Action:
        return Action.ATTACK
    def Defend(self):
        return Action.DEFEND