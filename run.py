
import argparse

import os
from os import walk
import sys

def main():
    # parser selects user input 

    # TODO: using jcrew for testing
    path = os.path.realpath("jcrew/jcrew/spiders")
    spiders = [spider for spider in os.listdir(path) if spider != "__init__"]
    # Implement helper/formatter function override that matches spider to description or usage

    parser_main = argparse.ArgumentParser(description="usage: [-h] <function> [arg_a] [arg_b] ...")
    parser_sub = parser_main.add_subparsers()


    # TODO: Initialize subparsers to a list
    all_parser_subs = []
    
    process_commands(parser_main, all_parser_subs)


def process_commands(parser_main, all_parser_subs):
    # calls proper scripts based on arguments provided
    
    # Require some type of file to organize sets of actions for each spider call
    # Have scripts handle arguments(?)
    pass