import requests
from concurrent.futures import ThreadPoolExecutor
import sys
import json
from utils import get_lat_lon
import math

def main():
    if len(sys.argv) != 3:
        print("Usage: predict.py [train file] [Ip predicting]")
        sys.exit()

    d = json.load(open(sys.argv[1]))
    predict_ip = sys.argv[2]
    (predict_lat, predict_lon) = get_lat_lon(predict_ip)
    if (predict_lat == None or predict_lon == None):
        print("API is offline")
        sys.exit()
    
    minDistance = -1
    closestIP = None
    for key in d.keys():
        distance = math.sqrt((predict_lat - d[key]["lat"])**2 + (predict_lon - d[key]["lon"])**2)
        if minDistance == - 1 or distance < minDistance:
            minDistance = distance
            closestIP = key

    if d[closestIP]["y"] == "FRAUD":
        minDistance *= 2

    print("The score for %s is %f. Its closest neighbor is %s which had label %s" % (predict_ip, minDistance,closestIP,d[closestIP]["y"]))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
