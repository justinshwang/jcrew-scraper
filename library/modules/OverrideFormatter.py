import argparse
import re

class SmartFormatter(argparse.HelpFormatter):
    # Override class for displaying help options

    @staticmethod
    def list_actions(options, title):
        final_list = "|" + title + "\n"
        # Indicate split at "|"
        indent_size = 10

        for item in options:
            item_name = item.split(".")[0]
            # used for indentation
            space = " "*(indent_size - len(item_name))
            final_list += (indent_size // 4 * " ") + item_name + space + "\n"
        return final_list

        
    def _split_lines(self, text, width):
        if text.startswith('|'):
            return text[1:].splitlines()  
        return argparse.HelpFormatter._split_lines(self, text, width)

