#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    result = []
    with open(filename) as f:
        text = f.read()

    return result

    # get year using regex
    year_match = re.match(r'Popularity\sin\s(\d\d\d\d)', text)
    # could use assert year_match(for example) to test anywhere in code only when using debugger
    if not year_match:
        print("Could not extract the year")
        return None
    year = year.match.group(1)
    print("Found year: {}".format(year))
    result.append(year)

    # get the baby names and their ranks, as tuples
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', test)

    # Each tuple looks like this now: ('984', 'Keven', 'Emilia')
    # From data in the tuple, insert into result list
    names_to_rank = {}  # can have duplicate values but not duplicate keys
    for rank, boy, girl in tuples:
        if boy not in names_to_rank:
            # creating a new dictionary entry, names_to_rank is unsorted(because you cannot sort a dictionary)
            names_to_rank[boy] = rank
        if girl not in names_to_rank:
            names_to_rank[girl] = rank

    # sorting namestorank by key which is the actual name
    sorted_names = sorted(names_to_rank.keys())
    for name in sorted_names:  # iterating through keys of names
        result.append(name + ' ' + names_to_rank[name])

    return result


def main():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files
    create_summary = args.summaryfile

    for file in file_list:
        names = extract_names(file)
        text = '\n'.join(names)

        if create_summary:
            txtFile = open(file + '.summary', 'w')
            txtFile.write(text)
            txtFile.close()
            pass
        else:
            print text


if __name__ == '__main__':
    main()
