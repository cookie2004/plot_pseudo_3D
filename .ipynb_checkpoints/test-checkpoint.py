from utils import *
from matplotpsuedo import *

# Assuming plot_pseudo_3D is already defined in plot_pseudo_3D.py
import matplotlib.pyplot as plt
import matplotlib
print (matplotlib.__version__)

# Load and convert PDB file to XYZ coordinates
pdb_file_path = "1aui.pdb"
xyz_coords = pdb_to_xyz(pdb_file_path)

# Plot the XYZ coordinates
fig, ax = plt.subplots()
plot_pseudo_3D(xyz_coords, ax=ax)


plt.savefig('test.png')