import xml.etree.ElementTree as ET #For xml parsing
import os #For file rename
import datetime #for handling dates
import dateutil.parser as parser
import matplotlib.pyplot as plt
import csv



NSMAP = {'mw':'http://www.mediawiki.org/xml/export-0.10/'}


def init(filename):
	tree = ET.parse(filename)
	root = tree.getroot()
	return root
	


def basic_statistics(filename):
	root = init(filename)
	#root[0] is <siteinfo> which contains basic info, root[1] is <page> which is usually only one in the xml from special:export

	count = 0
	number_of_revisions = 0
	for child in root[1]:
		count = count+1

	number_of_revisions = count-3 #first, second and third children of <page> are title (<title>), namespace (<ns>) and page id (<id>) respectively.

	start_date = root[1][3][1].text #for first revision, there is no parent id
	end_date = root[1][count-1][2].text #for all subsequent revisions, theer are...
	print '*******************'
	print 'The xml is about the article : ', root[1][0].text
	print 'Number of revisions : ', number_of_revisions
	print 'date of first revision in the xml : ', start_date
	print 'date of last revision in the xml : ', end_date
	print '*******************'

def file_rename(old, new):
	os.rename(old,new)

def rename_all_files():
	
	dict_of_name_sdate = {}
	
	# path = '/home/user1/Videos/india_data_expt/'

	# for filename in os.listdir(path):
	# 	print filename

	for filename in os.listdir(path):
		print filename
		if filename == 'index.xml':
			print filename
			root = init(path+filename)
			dict_of_name_sdate[filename] = root[1][3][1].text			
		else:
		 	root = init(path+filename)
		 	dict_of_name_sdate[filename] = root[1][3][2].text
		print 'done'

	print '*' *10
	print dict_of_name_sdate

	sorted_list_of_filenames = sorted(dict_of_name_sdate, key=lambda k: dict_of_name_sdate[k]) # sort keys based on values

	print '#' * 10
	print sorted_list_of_filenames

	sorted_list_of_dates = []
	for f in sorted_list_of_filenames:
		sorted_list_of_dates.append(dict_of_name_sdate[f])


	for d in sorted_list_of_dates:
			print d

	c=1

	for f in sorted_list_of_filenames:
		os.rename(path+f, path+str(c)+'.xml')
		c+=1

	total = c

	print '@'*20

	for filename in os.listdir(path):
		print filename, init(path+filename)[1][3][2].text


	print '-'*20
	for c in range(1,total):
		print str(c)+'.xml', init(path+str(c)+'.xml')[1][3][2].text		


def total_files_in_folder(path):
	return len(os.listdir(path))




def rename_test(path):
	#for filename in os.listdir('/home/user1/Dropbox/WIKI_ANALYSIS/test_folder'):
	#for filename in os.listdir('.'):
	# path= '/home/user1/Videos/india_data_expt/'
	for filename in os.listdir(path):
		if filename == 'index.xml':
			os.rename(path+filename, path+'new_index.xml')


def count_revisions_per_year(path):
	dict_year_rev = {}
	c = total_files_in_folder(path)
	for i in range(1, c):
		print 'hi'
		print path+str(i)+'.xml'
		do_something(path+str(i)+'.xml', dict_year_rev)
	print dict_year_rev

	

def do_something(filename, dict_year_rev):
	root = init(filename)
	print 'test'
	for t in root.findall('.//mw:timestamp', namespaces=NSMAP):
		# print t.text
		x = parser.parse(t.text).year
		if x in dict_year_rev.keys():
			dict_year_rev[x]+=1
		else:
			dict_year_rev[x] = 1
	writer1 = csv.writer(open("year_and_revisions.csv", "w")) #To store the dictionary in a csv file
	for key, val in dict_year_rev.items():
   		writer1.writerow([key, val])


def main():
	# path= '/home/user1/Videos/india_data_expt/'
	path = './test_folder/'
	#basic_statistics('india_100.xml')
	#rename_test()

	# rename_all_files()

	# count_revisions_per_year(path)
	count_revisions_per_year(path)


main()




	

