# ROS intro

## ROS preliminary setup

### Start the docker
In order to start the docker type ```docker run -it --rm -p 11311:11311 -v /home/prota/code/tutorialROS/:/home --name rossy myros```

If needed to open another terminal do it with ```docker exec -it rossy /ros_entrypoint.sh bash```

### Create a ROS package using catkin

First of all create a **workspace** folder such as *mkdir workspace*. Then create a package ```beginner_tutorials``` from the root folder:

```catkin_create_pkg beginner_tutorials std_msgs rospy roscpp```
 
### Compile the ROS package

First let's load the environment variables:

```source /opt/ros/noetic/setup.bash```

Then run ```catkin_make``` from the root of the workspace. It generates the structure of the ROS environment.

## Run the ROS core

To run the ros core run ```roscore``` something like this will happens


```
... logging to /root/.ros/log/a6b191e6-b32a-11eb-b210-0242ac110002/roslaunch-665bd6a547fd-269.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://665bd6a547fd:33833/
ros_comm version 1.15.9


SUMMARY
========

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.15.9

NODES

auto-starting new master
process[master]: started with pid [277]
ROS_MASTER_URI=http://665bd6a547fd:11311/

setting /run_id to a6b191e6-b32a-11eb-b210-0242ac110002
process[rosout-1]: started with pid [287]
started core service [/rosout]
```

### Update the devel setup.bash

Once compiled we need tot source the setup.bash under devel folder:

```source devel/setup.bash```

### Give execution permission to the scripts

```chmod +x <pythonfile>.py```

### Update the CMakeList file of the package, adding messages (if needed) and the script files

```
## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
catkin_install_python(PROGRAMS
  src/listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```
...
```
## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )
```

### run each node with rosrun

```rosurn <package_name>```
