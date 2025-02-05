import os
import sys
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split

ROOT = "/home/husammm/Desktop/Courses/CS_courses/Path Planning/Path_planinng/"
sys.path.append(os.path.abspath(ROOT))

from utils import load_config


def data_loader(config_path):
    # laod file path
    config = load_config(config_path)
    file_path = config.data['dataset_path']
    
    # Load data
    data = pd.read_csv(file_path, encoding='utf-8')
    data = pd.DataFrame(data)

    data.replace(True, 1, inplace=True)
    data.replace(False, 0, inplace=True)

    x = data.drop(columns = ['StartingNode', 'UnorderedGoalNodes',
     'OptimallyOrderedGoalNodes', 'CurrentNode', 'PossibleNextNode',
     'TemporaryGoalNode', 'OptimalCost', 'OrderingTime', 'NextNode',
     'isPossibleNextNodeTheNextNode'])
    
    # Normalize and replace the original column
    x['AlphaAngle'] = x['AlphaAngle'] / 180
    x['BetaAngle'] = x['BetaAngle'] / 180
    x['GammaAngle'] = x['GammaAngle'] / 180
    x['ZetaAngle'] = x['ZetaAngle'] / 180

    y = data['isPossibleNextNodeTheNextNode']

    # split data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, shuffle=True, stratify = y, random_state= 10)

    return x_train, x_test, y_train, y_test


if __name__ == "__main__":
    config_path = os.path.join(ROOT, "modeling/configs/logistic_reg.yml")
    x_train, x_test, y_train, y_test = data_loader(config_path)    
    print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
    print(x_train.columns)