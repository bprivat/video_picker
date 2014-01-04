Video Picker
============

Given a directory, randomly chooses and plays a video file in the default player.

Usage
------

`video_picker.py [-h] [-r] directory`

* Positional Arguments
  * directory
     * The random choice will be made among videos in this directory. If -r is set, will also include all subdirectories.
* Optional Arguments
  * -r, -R, --recursive
     * include all videos in subdirectories of 'directory'
  * -h, --help
     * shows usage and exits