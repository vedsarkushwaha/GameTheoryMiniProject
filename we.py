from seller import gen_seller,get_seller_price,get_remaining_cores
from buyer import get_buyer,get_buyer_occurrence,get_buyer_second_price
from crit_fun import chk_feasiblility,output,add_to_list,write_to_csv
from graph import buyer_occurence_graph,money_graph,resource_plot,we_price_plot
import operator

'''
 * python file containing providers's functions
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

def get_price(sellers,formula,total_we_profit=0):
	"""
	sellers is a list of lists where each list contains follwing item in order
	1. Seller Name
	2. Number of cores
	3. Price of each core

	If formula is  1 then curernt total profit should be subtracted from numberator

	total_we_profit is the "curernt total profit" to be subtracted

	return the price of 1 core to be charged from buyer by we
	"""
	
	total_price=0
	available_resource_cnt=0
	for i in sellers:
		#the product gives the price of sellers total core
		total_price+=i[1]*i[2]
		available_resource_cnt+=i[1]
	return max((float(total_price-(formula*total_we_profit))/available_resource_cnt),1)

def get_free_resources(sellers):
	"""
	sellers is a list of lists where each list contains follwing item in order
	1. Seller Name
	2. Number of cores
	3. Price of each core

	return the total number of free resources from sellers
	"""
	free_resources=0;
	for seller in sellers:
		free_resources+=seller[1]
	return free_resources

def simulate(formula,iter_cnt):
	"""
	if formula=0
	then exchange profit is not included in deciding posted price
	if formulat=1
	then exchange profit is included in deciding posted price
	All other values to formula is invalid

	iter_cnt will decide how many times the simulation will run

	This program plots following 4 graphs on current directory:
	1. Posted price with time
	2. Buyers allocation
	3. Remaining cores
	4. Profit of each agent

	With this *.csv file will also be generate for each graph
	"""
	if formula!=0 and formula!=1:
		print "Invalid Formula Argument."
		print "It should be either 1 or 0"

	#This variable has seller details
	sellers=gen_seller(10,20,50,1,10)
	output("Sellers",sellers)
	#This variable will store count of buyers occuring in 1 time interval
	time_event=1000
	occurence_of_buyer=get_buyer_occurrence(5,time_event)
	total_we_profit=0
	allocation=[[] for x in xrange(time_event)]
	current_time_event=0
	#####Variables for plotting graph#####
	total_buyer_occurence=[]
	buyer_allocated=[]
	total_cores_required=[] #not done
	total_cores_allocated=[] #not done

	seller_allocated=[] #not done
	total_cores_remaining=[]

	total_buyers_profit=[]
	total_we_profit=[]
	total_sellers_profit=[]
	total_profit=0
	total_we_profit_wo_time=0
	price_charged_by_we=[]
	# This variable is equal to total_we_profit[-1]. To be on safe side, we declare a new variable.
	# Values of list total_we_profit can be changed according to plot.
	#####Variables for plotting graph#####
	for current_time_event in xrange(time_event):
		buyer_cnt=occurence_of_buyer[current_time_event]
		# print "Time Event = "+str(current_time_event)
		#This variable is used to track how many buyers are allocated in current time interval
		buyer_allocated_curr=0
		buyer_profit_curr=0
		seller_profit_curr=0
		we_profit_curr=0
		# print allocation
		#This variable has buyer details
		buyers=get_buyer(buyer_cnt,1,5,1,10,time_event/40)
		buyers.sort(key=operator.itemgetter(2),reverse=True)
		#Reallocate all cores
		deallocate=allocation[current_time_event]
		if len(deallocate)!=0:
			for req in deallocate:
				sellers[req[0]][1]+=req[1]
		allocation[current_time_event]=[]
		print "==================="
		print "Time EVENT: "+str(current_time_event)
		print "==================="
		output("Buyers",buyers)
		#this variable is the price of 1 core charged by we to buyer
		price_for_buyers=get_price(sellers,formula,total_we_profit_wo_time)

		print "Price charged from buyers for 1 core (PP)"
		print price_for_buyers
		#This variable calculates our profit
		for buyeri in buyers:
			#buyeri[2] is the price buyer wants to give for 1 core
			if price_for_buyers<=buyeri[2]:
				# buyers_price=max(price_for_buyers,get_buyer_second_price(buyers,buyeri))
				print "Money taken from buyer"
				#first variale is the index of seller, second variable is the total price of that seller using second bid
				mapped_seller,price_by_seller=chk_feasiblility(buyeri,sellers)
				if mapped_seller!=None and (current_time_event+buyeri[3])<time_event:
					allocation[current_time_event+buyeri[3]].append([mapped_seller,buyeri[1]])
					sellers[mapped_seller][1]-=buyeri[1]
					buyer_allocated_curr+=1
					we_profit_curr+=(price_for_buyers*buyeri[1] - price_by_seller)*buyeri[3]
					total_we_profit_wo_time+=(price_for_buyers*buyeri[1] - price_by_seller)
					buyer_profit_curr+=((buyeri[2]-price_for_buyers)*buyeri[3]*buyeri[1])
					seller_profit_curr+=((price_by_seller-sellers[mapped_seller][2]*buyeri[1])*buyeri[3])
					print "Price charged by Seller"
					print price_by_seller
					print str(buyeri[0])+" matched with "+ str(sellers[mapped_seller][0])
				else:
					print "Price is Higher but no seller with required resource found"
			else:
				print "Price given by buyer is too low"
			print "After iteration"
			output("Sellers",sellers)
			print "Our Profit"
			print we_profit_curr

		price_charged_by_we.append(price_for_buyers)
		total_cores_remaining.append(get_remaining_cores(sellers))

		add_to_list(total_buyer_occurence,buyer_cnt)
		# total_buyer_occurence.append(buyer_cnt)
		add_to_list(buyer_allocated,buyer_allocated_curr)
		# buyer_allocated.append(buyer_allocated_curr)
		add_to_list(total_buyers_profit,buyer_profit_curr)
		# total_buyers_profit.append(buyer_profit_curr)
		add_to_list(total_sellers_profit,seller_profit_curr)
		# total_sellers_profit.append(seller_profit_curr)
		add_to_list(total_we_profit,we_profit_curr)
		# total_we_profit.append(we_profit_curr)

		total_profit+=we_profit_curr
		print "Total Profit = "+str(total_profit)
	
	#graph plotting starts from here
	buyer_occurence_graph(total_buyer_occurence,buyer_allocated,"buyers_occurence"+str(iter_cnt)+str(formula)+".pdf")
	money_graph(total_buyers_profit,total_we_profit,total_sellers_profit,"profit"+str(iter_cnt)+str(formula)+".pdf")
	resource_plot(total_cores_remaining,"rem_resource"+str(iter_cnt)+str(formula)+".pdf")
	we_price_plot(price_charged_by_we,"our_price"+str(iter_cnt)+str(formula)+".pdf")
	buyer_occurence_graph(total_buyer_occurence,buyer_allocated,"buyers_occurence"+str(iter_cnt)+str(formula)+".png")
	money_graph(total_buyers_profit,total_we_profit,total_sellers_profit,"profit"+str(iter_cnt)+str(formula)+".png")
	resource_plot(total_cores_remaining,"rem_resource"+str(iter_cnt)+str(formula)+".png")
	we_price_plot(price_charged_by_we,"our_price"+str(iter_cnt)+str(formula)+".png")

	# print total_buyer_occurence
	write_to_csv(total_buyer_occurence,"total_buyer_occurence"+str(formula)+str(iter_cnt)+".csv")
	write_to_csv(buyer_allocated,"buyer_allocated"+str(formula)+str(iter_cnt)+".csv")
	write_to_csv(total_buyers_profit,"total_buyers_profit"+str(formula)+str(iter_cnt)+".csv")
	write_to_csv(total_we_profit,"total_we_profit"+str(formula)+str(iter_cnt)+".csv")
	write_to_csv(total_sellers_profit,"total_sellers_profit"+str(formula)+str(iter_cnt)+".csv")
	write_to_csv(total_cores_remaining,"total_cores_remaining"+str(formula)+str(iter_cnt)+".csv")
	write_to_csv(price_charged_by_we,"price_charged_by_we"+str(formula)+str(iter_cnt)+".csv")
	# print total_buyers_profit, total_we_profit, total_sellers_profit

if __name__=="__main__":
	#increase this number to increase number of iterations.
	#iteration=1 means whole simulation runs 1 time
	iteration=1

	for i in xrange(iteration):
		print i
		simulate(1,i) 
		simulate(0,i)
