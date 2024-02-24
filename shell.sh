#!/bin/sh


pip install --upgrade pip
pip install -r requirements.txt

#docker run -dp 127.0.0.1:3000:3000 --mount type=volume,src=db,target=/etc/db getting-started