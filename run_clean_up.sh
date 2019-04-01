#!/bin/sh

docker stack rm sst_dashboard

docker image prune --all -f