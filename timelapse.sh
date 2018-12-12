#!/bin/bash
#
# Make HD timelapse of all jpg files in dir
STARTDATE="20180917-0000"
VEG_WEEKS=6

if [ -z ${SSH_STRING} ];
then
    echo "SSH_STRING is unset, please set to user@host:/path/to/*.jpg"
    exit -1
fi;

echo "Activating virtual env"
source ./bin/activate

echo "Deleting old .jpg and .mp4 files..."
#rm -rf *.jpg 
rm -rf *.mp4

echo "Fetching new .jpg files..."
scp -oStrictHostKeyChecking=no $SSH_STRING .

echo "Removing 2/3 .jpg files..."
#mkdir -p saved
#mv $(ls *.jpg | awk 'NR % 3 == 0') saved/.
#rm *.jpg
#mv saved/* .
#rmdir saved

echo "Timestamping .jpg files..."
#ls *.jpg | python2 ./timestamp.py
for filename in *.jpg; 
do
    python2 ./timestamp.py "$filename" $STARTDATE $VEG_WEEKS
done;

echo "Making timelapse..."
ffmpeg -r 15 -pattern_type glob -i "*.jpg"  -s hd720 -vcodec libx264 timelapse.mp4


echo "Clean up jpg's"
rm *.jpg
