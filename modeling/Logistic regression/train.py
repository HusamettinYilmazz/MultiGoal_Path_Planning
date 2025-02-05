import os
import sys
import yaml

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

ROOT = "/home/husammm/Desktop/Courses/CS_courses/Path Planning/Path_planinng/"
sys.path.append(os.path.abspath(ROOT))

from utils import load_config
from model import LogisticRegPathPlanning
from data_utils import data_loader


if __name__ == "__main__":
    
    config_path = os.path.join(ROOT, "modeling/configs/logistic_reg.yml")
    config = load_config(config_path)
    grid_parameters = config.grid_parameters
    save_path = config.data['save_path']

    x_train, x_test, y_train, y_test = data_loader(config_path)

    model = LogisticRegPathPlanning(grid_parameters)
    grid_search = model.forward(x_train, y_train)

    best_parameters = grid_search.best_params_
    best_model = grid_search.best_estimator_

    # print(best_model)
    y_predicted= best_model.predict(x_test)
    accuracy = accuracy_score(y_test, y_predicted)
    precision = precision_score(y_test, y_predicted)
    recall = recall_score(y_test, y_predicted)
    f1 = f1_score(y_test, y_predicted)
    confusionMatrix = confusion_matrix(y_test, y_predicted)


    print("Best Parameters:", best_parameters)
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)
    print("Confusion Matrix:\n", confusionMatrix)

    confusionMatrix_normalized = confusionMatrix / confusionMatrix.sum(axis=1, keepdims=True) * 100

    plt.figure(figsize=(8, 6))
    sns.set(font_scale=1.4)  # for label size
    sns.heatmap(confusionMatrix_normalized, annot=True, fmt='.2f', cmap='Greens', annot_kws={"size": 16})

    plt.savefig(save_path, bbox_inches='tight', dpi=300)
    print(f"Confusion matrix saved to {save_path}")

    # Add labels, title, and ticks
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title('Confusion Matrix for Logistic Regressor')
    plt.show()