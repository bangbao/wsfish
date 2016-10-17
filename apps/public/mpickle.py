# coding: utf-8


import cPickle as pickle


def pickle_dumps(data, zip_compress=True):
    s = pickle.dumps(data, protocol=1)
    if zip_compress:
        s = s.encode("zip")
    return s


def pickle_loads(data, zip_compress=True):
    if zip_compress:
        data = data.decode('zip')
    return pickle.loads(data)
