FROM ros:melodic-ros-base-bionic 
ARG DEBIAN_FRONTEND=noninteractive

#Fundamentals
RUN \
    apt update -y && \
    apt upgrade -y && \
    apt install -y vim git

#Environment
RUN \
    apt install -y g++ && \
    apt install -y python3-pip

RUN apt install -y \
    libblas-dev \
    liblapack-dev \
    libpng-dev \
    libfreetype6-dev \
    libjpeg-dev \
    zlib1g-dev
#Python
RUN pip3 install numpy

RUN pip3 install \
    Pillow \
    scipy \
    matplotlib

RUN pip3 install \
    snakeviz \
    line_profiler \
    psutil \
    memory_profiler \
    py-spy \
    Cython


#ROS
RUN apt install -y \
	build-essential \
	cmake \
	libyaml-cpp-dev \
	libpcap-dev \
	libeigen3-dev \
	libjsoncpp-dev

RUN apt install -y \
	ros-melodic-pcl-ros \
	ros-melodic-rviz \
	ros-melodic-tf2-geometry-msgs \
	ros-melodic-cv-bridge \
	ros-melodic-angles



#ROS python
RUN \
	apt install -y python3-pip && \
	apt install -y python3-catkin-tools python3-vcstool python3-osrf-pycommon

RUN pip3 install rospkg

RUN mkdir -p /workspace
WORKDIR /workspace

