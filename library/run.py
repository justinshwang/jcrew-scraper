import os
from os import walk
import sys

import subprocess

import argparse
from modules import OverrideFormatter

def main():
    spider_name = "new"
    crawler_loc = "jcrew"
    args = (["scrapy", "crawl", spider_name], crawler_loc)
    
    # # parser will selects user input 

    # path = os.path.realpath("scripts")
    # actions = [action for action in os.listdir(path)]
    # # Implement helper/formatter function override that matches spider to description or usage

    # parser_main = argparse.ArgumentParser(add_help=False, description="full usage: [-h] <action> [item_name] [size] ...", formatter_class=OverrideFormatter.SmartFormatter)
    # parser_subs = parser_main.add_subparsers(metavar="action", dest="action", help=OverrideFormatter.SmartFormatter.list_actions(actions, "possible options"))
    # all_parser_subs = {}
    # for action in actions:
    #     all_parser_subs[action] = parser_subs.add_parser(action, add_help=False)
    # for action in all_parser_subs:
    #     # Up to two additional params
    #     all_parser_subs[action].add_argument("arg_one", type=str, default="None", nargs='?')
    #     all_parser_subs[action].add_argument("arg_two", type=str, default="None", nargs='?')

    # check_help_flags(parser_main, all_parser_subs)
    # known_args, unknown_args = parser_main.parse_known_args()
    # # print(unknown_args)

    # path = os.path.realpath("scripts/" + known_args.action + ".sh")
    # args = [arg for arg in [path, known_args.arg_one, known_args.arg_two] + unknown_args if arg != "None"]
    
    call_script(args)


def check_help_flags(parser_main, all_parser_subs):
    # Override -h flag argparse default implementation at specific points

    if (len(sys.argv) < 2 or sys.argv[1] == '-h'):
        parser_main.print_help()
        sys.exit(1)
    if (sys.argv[2] == '-h'):
        all_parser_subs[sys.argv[1]].print_help()
        sys.exit(1)
    
    
def call_script(args):
    # calls proper scripts passing arguments for argparse
    # TODO: Implement argparse options

    cmds, crawler_loc = args
    process = subprocess.Popen(cmds, cwd=crawler_loc, stdin=sys.stdin, stderr=subprocess.PIPE, shell=True)
    
    output, err = process.communicate()
    print(output)

    # Handle errors/exit codes
    pass


if __name__ == "__main__":
    main()