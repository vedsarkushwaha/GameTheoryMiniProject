import names,random,operator
import numpy as np

'''
 * python file containing buyer's functions
 *
 * @author Vedsar Kushwaha and Ishwar Raut
 * @version 1.0
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

def get_buyer(n,mn_core,mx_core,mn_price,mx_price,total_time_event):
	"""
	generate n buyer
	each buyer will request in [mn_core,mx_core]
	price of each core will be in [mn_price,mx_price]
	total_time_event is the total time events

	return a list where each list contains follwing item in order
	1. buyer Name
	2. Number of cores
	3. Price of each core
	4. Allocation Time (This parameter should be in integer range from [1,time_event])
	"""
	buyer=[]
	for num in xrange(n):
		member=[]
		member.insert(0, names.get_full_name())
		member.insert(1,random.randint(mn_core, mx_core))
		member.insert(2,random.uniform(mn_price, mx_price))
		member.insert(3,random.randint(1, total_time_event))
		buyer.insert(n,member)
	return buyer

def get_buyer_occurrence(mean_buyer, total_time_event):
	"""
	mean_buyer is the lambda value for poisson
	total_time_event is the total sequence lenthg
	
	return a list of sequence generated by poisson
	"""
	tmp=np.random.poisson(mean_buyer,total_time_event)
	return  [x for x in tmp]

def get_buyer_second_price(buyers,buyeri):
	"""
	buyeri is a buyer with following values
	1. buyer Name
	2. Number of cores
	3. Price of each core
	4. Allocation Time (This parameter should be in integer range from [1,time_event])

	buyers is a list of list where each list contains follwing item in order
	1. buyer Name
	2. Number of cores
	3. Price of each core
	4. Allocation Time (This parameter should be in integer range from [1,rime_event])
	Note that buyers list is sorted in decreasing order of buyers[2] (price of buyer)

	return the total price of the buyer using second price auction
	if buyeri is with least ask then return its own price
	"""
	new_list = list(buyers)
	
	new_list.sort(key=operator.itemgetter(2) ,reverse=True)
	i=0;
	for x in new_list:
		if x==buyeri:
			break
		i+=1
	if i==len(buyers)-1:
		return new_list[i][2]*buyeri[1]
	else :
		price=0
		core=buyeri[1]
		price=0
		while core>0:
		 	i+=1
		 	if i==len(buyers)-1:
		 		price+=core*new_list[i][2]
		  		core=0
		 	else:
		 		if core>new_list[i][1]:
		 			core=core-new_list[i][1]
		 			price+=new_list[i][1]*new_list[i][2]
		 		else:
		 			price+=core*new_list[i][2]
		 			core=0
		return  price
