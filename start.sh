#!/bin/bash
docker build -t flask-docker:latest .
docker run -p 5000:5000 flask-docker
