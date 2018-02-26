#!/usr/bin/env python
# -*- coding:utf-8 -*-



import os  
  
def hostname():  
    sys = os.name  
  
    if sys == 'nt':  
        hostname = os.getenv('computername')  
        print hostname
        return hostname  
    elif sys == 'posix':  
        host = os.popen('echo $HOSTNAME')  
        try:  
            hostname = host.read()  
            print hostname
            return hostname  
        finally:  
            print hostname
            host.close()  
    else:  
        print hostname
        return 'Unkwon hostname'  