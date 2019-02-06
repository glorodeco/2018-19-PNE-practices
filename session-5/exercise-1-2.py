from Bases import count_bases


# Main program

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