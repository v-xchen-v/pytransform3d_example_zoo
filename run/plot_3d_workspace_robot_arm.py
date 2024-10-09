import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Or 'Qt5Agg', depending on your setup
import matplotlib.pyplot as plt
from pytransform3d.urdf import UrdfTransformManager
from pytransform3d.transformations import plot_transform
from mpl_toolkits.mplot3d import Axes3D

# Load the URDF file and initialize the transformation manager
def load_urdf_and_initialize():
    urdf_filename = "data/rm_75_6f_description/urdf/rm_75_6f_description.urdf"  # Replace with the path to your URDF file
    tm = UrdfTransformManager()
    with open(urdf_filename, "r") as f:
        urdf = f.read()
    tm.load_urdf(urdf)
    return tm

# Function to sample random joint angles within joint limits
def sample_random_joint_angles(tm, num_samples=1000):
    # get joint limits and names
    # joint_limits = tm.joint_limits()
    joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6', 'joint7']
    
    joint_samples = []
    for _ in range(num_samples):
        joint_angles = []
        for joint_name in joint_names:
            lower_limit, upper_limit = tm.get_joint_limits(joint_name)
            joint_angles.append(np.random.uniform(lower_limit, upper_limit))
        joint_samples.append(dict(zip(joint_names, joint_angles)))
    
    return joint_samples

# Function to compute the end-effector position for a given joint configuration
def compute_end_effector_position(tm, joint_angles):
    # tm.set_joint("base_link", np.eye(4))  # Set the root joint to identity (no transformation)
    for joint_name, joint_angle in joint_angles.items():
        tm.set_joint(joint_name, joint_angle)
    end_effector_pose = tm.get_transform("Link7", "base_link")  # Replace with the correct end-effector name
    end_effector_position = end_effector_pose[:3, 3]  # Extract the position from the 4x4 pose matrix
    return end_effector_position

# Function to plot the initial robot pose in 3D
def plot_initial_robot_pose(tm, ax):
    link_names = ['base_link', 'Link1', 'Link2', 'Link3', 'Link4', 'Link5', 'Link6', 'Link7']
    # Extract and plot the transformation for each link
    for link_name in link_names:
        transform = tm.get_transform(link_name, "base_link")  # Root is the base frame of the robot
        plot_transform(ax, transform, s=0.1, name=link_name)
    return ax

# Main function to compute and plot the workspace
def visualize_workspace(num_samples=1000):
    tm = load_urdf_and_initialize()
    
    # Sample random joint configurations
    joint_samples = sample_random_joint_angles(tm, num_samples)
    
    # Compute end-effector positions for each sampled joint configuration
    end_effector_positions = np.array([
        compute_end_effector_position(tm, joint_angles) for joint_angles in joint_samples
    ])
    
    # Plot the 3D workspace of the robot arm
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')  
    ax.scatter(end_effector_positions[:, 0], end_effector_positions[:, 1], end_effector_positions[:, 2], s=1, c='blue')
    ax.set_title('3D Workspace of Robot Arm')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_zlabel('Z Position')
    
    # Plot the initial robot pose
    # plot_initial_robot_pose(tm, ax)
    
    
    # draw x, y, z axes on origin with red, green, blue colors
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='X')
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Y')
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Z')
    
    plt.show()

# Run the visualization
visualize_workspace(num_samples=10000)
