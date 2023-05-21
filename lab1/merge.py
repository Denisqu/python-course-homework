import os
import sys
import logging
import json
from argparse import ArgumentParser
import pathlib


def find_files(catalog):
    find_files = []
    for root, dirs, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files if name.split('.')[-1] == 'txt']
    return find_files


# marge.py -v --root_dir=ROOT_FOLDER output.json
def init_logger():
    logger = logging.getLogger()
    logger.name = "My Application"
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s %(name)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def init_parser():
    parser = ArgumentParser(prog="merge", description="Программа для знакомства с библ. argparse.",
                            epilog="Приятного пользования!")
    parser.add_argument('output', help="выходной файл")
    parser.add_argument('--root_dir', help='parsed dir')

    return parser


if __name__ == "__main__":
    logger = init_logger()
    logger.setLevel(logging.INFO)
    parser = init_parser()
    args = parser.parse_args()

    files = find_files(args.root_dir)
    logger.info(f"Merged files: {files}")
    json_output = {}

    for file in files:
        with open(file) as _file:
            data = _file.read()
            json_output[file] = data

    with open(args.output, 'w') as outfile:
        json.dump(json_output, outfile)

