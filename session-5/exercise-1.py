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


# Main programme
s=input('Please enter the DNA sequence: ')
s= s.upper()
info= count_bases(s)



# Calculate the total sequence lenght
tl=len(s)

# Calculate the percentage of As in the sequence and number of bases
if tl>0:

    print('The total length is: {}'.format(tl))

    for k, v in info.items():
        print(k, ':', v)
        perc=round(100.0*v/tl,1)
        print('     The percentage of this letter '
              'is: {}%'.format(perc))

else:
    perc=0






