#!/bin/bash
pubDNSName=$(python3 aws-start.py $2 $3)
ssh -i $1 -L 8000:localhost:8888 -o "StrictHostKeyChecking=no" -l ubuntu $pubDNSName
stopping=$(python3 aws-stop.py $2)
echo $stopping