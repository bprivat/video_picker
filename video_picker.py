import argparse
import os
import subprocess
import random

class VideoPickerException(Exception):
    '''Root Exception for the video_picker module'''
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.msg)

class NoVideosException(VideoPickerException):
    '''Exception for video_picker module. Raised when there are no
    compatible video files found in the chosen directory.
    '''
    def __init__(self):
        VideoPickerException.__init__(self, 
                                      "No compatible video files found in given directory.")

class UnsupportedOSException(VideoPickerException):
    '''Exception for video_picker module. Raised when attempting 'pick' on an
    unsupported OS.
    '''
    def __init__(self):
        VideoPickerException.__init__(self, 
                                      "Unsupported operating system, unsure how to launch video.")

def pick(directory, recursive=False, video_types=('.avi', '.mp4', '.wmv', '.mkv')):
    '''Randomly chooses and plays a video file in the given directory.
       With 'recursive', starts at specified directory and includes all
       files underneath it. Modify video_types in this script to include other file types.
    '''     
    videos = []
    
    #gather files recursively or just in the given directory
    if recursive:
        for root, dirs, files in os.walk(args.directory):
            videos+=[os.path.join(root, f) for f in files]
    else:
        videos = os.listdir(directory)
    
    #ensure extensions are lower case
    video_types = [t.lower() for t in video_types]
    #take only videos whose extensions are in video_types        
    videos = [v for v in videos if v.lower().endswith(tuple(video_types))]
    if len(videos) == 0:
        raise NoVideosException()
    
    #choose a random video        
    v = videos[random.randint(0, len(videos)-1)]
    filepath = os.path.join(directory, v)
    
    #figure out how to play it
    if os.name == 'nt':    
        os.startfile(filepath)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', filepath))
    else:
        raise UnsupportedOSException()
        
            
if __name__ == '__main__':
    desc = """Randomly chooses and plays a video file in the given directory.
           With --recursive, starts at specified directory and includes all
           files underneath it. Modify VIDEO_TYPES in this script to include other file types."""
    
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("directory", help="""The random choice will be made among videos in this directory. 
                                          If --recursive is set, will also include all subdirectories.""")
    parser.add_argument("-r", "-R", "--recursive", help="Include all videos in subdirectories of 'directory'", action="store_true")
    args = parser.parse_args()
    
    try:
        pick(args.directory, args.recursive)
    except VideoPickerException as e:
        print("Error: {}".format(e.msg))
