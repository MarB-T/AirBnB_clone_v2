#!/usr/bin/python3
"""
Script that generates a .tgz archive from the contents of web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ generate .tgz achive from web_static """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}".format(timestamp)
    local("mkdir -p versions")
    results = local("tar -czvfn versions/{} web_static".format(archive_name))

    if results.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
