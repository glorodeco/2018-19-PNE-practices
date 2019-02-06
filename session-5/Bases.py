def  count_bases(seq):
    """""Counting the number of As in the sequence"""


   # Counter for the bases
    result_a=0
    result_t=0
    result_c=0
    result_g=0


    for b in seq:
        if b=='A':
            result_a+=1
        elif b=='C':
            result_c+=1
        elif b=='G':
            result_g+=1
        elif b=='T':
            result_t+=1
# Making dictionaries
    dic = {'Number of A': result_a, 'Number of T ': result_t, 'Number of G ': result_g, 'Number of C ': result_c}

    # Return the dictionaries
    return dic