import time
import progressbar

def read_file(filename):
	data = []
	count = 0
	bar = progressbar.ProgressBar(max_value=1000000)
	bar.start()
	with open(filename,'r') as f:
		for line in f:
			data.append(line)
			count += 1
			bar.update(count)
	bar.finish()
	print('總共', len(data), '筆資料')
	return data

# Nested For Loop 巢狀迴圈
def count_word(data):
	start_time = time.time()
	wc = {} #word_count
	for d in data:
		words = d.strip().split()
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1
	#for word in wc:
		#if wc[word] > 1000000:
			#print(word,wc[word])
	end_time = time.time()
	print('花了', end_time - start_time, 'sec')
	return wc

def find_word(wc):
	while True:
		word = input('請問想查什麼字：')
		if word == 'q':
			break
		elif word not in wc:
			print('找不到這個字')
		else:
			print(word,'出現過',wc[word], '次')
	print('感謝使用')
	
def main():
	data = read_file('reviews.txt')
	wc = count_word(data)
	find_word(wc)

main()