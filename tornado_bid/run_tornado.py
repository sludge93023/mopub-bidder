from __future__ import with_statement
import tornado.ioloop
import tornado.web
import sys
import os

from utils import python_daemon         
from tornado_bidder import application

if __name__ == "__main__":

    with python_daemon.DaemonContext():
        application.listen(sys.argv[1])
            
        # Write the pid to a file so we know how to kill it if necessary
        f = open("/tmp/tornado_pids", "a")
        f.write("%s\n" % os.getpid())
        f.close()
        
        tornado.ioloop.IOLoop.instance().start()
