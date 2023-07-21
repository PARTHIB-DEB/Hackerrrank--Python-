if __name__ == '__main__':
    name_list=[]
    score_list=[]
    # index_list=[]
    sub_name=[]
    for _ in range(int(input())):
        name = input()
        name_list.append(name)
        score = float(input())
        score_list.append(score)
# print(name_list)
# print(score_list)
# min_score=min(score_list)
for i in range(len(score_list)):
    if score_list[i]==min(score_list):
        score_list.remove(score_list[i])
        name_list.remove(name_list[i])
# print(name_list)
# print(score_list)
for i in range(len(score_list)):
    if score_list[i]==min(score_list):
        sub_name.append(name_list[i])
print(sub_name)
sub_name.sort()
print(sub_name)
for i in sub_name:
    print(i)
# sub_name=name_list[index_list[0]:index_list[len(index_list)-1]]
# print(sub_name)
# for i in sub_name:
#     print(i)

        