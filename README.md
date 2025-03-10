# Space_Chase
## Game Description
Chase Space is a maze chase game where an alien gets chased by different mobs from different planets. Each planet is a different level progressively getting more difficult and adding more mobs and powerups. It is like Pac-Man in a way with the a similar set up of the player being chased in a maze. However the player is graded based on a teraform score, of how succesfully they are able to defeat the mobs in their enviornment, collect credits, and plant crops. The player can leave the planet as soon as they get enough credits to fly the rocket to the next planet, however they can also stay longer if they want to improve their teraform score by planting crops and defeating aliens. There is a strategy to it as well because if a player stays longer they can save up credits and spend less time on other planets in the future.
## Functions
1. move_player(direction: str) -> None: The most basic function of this game will be the function of moving a character around the 2D space using the arrow keys. This will allow the player to move up, down, left, right, and possibly diagnal if I decide to allow that.
2. spawn_mobs(level: int) -> list: This function generates enemy mobs based on the current planet’s difficulty level, increasing their number and abilities as the player progresses. Each mob type has unique movement patterns and behaviors that keep the game feeling fresh.
3. use_powerup(powerup_name: str) -> None: This function will allow for a string of powerups to be spawned in at random to the maze. Each power up give the player different advantages during different stages of gameplay.
