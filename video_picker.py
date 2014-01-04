import argparse
import os
import random

VIDEO_TYPES = ['.avi', '.mp4', '.wmv', '.mkv']

def main():
    desc = """Randomly chooses and plays a video file in the given directory.
           With --recursive, starts at specified directory and includes all
           files underneath it. Modify VIDEO_TYPES in this script to include other file types."""
    
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("directory", help="""The random choice will be made among videos in this directory. 
                                          If --recursive is set, will also include all subdirectories.""")
    parser.add_argument("-r", "-R", "--recursive", help="Include all videos in subdirectories of 'directory'", action="store_true")
    args = parser.parse_args()
    
    videos = []
    if os.name == 'nt':
        if args.recursive:
            for root, dirs, files in os.walk(args.directory):
                videos+=[os.path.join(root, f) for f in files]
        else:
            videos = os.listdir(args.directory)
            
        videos = [v for v in videos if v[-4:].lower() in VIDEO_TYPES]    
        v = videos[random.randint(0, len(videos)-1)]
        os.startfile(os.path.join(args.directory, v))
            
if __name__ == '__main__':
    main()