from pytransform3d.urdf import UrdfTransformManager
import pytransform3d.visualizer as pv
import numpy as np
import time

# Initialize the URDF Transform Manager
tm = UrdfTransformManager()

# Load the URDF file
urdf_filepath = "/home/yichao/Documents/repos/pytransform3d_example_zoo/data/rm_75_6f_description/urdf/rm_75_6f_description.urdf"
urdf_content = open(urdf_filepath, "r").read()
tm.load_urdf(urdf_content)

# Joint names as per your URDF
joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6', 'joint7']

# Create the figure for visualization
fig = pv.figure("URDF Animation")
fig.set_zoom(1.2)
# Plot the initial robot graph
graph = fig.plot_graph(
    tm, "base_link", show_frames=True, show_connections=True, show_name=True,
    whitelist=['base_link', 'Link1', 'Link2', 'Link3', 'Link4', 'Link5', 'Link6', 'Link7'],
    s=0.05
)
fig.view_init()

# Define the animation loop with varying joint angles
def animate():
    fig.animate(
        animation_callback, n_frames, loop=True, fargs=(n_frames, tm, graph))
    fig.show()
    
    # for t in np.linspace(0, 2 * np.pi, 100):  # Generate 100 frames in one full cycle
    #     joint_angles = [0.2 * np.sin(t + i) for i in range(len(joint_names))]

    #     # Update joint angles in the URDF model
    #     for name, angle in zip(joint_names, joint_angles):
    #         tm.set_joint(name, angle)
         
    #     # Clear the previous plot and re-plot the frames
         
         
    #     fig.plot_graph(
    #         tm, "base_link", show_frames=True, show_connections=True, show_name=True, 
    #         # show_visuals=True, # this will show the visual meshes, but the urdf file should have the visual meshes
    #         whitelist=['base_link', 'Link1', 'Link2', 'Link3', 'Link4', 'Link5', 'Link6', 'Link7'],
    #         s=0.05
    #     )


    #     time.sleep(0.05)

# Check if running interactively or save the image if not
if "__file__" in globals():
    animate()
else:
    fig.save_image("/tmp/urdf_animation.png")
