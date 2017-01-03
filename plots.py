import matplotlib.pyplot as plt
import csv
import pylab as pl
import numpy as np
import pickle

import wiki_xml_functions


def plot():
	dict1 = {} #Retrieve values from file to dictionary
	for key, val in csv.reader(open("year_and_revisions.csv")):
	    dict1[key] = val


	plt.bar(range(len(dict1)), dict1.values(), align='center')
	plt.xticks(range(len(dict1)), dict1.keys())
	plt.show()

def hist():
	with open('contribution_pkl.txt', 'rb') as handle:
		dict_contri = pickle.loads(handle.read())


	X = np.arange(len(dict_contri))
	pl.bar(X, dict_contri.values(), align='center', width=0.5)
	pl.xticks(X, dict_contri.keys())
	ymax = max(dict_contri.values()) + 1
	pl.ylim(0, ymax)
	pl.show()

def main():
	hist()

main()

	