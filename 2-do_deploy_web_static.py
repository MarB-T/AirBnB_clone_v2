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
    if not path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_base = archive_name(".")[0]

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(archive_base))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_name, archive_base))
        run("rm /tmp/{}".format(archive_name))
        run("mv /data/web_static/release/{}/web_static/* \
            /data/web_static/release/{}/".format(archive_base, archive_base))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_base))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_base))
        return True
    except Exception:
        return False
