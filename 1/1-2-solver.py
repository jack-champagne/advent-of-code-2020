my_file = open('1-1-input.txt')

line_list = my_file.read().split('\n')
line_list.remove('')

i_list = [];
for elem in line_list:
  i_list.append(int(elem))

sub_list = []
for elem in i_list:
  sub_list.append(2020 - elem)

ans = []

for elem1 in i_list:
    for elem2 in i_list:
        if (elem1 + elem2) in sub_list:
            if elem1 not in ans:
                ans.append(elem1)
            if elem2 not in ans:
                ans.append(elem2)

print(ans[0] * ans[1] * ans[2])