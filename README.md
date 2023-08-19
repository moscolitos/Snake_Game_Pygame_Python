# 🐍 Python Snake Game Using Pygame

Created by Mosco on Sat Aug 19, 2023.

An enthralling rendition of the classic Snake game using Python and Pygame. Navigate your snake through the grid, grow in length by consuming food, and level up while avoiding collisions with yourself!

## Features:
- 🟩 Classic snake gameplay with modern twists.
- 🌟 Points system that rewards you for every food consumed.
- 🚀 Dynamic leveling system - the game speeds up as you level up.
- 🎮 Smooth arrow key controls for snake movement.
- 🌈 Crisp graphics with distinct colors for better visibility.

## Installation:
Clone the repository.
git clone https://github.com/Mosco/SnakeGame.git

Navigate to the project directory.

cd SnakeGame

Install pygame if you haven't already.

pip install pygame

Run the game.

python snake_game.py

## How to Play:
Use the arrow keys (↑, ↓, ←, →) to move the snake.

Consume the red food that randomly appears.

Every food you consume will increase your snake's length.

The game speeds up as you earn more points.

Avoid running into yourself - this will end the game.

## Game Structure:
- Classes:

Snake: Represents the snake entity. Key methods include:

move(): Propels the snake based on its direction.

grow_snake(): Increases the snake's length.

change_direction(): Alters the snake's movement direction based on user input.

draw(): Renders the snake on the game screen.

Food: Represents the food entity. Key methods:

randomize_position(): Picks a new random position for the food item.

draw(): Displays the food on the game screen.

Game: The main game orchestrator. Key methods include:

check_collision(): Checks if the snake has eaten the food or collided with itself.

level_up(): Increases game difficulty.

run(): Central game loop, managing all game mechanics.

## Contribute:
Feel free to fork, improve, make pull requests or fill issues. I'll appreciate any help and insight to make the game better and more fun!

## Credits:
Game logic, design, and coding: Mosco

## Libraries used: Pygame
## License:
This project is licensed under the MIT License. See LICENSE for more details.
