from sklearn.neural_network import MLPClassifier
import numpy as np

def neural_network(R, data):

    num_users, num_items = R.shape
    rating_array = data
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)


