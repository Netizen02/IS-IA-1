from catboost import CatBoostClassifier

CWD = 'model/baseline/'

filename = CWD + 'baseline'

def forward(X):
    model = CatBoostClassifier()
    model.load_model(filename, format='cbm')
    return model.predict(X)