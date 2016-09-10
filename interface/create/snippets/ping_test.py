import os
import argparse


def main(args):
    if args.ip is not None:
        os.system('ping {}'.format(args.ip))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ping Test')
    parser.add_argument('-ip', help='enter the ip')
    main(parser.parse_args())
    