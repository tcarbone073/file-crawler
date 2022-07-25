"""
test/
    test1/
        file.txt            <-- contents: "some text in this file"
        file-v2.txt         <-- contents: "some text in this file"
        blah.txt            <-- contents: "some text in this file"
    test2/
        file.txt            <-- contents: "some different text in this file"
    test3/
        test31/
            spam.txt        <-- contents: "some text in this file"
            file.txt        <-- contents: "some text in this file\non two lines"
        test21/
            file_twc.txt    <-- contents: "some text in this file"


Walk '-d --dir 

<filename>: [
    <#>: {
        "name": str,
        "path": str,
        "shallow_match": list  <-- [<#>, <#>, <#> ... ]
        "deep_match": list     <-- [<#>, <#>, ...]
    },
    <#>: {

    }

]
"""

import os
import argparse

def walk(dir_, verbosity):
    for root, dirs, files in os.walk(dir_):
        if verbosity > 1:
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))

def parse():
    parser = argparse.ArgumentParser(description="Walk directory, reporting matching files.")
    group = parser.add_mutually_exclusive_group()

    parser.add_argument("dir", help="Specify root of directory to walk", default=".")
    parser.add_argument("-n", "--name", help="Find only files matching this RegEx")
    group.add_argument("-v", "--verbosity", action="count", default=0, help="Increase output verbosity")
    group.add_argument("-q", "--quiet", action="store_true", help="Run silently")
    
    return parser.parse_args()

def main():
    args = parse()
    if args.verbosity >= 2:
        print(f"Running '{__file__}'")
    walk(args.dir, args.verbosity)

if __name__ == "__main__":
    main()
    