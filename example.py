import os
from tree_of_thoughts.openaiModels import OpenAILanguageModel
from tree_of_thoughts.treeofthoughts import TreeofThoughts
#


api_model= "gpt-3.5-turbo"


model = OpenAILanguageModel(api_key='', api_model=api_model)

#choose search algorithm('BFS' or 'DFS')
search_algorithm = "BFS"

# value or vote
evaluation_strategy = "value"

tree_of_thoughts= TreeofThoughts(model, search_algorithm)

input_problem = "use 4 numbers and basic arithmetic operations (+-*/) to obtain 24"
k = 2
T = 3
b = 5
vth = 0.5
timeout = 10
confidence = 0.8 #cmodel is confident on performance
max_iterations = 40 #tree branh nodes 
convergence_threshold = 0.01
convergence_count = 5

#call the solve emthod with the input problem and other params

solution = tree_of_thoughts.solve(input_problem, num_thoughts=k,
    max_steps=T,
    max_states=b,
    value_threshold=vth,
    confidence_threshold=convergence_threshold,
    max_iterations=max_iterations,
    convergence_threshold=convergence_threshold,
    convergence_count=convergence_count)
    
#use the solution in your production environment
print(f"solution: {solution}")


# # Save the tree and metrics to a JSON file
# file_name = "logs/tree_of_thoughts_output.json"
# tree_of_thoughts.save_tree_to_json(file_name)

    # k = 1#number of thoughts to input
    # T = 1 # maximum depth of the search tree
    # b = 1 # branching factor -< number of child nodes for each branch
    # vth = 0.9 # pruning state -> any evaluated thought below this is eliminated
    # timeout = 10 #10 seconds timeout before stop
    # confidence = 0.8 #cmodel is confident on performance
    # max_iterations = 40 #tree branch nodes 
    # convergence_threshold = 0.01 #determining when the search process has converged
    # convergence_count = 5 # number of searchers to be considered converged
    # # read documentation for more
