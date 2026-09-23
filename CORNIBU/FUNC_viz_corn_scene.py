import numpy as np
import plotly.graph_objects as go

def visualize_corn_scene(file_path):
    # 1. Load the data
    # The file contains rows of 9 values (3 vertices * 3 coords)
    try:
        data = np.loadtxt(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # 2. Reshape the data
    # Current shape: (N_facets, 9)
    # We want to group them into triangles: (N_facets, 3, 3) 
    # where each triangle has 3 vertices, and each vertex has x,y,z
    try:
        facets = data.reshape(-1, 3, 3)
    except ValueError:
        print("Error: The file structure does not match expected 9-column (3x3) format.")
        return

    # 3. Prepare coordinates for Plotly
    # Plotly's go.Mesh3d expects x, y, z arrays of vertex coordinates 
    # and 'i, j, k' indices that point to those vertices.
    # However, for a large number of separate triangles, it is easier to 
    # flatten the vertices and use the 'i, j, k' indexing method.
    
    # Flatten all vertices into one long array
    # Each facet has 3 vertices, each vertex has 3 coordinates
    all_vertices = facets.reshape(-1, 3) 
    
    # Create indices: [0, 1, 2, 3, 4, 5, ...] 
    # This tells plotly that the first triangle is vertices 0,1,2; second is 3,4,5...
    num_facets = facets.shape[0]
    i = np.arange(0, num_facets * 3, 3)
    j = np.arange(1, num_facets * 3, 3)
    k = np.arange(2, num_facets * 3, 3)

    # Extract X, Y, Z coordinates for all vertices
    x_coords = all_vertices[:, 0]
    y_coords = all_vertices[:, 1]
    z_coords = all_vertices[:, 2]

    # 4. Create the 3D Plot
    fig = go.Figure(data=[
        go.Mesh3d(
            x=x_coords, 
            y=y_coords, 
            z=z_coords, 
            i=i, 
            j=j, 
            k=k, 
            opacity=0.8,
            color='forestgreen' # Default color for the canopy
        )
    ])

    # Improve layout
    fig.update_layout(
        title="CORNIBU Synthetic Scene Visualization",
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='Z (Height)',
            aspectmode='data' # Keeps the physical proportions correct
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    fig.show()