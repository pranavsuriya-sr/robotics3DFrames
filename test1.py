import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to create a rotation matrix
def rotation_matrix(axis, theta):
    axis = np.asarray(axis)
    axis = axis / np.sqrt(np.dot(axis, axis))
    a = np.cos(theta / 2.0)
    b, c, d = -axis * np.sin(theta / 2.0)
    return np.array([
        [a*a + b*b - c*c - d*d, 2*(b*c - a*d), 2*(b*d + a*c)],
        [2*(b*c + a*d), a*a + c*c - b*b - d*d, 2*(c*d - a*b)],
        [2*(b*d - a*c), 2*(c*d + a*b), a*a + d*d - b*b - c*c]
    ])

# Function to plot the frame
def plot_frame(ax, origin, R, color='b'):
    ax.quiver(origin[0], origin[1], origin[2], R[0, 0], R[1, 0], R[2, 0], color='r')
    ax.quiver(origin[0], origin[1], origin[2], R[0, 1], R[1, 1], R[2, 1], color='g')
    ax.quiver(origin[0], origin[1], origin[2], R[0, 2], R[1, 2], R[2, 2], color=color)

st.title('3D Real-Time Rotation of Frames')

st.sidebar.markdown("# Change rotation angles: ")

# Streamlit sidebar for selecting rotation angles
x_angle = st.sidebar.slider('Rotate around X-axis (degrees)', 0, 360, 0)
y_angle = st.sidebar.slider('Rotate around Y-axis (degrees)', 0, 360, 0)
z_angle = st.sidebar.slider('Rotate around Z-axis (degrees)', 0, 360, 0)

# Convert angles to radians
x_angle = np.deg2rad(x_angle)
y_angle = np.deg2rad(y_angle)
z_angle = np.deg2rad(z_angle)

# Define the rotation matrices
Rx = rotation_matrix([1, 0, 0], x_angle)
Ry = rotation_matrix([0, 1, 0], y_angle)
Rz = rotation_matrix([0, 0, 1], z_angle)

# Combined rotation matrix
R = Rz @ Ry @ Rx

# Plotting the frames dynamically
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Plot the original frame (identity matrix)
plot_frame(ax, [0, 0, 0], np.eye(3), color='b')
# Plot the rotated frame
plot_frame(ax, [0, 0, 0], R, color='orange')

# Set labels with smaller font sizes
ax.set_xlabel('X', fontsize=10)
ax.set_ylabel('Y', fontsize=10)
ax.set_zlabel('Z', fontsize=10)

# Set tick label sizes
ax.tick_params(axis='both', which='major', labelsize=6)

# Set the view angle
ax.view_init(elev=20, azim=30)

st.pyplot(fig)


st.sidebar.markdown(
    '<div style="text-align:center; margin-top: 152px">'
    '<a href="https://pranavsuriya.netlify.app/" style="text-decoration: none;" ><p style="font-size: 10px;">PS Devs © 2023 Project Hack Community.</a></p>'
    '<p style="font-size: 10px;">Open Source rights reserved.</p>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div style="text-align:center; margin-top: 42px">'
    '<a href="https://pranavsuriya.netlify.app/" style="text-decoration: none;" ><p style="font-size: 10px;">PS Devs © 2023 Project Hack Community.</a></p>'
    '<p style="font-size: 10px;">Open Source rights reserved.</p>'
    '</div>',
    unsafe_allow_html=True
)