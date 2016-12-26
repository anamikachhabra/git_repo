import xml.etree.ElementTree as ET #For xml parsing
import os #For file rename

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

def rename_all_files(filename):
	dict_of_name_sdate = {}


def rename_test():
	#for filename in os.listdir('/home/user1/Dropbox/WIKI_ANALYSIS/test_folder'):
	#for filename in os.listdir('.'):
	for filename in os.listdir('test_folder'):
		if filename == 'index.xml':
			os.rename(filename, 'new_index.xml')


#basic_statistics('india_100.xml')
rename_test()




	

