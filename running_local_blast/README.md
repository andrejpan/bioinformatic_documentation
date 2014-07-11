Running multiple local blastp/deltablast searches
=================================================

Please do not use space separating directories and files as arguments for calling this scripts.

For start you need seperate fasta files like [here](https://github.com/andrejpan/bioinformatic_documentation/tree/master/split_multiple_fasta_file/amilaze_aa) and then you can use script like this:

./run_blast.sh /full_path_to_blast_database /full_path_to_separate_fasta_files_directory

Result files are written in the same directory where input fasta files were given.
