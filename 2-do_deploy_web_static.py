#!/usr/bin/python3
"""
Script that distributes an archive to the web server
"""
from fabric.api import *
from os import path


env.user = "ubuntu"
env.hosts = ['52.87.154.89', '54.174.246.6']


def do_deploy(archive_path):
    """ deploy static files to the web server """
    file = os.path.basename(archive_path)
    folder = file.replace(".tgz", "")
    path = "/data/web_static/releases/{}/".format(folder)
    yes = False
    if os.path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            run("mkdir -p {}".format(path))
            run("tar -xzf /tmp/{} -C {}".format(file, path))
            run("rm -rf /tmp/{}".format(file))
            run("mv {}web_static/* {}".format(path, path))
            run("rm -rf {}web_static".format(path))
            run("rm -rf /data/web_static/current")
            run("ln -sf {} /data/web_static/current".format(path))
            print('Ran SUccesfully')
            yes = True
        except Exception as e:
            print(e)
            yes = False
    else:
        return (False)
    return (yes)
