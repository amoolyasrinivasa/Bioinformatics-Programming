"""
File:  intersection.py

This program  takes in two file containing genes from
human chromosome 21 and all human genes approved by HUGO committee
and determines the unique and common gene symbols from both.
It also sorts the gene symbols alphabetically and writes the output to a
text file.

Sample command for executing the program:
python3 intersection.py -i1 chr21_genes.txt -i2 HUGO_genes.txt
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
    infile1 = args.infile1
    infile2 = args.infile2
    fh_in = my_io.get_fh(infile1, "r")
    fh_in_2 = my_io.get_fh(infile2, "r")
    outfile = my_io.get_fh("OUTPUT/intersection_output.txt", "w")
    chr21_genes, hugo_genes = get_lists_of_gene_symbols(fh_in, fh_in_2)
    unique_chr21, unique_hugo = get_unique_genes(chr21_genes, hugo_genes)
    alphabetic_list = get_common_genes(unique_chr21, unique_hugo, outfile)
    print(f"Number of unique gene names in {infile1}: {len(unique_chr21)}")
    print(f"Number of unique gene names in {infile2}: {len(unique_hugo)}")
    print(f"Number of common gene symbols found: {len(alphabetic_list)}")
    print("Output stored in OUTPUT/intersection_output.txt")


def get_lists_of_gene_symbols(fh_in, fh_in_2):
    """
    Reads both the input files and creates two dictionaries to
    store the gene symbols from both files, in two seperate
    dictionaries.
    @param fh_in: chr21_genes.txt input file
    @param fh_in_2: HUGO-genes.txt input file
    @return: Gene symbol dictionaries from both the files
    """
    chr21_genes = []
    hugo_genes = []
    lines1 = fh_in.readlines()[1:]
    lines2 = fh_in_2.readlines()[1:]
    for line in lines1:
        gene_symbol_chr21 = line.replace("\n", "").split("\t")[0]
        chr21_genes.append(gene_symbol_chr21)
    for line in lines2:
        gene_symbol_hugo = line.replace("\n", "").split("\t")[0]
        hugo_genes.append(gene_symbol_hugo)
    return chr21_genes, hugo_genes


def get_unique_genes(chr21_genes, hugo_genes):
    """
    Takes in the dictionaries of gene symbols and determines the unique
    symbols in each file seperately.
    @param chr21_genes: Gene symbol dictionary of chr21_gene.txt
    @param hugo_genes: Gene symbol dictionary of HUGO_gene.txt
    @return: Sets of unique gene symbols from both the input files
    """
    unique_chr21 = set(chr21_genes)
    unique_hugo = set(hugo_genes)
    return unique_chr21, unique_hugo


def get_common_genes(unique_chr21, unique_hugo, outfile):
    """
    Takes in the unique gene symbols from each file and finds
    the common gene symbols present in both an sorts it alphabetically.
    @param unique_chr21: Unique gene symbols in chr21_genes.txt
    @param unique_hugo: Unique gene symbols in HUGO_genes.txt
    @param outfile: Output written to OUTPUT/intersection_output.txt
    @return: List of gene symbols arranges alphabetically
    """
    intersection = unique_chr21.intersection(unique_hugo)
    alphabetic_list = sorted(intersection)
    for item in alphabetic_list:
        outfile.write(str(item) + "\n")
    return alphabetic_list


def get_cli_args():
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Provide two gene list (ignore header line), \
                                    find intersection')
    parser.add_argument('-i1', '--infile1', dest='infile1',
                        type=str, help='Gene list 1 to open',
                        required=False, default='chr21_genes.txt')
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        type=str, help='Gene list 2 to open',
                        required=False, default='HUGO_genes.txt')

    return parser.parse_args()


if __name__ == '__main__':
    main()
