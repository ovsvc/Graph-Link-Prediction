# Social Network Analysis 

Students responsible: *Tanay Gergely Marton* - 11702428, *Ovsianik Viktoriia* - 12217985, *Cissa Anastasia* - 11937948, *Ndiwa Sherlyne* - 12331442, *Hegetschweiler Lionel* - 12404717

### Topic  - **Link Prediction: Predicting if one user will vote for other user's post** 

Approaches applied: 
 - Similarity-based link prediction 
 - Embedding-based: node2vec
 - Deep learning based: GraphSAGE 

### Repository structure:

```bash
ADL-WS-2024/
│
├── archive/                                    # Folder with archived scripts
│
├── exploratory/                                # Scripts needed for EDA and data preparation, results of graphs
│
├── models/                                     # Saved models
│
├── scripts/                                    # Scripts for running algorithms for each graph
│   ├── graphsage_model.ipynb                   
│   ├── node2vec.ipynb
│   └── similarity_based.ipynb                  # Data used as a test set
│
├── parameter_results.csv                       # ??
├── README.md                                   # Project description, setup
├── requirements.txt                            # Python dependencies
└── .gitignore                                  # Ignore unnecessary files (e.g., parts of 'data' folder)
```

 ### How to install

 In order to run the code for each model, you would need to install libraries in the requirements file **requirements.txt**. 

 ```bash
pip install -r requirements.txt
 ```

 All saved models are located in the **models** folder. In order to install model, you would need to follow the instructions:

 #### 1. GraphSAGE

 ````bash
 # Loading the full model 
model = torch.load('full_graphsage_model.pth')
model.eval()
 ````
NEED TO FINISH THAT 
 Example of using the model for the inference: 
 ````bash
 
 ````

 #### 2. Node2Vec


 #### 3. Similarity-based
 