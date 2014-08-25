#!/usr/bin/python

from fabric.api import local

def lsfab():
#   print('%s=%s!'%(name,value))
local('cd ~/tmp')
local('ls') 
