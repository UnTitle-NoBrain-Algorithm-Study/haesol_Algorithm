from readline import set_history_length


N = int(input())
str = []

for i in range(N):
    str.append(input())

set_str = list(set(str))

len_info_str = []
for i in set_str:
    len_info_str.append((len(i), i))

sorted_str = sorted(len_info_str)

result = []
for lgt, word in sorted_str:
    result.append(word)

for word in result:
    print(word)