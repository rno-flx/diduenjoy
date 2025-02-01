#!/usr/bin/env python3

FAILURE = 84
SUCCESS = 0

import sys
from src.parsing.parseFile import parseFile
from src.database.addIntoDataBase import addIntoDatabase

def main():
    if len(sys.argv) != 2:
        print("Usage: ./diduenjoy <file>")
        sys.exit(FAILURE)
    data = parseFile(sys.argv[1])
    # addIntoDatabase(data)
    sys.exit(SUCCESS)

if __name__ == "__main__":
    main()