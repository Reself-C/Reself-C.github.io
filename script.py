import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='script')
    parser.add_argument('--PATH', type=str)
    args = parser.parse_args()

    return args

def convert(path):
    """# generate markdown insert code

    Args:
        folder: path to image foler
    """
    fullpath = os.path.join("./assets/img/photography/", path)
    for img in os.listdir(fullpath):
        print("![](../assets/img/photography/{}/{})".format(path,img))
    return

if __name__ == '__main__':
    args = parse_args()
    convert(args.PATH)