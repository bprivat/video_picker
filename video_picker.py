import argparse

VIDEO_TYPES = ['.avi', '.mp4', '.wmv']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="The random choice will be made among videos in this directory. If --recursive is set, will also include all subdirectories.")
    parser.add_argument("-r", "-R", "--recursive", help="Include all videos in subdirectories of 'directory'", action="store_true")
    args = parser.parse_args()

if __name__ == '__main__':
    main()