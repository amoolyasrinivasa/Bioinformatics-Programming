import pytest
list_headers = [">EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)"]
list_seqs =["AACAGCACGGCAACGCTGTGCCTTGGGCACCATGCAGTACCAAACGGAACGATAGTGAAAACAATCACGA"]
from pdb_fasta_splitter import get_fh, get_header_and_sequence_lists, _check_size_of_lists

def test_get_fh():
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")

def test__check_size_of_lists():
    assert _check_size_of_lists(list_headers, list_seqs) == True










