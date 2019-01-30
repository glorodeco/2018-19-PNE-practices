dna_seq= input("Introduce the sequence: ").upper()


numb_a = dna_seq.count("A")
numb_g = dna_seq.count("G")
numb_c = dna_seq.count("C")
numb_t = dna_seq.count("T")

print("Total length:",len(dna_seq))
print("A:", numb_a)
print("G:", numb_g)
print("C:", numb_c)
print("T:", numb_t)