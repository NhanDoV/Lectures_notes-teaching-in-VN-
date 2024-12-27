import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

class CircleSimulation:
    """
        Instruction
        >> # Instantiate and run the simulation
        >> simulation = CircleSimulation()
        >> simulation.run()
    """
    def __init__(self):
        self.pi = np.pi
        self.coordinates = [(r * np.cos(t), r * np.sin(t)) 
                            for r in np.linspace(2, 10, 21) 
                            for t in np.linspace(0, 2 * self.pi, 101)]
        self.fig, self.ax = plt.subplots()
        self.circle, = self.ax.plot([], [], 'go', markersize=15, zorder=5)  # Green circle marker
        
        self._setup_plot()

    def _setup_plot(self):
        """Configure the plot axes, title, and grid."""
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_title('Simulating Center-circling Over Time')
        self.ax.set_xticks(np.arange(-11, 12, 1))
        self.ax.set_yticks(np.arange(-11, 12, 1))
        self.ax.set_axis_off()
        self.ax.grid(True)

    def init_circle(self):
        """Initialize the circle's position."""
        self.circle.set_data([], [])
        return self.circle,

    def update_circle(self, frame):
        """Update the circle's position and title for each frame."""
        if frame < len(self.coordinates):
            x, y = self.coordinates[frame]
        else:
            x, y = self.coordinates[-1]  # Keep the circle at the last coordinate
        
        # Update the circle's position
        self.circle.set_data([0, x], [0, y])
        
        # Update the title with the current coordinates
        self.ax.set_title(f'Circling-simulation   current-coordinate: (x={x:.2f}, y={y:.2f})')
        return self.circle,

    def run(self):
        """Run the animation."""
        ani = animation.FuncAnimation(self.fig, self.update_circle, 
                                      frames=len(self.coordinates), 
                                      init_func=self.init_circle, 
                                      interval=10, repeat=False)
        plt.show()

class MazeAnimation:
    """
        Instruction:
        >> # Instantiate and run the maze animation
        >> maze_animation = MazeAnimation()
        >> maze_animation.run()    
    """
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.maze = np.ones((height, width))
        self.edges = []  # List to store the edges
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions for movement
        self.entrance = (1, 0)  # Entrance position
        self.exit = (width - 2, height - 1)  # Exit position
        self.generate_maze(1, 1)  # Start maze generation
        
        self.fig, self.ax = plt.subplots()

    def generate_maze(self, x, y):
        """Generate a maze using Depth-First Search (DFS) and track edges."""
        self.maze[y, x] = 0
        random.shuffle(self.directions)
        for direction in self.directions:
            nx, ny = x + direction[1] * 2, y + direction[0] * 2
            if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny, nx] == 1:
                self.maze[y + direction[0], x + direction[1]] = 0
                self.edges.append(((x, y), (nx, ny)))  # Track the edge
                self.generate_maze(nx, ny)

    def create_maze_frame(self, frame):
        """Update the maze animation frame by drawing edges incrementally and marking the entrance and exit."""
        self.ax.clear()
        self.ax.set_xlim(-0.5, self.width - 0.5)
        self.ax.set_ylim(-0.5, self.height - 0.5)
        self.ax.set_aspect('equal')
        self.ax.invert_yaxis()

        # Draw the edges up to the current frame
        for i in range(frame + 1):
            (x1, y1), (x2, y2) = self.edges[i]
            self.ax.plot([x1, x2], [y1, y2], 'b-', lw=2)
        
        # Mark the entrance (always visible)
        self.ax.text(self.entrance[1], self.height - self.entrance[0] - 1, 'In', color='red', fontsize=10, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))
        
        # Mark the exit (only visible on the last frame)
        if frame == len(self.edges) - 1:
            self.ax.text(self.exit[1], self.height - self.exit[0] - 1, 'Out', color='green', fontsize=10, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))

        # Hide the ticks
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_title(f'Frame {frame + 1}')

    def run(self):
        """Run the maze animation."""
        frame_count = len(self.edges)
        ani = animation.FuncAnimation(self.fig, self.create_maze_frame, frames=frame_count, interval=50, repeat=False)
        plt.show()

