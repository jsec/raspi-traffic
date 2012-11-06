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
    return
    
def set_light_yellow():
    # change GPIO status to set the traffic light to yellow
    return
    
def set_light_green():
    # change GPIO status to set the traffic light to green
    return

# loops for a given time increment and updates
# GPIO relays appropriately (in progress)
def main():
    while True:
        print get_http_status("jsec.me")
        time.sleep(10)
    return
    
main()

    
