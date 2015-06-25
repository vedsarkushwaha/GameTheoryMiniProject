import names,random,operator

'''
 * python file containing seller's functions
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

def gen_seller(n,mn_core,mx_core,mn_price,mx_price):
	"""
	generate n sellers
	each seller will have [mn_core,mx_core]
	and	price of each core will be [mn_price,mx_price]

	return a list where each list contains follwing item in order
	1. Seller Name
	2. Number of cores
	3. Price of each core
	"""
	seller=[]
	for num in xrange(n):
		member=[]
		member.insert(0, names.get_full_name())
		member.insert(1,random.randint(mn_core, mx_core))
		member.insert(2,random.uniform(mn_price, mx_price))
		seller.insert(n,member)
	return seller


def get_seller_price(sellers,seller_id,core_request):
	"""
	sellers is a list of list where each list contains follwing item in order
	1. Seller Name
	2. Number of available cores
	3. Price of each core
	4. List of lists where length of main list is equal to number of cores. Length of minor list will be zero.
	seller_id is the seller index whose price to be determined.
	You can access this seller by seller[seller_id]
	core_request is the number of core requested

	return the total price of this deal using second price auction
	if seller_id is with largest ask then return its own price
	"""
	
	new_list = list(sellers)
	new_list.sort(key=operator.itemgetter(2))
	i=0;
	for x in new_list:
		if x==sellers[seller_id]:
			break
		i+=1
	#print i
	if i==len(sellers)-1:
		return new_list[i][2]*core_request
	else :
		price=0
		core=core_request
		price=0
		while core>0:
		 	i+=1
		 	if i==len(sellers)-1:
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
		 			
def get_seller(buyer,sellers):
	"""
	buyer is the list with following items:
	1. buyer Name
	2. Number of cores
	3. Price of each core
	4. Allocation Time (This parameter should be in integer range from [1,rime_event])

	sellers is a list of list where each list contains follwing item in order
	1. Seller Name
	2. Number of available cores
	3. Price of each core
	
	return the first seller index who fulfills the request of buyer(i.e number of cores).
	Here first seller is the seller with highest price. Similarly last seller is the seller with lowest price.
	Price of each seller is the third entry in sellers lists.
	
	If none of the seller fulfills the request then return None.
	"""
	new_list = list(sellers)
	new_list.sort(key=operator.itemgetter(2))
	i=0;
	for x in new_list:
		 if x[1]>=buyer[1]:
		 	return sellers.index(x)
	return None

def get_remaining_cores(sellers):
	"""
	sellers is a list of list where each list contains follwing item in order
	1. Seller Name
	2. Number of available cores
	3. Price of each core
	
	return the total number of cores unallocated
	"""
	rem_core=0
	for selleri in sellers:
		rem_core+=selleri[1]
	return rem_core
