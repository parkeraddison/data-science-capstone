#!/usr/bin/env python

import sys
import json
import os

import src


def main(targets):

    if 'collect' in targets:
        raise NotImplementedError("This is a work in progress.")

        with open('config/data-generation-params.json') as f:
            generation_params = json.load(f)
            src.data.collect.get_data(generation_params)
        
    if 'data' in targets:
        # Load, clean, and preprocess data. Then store preprocessed data to
        # intermediate directory.

        print('Data target recognized.')

        with open('config/data-params.json', 'r') as f:
            data_params = json.load(f)
        print('Data configuration loaded.')
        
        print('Running ETL pipeline.')
        src.data.etl(**data_params)
        print('ETL pipeline complete.')

    if 'features' in targets:
        # Load preprocessed data, chunk each file into smaller windows of time,
        # then engineer features and write sets of features and labels to table.

        print('Features target recognized.')

        with open('config/features-params.json') as f:
            features_params = json.load(f)
        print('Features configuration loaded.')

        print('Engineering features.')
        src.features.apply_features(**features_params)
        print('Feature engineering complete.')

    if 'train' in targets:
        # Train a model on feature-engineered data and report its ROC AUC.

        print('Train target recognized.')

        with open('config/train-params.json') as f:
            train_params = json.load(f)
        print('Train configuration loaded.')

        print('Training model.')
        src.models.train(**train_params)
        print('Model training complete.')
        
        
    return
    
if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)