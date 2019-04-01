#!/bin/sh

docker image build -t adapter app/

docker image build -t my_opentsdb opentsdb-docker/

docker stack deploy -c stack.yml sst_dashboard