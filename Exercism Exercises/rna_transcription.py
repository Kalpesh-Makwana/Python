def to_rna(dna_strand):
    nuc={'A':'U','C':'G','G':'C','T':'A'}
    rna=""
    for i in dna_strand:
        rna+=nuc[i]
    return rna
