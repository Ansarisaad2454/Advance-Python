
def removeDuplicate(str, n):
	s = set()
	
	for i in str:
		s.add(i)

	st = ""
	for i in s:
		st = st+i
	return st


str = "missisippi"
n = len(str)
print(removeDuplicate(list(str), n))

