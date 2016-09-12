import sys
import os
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str)
    parser.add_argument('--column', type=int, required=True)
    parser.add_argument('--shift', type=float, required=True)

    args = parser.parse_args()
    filepath = args.filepath

    filename_without_ext = os.path.splitext(filepath)[0]
    data = np.loadtxt(filepath)

    data[:, args.column -1] = data[:, args.column -1] + args.shift

    np.savetxt(
        filename_without_ext + '-shifted-col%d-%1.2lf.txt' % (args.column, args.shift), 
        data)
