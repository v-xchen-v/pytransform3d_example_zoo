from pytransform3d.urdf import UrdfTransformManager
import pytransform3d.visualizer as pv

tm = UrdfTransformManager()

# load URDF file
urdf_filepath = "/home/yichao/Documents/repos/pytransform3d_example_zoo/data/rm_75_6f_description/urdf/rm_75_6f_description.urdf"
## read the URDF file
urdf_content = open(urdf_filepath, "r").read()
tm.load_urdf(urdf_content)

# set joint angles
joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6', 'joint7']
joint_angles = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
for name, angle in zip(joint_names, joint_angles):
    tm.set_joint(name, angle)
    
# visualize the URDF
fig = pv.figure("URDF")
fig.plot_graph(
    tm, "base_link", show_frames=True, show_connections=True, show_name=True, 
    # show_visuals=True, # this will show the visual meshes, but the urdf file should have the visual meshes
    whitelist=['base_link', 'Link1', 'Link2', 'Link3', 'Link4', 'Link5', 'Link6', 'Link7'],
    s=0.05
)
fig.view_init()
if "__file__" in globals():
    fig.show()
else:
    fig.save_image("/tmp/urdf.png")
