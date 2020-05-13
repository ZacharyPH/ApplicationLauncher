import os
from collections import defaultdict


def launch(*apps):
    """
    Launches applications
    :param apps: List of apps to be launched
    :return: Dictionary with failures due to invalid or missing paths in paths.csv
    """
    paths = get_apps(default=True)
    fails = {"NoPath": [], "InvalidPath": []}
    if len(apps) == 0:
        return
    if not (all(type(app) is str for app in apps) or not type(apps[0]) is list or not type(apps[0]) is set):
        raise ValueError("*apps must be a list or multiple arguments, but not both")
    if not type(apps[0]) is str:
        apps = (*apps,)[0]
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


def sort_paths(filename="paths.csv") -> None:
    """
    Alphabetizes apps in paths csv
    :param filename: name of app paths csv file
    :return: None, except several apps launching
    """
    paths = get_apps()
    paths = {k: v for k, v in sorted(paths.items(), key=lambda item: item[0])}
    with open(filename, "w") as file:
        file.write("APPLICATION, PATH\n")
        for app, path in paths.items():
            file.write(app + "," + path)


def add_app(name, path):
    pass
    # TODO: Implement
    sort_paths()


def get_apps(filename="paths.csv", default=False):
    """
    Get the list of apps and paths
    :param filename: name of app paths csv file
    :param default: whether to return as a default or normal dictionary
    :return: dictionary of {app: path} entries
    """
    apps = defaultdict(lambda: "") if default else {}
    with open(filename, "r") as file:
        for row in file.readlines()[1:]:
            k, v = row.strip().split(",")
            apps[k] = v

    return apps
