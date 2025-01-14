
import os
import pandas as pd
from pathlib import Path

os.getcwd()

# Directory containing your Parquet files
relative_path_to_data = "../data/Additional Data"  # Relative to the current working directory
data_directory = os.path.abspath(relative_path_to_data)

# Path to the file to exclude
#exclude_file_path = '/home/e12217985/shared/194.050-2024W/Data/Group_Project/df_edge_list_undirected_users_click_similarity.parquet'

# Dictionary to store DataFrames with stem names as keys
dataframes = {}

# Iterate over all Parquet files in the directory
for file_path in Path(data_directory).glob("*.parquet"):

    # Extract the file stem (name without extension)
    file_stem = file_path.stem
    print(f"Reading file: {file_stem}")
    
    # Read the Parquet file into a DataFrame
    df = pd.read_parquet(file_path)
    
    # Optionally limit the size of the DataFrame
    #df = df[:20001]
    
    # Store the DataFrame in the dictionary with the stem as the key
    dataframes[file_stem] = df

# Access DataFrames by their file stem
print(dataframes.keys())  # Prints the stems of all loaded files


vote_timestamps = dataframes['df_Votes_filtered_net']
posting_timestamps = dataframes['df_Postings_filtered_net']

#Check if there are any months with less postings than usually
from matplotlib import pyplot as plt

posting_timestamps['YearMonth'] = posting_timestamps['createdAt'].dt.to_period('M')

# Group by 'YearMonth' and count the number of postings
monthly_postings = posting_timestamps.groupby('YearMonth').size().reset_index(name='Count')

# Plot the data
plt.figure(figsize=(7, 3))
plt.plot(monthly_postings['YearMonth'].astype(str), monthly_postings['Count'], marker='o', linestyle='-', color='b')

# Customize the chart
plt.title('Number of Postings Created Each Month', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Postings', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()

# Since there is no difference between months in the # of postings we can focus on any month.

# Define the date range for filtering
start_date = '2017-11-01'
end_date = '2017-12-01'

#Filter the vote and posting timestamp data by date
def filter_by_date(df, date_column, start_date, end_date):
    df[date_column] = pd.to_datetime(df[date_column])  # Ensure datetime format
    return df[(df[date_column] >= start_date) & (df[date_column] <= end_date)]

# Filter the postings and votes dataframes
filtered_postings = filter_by_date(posting_timestamps, 'createdAt', start_date, end_date)
#filtered_votes = filter_by_date(vote_timestamps, 'CreatedAt', start_date, end_date)

# Merge the datasets using 'ID_Posting' as the key
merged = pd.merge(filtered_postings, vote_timestamps, on='ID_Posting', how='inner')

merged.info()

#take only information relevant to the task

for_graph = merged[["ID_Posting", "ID_CommunityIdentity_x", "ID_CommunityIdentity_y"]]

#Calculate frequency of every pair
pair_counts = merged.groupby(['ID_CommunityIdentity_x', 'ID_CommunityIdentity_y']).size().reset_index(name='count')

# Display the resulting DataFrame
pair_counts

pair_counts["count"].unique()

pair_counts[pair_counts["count"]==96]

#Example of the pair appeared 96 times
merged[
    (merged["ID_CommunityIdentity_x"] == 516017) & 
    (merged["ID_CommunityIdentity_y"] == 572366)
]

# Prepaire graph

# 1. Convert the directed votes dataset into a graph
import networkx as nx

G = nx.from_pandas_edgelist(
    pair_counts,  # Replace with your DataFrame variable
    source="ID_CommunityIdentity_x",
    target="ID_CommunityIdentity_y",
    edge_attr="count",  # Optional: edge weights
    create_using=nx.Graph()  # Ensure a non directed graph
)

# %%
#Check size of the graph

print("# of nodes in G:", G.number_of_nodes())
print("# of edges in G:", G.number_of_edges())

# %%
subgraph = G.subgraph(list(G.nodes)[:100])  # Adjust size

# %%
# Visualize the subgraph with basic layout
from matplotlib import pyplot as plt
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(subgraph)
nx.draw(
    subgraph,
    pos,
    with_labels=False,
    node_size=50,
    edge_color='gray',
    alpha=0.7
)
plt.title("Directed Graph Visualization")
plt.show()


