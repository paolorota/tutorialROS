FROM osrf/ros:noetic-desktop-full

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstools \
    python3-pip \
    tree \
    vim
#    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
# RUN rosdep init && \
#   rosdep update --rosdistro $ROS_DISTRO

# # install ros packages
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     ros-noetic-ros-base=1.5.0-1*
#    && rm -rf /var/lib/apt/lists/*

RUN pip3 install scipy tornado matplotlib numpy opencv-python 

WORKDIR "/home"

# COPY *.py /home/