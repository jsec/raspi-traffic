raspi-traffic
=============

A traffic light controller for a Raspberry Pi to be used in conjunction with a TeamCity build server

Usage
-----

This script checks at a specified time interval for an HTTP response code from a page set up by a TeamCity plugin, indicating build status (see link below).
The script then changes the output of an LED traffic light based on the response code returned.

Features
--------

* Written for Python 2.7.3
* Makes use of the RPi.GPIO library [LINK](http://pypi.python.org/pypi/Rpi.GPIO)

TeamCity Plugin
---------------

I am using a modified version of the TeamCityBuildStatus plugin found [here](https://github.com/lholman/TeamCitySimpleBuildStatus).

I will be adding an additional status to indicate a successful build, but a failed unit test suite.
