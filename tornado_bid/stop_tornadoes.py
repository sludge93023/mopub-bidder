#!/usr/bin/env python
import os
import re
import subprocess
import logging
import optparse

def main():
    
    # Kill all active tornados ps
    tornado_pids = open(r"/tmp/tornado_pids", "r")
    for pid in tornado_pids:
        stdout,stderr = call_command("kill %s" % pid[:-1])
        if stderr:
            logging.warning("Could not kill tornado branch with pid: %s" % pid)
        
    tornado_pids.close()
    
    # Empty out tornado pids
    tornado_pids = open(r"/tmp/tornado_pids", "w")
    tornado_pids.close()

def call_command(command):
    process = subprocess.Popen(command.split(' '),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process.communicate()
if __name__ == "__main__":
    main()
