from utils import *
from pseudoplotlib import *

# Assuming plot_pseudo_3D is already defined in plot_pseudo_3D.py
import matplotlib.pyplot as plt
import matplotlib
print (matplotlib.__version__)


# Load and convert PDB file to XYZ coordinates
monomer_filename = "tests/monomer/1clm.pdb"
xyz_coords = pdb_to_xyz(monomer_filename)
# Plot the XYZ coordinates
fig, ax = plt.subplots()
plot_pseudo_3D(xyz_coords, ax=ax)
plt.savefig('tests/monomer/monomer_test.png')

# Load and convert PDB file to XYZ coordinates
monomer_filename = "tests/heterodimer/1aui.pdb"
xyz_coords = pdb_to_xyz(monomer_filename)
# Plot the XYZ coordinates
fig, ax = plt.subplots()
plot_pseudo_3D(xyz_coords, ax=ax)
plt.savefig('tests/heterodimer/heterodimer_test.png')

# Load and convert PDB file to XYZ coordinates
idp_traj_filename = "tests/traj/idp_traj.pdb"
xyz_coords = pdb_traj_to_xyz(idp_traj_filename)
# Plot the XYZ coordinates
animation = make_animation(xyz_coords, ax=ax)
animation.save('tests/traj/idp_traj.mp4')
