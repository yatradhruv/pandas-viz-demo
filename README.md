# Visualizing Time Series in Pandas

Notebook for a data science demo webinar on exploring and visualizing time series data in Pandas.

Click the badge below to open this repository as a Binder notebook repository:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mcullan/pandas-viz-demo/master)

## To run locally:
* Download or clone the repository
* Ensure that you have Python and conda installed. 
* Create a conda environment from `environment.yml` by:
    * Running `conda env create -f environment.yml` from within this directory 
    * Using the Anaconda Navigator app
* Activate the environment and open Jupyter:
    * `conda activate pandas-viz; jupyter notebook`
    * Or use Anaconda Navigator

## Dataset: [CalIt2 Building People Counts](https://archive.ics.uci.edu/ml/datasets/CalIt2+Building+People+Counts)

This dataset, hosted on the UCI Machine Learning Repository, contains the following:
> "Observations come from 2 data streams (people flow in and out of the building), over 15 weeks, 48 time slices per day (half hour count aggregates).

Elements of the `.data` file contains the following features:
1. Flow ID: 7 is out flow, 9 is in flow
2. Date: MM/DD/YY
3. Time: HH:MM:SS
4. Count: Number of counts reported for the previous half hour

There is also an `.events` file that contains information about the occurrence of events in the building. Elements have the following features:
1. Date: MM/DD/YY
2. Begin event time: HH:MM:SS (military)
3. End event time: HH:MM:SS (military)
4. Event name (anonymized)

The dataset was originally intended for use in training an event detection model, so the events file serves as the ground truth. 

We will just be using the dataset to demonstrate some powerful Pandas techniques for transforming and visualizing temporal data, as well as performing some feature engineering.
