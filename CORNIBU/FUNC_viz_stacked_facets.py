import numpy as np
import plotly.graph_objects as go

def visualize_stacked_facets(Stacked_facets):
    """
    Parses the 9-element flat structure of Stacked_facets where the format is:
    [x1, x2, x3, y1, y2, y3, z1, z2, z3]
    and renders it as a 3D mesh.
    """
    if not Stacked_facets:
        print("No facets to display.")
        return

    # 1. Convert list to numpy array
    data = np.array(Stacked_facets) # Shape: (N_facets, 9)

    # 2. Extract X, Y, Z coordinates based on the new format
    # Column indices 0,1,2 are X; 3,4,5 are Y; 6,7,8 are Z
    # We flatten the selection to create a long list of coordinates for Plotly
    x_coords = data[:, 0:3].flatten()
    y_coords = data[:, 3:6].flatten()
    z_coords = data[:, 6:9].flatten()

    # 3. Create the Index Map (i, j, k)
    # Each facet has 3 vertices. In the flattened arrays above:
    # Facet 0 uses indices (0, 1, 2), Facet 1 uses (3, 4, 5), etc.
    n_f = data.shape[0]
    i = np.arange(0, n_f * 3, 3)
    j = np.arange(1, n_f * 3, 3)
    k = np.arange(2, n_f * 3, 3)

    # 4. Create the Figure
    fig = go.Figure(data=[
        go.Mesh3d(
            x=x_coords, 
            y=y_coords, 
            z=z_coords, 
            i=i, 
            j=j, 
            k=k, 
            opacity=0.8,
            color='forestgreen'
        )
    ])

    # 5. Layout settings
    fig.update_layout(
        title="Leaf Surface Mesh (Stacked_facets)",
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='data' 
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    fig.show()