import requests
import csv


def listallhuman(url, writer):
    r = requests.get(url)
    data = r.json()
    info = data["info"]
    next = info["next"]
    if next is None:
        return writer
    results = data["results"]
    for r in results:
        name = r["name"]
        location = r["location"]
        location = location["name"]
        imageurl = r["image"]
        origin = r["origin"]
        originname = origin["name"]
        if "Earth" in originname:
            data = [name, location, imageurl]
            writer.writerow(data)

    return listallhuman(next, writer)


if __name__ == '__main__':
    r = requests.get('https://rickandmortyapi.com/api/character/?species=Human&status=alive&')
    url = "https://rickandmortyapi.com/api/character/?species=Human&status=alive"
    header = ['Name', 'Location', 'Image']
    f = open("results.csv", 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(header)
    listallhuman(url, writer)
    f.close()



