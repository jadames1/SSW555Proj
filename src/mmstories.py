import unittest
from datetime import datetime

#takes date in form DD Mon YYYY

def checkIfDateBeforeNow(date):
	try:
		datetime_object = datetime.strptime(date, '%d %b %Y')
		currDate = datetime.today()
		if datetime_object <= currDate:
			return True
		else:
			return False
	except:
		return False

def checkLessThan5SharedSiblingBdays(fam, ind):
	for f in fam:
		if "CHIL" in fam[f]:
			if len(fam[f]["CHIL"]) > 4: #could be situation where more than 5
				children = fam[f]["CHIL"].copy()
				dates = {}
				for c in children: #have list of children
					cDate = ind[c]["BIRT"]
					if cDate in dates:
						dates[cDate] = dates[cDate] + 1
					else:
						dates[cDate] = 1
				for d in dates:
					if dates[d] >= 5:
						#NOT VALID, maybe delete individuals, and siblings in fam
						for i in range(len(fam[f]["CHIL"])):
							newList = []
							print(fam[f]["CHIL"][i])
							if ind[fam[f]["CHIL"][i]]["BIRT"] != d:
								newList.append(fam[f]["CHIL"][i])
						fam[f]["CHIL"] = newList.copy()

						for c in children:
							if ind[c]["BIRT"] == d:
								ind.pop(c, None)

						newList = []
					
						# print(fam)
						# print(ind)
						print("Sorry this amount of children born on the same day is not valid")
	


class MyTest(unittest.TestCase):
	def test(self):
		self.assertTrue(checkIfDateBeforeNow("23 SEP 1960"))
		self.assertEqual(checkIfDateBeforeNow("17 JUN 2029"), False)
		self.assertTrue(checkIfDateBeforeNow(datetime.today().strftime('%d %b %Y')))
		self.assertEqual(checkIfDateBeforeNow("123 JUN 2020"), False)
		self.assertEqual(checkIfDateBeforeNow("31 FEB 2011"), False)
		
# if __name__ == '__main__':
#     unittest.main()

ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
		'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F16'},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'}}


fam = {'F23': 
		{'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
		 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','HUSB': 'I32', 'WIFE': 'I30'}}

#checkLessThan5SharedSiblingBdays(fam, ind)