# Apps to launch: MEGA, Slack, PyCharm, Solidworks?
# Future features: Autolaunch, launch on next startup, single time launch, floating app window / microsevice in bar
import os
import csv
from collections import defaultdict


def launch(apps: list):
    """
    Launches applications
    :param apps: List of apps to be launched
    :return: Dictionary with failures due to invalid or missing paths in paths.csv
    """
    paths = defaultdict(lambda: "")
    with open("paths.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            paths[row["APPLICATION"]] = row["PATH"]
    print(paths)
    fails = {"NoPath": [], "InvalidPath": []}

    for app in apps:
        path = paths[app.upper()]
        if path == "":
            fails["NoPath"].append(app)
        else:
            try: 
                os.startfile(path)
            except FileNotFoundError:
                fails["InvalidPath"].append(app)

    return fails


def sort_paths(filename="paths.csv"):
    paths = {}
    with open(filename, "r+") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            paths[row["APPLICATION"]] = row["PATH"]
        csvfile.write("APPLICATION, PATH\n")
        paths = {k: v for k, v in sorted(paths.items(), key=lambda item: item[0])}
        writer = csv.writer(csvfile, delimiter=",")
        for app, path in paths.items():
            writer.writerow(app + "," + path)
        # TODO: This doesn't work at all :)


sort_paths()
