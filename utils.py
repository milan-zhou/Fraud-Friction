import requests

def get_lat_lon(ip):
    r = requests.get("http://ipinfo.io/%s/geo" % ip)
    #For future implementations, implement callback for even faster speedup
    if r.status_code != 200:
        return (None,None)
    else:
        lat, lon = r.json()['loc'].split(",")
        return (float(lat), float(lon))