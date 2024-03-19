class GameCharacter:
    def __init__(self):
        self.state = "Chasing"
        self.enemy_Distance = 57.5;
        self.enemy_Health = 100;
        self.enemy_Attackrate = 10;

    def attack(self):
        if self.state == "Chasing" and self.enemy_Distance <= 10:
            print("Attacking!")
            self.state = "Attacking"
            player_health -= self.enemy_Attackrate
        else:
            print("Already in attacking state")

    def chase(self):
        if self.state == "Attacking" and self.enemy_Distance > 10:
            print("Switching to chasing mode")
            self.state = "Chasing"
        else:
            print("Already in chasing state")

    def Stand(self):
        if self.state == "Chasing" and self.enemy_Distance > 50:
            print("Switching to Standing mode")
            self.state = "Stand"
        else:
            print("Already in Standing state")

    def display_state(self):
        print(f"Character is currently {self.state}")


# Example usage
game_character = GameCharacter()

game_character.display_state()
game_character.attack()
game_character.display_state()
game_character.chase()
game_character.display_state()
game_character.Stand()
