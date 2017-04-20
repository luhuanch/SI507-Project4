
import csv

data_is_loaded = False

def load_data():

	with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader)
		dic = {}
		for row in reader:
			if row[9] == 'AK':
				continue
			else:
				if row[9] in dic:
					dic[row[9]][0] = str(float(dic[row[9]][0])+float(row[2]))
					dic[row[9]][1] = str(float(dic[row[9]][1])+float(row[3]))
					dic[row[9]][2] = str(float(dic[row[9]][2])+float(row[4]))
				else:
					vote_count = [row[2],row[3],row[4]]
					dic[row[9]] = vote_count
		data_is_loaded = True
		return dic

def get_data(party='dem', raw=True, sort_ascending=True, year=2016):
	# if not data_is_loade:
	dic = load_data()
	if raw == True:
		if party == 'dem':
			if sort_ascending == True:
				sequence_lst = sorted(dic, key = lambda x:float(dic[x][0]))
			elif sort_ascending == False:
				sequence_lst = sorted(dic, key = lambda x:float(dic[x][0]), reverse = True)
			value_lst = [(item, float(dic[item][0])) for item in sequence_lst]
		elif party == 'gop':
			if sort_ascending == True:
				sequence_lst = sorted(dic, key = lambda x:float(dic[x][1]))
			elif sort_ascending == False:
				sequence_lst = sorted(dic, key = lambda x:float(dic[x][1]), reverse = True)
			value_lst = [(item, float(dic[item][1])) for item in sequence_lst]
	elif raw == False:
		if party == 'dem':
			if sort_ascending == True:
				sequence_lst = sorted(dic, key = lambda x:(float(dic[x][0])/float(dic[x][2])))
			elif sort_ascending == False:
				sequence_lst = sorted(dic, key = lambda x:(float(dic[x][0])/float(dic[x][2])), reverse = True)
			value_lst = [(item, (float(dic[item][0])/float(dic[item][2]))) for item in sequence_lst]
		elif party == 'gop':
			if sort_ascending == True:
				sequence_lst = sorted(dic, key = lambda x:(float(dic[x][1])/float(dic[x][2])))
			elif sort_ascending == False:
				sequence_lst = sorted(dic, key = lambda x:(float(dic[x][1])/float(dic[x][2])), reverse = True)
			value_lst = [(item, (float(dic[item][1])/float(dic[item][2]))) for item in sequence_lst]
	return value_lst


	# build the appropriate list of tuples to return

	# return [('A', 1), ('B', 2)]

if __name__ == "__main__":

	points = 0

	data = get_data()
	if data[0] == ('WY', 55949.0) and data[-1] == ('CA', 7362490.0):
		points += 3.33

	data = get_data(party='gop', raw=False)
	if data [0][0] == 'DC' and int(data[0][1] * 100) == 4 and \
		data[-1][0] == 'WY' and int(data[-1][1] * 100) == 70:
		points += 3.33

	data = get_data(party='dem', raw=True, sort_ascending=False)
	if data[0] == ('CA', 7362490.0) and data[-1] == ('WY', 55949.0):
		points += 3.34

	print("points :", points)
