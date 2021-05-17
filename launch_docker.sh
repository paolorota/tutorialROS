#!/bin/bash
echo $PWD/workspace

docker run -it --rm -p 11311:11311 -v $PWD/workspace:/home --name roscore myros roscore