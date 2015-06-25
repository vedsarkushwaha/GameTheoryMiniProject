from seller import get_seller,get_seller_price
import csv

'''
 * python file containing supportive functions
 *
 * Copyright 2015 Vedsar and Ishwar
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 '''

def chk_feasiblility(buyeri,sellers):
	"""
	buyeri is lst contains the following items:
	1. buyer Name
	2. Number of cores
	3. Price of each core

	sellers is a list of lists where each list contains the following item:
	1. seller Name
	2. Available Cores
	3. Price of each core
	
	return two values
	1. The index of seller who can fulfill the request of buyeri else return None
	2. Price of seller
	"""
	mapped_seller=get_seller(buyeri,sellers)
	if mapped_seller==None:
		return None,None
	price=get_seller_price(sellers,mapped_seller,buyeri[1])
	return mapped_seller,price

def add_to_list(lst,value):
	"""
	insert the value into lst.
	For each insertion, add the value and previous value of the list.
	Previous value of the list can be accessed by lst[-1]
	"""
	if len(lst)==0:
		lst.append(value)
	else:
		lst.append(value+lst[-1])

def output(prestring, lst):
	"""
	prestring is the string to be printed before the list will print
	lst is the list which is to be printed
	
	No return type/data for this function
	"""
	print "These are the "+prestring
	for i in lst:
		print i

def write_to_csv(lst,fname):
	"""
	lst is the 1D list
	fname is the file name where the lst will be stored
	"""
	fp=open(fname, "w")
	wr=csv.writer(fp,dialect='excel')
	wr.writerow(lst)
