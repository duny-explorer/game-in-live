import argparse
import sys
import random

parser = argparse.ArgumentParser()
parser.add_argument("-w", type=int, nargs=?, help="area's width", default=10)
parser.add_argument("-l", type=int, nargs=?, help="area's lenght", default=10)  
parser.add_argument("-cf", type=int, nargs=?, help="count of fishes", default=10)
parser.add_argument("-cs", type=int, nargs=?, help="count of shimpes", default=10)
parser.add_argument("-cr", type=int, nargs=?, help="count of rocks", default=10)

args = parser.parser_args()
