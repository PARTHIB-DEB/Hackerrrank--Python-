# n=int(input("\n\tHow many:"))
# elem1=(input("\n\telem1:"))
# my_set1=set(map(int,elem1.split(" ")))
# print(my_set1)

# elem2=(input("\n\telem2:"))
# my_set2=set(map(int,elem2.split(" ")))
# print(my_set2)

# my_set3=my_set1.intersection(my_set2)
# print(len(my_set3))

n1=int(input(""))
elem1=(input(""))
my_set1=set(map(int,elem1.split(" ")))
# print(my_set1)

n2=int(input(""))
elem2=(input(""))
my_set2=set(map(int,elem2.split(" ")))
# print(my_set2)

my_set3=my_set1.intersection(my_set2)
print(len(my_set3))