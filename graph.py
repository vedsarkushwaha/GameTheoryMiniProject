import matplotlib.pyplot as plt

'''
 * python file to plot graphs
 *
 *
 * @author _________________________
 * @version 1.0
 * 
 * Copyright 2014, Indian Institute of Science, 2014
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

def buyer_occurence_graph(total_buyer_occurence,buyer_allocated,fname):
	plt.figure(dpi=1000)
	plt.plot(total_buyer_occurence)
	plt.plot(buyer_allocated)
	plt.xlabel('Time Event')
	plt.ylabel('Buyers Count')
	plt.grid(True)
	plt.legend(["Total Buyer Occurence","Buyer Allocated"],prop={'size':9},loc="best")
	# plt.show()
	plt.savefig(fname,bbox_inches='tight')
	plt.close()

def money_graph(seller_profit,we_profit,buyer_profit,fname):
	plt.figure(dpi=1000)
	plt.plot(seller_profit)
	plt.plot(we_profit)
	plt.plot(buyer_profit)
	plt.xlabel('Time Event')
	plt.ylabel('Units of Money')
	plt.grid(True)
	plt.legend(["Seller's Profit","Exchange's Profit","Buyer's Profit"],prop={'size':9},loc="best")
	# plt.show()
	plt.savefig(fname,bbox_inches='tight')
	plt.close()

def resource_plot(rem_resource,fname):
	plt.figure(figsize=(8, 6), dpi=1000)
	plt.plot(rem_resource)
	plt.xlabel('Time Event')
	plt.ylabel('Remaining Cores')
	plt.grid(True)
	plt.legend(["Remaining Cores"],prop={'size':9},loc="best")
	# plt.show()
	plt.savefig(fname,bbox_inches='tight')
	plt.close()

def we_price_plot(our_price,fname):
	plt.figure(figsize=(8, 6), dpi=1000)
	plt.plot(our_price)
	plt.xlabel('Time Event')
	plt.ylabel("Exchange's Price")
	plt.grid(True)
	plt.legend(["Exchange's Price"],prop={'size':9},loc="best")
	# plt.show()
	plt.savefig(fname,bbox_inches='tight')
	plt.close()