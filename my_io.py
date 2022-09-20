"""my_io.py
A python module which contains a function"""
import sys


def get_fh(infile=None, mode=None):
    """Takes in two arguments - the input file and the mode
    - opens the file and validates it
    to check if it the correct type of input and opening mode.
    @param infile: Input file to open and read
    @param mode: Specification of the opening mode
    @return: The file handle with the data to be read"""
    try:
        fobj = open(infile, mode)
        return fobj
    except OSError:
        print(f"Could not open the file: {infile} for type '{mode}'", file=sys.stderr)
        raise
    except ValueError:
        print(f"Could not open the file: {infile} for type '{mode}'", file=sys.stderr)
        raise
