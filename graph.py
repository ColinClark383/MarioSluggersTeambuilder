import json
import sqlite3
from pyvis.network import Network

# Load database
def load_graph_from_db(db_file, edgeType):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Initialize Pyvis network
    net = Network(notebook=True, cdn_resources='in_line', select_menu=True)
    
    # Add nodes
    cursor.execute("SELECT * FROM Sluggers")
    nodes = cursor.fetchall()
    cursor.execute("SELECT DISTINCT name FROM Varients")
    varients = cursor.fetchall()
    varientsString = {row[0] for row in varients}
    for node in nodes:
        if node[0] in varientsString:
            cursor.execute(f"SELECT varient FROM Varients WHERE name = '{node[0]}'")
            charVarients = cursor.fetchall()
            charVarientsString = {row[0] for row in charVarients}
            hoverText = f"{node[0]} Varients:\n{", ".join(charVarientsString)}"
        else:
            cursor.execute(f"SELECT pitching, batting, feilding, speed FROM Sluggers WHERE name = '{node[0]}'")
            charStats = cursor.fetchall()
            pitching, batting, feilding, speed = charStats[0]
            hoverText = f"{node[0]}\nPitching: {pitching}\nBatting: {batting}\nFeilding: {feilding}\nSpeed: {speed}"
        net.add_node(node[0], label=node[0], title=hoverText)
    
    # Add edges with weights
    cursor.execute(f"SELECT name1, name2 FROM Connections WHERE pos = {edgeType}")
    edges = cursor.fetchall()
    for edge in edges:
        net.add_edge(edge[0], edge[1])
        
    conn.close()
    return net

# Visualize the graph interactively
def visualize_graph(net, filename):
    net.show(filename)  # This will open the graph in a browser

# Main function to load, build and visualize
def main(edgeType, resultfile):
    db_file = 'backend/sluggers.db'
    net = load_graph_from_db(db_file, edgeType)
    net.set_options(json.dumps({
        "physics": {
            "forceAtlas2Based": {
                "springLength": 100
            },
            "minVelocity": 0.75, 
            "solver": "forceAtlas2Based"
        }
    }))
    visualize_graph(net, resultfile)


if __name__ == "__main__":
    main(True, "sluggers/public/graph.html")
    main(False, 'sluggers/public/graph2.html')
