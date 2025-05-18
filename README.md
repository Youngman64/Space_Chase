# Space_Chase
## Game Description
Space Chase is a  game where an alien gets chased by different an enemy on different planets. To access the next planet the player has to colect the required amount of credits. Once the correct amount of credits is collected the player can hit the rocketship which will take them to the next planet. If at any point the player runs into the enemy they lose. If they succsessfully survive all 10 planets then they win.
## Functions
1. move_player(keys, player_speed)
Handles the player's movement using the arrow keys. It updates the player's position while making sure they stay within screen boundaries. Movement is smooth and responsive in all directions.

2. apply_magnet_effect(player_x, player_y, credit_positions)
This ability is unique to Zicro. When the Space key is pressed, credits within a certain radius are pulled toward the player like a magnet, making it easier to collect them quickly.

3. track_enemy(player_x, player_y, enemy_x, enemy_y, speed)
This mechanic constantly updates the enemy’s position so it follows the player. The enemy moves toward the player’s coordinates, making it feel like it’s chasing them in real time.



## Use Cases
1. Really the only use for this is entertainment. It is a game that is made for the purpose of having fun playing it.
