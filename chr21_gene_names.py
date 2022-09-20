"""
File:  chr21_gene_names.py

This program  takes in a file containing genes from
human chromosome 21 prints the description for a
particular gene symbol as entered by the user.

Sample command for executing the program:
python3 chr21_gene_names.py -i chr21_genes.txt
"""
import argparse
import sys
from assignment4 import my_io


def main():
    """
    Business Logic
    The main function where all other functions are invoked
    """
    args = get_cli_args()
    infile = args.infile
    fh_in = my_io.get_fh(infile, "r")
    description = get_description_dictionary(fh_in)
    i = 0
    while i < 10:
        gene_symbol = input("\nEnter gene name of interest. Type quit to exit: ")
        gene_symbol = gene_symbol.lower()
        if gene_symbol in description:
            result = description[gene_symbol]
            print(f"{gene_symbol} found! Here is the description: ")
            print(result)
        elif gene_symbol == 'quit':
            print("Thanks for querying the data.")
            sys.exit()
        elif gene_symbol == 'QUIT':
            print("Thanks for querying the data.")
            sys.exit()
        elif gene_symbol == 'EXIT':
            print("Thanks for querying the data.")
            sys.exit()
        elif gene_symbol == 'exit':
            print("Thanks for querying the data.")
            sys.exit()
        else:
            print("Not a valid gene name.")


def get_description_dictionary(fh_in):
    """
    Takes in the input file, reads it and returns a dictionary of
    descriptions corresponding to each category.
    @param infile: The chr21_genes.txt input file
    @return: The dictionary consisting of gene symbol and
    corresponding description for it
    """
    description_dictionary = {}
    lines = fh_in.readlines()
    lines = lines[1:]
    for line in lines:
        gene_symbol = line.strip()
        description = line.strip()
        gene_symbol = gene_symbol.split("\t")[0].lower()
        description = description.split("\t")[1]
        description_dictionary[gene_symbol] = description
    return description_dictionary


def get_cli_args():
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, \
                                        and ask user for a gene name')
    parser.add_argument('-i', '--infile', dest='infile',
                        type=str, help='Path to the file to open',
                        required=False, default='./chr21_genes.txt')
    return parser.parse_args()


if __name__ == '__main__':
    main()
