from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2

for x in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for y in range(4):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()