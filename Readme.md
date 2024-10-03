# Stream Kinect V1 from ubuntu/raspberry pi with python 3

Note: I am using libfreenect from the below source. I have updated the instructions here that worked for me.

# Prereq

sudo apt install v4l-utils vlc freenect git cmake build-essential libusb-1.0-0-dev libglfw3-dev python3 python3-dev python3-pip

pip install Cython==0.29.33

## To test the Kinect’s RGB camera:

freenect-glview

- This command will show you a window with both depth and RGB camera views. If this works, the Kinect hardware and drivers are functioning properly.

# libfreenect Build Instructions

- clone this repo
  cd libfreenect
  mkdir build
  cd build
  cmake .. -DBUILD_PYTHON=ON -DBUILD_PYTHON3=ON -DPYTHON_EXECUTABLE=$(which python3) -DCYTHON_EXECUTABLE=$(which cython) -DPYTHON_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") -DPYTHON_LIBRARY=$(python3 -c "from distutils.sysconfig import get_config_var; print(get_config_var('LIBDIR'))")

### The above step should run without any errors

make
sudo make install
sudo ldconfig

cd ../wrappers/python
sudo python3 setup.py install

### once the python3 wrapper is installed we are good to run the streamer

# Installing streamer

- Download the media mtx for your linux from https://github.com/bluenviron/mediamtx/releases (For me it is arm 64 as I am installing it on rpi 4)

tar -xvzf mediamtx*<version>\_linux*<your-arch>.tar.gz
cd mediamtx
./mediamtx

- keep this terminal open

# Running the code

- Now run the python code CamStreamer.py
  python3 CamStreamer.py

## Once the script is running, you can use a media player like VLC to view the RTSP stream:

- Open VLC.
- Go to Media > Open Network Stream.
- In the Network URL field, enter the following: rtsp://localhost:8554/live.sdp
- Click Play.

## You should see the Kinect video stream in VLC.
