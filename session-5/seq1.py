class Seq:
    """"A class for rpresenting sequences"""
    def __init__ (self, strbases):
        print('New empty sequece created')

        self.strbases = strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    """This class is derived from the Seq
       All the objects of class Gene will
       inheritage the methods from Seq Class"""

s1 = Gene('ATTCGATCC')
s2 = Seq('AACCCTTTGG')

str1=s1.strbases
str2=s2.strbases

l1=s1.len()
l2=s2.len()

print('Sequence1: {}'.format(str1))
print('Length Sequence1: {}'.format(l1))
print('Sequence2: {}'.format(str2))
print('Length Sequence2: {}'.format(l2))
print('The end')
