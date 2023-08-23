import numpy as np
from mayavi import mlab

# Generate some random data
x, y = np.mgrid[-5:5:100j, -5:5:100j]
z = np.sin(x**2 + y**2) / (x**2 + y**2)

# Create a Mayavi figure
fig = mlab.figure()

# Plot the surface
surf = mlab.surf(x, y, z, colormap='cool')

# Display the Mayavi plot
mlab.show()
