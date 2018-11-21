#Request the lat, longitude of all training data beforehand so that we dont need to repeatedly do so later

import sys
import requests
from concurrent.futures import ThreadPoolExecutor
import math
import json

#Not using utils version right now because in future, should make callback to increase efficiency
def get_lat_lon(ip):
    r = requests.get("http://ipinfo.io/%s/geo" % ip)
    if r.status_code != 200:
        return (None,None)
    else:
        lat, lon = r.json()['loc'].split(",")
        return (float(lat), float(lon))

def process(y, ip,d):
    (lat,lon) = get_lat_lon(ip)
    d[ip] = {"y": y, "lat": lat, "lon": lon}

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "-f":
        print("Usage: preprocess.py -f [file]")
        sys.exit()

    #Use threadpool to parallelize work (API call is most expensive operation here)
    executor = ThreadPoolExecutor(max_workers=10)

    #Avoid duplicate API calls if possible
    seen = set()

    #Submit each API call to the threadpool to kick them off
    with open(sys.argv[2]) as f:
        d = {}
        for line in f.readlines():
            (y,ip) = line.rstrip().split()
            if ip in seen:
                continue
            seen.add(ip)
            executor.submit(process, y, ip, d)

        executor.shutdown()

    with open("precomputed.txt", "w") as g:
        g.write(json.dumps(d))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
