data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('读取完成, 共', len(data), '笔资料')

s = 0
for i in data:
	s = s + len(i)
	avg = s / len(data)
print('avg=', avg)

new = []
for i in data:
	if len(i) < 100:
		new.append(i)
print('共几笔小于100字:', len(new))

prize = []
for i in data:
	if 'good' in i:
		prize.append(i)
print('共有: ', len(prize), '笔留言有good出现')