data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # 每 1000 筆時印出
            print(len(data))
print(f'檔案讀取完了，總共有 {len(data)} 筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
    # print(sum_len)

print(f'留言的平均長度為 {sum_len/len(data)}')


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print(f'一共有 {len(new)} 筆留言長度小於 100')
print(new[0])
print(new[1])

"""
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print(f'一共有 {len(good)} 筆留言提到good')
print(good[0])
"""

# 清單快寫法 : List Comprehension 
good = [d for d in data if 'good' in d]
print(f'一共有 {len(good)} 筆留言提到good')
print(good[0])


# 清單快寫法 : List Comprehension 
good = [1 for d in data if 'good' in d]
print(f'一共有 {len(good)} 筆留言提到good')
print(good)

bad = ['bad' in d for d in data]
print(bad)

bad = []
for d in data:
    bad.appen('bad' in d)
    
