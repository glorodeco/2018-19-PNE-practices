from Seq import Seq

s1=Seq('AACCACAGACATAA')
s2=Seq('ACCATACATACATTTACA')

s3= Seq(s1.complement())
s4=Seq(s3.reverse())

list1=[s1,s2,s3,s4]

for element in list1:
    print('Information about the sequence: ', list1.index(element) + 1)
    lenght=element.len()
    print('     The lenght is:', lenght)
    count_A= element.count('A')
    count_C = element.count('C')
    count_G = element.count('G')
    count_T = element.count('T')
    print('     Bases Count: A:',count_A, ' C:', count_C, ' G:',count_G, 'T:', count_T )
    p_A= element.perc('A')
    p_C = element.perc('C')
    p_G = element.perc('G')
    p_T = element.perc('T')
    print('     Percentage: A:',p_A,'%', ' C:',p_C,'%', ' G:',p_G, '%', 'T:', p_T, '%' )
    print('-'*10)