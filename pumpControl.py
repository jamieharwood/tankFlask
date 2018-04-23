#!/usr/bin/env python3


#import json
import http.client

def main():
    conn = http.client.HTTPConnection("localhost:5000")
    conn.request("GET", "/")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    
    if (r1.status == 200 ):
        data1 = r1.read()  # This will return entire content.
        print(data1)
    
main()
