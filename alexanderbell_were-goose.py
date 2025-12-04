'''

'''
import pygame, simpleGE

class Introduction (simpleGE.Scene):
    def __init__(self, size= (1280,720)):
        super().__init__(size)
        self.setImage("assets/white.png")
        self.response = "quit"

        self.title = simpleGE.MultiLabel()
        self.title.text = "TEST INTRO TEXT"
        self.title.size = (500,300)

        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "PLAY"
        self.btnPlay.center = (100,800)
        self.btnPlay.bgColor = "green"

        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "QUIT"
        self.btnQuit.center = (100,400)
        self.btnQuit.bgColor = "red"

        self.sprites = [self.title, self.btnPlay, self.btnQuit]

    def process(self):
        if self.btnQuit.clicked: 
            self.response = "quit"
        if self.btnPlay.clicked: 
            self.response = "start"


class Desk (simpleGE.Scene):
    def __init__(self, phase = 0, size = (1280,720), support = 0, awareness = 0, survivors = 0, casualties = 0, turns_left = 0):
        super().__init__(size)
#        self.setImage("assets/desk-background.png") 

        self.background.fill((120, 85, 17))

        self.support = support
        self.awareness = awareness
        self.survivors = survivors
        self.casualties = casualties
        self.turns_left = turns_left

        self.lblSupport = simpleGE.Label()
        self.lblSupport.text = f"Support: {self.support}%"
        self.lblSupport.center = (120,57.5)
        self.lblSupport.size = (200,75)

        self.lblAwareness = simpleGE.Label()
        self.lblAwareness.text = f"Awareness: {self.awareness}%"
        self.lblAwareness.center = (120,157.5)
        self.lblAwareness.size = (200,75)

        self.lblSurvivors = simpleGE.Label()
        self.lblSurvivors.text = f"Survivors: {self.survivors}"
        self.lblSurvivors.center = (345,57.5)
        self.lblSurvivors.size = (200,75)

        self.lblCasualties = simpleGE.Label()
        self.lblCasualties.text = f"Casualties: {self.casualties}"
        self.lblCasualties.center = (345,157.5)
        self.lblCasualties.size = (200,75)

        self.lblTurnsLeft = simpleGE.Label()
        self.lblTurnsLeft.text = f"Turns Left: {self.turns_left}"
        self.lblTurnsLeft.center = (1116,57.5)
        self.lblTurnsLeft.size = (200,75)

        self.btnApprove = simpleGE.Button()
        self.btnApprove.text = "APPROVE"
        self.btnApprove.size = (80,40)
        self.btnApprove.position = (1585,580)
#        self.btnApprove.bgColor = "green"

        self.btnDeny = simpleGE.Button()
        self.btnDeny.text = "DENY"
        self.btnDeny.size = (80,40)
        self.btnDeny.position = (1900,580)
#        self.btnDeny.bgColor = "red"


        self.response = "remain_desk"

        self.document_A = Document_A(self)
        self.document_B = Document_B(self)


        self.sprites = [self.lblTurnsLeft, self.lblSupport, self.lblAwareness, self.lblSurvivors, self.lblCasualties, self.document_A, self.document_B, self.btnApprove, self.btnDeny]
        
        self.phase = phase
    def process(self):

# switch to the map every 2 document decisions
        if self.phase == 0:
            if self.btnApprove.clicked:
                self.document_A.visible = False
                self.document_A.update_values_accept()
                self.phase += 1

            if self.btnDeny.clicked:
                self.document_A.visible = False
                self.document_B.visible
                self.document_A.update_values_deny()
                self.phase += 1

        if self.phase == 1:
            if self.btnApprove.clicked:
                self.document_B.visible = False
                self.document_B.update_values_accept()
                self.phase += 1

            if self.btnDeny.clicked:
                self.document_B.visible = False
                self.document_B.update_values_deny()
                self.phase += 1

        if self.phase == 2:
            self.response = "go_to_map"
            self.stop()



class Document_A (simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)
        
        self.setImage("assets/document_A.png")
        self.setSize(315,460)
        self.position = (687.5,385)

    def update_values_accept(self):
        self.scene.support -= 100
        self.scene.awareness -= 100
    def update_values_deny(self):
        self.scene.support += 100
        self.scene.awareness += 100

	
class Document_B (simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)

        self.setImage("assets/document_B.png")
        self.setSize(315,460)
        self.position = (687.5,385)
#        self.visible = False

    def update_values_accept(self):
        self.scene.support += 100
        self.scene.awareness += 20
    def update_values_deny(self):
        self.scene.support -= 100
        self.scene.awareness -= 100




def main():
    keepGoing = True
    while keepGoing:
        game = Desk()
        game.start()



'''
    keepGoing = True
    while keepGoing:
        intro = Introduction()
        intro.start()
        if intro.response == "start":
            game = Desk()
            game.start()
'''
if __name__ == "__main__":
    main()




