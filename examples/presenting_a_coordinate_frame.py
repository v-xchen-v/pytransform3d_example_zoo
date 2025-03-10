import numpy as np
import matplotlib.pyplot as plt
from pytransform3d.transformations import plot_transform
from scipy.spatial.transform import Rotation as R

# Helper function to create a transformation matrix with rotation and translation
def create_frame(origin, euler_angles):
    """
    Create a 4x4 transformation matrix for a frame with a given origin and rotation.
    
    Parameters:
    - origin: A tuple (x, y, z) representing the origin of the frame.
    - euler_angles: A tuple (roll, pitch, yaw) for the frame's rotation in radians.
    
    Returns:
    - A 4x4 transformation matrix.
    """
    T = np.eye(4)  # Initialize 4x4 identity matrix
    T[:3, :3] = R.from_rotvec(euler_angles).as_matrix()  # Apply rotation
    T[:3, 3] = origin  # Set the origin (translation)
    return T

# Create frames with different origins and rotations
frame_A = create_frame((0, 0, 0), (0, 0, 0))  # Frame A at origin with no rotation
frame_B = create_frame((1, 1, 0), (0, np.pi/4, 0))  # Frame B rotated 45° about Y-axis

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot Frame A (at the origin)
plot_transform(ax=ax, A2B=frame_A, s=0.5, name="Frame A")

# Plot Frame B (rotated and translated)
plot_transform(ax=ax, A2B=frame_B, s=0.5, name="Frame B")

# Set plot limits
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])

# Add labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.title("Visualization of Coordinate Frames with Origin and Axes Directions")

# Show the plot
plt.show()
