#!/usr/bin/env python
import os, sys
import re
import subprocess
import logging
import optparse
                
here = os.path.dirname(os.path.abspath(__file__))  

def main():
    
    # Run Tornado servers as daemons 
    for port in xrange(8000, 8004):
        stdout,stderr = call_command('python %s/run_tornado.py %s &' % (here, port))
        if stderr:
            logging.warning(stderr)
            print "error"


def call_command(command):
    process = subprocess.Popen(command.split(' '),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process.communicate()
if __name__ == "__main__":
    main()
