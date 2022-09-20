"""
File:  pdb_fasta_splitter.py

This program  takes in a file and generates two files
one for sequence and one for secondary structure.

Sample command for executing the program:
python3 pdb_fasta_splitter.py --infile ss.txt
"""
import argparse
import sys


def main():
    """ Business Logic
    The main function where all other functions are invoked
    """
    args = get_cli_args()
    infile, mode = args.infile, 'r'
    infile = args.infile
    fh_in = get_fh(infile, mode)
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    protein_sequence_fh = get_fh('pdb_protein.fasta', 'w')
    secondary_structure_fh = get_fh('pdb_ss.fasta', 'w')
    count_seq = 0
    count_ss = 0
    for i, header in enumerate(list_headers):
        if header.endswith('sequence'):
            protein_sequence_fh.write(header+"\n")
            protein_sequence_fh.write(list_seqs[i]+"\n")
            count_seq += 1
        elif header.endswith('secstr'):
            secondary_structure_fh.write(header+"\n")
            secondary_structure_fh.write(list_seqs[i]+"\n")
            count_ss += 1
    sys.stderr.write("Found {} protein sequences\n".format(count_seq))
    sys.stderr.write("Found {} secondary structure sequences\n".format(count_ss))
    protein_sequence_fh.close()
    secondary_structure_fh.close()


def get_fh(infile, mode):
    """
    Takes in two arguements - the input file and the mode
    - opens the file and validates it
    to check if it the correct type of input and opening mode.
    @param infile: Input file to open and read
    @param mode: Specification of the opening mode
    @return: The file handle with the data to be read
    """
    try:
        file_handle = open(infile, mode=mode)
        return file_handle
    except IOError as error:
        print('Unable to open the input file. Please recheck!', infile)
        raise error
    except ValueError as error:
        print('Wrong argument passed for the opening mode', mode)
        raise error


def get_header_and_sequence_lists(fh_in):
    """
    Takes in one argument which is the input file handle, and splits into
    a list of headers and list of sequences.
    @param fh_in: Input file handle
    @return: list of headers, list of sequences
    """
    list_headers, list_seqs = [], []
    filelines = fh_in.readlines()
    for j, line in enumerate(filelines):
        line = line.rstrip()
        if line.startswith('>'):
            list_headers.append(line)
            sequence = ""
            j += 1
            while j < len(filelines) and not filelines[j].startswith('>'):
                sequence += filelines[j].replace("\n", "")
                j += 1
            if sequence != "":
                list_seqs.append(sequence)
            else:
                continue
    if _check_size_of_lists(list_headers, list_seqs):
        return list_headers, list_seqs
    return True


def _check_size_of_lists(list_headers, list_seqs):
    """
    Takes in two arguments - the list of headers and sequences- and checks
    if the length of headers and sequences are the same
    @param list_headers: list containing headers
    @param list_seqs: list containing sequences
    @return: Boolean value
    """
    if len(list_seqs) != len(list_headers):
        sys.exit("The size of the sequences and the header "
                 "lists is different \n"
                 "Are you sure the FASTA is in correct format")
    else:
        return True


def get_cli_args():
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description="Give the input fasta file")
    parser.add_argument("-i", "--infile", dest='infile', type=str,
                        help='Path to the file to be open', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
