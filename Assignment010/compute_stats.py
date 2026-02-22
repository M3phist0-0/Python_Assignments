import sys
import numpy as np


def my_stats():
    """
    Takes the values from the data coming from standard input. It then computes some basic statistics over the values that are read
    in, and returns those statistics to standard output
    """
    data = []
    for line in sys.stdin:
        try:
            value = float(line.strip())
            data.append(value)
        except ValueError:
            continue

    min_val = np.min(data)
    max_val = np.max(data)
    avg_val = np.mean(data)
    median_val = np.median(data)

    print(f'min:{min_val}, max:{max_val}, average:{avg_val}, median:{median_val}')

if __name__ == "__main__":
    my_stats()