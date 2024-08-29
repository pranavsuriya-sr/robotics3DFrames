import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to create a rotation matrix
def rotation_matrix(axis, theta):
    axis = axis / np.linalg.norm(axis)
    a = np.cos(theta / 2.0)
    b, c, d = -axis * np.sin(theta / 2.0)
    return np.array([[a*a + b*b - c*c - d*d, 2*(b*c - a*d), 2*(b*d + a*c)],
                     [2*(b*c + a*d), a*a + c*c - b*b - d*d, 2*(c*d - a*b)],
                     [2*(b*d - a*c), 2*(c*d + a*b), a*a + d*d - b*b - c*c]])

# Function to apply rotation to a coordinate frame
def apply_rotation(R, vectors):
    return np.dot(R, vectors)

st.title("Coordinate Frame Rotation Visualization")

st.sidebar.title("Rotation Parameters")

# Get the rotation angles and axes
theta1 = st.sidebar.slider("Rotation 1 Angle (degrees)", 0, 360, 45)
axis1 = st.sidebar.selectbox("Rotation 1 Axis", ["X", "Y", "Z"])

theta2 = st.sidebar.slider("Rotation 2 Angle (degrees)", 0, 360, 45)
axis2 = st.sidebar.selectbox("Rotation 2 Axis", ["X", "Y", "Z"])

# Define the rotation axes
axes = {
    "X": np.array([1, 0, 0]),
    "Y": np.array([0, 1, 0]),
    "Z": np.array([0, 0, 1]),
}

# Convert angles to radians
theta1_rad = np.radians(theta1)
theta2_rad = np.radians(theta2)

# Generate rotation matrices
R1 = rotation_matrix(axes[axis1], theta1_rad)
R2 = rotation_matrix(axes[axis2], theta2_rad)

# Original coordinate frame
vectors = np.eye(3)

# Apply rotations
rotated_vectors = apply_rotation(R2, apply_rotation(R1, vectors))

# Plotting the original and rotated frames
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Original frame
ax.quiver(0, 0, 0, vectors[0, 0], vectors[1, 0], vectors[2, 0], color='r', label='X')
ax.quiver(0, 0, 0, vectors[0, 1], vectors[1, 1], vectors[2, 1], color='g', label='Y')
ax.quiver(0, 0, 0, vectors[0, 2], vectors[1, 2], vectors[2, 2], color='b', label='Z')

# Rotated frame
ax.quiver(0, 0, 0, rotated_vectors[0, 0], rotated_vectors[1, 0], rotated_vectors[2, 0], color='r', linestyle='--')
ax.quiver(0, 0, 0, rotated_vectors[0, 1], rotated_vectors[1, 1], rotated_vectors[2, 1], color='g', linestyle='--')
ax.quiver(0, 0, 0, rotated_vectors[0, 2], rotated_vectors[1, 2], rotated_vectors[2, 2], color='b', linestyle='--')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.tick_params(axis='both', which='major', labelsize=8)

ax.legend()
ax.set_title('Coordinate Frame Rotation')

st.pyplot(fig)


st.sidebar.markdown(
    '<div style="text-align:center; margin-top: 80px">'
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