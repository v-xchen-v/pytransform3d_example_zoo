import numpy as np
from pytransform3d.transformations import plot_transform, transform

# Helper function to create transformation matrices (rotation + translation)
def create_transformation_matrix(rotation_angles, translation_vector):
    """
    Create a 4x4 transformation matrix with given Euler angles (XYZ) and translation.
    """
    from scipy.spatial.transform import Rotation as R
    T = np.eye(4)
    T[:3, :3] = R.from_rotvec(rotation_angles).as_matrix()
    T[:3, 3] = translation_vector
    return T

# Define transformations between frames
T_sim_to_real = create_transformation_matrix((0.0, 0.0, np.pi/2), (1, 2, 0))  # Example rotation & translation
T_object_sim_to_robot_right_hand_base = create_transformation_matrix((0.1, 0.2, 0.3), (0.5, 0.5, 0.2))
T_object_real_to_robot_right_hand_base = create_transformation_matrix((0, 0, 0), (0.1, 0.1, 0.0))

# Function to apply a transformation to a point (in homogeneous coordinates)
def apply_transformation(T, point):
    """
    Apply a 4x4 transformation matrix T to a 3D point (x, y, z).
    """
    point_homogeneous = np.hstack([point, 1])  # Convert to homogeneous coordinates
    transformed_point = T @ point_homogeneous  # Apply transformation
    return transformed_point[:3]  # Convert back to 3D coordinates

# Example points to transform
object_sim_point = np.array([0.2, 0.3, 0.4])
object_real_point = np.array([1.0, 2.0, 3.0])

# Transform points between frames
transformed_sim_point = apply_transformation(T_object_sim_to_robot_right_hand_base, object_sim_point)
transformed_real_point = apply_transformation(T_object_real_to_robot_right_hand_base, object_real_point)

print("Transformed Simulated Object Point:", transformed_sim_point)
print("Transformed Real Object Point:", transformed_real_point)

# Visualization of the frames and transformations
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot frames: Sim World, Real World, Robot Right Hand, and Object Frames
plot_transform(ax=ax, A2B=np.eye(4), name="sim_world", s=0.2)
plot_transform(ax=ax, A2B=T_sim_to_real, name="real_world", s=0.2)
plot_transform(ax=ax, A2B=T_object_sim_to_robot_right_hand_base, name="object_sim_to_hand", s=0.2)
plot_transform(ax=ax, A2B=T_object_real_to_robot_right_hand_base, name="object_real_to_hand", s=0.2)

# Customize plot appearance
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.title("Visualization of Frame Transformations")
plt.show()
