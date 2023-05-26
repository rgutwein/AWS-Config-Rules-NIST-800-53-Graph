import pandas as pd
from pyvis.network import Network

# Read the CSV file
data = pd.read_csv('your_data.csv')

# Extract the required columns
columns = ['NIST 800-53 r4 Control ID', 'AWS Config Rule']
selected_data = data[columns]

# Create an empty graph
G = Network(height='1000px', width='100%', notebook=True)

# Add nodes and edges to the graph
for index, row in selected_data.iterrows():
    control_id = row['NIST 800-53 r4 Control ID']
    aws_config_rule = row['AWS Config Rule']
    G.add_node(control_id, label=control_id)
    G.add_node(aws_config_rule, label=aws_config_rule)
    G.add_edge(control_id, aws_config_rule)

# Show the graph
G.show('aws-config-800-53-mapping.html')
