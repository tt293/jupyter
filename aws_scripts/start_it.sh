#!/bin/bash
pubDNSName=$(python3 aws-start.py $1)
ssh -i /mnt/c/temp/MyJupyter.pem -L 8000:localhost:8888 -o "StrictHostKeyChecking=no" -l ubuntu $pubDNSName
stopping=$(python3 aws-stop.py $1)
echo $stopping