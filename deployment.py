#!/usr/bin/env python

import os
import json
from datetime import datetime
from fabric.api import env
from fabric.api import run
from fabric.api import local
from fabric.contrib.files import exists
from fabric.context_managers import cd
from fabric.operations import put
from fabric.operations import get
from fabric.operations import sudo

env.hosts = ['slow.secret.equipment']
env.user = 'ubuntu'

def deployDocker():
    run("rm -rf /home/ubuntu/car-network")
    run("mkdir -p /home/ubuntu/car-network")
    put("Dockerfile.traditional", "/home/ubuntu/car-network/")
    put("Makefile", "/home/ubuntu/car-network/")
    put("lib", "/home/ubuntu/car-network/")
    put("Car*", "/home/ubuntu/car-network/")
    sudo("cd /home/ubuntu/car-network && make build")
    sudo("cd /home/ubuntu/car-network && make run")


