import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def is_any_element_in_line(array, line):
    """
    Checks if any element of array is present in the line.
    
    Parameters:
    array (list): List of elements to check.
    line (str): Line of text to check against.
    
    Returns:
    bool: True if any element of array is found in the line, False otherwise.
    """
    return any(element in line for element in array)
    
def pdb_to_xyz(pdb_file, atom_types=['CA']):
    """
    Reads a PDB file and extracts atom coordinates into an XYZ coordinate list for the specified atom types.
    
    Parameters:
    pdb_file (str): Path to the input PDB file.
    atom_types (list of str): List of atom types to filter by (e.g., ['C', 'O'] for carbon and oxygen).
    
    Returns:
    list: List of tuples representing XYZ coordinates of the specified atom types.
    """
    assert type(atom_types) == list, 'atom_types must be a list of atoms!'
    atom_types = [i.strip() + ' ' for i in atom_types]
    xyz_coordinates = []
    with open(pdb_file, 'r') as file:
        for line in file:
            if (line.startswith("ATOM") or line.startswith("HETATM")) and is_any_element_in_line(atom_types, line):
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                xyz_coordinates.append((x, y, z))
    return xyz_coordinates

