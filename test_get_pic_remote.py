#!/usr/bin/python -w
# -*- coding:utf8 -*-


import time
from getPicture import *

log_path = "/qae/log/%.0f.log" % (time.time())

a = {"task": "time", 
"log": log_path,
"outdir": "./outdir", 
"outprefix": "tongbu1.0_", 
"inputfile": "/mnt/gluster/shdx15/sh-ppc57-mams/operation/video/2018/07/03/16/62/01af6676749e18d79a8046d2d0fafc0e.mkv", 
"outfile": "output",
"capture_mode": 1, 
"tmpdir": "", 
"timeArray": [4750.616]}

start_time = time.time()
getPictureByTimeArray(json.dumps(a))
end_time = time.time()

print("getPictureByTimeArray time duration: %.2f s" % (end_time - start_time))

