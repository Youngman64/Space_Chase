# Space_Chase
## Game Description
Space Chase is a  game where an alien gets chased by different mobs from different planets. Each planet is a different level progressively getting more difficult and adding more mobs and powerups. The player colects credits while being chased by mobs. Once they get enough credits a rocket ship will appear. Running into the rockecship will transport the player to the next level. The player wins by beating all 10 levels. 
## Functions
1. move_player: The most basic function of this game will be the function of moving a character around the 2D space using the arrow keys. This will allow the player to move up, down, left, right, and diagnal. So far I have drawn a rectangle to represent the player and connected the keyboard inputs of A, S, D, and E to correspond with the rectangle moving in different directions.  
2. spawn_mobs(level: int) -> list: This function generates enemy mobs based on the current planet’s difficulty level, increasing their number and abilities as the player progresses. Each mob type has unique movement patterns and behaviors that keep the game feeling fresh.
3. use_powerup(powerup_name: str) -> None: This function will allow for a string of powerups to be spawned in at random to the maze. Each power up give the player different advantages during different stages of gameplay.
