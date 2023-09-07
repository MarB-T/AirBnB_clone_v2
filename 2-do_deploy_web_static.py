#!/usr/bin/python3
"""
Script that distributes an archive to the web server
"""
from fabric.api import *
from os import path


env.user = "ubuntu"
env.hosts = ['52.87.154.89', '54.174.246.6']


def do_deploy(archive_path):
    if not archive_path:
        return (False)
    name = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(name, name))
        run("rm /tmp/{}".format(name))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed")
        return (True)
    except BaseException:
        return (False)
