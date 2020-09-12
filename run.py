import argparse

import os
from os import walk
import sys

from subprocess import Popen


def main():
    # parser selects user input 

    path = os.path.realpath("scripts")
    actions = [action for action in os.listdir(path)]
    # Implement helper/formatter function override that matches spider to description or usage

    parser_main = argparse.ArgumentParser(description="usage: [-h] <action> [arg_a] [arg_b] ...")
    parser_subs = parser_main.add_subparsers(metavar="action", dest="action")
    all_parser_subs = {}
    for action in actions:
        all_parser_subs[action] = parser_subs.add_parser(action)
    for action in all_parser_subs:
        # Up to two additional params
        all_parser_subs[action].add_argument("arg_one", type=str, default="None", nargs='?')
        all_parser_subs[action].add_argument("arg_two", type=str, default="None", nargs='?')

    check_help_flags(parser_main, all_parser_subs)
    known_args, unknown_args = parser_main.parse_known_args()
    # print(unknown_args)

    path = os.path.realpath("scripts/" + known_args.action + ".sh")
    args = [arg for arg in [path, known_args.arg_one, known_args.arg_two] + unknown_args if arg != "None"]
    call_script(args)


def check_help_flags(parser_main, all_parser_subs):
    # Override -h flag argparse default implementation at specific points

    if (sys.argv[1] == '-h' or len(sys.argv) < 2):
        parser_main.print_help()
        sys.exit(1)
    if (sys.argv[2] == '-h'):
        all_parser_subs[sys.argv[1]].print_help()
        sys.exit(1)
    pass
    
    
def call_script(args):
    # calls proper scripts passing arguments

    Process=Popen(args, shell=True)
    print("Process exit status: " + Process)

    # Handle errors/exit codes
    pass


if __name__ == "_main_":
    main()