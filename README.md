<h1 align="center"> ML-Driven MultiGoal Planner </h1>

## Problem definition

Path-planning and motion-planning play a critical role in enabling full autonomy in mobile robots.
The key challenge in path-planning involves identifying the optimal route that minimizes factors like distance, terrain roughness, and travel time between two points on a map.

Path-planning becomes considerably more challenging when the robot is required to
efficiently visit multiple target nodes. 

## Table of Contents
1. [Methodology](#methodology)
2. [Testing & Evaluation](#testing--evaluation)
3. [Improvement](#improvement)

## Methodology
Finding the exact optimal order for visiting N goal nodes is computationally infeasible due to its factorial complexity, N!. While this is manageable for small values of N, the computation becomes impractical as N grows. Even with advanced technologies, brute-force approaches can take days to complete. 

>[!NOTE]
> This work is planned to be published and will be available afterward.

## Testing & Evaluation

|  Criteria  |  %   |
|------------|------|
| Accuracy   | 0.83 |
| Precision  | 0.80 |
| Recall     | 0.81 |
| F1 Score   | 0.80 |

<img src="modeling/Logistic%20regression/outputs/confusion_matrix.png" alt="confusion matrix" width="60%">

## Improvement
The results shown in the following table indicate a significant improvement in ordering time when using the model, especially as the number of goal nodes increases.

| **Average of 100 Experiments** |
|----------------|--------------------------------|-------------------------------------|-----------------------------------|
|**# Goal nodes**|**A* Average ordering time (s)**| **Model average Ordering time (s)** | **Ordering time improvement (s)** |
|----------------|--------------------------------|-------------------------------------|-----------------------------------|
|        7       |             3.758              |                 2.01                |               1.75                |
|        10      |             87.239             |                 3.77                |               83.46               |


