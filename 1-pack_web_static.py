#!/usr/bin/python3
"""
Script that generates a .tgz archive from the contents of web_static
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ generate .tgz achive from web_static """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    if not (os.path.isdir("versions")):
        local("mkdir versions")
    archive_path = "versions/web_static_{}".format(timestamp)
    results = local("tar -czvfn {} web_static".format(archive_path))

    if results.succeeded:
        return (archive_path)
    else:
        return (None)
