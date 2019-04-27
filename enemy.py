from actions import Action
class Enemy:
    def Response(self, action) -> Action:
        if(action == Action.DEFEND):
            return Action.DEFEND
        elif(Action.ATTACK):
            return Action.ATTACK
        else:
            return Action.ATTACK