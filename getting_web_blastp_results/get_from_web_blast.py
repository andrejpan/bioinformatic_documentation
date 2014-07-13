from Bio import SeqIO
from Bio.Blast import NCBIWWW

if len(sys.argv) == 1:
    print "Please call: python " + sys.argv[0] + " multi_or_single.fasta"
    sys.exit(1)

i=1
try:
    handle = open(sys.argv[1], 'r')
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit(1)

for record in SeqIO.parse(handle, "fasta") :
    print i,'Getting element:', record.id    
    # for now there is nasty error when I get Error 502 from server
    result = NCBIWWW.qblast('blastp', 'nr', record.seq, hitlist_size=5, format_type='Text') 
    print 'Got the element'
    save_file = open(record.id + '.out', 'w')
    save_file.write(result.read())
    save_file.close()
    result.close()
    i += 1

handle.close()
print 'Done'
