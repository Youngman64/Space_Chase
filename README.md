# Space_Chase
## Game Description
Space Chase is a  game where an alien gets chased by different an enemy on different planets. To access the next planet the player has to colect the required amount of credits. Once the correct amount of credits is collected the player can hit the rocketship which will take them to the next planet. If at any point the player runs into the enemy they lose. If they succsessfully survive all 10 planets then they win.
## Functions
1. title_screen()
Handles the game's title screen. It displays the main menu options ("Character Select" and "How To Play") and lets the player use the arrow keys to move between them. Hitting Enter will load the corresponding screen.

2. main_menu()
Lets the player choose between three characters: Electro, Vermus, or Zicro. It uses arrow keys to cycle between characters and Enter to confirm a selection. Each character comes with a unique ability that changes the way the game plays.

3. game_loop(player_index: int)
This is the heart of the game. It tracks player input, updates positions, checks collisions, spawns rocketships, switches levels, plays sounds, and handles ability logic. It also tracks whether the player has won or lost.

4. move_player(keys, player_speed)
Handles the player's movement using the arrow keys. It updates the player's position while making sure they stay within screen boundaries. Movement is smooth and responsive in all directions.

5. apply_speed_boost()
This ability belongs to Electro. When activated by pressing Space, it temporarily doubles the player's speed for 5 seconds, allowing for quick escapes and fast coin collection.

6. apply_invincibility()
This ability belongs to Vermus. When triggered, the player becomes invincible for 5 seconds, letting them pass through the enemy without taking damage. While active, the character is tinted with rainbow colors.

7. apply_magnet_effect(player_x, player_y, credit_positions)
This ability is unique to Zicro. When the Space key is pressed, credits within a certain radius are pulled toward the player like a magnet, making it easier to collect them quickly.

8. track_enemy(player_x, player_y, enemy_x, enemy_y, speed)
This mechanic constantly updates the enemy’s position so it follows the player. The enemy moves toward the player’s coordinates, making it feel like it’s chasing them in real time.

9. how_to_play_screen()
Displays the "How to Play" instructions. It lists the game's objective and controls. The player can return to the main menu by pressing Backspace.

10. you_win_screen() / game_over()
These functions are called when the player wins or loses. They display a full-screen message and hold the screen for a few seconds before returning to the main menu.


## Use Cases
1. Really the only use for this is entertainment. It is a game that is made for the purpose of having fun playing it.
