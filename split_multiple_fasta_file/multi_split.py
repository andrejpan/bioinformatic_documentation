import sys
import os

# split big multiple fasta file in to smaller fasta files(41 sequences)
# argv[1] - big multiple fasta file
# argv[2] - directory where to store new generated fasta files

if len(sys.argv) <= 2:
    print "Please call: python " + sys.argv[0] + " *.fasta directory_location"
    sys.exit(1)

if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])
    print "Just made new directory:", sys.argv[2]

counter = 0
how_many = 0

def read2(f):
    for line in f:
        try:
            line2 = f.next()
        except StopIteration:
            line2 = ''

        yield line, line2

with open(sys.argv[1], 'r') as f:
    for line1, line2 in read2(f):
        if how_many == 0:
            tmp_file = open(sys.argv[2] + "/" + str(counter) + ".fasta","w")
            tmp_file.write(line1)
            tmp_file.write(line2)
            how_many = how_many + 1
            counter = counter + 1
            continue
        if how_many > 0 and how_many < 40:
            tmp_file.write(line1)
            tmp_file.write(line2)
            how_many = how_many + 1
            continue
        if how_many == 40:
            tmp_file.write(line1)
            tmp_file.write(line2)
            how_many = 0
            tmp_file.close()
            continue
        else:
            print "Something went wrong"
            sys.exit(1)
f.close()
print "Done"
