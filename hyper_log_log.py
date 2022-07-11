# Implementations taken from:
# https://github.com/lucasschmidtc/Probabilistic-Algorithms/blob/master/Probabilistic%20Algorithms.ipynb
# Credits go to Lucas Schmidt.
# Code was adjusted to fit the requirements of the task.

import hashlib

import numpy as np


def cardinality_hyper_log_log(buckets):
    buckets = [1 if bucket == 0 else 1 / (bucket << 1) for bucket in buckets]
    return 0.72134 * len(buckets) ** 2 / np.sum(buckets)


def hash_sha(s):
    return int(hashlib.sha1(str(s).encode('utf-8')).hexdigest(), 16) & 0xffffff


def least1(x, L):
    if x == 0:
        return 2 ** L
    return x & -x


class HyperLogLogEstimator:
    def __init__(self, data_set):
        self.data_set = data_set
        self.estimate = self.calculate_estimate()

    def calculate_estimate(self):
        buckets = np.array([0] * 64)

        for w in self.data_set:
            hashed = hash_sha(w)
            buckets[hashed % 64] = max(buckets[hashed % 64], least1(hashed >> 6, 24))

        return int(cardinality_hyper_log_log(buckets))
