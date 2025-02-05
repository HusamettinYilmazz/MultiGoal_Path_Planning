import os
import sys

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

ROOT = "/home/husammm/Desktop/Courses/CS_courses/Path Planning/Path_planinng/"
sys.path.append(os.path.abspath(ROOT))


class LogisticRegPathPlanning:
    def __init__(self, grid_parameters):
        self.grid_parameters = grid_parameters
        self.logistic_regression = LogisticRegression(random_state=0)
        pass

    def forward(self, x_train, y_train):
        grid_search = GridSearchCV(self.logistic_regression, self.grid_parameters, cv=5, scoring='f1', verbose=1, n_jobs=-1)
        grid_search.fit(x_train, y_train)
    
        return grid_search
