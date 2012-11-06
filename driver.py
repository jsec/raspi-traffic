##################################################################
#  Raspi Traffic Light Controller                                #
#  Author : jsec                                                 #
#  Date   : 11/5/12                                              #
#                                                                #
#  Description: This script runs continuously on a Raspberry Pi, #
#               checking every 5 minutes for an HTTP header      #
#               provided by a TeamCity plugin, and changes the   #
#               display of an LED traffic light to reflect       #
#               current build status.                            #
##################################################################

# HTTP Response Codes Used:
#	200 OK 			- Signifies a successful build and unit tess passing.
#	412 Precondition Failed - Signifies successful build, failed unit tests.
#	409 Conflict		- Signifies a failed build
#
#	The link to the TeamCity plugin used can be found in the README.
#	This code is in the public domain.


# library imports
import time;
import httplib;

# fetch HTTP header code
def get_http_status(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None
    
def set_light_red():
    # change GPIO status to set the traffic light to red
    print "Build Failed                             {RED}"
    return
    
def set_light_yellow():
    # change GPIO status to set the traffic light to yellow
    print "Build Succeeded - Unit Tests Failed      {YELLOW}"
    return
    
def set_light_green():
    # change GPIO status to set the traffic light to green
    print "Build Succeeded - Unit Tests Passed      {GREEN}"
    return

def set_light_error():
    # error with the HTTP fetch request
    print "ERROR				    {ERR}"

# loops for a given time increment and updates
# GPIO relays appropriately (in progress)
def main():
    url = raw_input("Please enter a url: ")
    while True:
        status = get_http_status(url)
	
	# All Good Status - HTTP 200
	if status == 200:
	    set_light_green()

	# Unit Test Failure Status - HTTP 412
	elif status == 412:
	    set_light_yellow()

	# Build Failure Status - HTTP 409
	elif status == 409:
	    set_light_red()

	# Error Status - Null response
	else:
	    set_light_error()

        time.sleep(10)
    return
    
main()

    
