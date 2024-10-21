import sys
import bids

def main():
    layout = bids.BIDSLayout(sys.argv[1])
    print(layout.get_subjects())
