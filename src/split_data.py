import os
import yaml
import pandas as pd # type: ignore
import numpy as np # type: ignore
import argparse
from pkgutil import get_data
from get_data import get_data, read_param
from sklearn.model_selection import train_test_split # type: ignore

def split_data(config_path):
    config = read_param(config_path)
    #df = get_data(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    raw_data_path = config["load_data"]["clean_data"]
    split_data = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    df = pd.read_csv(raw_data_path, sep=",")

    train, test = train_test_split(df, test_size=split_data, random_state=random_state)

    train.to_csv(train_data_path, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yml")
    parsed_args= args.parse_args()
    split_data(config_path=parsed_args.config)