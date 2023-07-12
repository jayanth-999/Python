import sys,os
range=os.getenv('range')

def main():
    global sample
    global range
    range=int(range)
    sample=sys.argv[0]
    print(sample)
