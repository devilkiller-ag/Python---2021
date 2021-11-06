class Remote:
    pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveUp(self):
        pass

    def moveDown(self):
        pass

remote1 = Remote()

Player1 = Player()
if(remote1.isLeftPressed()):
    Player1.moveLeft()