class GravitySimulation:
    """
        Instruction
        >> # Instantiate and run the gravity simulation
        >> gravity_simulation = GravitySimulation()
        >> gravity_simulation.run()    
    """
    def __init__(self):
        self.pi = np.pi
        
        # Define the coordinates for simulation
        self.xy1 = [(x, abs(19*np.sin(self.pi*x / 5))) if x < 5 else (x, abs(17*np.sin(self.pi*x / 5))) for x in np.linspace(0, 10, 101)]
        self.xy2 = [(x, abs(15*np.sin(self.pi*x / 5))) if x > 5 else (x, abs(13*np.sin(self.pi*x / 5))) for x in np.linspace(10, 0, 101)]
        self.xy3 = [(x, abs(11*np.sin(self.pi*x / 5))) if x < 5 else (x, abs(9*np.sin(self.pi*x / 5))) for x in np.linspace(0, 10, 101)]
        self.xy4 = [(x, abs(7*np.sin(self.pi*x / 5))) if x > 5 else (x, abs(5*np.sin(self.pi*x / 5))) for x in np.linspace(10, 0, 101)]
        self.xy5 = [(x, abs(3*np.sin(self.pi*x / 5))) if x < 5 else (x, abs(1*np.sin(self.pi*x / 5))) for x in np.linspace(0, 10, 101)]
        
        self.coordinates = self.xy1 + self.xy2 + self.xy3 + self.xy4 + self.xy5
        
        # Initialize figure and axis
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 12)
        self.ax.set_ylim(0, 20)
        self.ax.set_title('Simulating Gravity Fading Over Time')
        self.ax.set_xticks(np.arange(-0.6, 12, 1))
        self.ax.set_yticks(np.arange(-0.6, 20, 1))
        self.ax.set_axis_off()
        self.ax.grid(True)

        # Add a scatter plot for the circle
        self.circle, = self.ax.plot([], [], 'go', markersize=15, zorder=5)  # 'ko' for black circle marker

    def init(self):
        self.circle.set_data([], [])
        return self.circle,

    def update(self, frame):
        if frame < len(self.coordinates):
            x, y = self.coordinates[frame]
        else:
            x, y = self.coordinates[-1]  # Ensure circle stays at last coordinate if frames exceed list length
        
        # Update the circle's position (ensure x and y are sequences)
        self.circle.set_data([x], [y])
        
        # Update the title with the current coordinates
        self.ax.set_title(f'Gravity-simulation   current-coordinate: (x={x:.2f}, y={y:.2f})')

        return self.circle,

    def run(self):
        """Run the gravity simulation animation."""
        ani = animation.FuncAnimation(self.fig, self.update, frames=len(self.coordinates), 
                                      init_func=self.init, interval=5, repeat=False)
        plt.show()

class KnightMoveSimulation:
    """
        Instruction:
        >> # Instantiate and run the knight move simulation
        >> knight_simulation = KnightMoveSimulation(grid_size=10)
        >> knight_simulation.run(frames=10, interval=1000)        
    """
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        
        # Define possible knight moves
        self.knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        # Initialize figure and axis
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-0.5, self.grid_size + 0.5)
        self.ax.set_ylim(-0.5, self.grid_size + 0.5)
        self.ax.set_title('Knight move (x, y)')
        self.ax.set_xticks(np.arange(0, self.grid_size + 1, 1))
        self.ax.set_yticks(np.arange(0, self.grid_size + 1, 1))
        self.ax.grid(True)

        # Add a scatter plot for the circle
        self.circle, = self.ax.plot([], [], 'ko', markersize=15)  # 'ko' for black circle marker

        # Initialize the starting position
        self.current_position = (0.5, 0.5)  # Default starting position

    def init(self):
        self.circle.set_data([], [])
        return self.circle,

    def update(self, frame):
        if frame == 0:
            # Start from a random position
            self.current_position = (0.5 + np.random.randint(self.grid_size), 0.5 + np.random.randint(self.grid_size))
        else:
            # Calculate next position
            possible_moves = [(self.current_position[0] + dx, self.current_position[1] + dy) for dx, dy in self.knight_moves]
            possible_moves = [(x, y) for x, y in possible_moves if 0 <= x < self.grid_size and 0 <= y < self.grid_size]
            
            if possible_moves:
                self.current_position = possible_moves[np.random.randint(len(possible_moves))]
        
        # Update the circle's position
        self.circle.set_data([self.current_position[0]], [self.current_position[1]])
        
        # Update the title with the current coordinates
        self.ax.set_title(f'Knight move (x={self.current_position[0]}, y={self.current_position[1]}), frame_id: {frame}')

        return self.circle,

    def run(self, frames=10, interval=1000):
        """Run the knight move simulation animation."""
        ani = animation.FuncAnimation(self.fig, self.update, frames=frames, 
                                      init_func=self.init, interval=interval, repeat=True)
        plt.show()