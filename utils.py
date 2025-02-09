def pdb_to_xyz(pdb_file):
    """
    Reads a PDB file and extracts atom coordinates into an XYZ coordinate list.
    
    Parameters:
    pdb_file (str): Path to the input PDB file.
    
    Returns:
    list: List of tuples representing XYZ coordinates.
    """
    xyz_coordinates = []
    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                xyz_coordinates.append((x, y, z))
    return xyz_coordinates

