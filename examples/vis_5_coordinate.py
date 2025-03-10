import numpy as np
import matplotlib.pyplot as plt
from pytransform3d.transformations import transform, plot_transform
from scipy.spatial.transform import Rotation as R

# Helper function to create a transformation matrix (Rotation + Translation)
def create_transformation(rotation_angles, translation_vector):
    """Create a 4x4 transformation matrix."""
    T = np.eye(4)
    T[:3, :3] = R.from_rotvec(rotation_angles).as_matrix()  # XYZ Euler rotation
    T[:3, 3] = translation_vector  # Translation
    return T

# Define 5 frames with different transformations
frames = [
    create_transformation((0, 0, 0), (0, 0, 0)),  # Frame A (Origin)
    create_transformation((0.5, 0.3, 0), (1, 0, 0)),  # Frame B
    create_transformation((0, 0.5, 0.3), (0, 1, 0)),  # Frame C
    create_transformation((0.3, 0, 0.5), (0, 0, 1)),  # Frame D
    create_transformation((0.2, 0.1, 0.4), (1, 1, 1)),  # Frame E
]

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot all frames in sequence
origin = np.eye(4)  # The base frame (world frame)

for i, frame in enumerate(frames):
    plot_transform(ax=ax, A2B=frame, s=0.3, name=f"Frame {chr(65 + i)}")

# Customize the plot
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.title("Visualization of 5 Coordinate Frames")
plt.show()
