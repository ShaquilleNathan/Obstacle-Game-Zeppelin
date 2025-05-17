# 🎈 Zeppelin Obstacle Game

A Python-based **side-scrolling obstacle game** where the player controls a zeppelin and must avoid various hazards like bees, caves, and trees. The game challenges your reflexes and precision as you navigate through an increasingly difficult environment.

---

## 🎮 Features

- 🌪️ **Side-scrolling gameplay**: Navigate a zeppelin by click `mouse` or using `touchpad` to fly through an endless course filled with dynamic obstacles.
- 🐝 **Multiple Hazards**: Avoid bees, caves, and trees that appear as you move forward.
- 🧠 **Score System**: Earn points for every cave or tree successfully passed.
- ❌ **Instant Game Over**: Colliding with the ground, sky, or any obstacle (bees, caves, or trees) ends the game.

---

## 🧠 Game Logic

1. The player controls a zeppelin that continuously moves forward across the screen.
2. The environment scrolls to simulate movement, and random obstacles appear along the path.
3. The player must carefully maneuver the zeppelin to avoid:
   - Bees flying in random patterns.
   - Caves that form upper or lower tunnel challenges.
   - Trees placed in varying vertical positions.
4. Scoring:
   - Each time the player successfully passes a **cave** or a **tree**, **1 point** is added to the score.
5. Game Over Conditions:
   - The game ends immediately if the zeppelin:
     - Touches the **ground** or the **sky/ceiling**.
     - Collides with any **bee**, **cave**, or **tree**.

<div align="center">
  <img src="https://i.postimg.cc/zBVL3qwr/2025-05-17-31.png" alt="Demo Image" style="width: 300px; height: auto;" />
  <img src="https://i.postimg.cc/9MZDyJk8/2025-05-17-29.png" alt="Demo Image" style="width: 300px; height: auto;" />
</div>

---

## 🔧 Requirements

- Python 3.x
- Pygame library

To install Pygame, run:
```bash
pip install pygame
```

---

## 🔑 Controls
- Use a `mouse` or `touchpad` to control the zeppelin's vertical movement.
- The control scheme may vary depending on your implementation.

---

## Notes
This is a basic python game-development project. You can explore and modify it yourself to make it better!
