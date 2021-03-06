def bisect_position(int_list, add_num):

	if add_num >= int_list[-1]:
			return(int_list.index(int_list[-1]) +1)

	if add_num < int_list[0]:
			return(int_list.index(int_list[0]))

	if int_list[0] <= add_num < int_list[-1]:
		ind_list = []
		for i in range(len(int_list)):
			if add_num >= int_list[i]:
				ind_list.append(i)
			ind_ret = ind_list[-1] + 1
		
		return ind_ret

print(bisect_position([1, 4, 5, 7], 0))



#2nd task
def all_sums(inp_num):	
	first_ind = 0
	last_ind = 0

	a = [item for item in range(1, inp_num)]
	for i in range(int(len(a)/2)):
		b = (a[first_ind], a[last_ind - 1])
		print(b, end = " ")
		first_ind += 1
		last_ind -= 1
		
	
(all_sums(7))


#3rd task
from collections import defaultdict

def duplicate_characters(inp_str):
	d = defaultdict(int)
	for k in inp_str.replace(" ", ""):
		d[k] += 1
	set_ret = set()
	for char in sorted(d, key = d.get):
		if d[char] > 1:
			set_ret.add(char)
	return(set_ret)

print(duplicate_characters('Here we have some duplicates'))




#4th task
def compare_lists(int_list1, int_list2):
	if len(int_list1) != len(int_list2):
		return False
	else:

		for i in int_list1:
			for i in range(len(int_list1)-1):
				if int_list1[i] > int_list1[i+1]:
						int_list1[i] = int_list1[i] + int_list1[i+1]
						int_list1[i+1] = int_list1[i] - int_list1[i+1]
						int_list1[i] = int_list1[i] - int_list1[i+1]

		for i in int_list2:
			for i in range(len(int_list2)-1):		
				if int_list2[i] > int_list2[i+1]:
						int_list2[i] = int_list2[i] + int_list2[i+1]
						int_list2[i+1] = int_list2[i] - int_list2[i+1]
						int_list2[i] = int_list2[i] - int_list2[i+1]

		if int_list1 == int_list2:
			return True
		else:
			return False

print(compare_lists([6,1,1,4], [4,1,1,6]))


#5th task
def heapq(int_list, int_num):


	if int_num >= int_list[-1]:
		int_list.append(int_num)
		return int_list

	if int_num < int_list[0]:
		return([int_num] + int_list)


	if int_list[0] <= int_num < int_list[-1]:
		ind_list = []
		for i in range(len(int_list)-1):
			if int_num >= int_list[i] and int_num <= int_list[i+1] :
				
				return (int_list[:i+2:] + [int_num] + int_list[i+2::])
		

print(heapq([1,2,3,4],5))


#6th task
def sort_list(int_list, order = "ascending"):

	if order == "descending":
		for i in int_list:
			for i in range(len(int_list)-1):
				if int_list[i] < int_list[i+1]:
					int_list[i] = int_list[i] + int_list[i+1]
					int_list[i+1] = int_list[i] - int_list[i+1]
					int_list[i] = int_list[i] - int_list[i+1]


	if order == "ascending":
		for i in int_list:
			for i in range(len(int_list)-1):
				if int_list[i] > int_list[i+1]:
					int_list[i] = int_list[i] + int_list[i+1]
					int_list[i+1] = int_list[i] - int_list[i+1]
					int_list[i] = int_list[i] - int_list[i+1]

	return int_list

print(sort_list([1, 5, 7, 9, 1, 3, 0, -1], ))
