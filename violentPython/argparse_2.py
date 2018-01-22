"""
Created on Jan 21st 2018

@author: smercy
"""

import argparse

parser = argparse.ArgumentParser(description="Calculate x to the power of y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quite", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y
if args.quite:
    print(answer)
elif args.verbose:
    print("{} to the power of {} is equal{}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
