# Shapes

A small collection of interactive shape experiments.

## 2D Convex Hull

`2d_hull.py` is a Pygame sketch for building and visualizing a 2D convex hull.

- Click anywhere in the window to add a point.
- Drag an existing point to move it.
- Press `Esc` or close the window to quit.

The hull is generated from the current point set using a monotonic chain style algorithm.

## Setup

Install Python 3 and Pygame:

```powershell
python -m pip install pygame
```

Run the visualizer:

```powershell
python 2d_hull.py
```
