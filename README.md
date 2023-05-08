# Web Traffic Detection

## Description
This is a set of basic code and algorithm which can be used to detect malicious web traffic. The way the model is designed is there is data from a csv file which will transferred into a database. From the database the data will be calculated to generate a baseline. If the model encounter future web traffic which severely exceeds the baseline then the model will detect it.

## Dataset:

CIRA-CIC-DoHBrw-2020 Dataset ([link](https://www.unb.ca/cic/datasets/dohbrw-2020.html))

## Models:

- Baseline: Catboost model, achieve F-score 0.99789
- PCA: A PCA process that projects the data into 3D

## Included:

- [x] Flask routes for prediction and clustering
- [x] Testing capability

## Testing & Debug

Run the `Flask` test with the command:

```
$ python3 -m pytest -v
```
## Current Problems and Issues:
There is current problem of not being able to connect to a database properly. Because of this the setup of the baseline model is not yet functioning correctly. Beside that in the tests the clustering model is working well. However due to the issue of not being able to connect properly to a database and not having a proper baseline setup, it gives output of missing data.
