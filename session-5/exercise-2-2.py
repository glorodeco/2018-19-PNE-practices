from Bases import count_bases

# Main programme
s1=input('Please enter the DNA sequence 1: ')
s1= s1.upper()
s2=input('Please enter the DNA sequence 2: ')
s2= s2.upper()
list_1=[s1,s2]

for element in list_1:
    s=element
    info= count_bases(s)
    print('-'*10)
    print('Information about the sequence: ', list_1.index(element) + 1)

    # Calculate the total sequence lenght
    tl=len(s)

    # Calculate the percentage of As in the sequence and number of bases


    print('The total length of the sequence', list_1.index(element)+1,': {}'.format(tl))
    if tl>0:

        for k, v in info.items():
            print(k, ':', v)
            perc=round(100.0*v/tl,1)
            print('        The percentage of this letter '
                  'is: {}%'.format(perc))
    else:
        perc = 0
