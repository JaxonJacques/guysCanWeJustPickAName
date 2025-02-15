import random

class Workout:

    def skibidiForniteMonster():
        first = random.randint(1, 10)

        match first:
            case 1:
                exercise = "Wrist Extension"
            case 2:
                exercise = "Heel-To-Toe Walk"
            case 3:
                exercise = "Squats"
            case 4:
                exercise = "Chair Sit-To-Stand"
            case 5:
                exercise = "Step Ups"
            case 6:
                exercise = "Pelvic Tilts"
            case 7:
                exercise = "Bird-Dog Exercise"
            case 8:
                exercise = "Reach Up and Down"
            case 9:
                exercise = "Tree Pose"
            case 10:
                exercise = "Side Stretch"

        print(f"The selected exercise is {exercise}.")
    skibidiForniteMonster()