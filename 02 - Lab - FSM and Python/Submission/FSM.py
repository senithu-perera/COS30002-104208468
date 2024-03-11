class GameCharacter:
    def __init__(self):
        self.state = "Chasing"

    def attack(self):
        if self.state == "Chasing":
            print("Attacking!")
            self.state = "Attacking"
        else:
            print("Already in attacking state")

    def chase(self):
        if self.state == "Attacking":
            print("Switching to chasing mode")
            self.state = "Chasing"
        else:
            print("Already in chasing state")

    def display_state(self):
        print(f"Character is currently {self.state}")


# Example usage
game_character = GameCharacter()

game_character.display_state()
game_character.attack()
game_character.display_state()
game_character.chase()
game_character.display_state()
