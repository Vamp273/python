import sys
sys.setrecursionlimit(10)
def hello():
    print("HELLO WORLD")
    hello()

hello()