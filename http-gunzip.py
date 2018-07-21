#!/usr/bin/python

import binascii
import sys
import zlib
import json

filename = sys.argv[1]

with open(filename, "rb") as f:
    contents = f.read()

cl = contents.index("Content-Length:")
while cl != -1:
    nl = contents.index("\n", cl)
    dl = nl + 3
    el = contents.index("HTTP/1.1", dl)
    zd = contents[dl:el]
    
    ud = zlib.decompress(zd, 16+zlib.MAX_WBITS)
    print "\n\n******************"
    print "Length: %d" % (el-dl)

    print ud
    #print ud.replace(",",",\n")                                 # Poor Man's JSON formatting
    #print json.dumps(json.loads(ud.decode("utf-8")), indent=4)  # Real JSON formatting (requires real JSON)

    cl = contents.index("Content-Length:",el)
