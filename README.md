Solar System Model (Pygame)

<img width="1987" height="1392" alt="image" src="https://github.com/user-attachments/assets/ae63899c-3bd5-448c-9525-c8b5a2fbccbf" />

A simple interactive solar system visualization built with Python and Pygame.
It renders:
- A sun at the center of the world
- Multiple planets orbiting the sun
- Orbit rings for each planet
- A starfield background with slower camera movement for a parallax effect

Features
- Real-time orbit animation
- Camera movement with WASD
- Mouse-wheel zoom in and out
- Zoom-aware planet distances and orbit circles

Project Structure
- src/system.py: Main loop, input handling, camera, rendering order
- src/planet.py: Planet orbit math and drawing
- src/star.py: Background star rendering

Requirements
- Python 3.9+
- pygame

Setup
1. Create a virtual environment (optional but recommended):
	python -m venv venv
2. Activate it:
	Windows PowerShell: .\venv\Scripts\Activate.ps1
3. Install dependencies:
	pip install pygame

Run
From the Solar-system-model folder:
python src/system.py

Controls
- W: Move camera up
- A: Move camera left
- S: Move camera down
- D: Move camera right
- Mouse wheel up: Zoom in
- Mouse wheel down: Zoom out
- Close window: Exit simulation

Notes
- Zoom is clamped to a min and max range to keep rendering stable.
- Stars use a slower camera offset than planets/sun to create depth.
