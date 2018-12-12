# jpg-timelapse
##### A program to stitch together a series of jpg images to a timelapse video

This script will pull images from a remote server via. scp, process an info overlay to each image, and stitch together the final product to an .mp4 movie. The timestamping script (`timestamp.py`) can be used by itself on single .jpg images.

![alt text](https://raw.githubusercontent.com/dancingshrubbery/jpg-timelapse/master/example.jpg)

## Setup
Install ffmpeg. Create a python2 virtual environment, activate it and download the requirements.

```
> virtualenv jpg-timelapse/
New python executable in jpg-timelapse/bin/python
Installing setuptools, pip, wheel...
done.
> cd jpg-timelapse
> source bin/activate
(jpg-timelapse) > pip install -r requirements.txt
```

## Usage
* You may configure the start date of your grow and how many vegitative weeks your grow has in `timelapse.sh`.
* Make sure your SSH public key is authenticated by the server you are pulling images from.
* Set the environment variable `SSH_STRING` to `user@host:/path/to/*.jpg` to fetch images from your remote server.
* Currently the project is hardcorded for processing images of the name format `Camera1-YYYYMMDD-HHMMSS.jpg` to get the date of each image from the filename. This can be changed in `timestamp.py`
* Run `timelapse.sh`

