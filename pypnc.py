#!/usr/bin/env python

import sys
import csv

import sqlite3
import re
import datetime

import larkinCatActivity

conn = sqlite3.connect('keyword_category.db')
cur = conn.cursor()

def createDB():
  with conn:
    cur = conn.cursor()    
    cur.execute("DROP TABLE IF EXISTS Keywords")
    cur.execute("CREATE TABLE Keywords(keyword TEXT, category1 TEXT, category2 TEXT)")
    cur.executemany("INSERT INTO Keywords VALUES(?, ?, ?)", larkinCatActivity.keywords())

def loadDB():
  print "loadDB():"

  with conn:    
    cur = conn.cursor()    
    cur.execute("SELECT * FROM Keywords")
    rows = cur.fetchall()
    array = []
    for row in rows:
#      print row
      array.append(row)
  return array

def open_csv_remove_first_line(file_csv):  
  with open(file_csv, 'rb') as csvfile:
    array_csv= csv.reader(csvfile, delimiter=',')
    array_csv_orig = []
    array_csv_new = []
    for idx, row in enumerate(array_csv): 
#      print ', '.join(row)
      array_csv_orig.append(row)
    for idx, row in enumerate(array_csv_orig[1:]):
      array_csv_new.append(row)
#      print row
  return array_csv_new

def open_csv_remove_first_line_activity(file_csv):  
  with open(file_csv, 'rb') as csvfile:
    array_csv= csv.reader(csvfile, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL)
    array_csv_orig = []
    array_csv_new = []
    for idx, row in enumerate(array_csv): 
#      print ', '.join(row)
      array_csv_orig.append(row)
    for idx, row in enumerate(array_csv_orig[1:]):
      array_csv_new.append(row)
#      print row
  return array_csv_new

def open_csv_activity(file_csv):  
  with open(file_csv, 'rb') as csvfile:
    array_csv= csv.reader(csvfile, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL)
    array_csv_orig = []
    array_csv_new = []
    for idx, row in enumerate(array_csv): 
#      print ', '.join(row)
      array_csv_orig.append(row)
    for idx, row in enumerate(array_csv_orig[1:]):
      array_csv_new.append(row)
#      print row
  return array_csv_orig

def processActivity(keywords,categories,array):
  array_curr = array
  debitStringArray = [[] for i in range(len(categories))]
  creditStringArray = [[] for i in range(len(categories))]
  total_debit = [0.0] * len(keywords)
  total_credit = [0.0] * len(keywords)
  total_unknown_debit = []
  total_unknown_credit = []
  unknown_credit = []
  unknown_debit = []

#  print "categories = ", categories
#  print "keywords = ", keywords

  for idx_row,row in enumerate(array):
#    print "idx_row = ", idx_row
#    print "row = ", row
    def checkCatKey():
      for idx_cat,category in enumerate(categories):
        for idx_key,keyword in enumerate(keywords): 
          a = re.compile(str(keyword[0]),re.IGNORECASE)
          if a.search(str(row[1])):
            if category==str(keyword[1]):   
              if not str(row[3]): #DEBIT
                cost_string = str(row[2]) 
                cost = float(cost_string.replace('$', '').replace(',','')) 
                debitStringArray[idx_cat].append(str(row[1:3]))
                total_debit[idx_cat] = total_debit[idx_cat] + cost
                return
              else: #CREDIT
                cost_string = str(row[3]) 
                cost = float(cost_string.replace('$', '').replace(',',''))
                total_credit[idx_cat] = total_credit[idx_cat] + cost
                creditStringArray.append(str(row[1:3]))
                return
        if idx_key == len(keywords)-1 and idx_cat == len(categories)-1:
          if not str(row[3]):
            unknown_debit.append(row)
          else:
            unknown_credit.append(row)
    checkCatKey()
         
#                continue
#              for line in array: 
#                print "line = ", line
#            print "idx_cat = ", idx_cat
#            print "total_debit = ",total_debit[idx_cat]
#            print "total_credit = ",total_credit[idx_cat]
#        print "idx_key = ", idx_key
#        print "len(keywords) = ", len(keywords)
#        print "keyword_found = ", keyword_found
        
#        elif not a.search(str(row[1])) and idx_key == len(keywords)-1 and idx_cat == len(categories)-1 and :
#          print "unknown keyword = ", row
#          if not str(row[3]): #DEBIT
#            cost_string = str(row[2])
#            cost = float(cost_string.replace('$', '').replace(',',''))
#            total_unknown_debit.append(cost) 
#          else: #CREDIT
#            cost_string = str(row[3])
#            cost = float(cost_string.replace('$', '').replace(',',''))
#            total_unknown_credit.append(cost) 


#----------------------------------------------------------------------------

#  print "total credit = {1}".format(category,total_credit[idx_cat])
#  print "total debit = {1}".format(category,total_debit[idx_cat])      

  print "------------------------------------------------"
  print "credits"
  print "------------------------------------------------"
  for idx_cat,category in enumerate(categories):
    print "------------------------------------------------"
    print "category: {0:20} total = {1}".format(category,total_credit[idx_cat])
    print "------------------------------------------------"
    for line in creditStringArray[idx_cat]:
      print "line = ", line
    print "------------------------------------------------"
  print "------------------------------------------------"
  print "debits"
  print "------------------------------------------------"
  for idx_cat,category in enumerate(categories):
    print "------------------------------------------------"
    print "category: {0:20} total = {1}".format(category,total_debit[idx_cat])
    print "------------------------------------------------"
    for line in debitStringArray[idx_cat]:
      print "line = ", line
    print "------------------------------------------------"

  print "------------------------------------------------"
  print "credits"
  print "------------------------------------------------"
  for idx_cat,category in enumerate(categories):
    print "category: {0:20} total = {1}".format(category,total_credit[idx_cat])
  print "------------------------------------------------"
  print "debits"
  print "------------------------------------------------"
  for idx_cat,category in enumerate(categories):
    print "category: {0:20} total = {1}".format(category,total_debit[idx_cat])

  print "------------------------------------------------"
  print "total_credit = ", sum(total_credit)
  print "------------------------------------------------"

  print "------------------------------------------------"
  print "total_debit = ", sum(total_debit)
  print "------------------------------------------------"

  print "------------------------------------------------"
  print "total_unknown_debit = ", sum(total_unknown_debit)
  print "------------------------------------------------"
  print "total_unknown_credit = ", sum(total_unknown_credit)
  print "------------------------------------------------"
  print "total_credit - total_debit = ", sum(total_credit) - sum(total_debit)
  print "------------------------------------------------"
  print "------------------------------------------------"
  print "------------------------------------------------"
  print "------------------------------------------------"
  print "------------------------------------------------"
  print "------------------------------------------------"
  print "------------------------------------------------"
  print "unknown credit"
  for line in unknown_credit:
    print "line = ", line
  print "unknown debit"
  for line in unknown_debit:
    print "line = ", line  



def main():
  file_csv = sys.argv[1]
  print 'file csv = ', file_csv
  date = sys.argv[2]
#  array_csv = open_csv_remove_first_line(file_csv)

#  array_csv = open_csv_remove_first_line_activity(file_csv)
  array_csv = open_csv_activity(file_csv)

  createDB()
  keywords = loadDB()

  categories = larkinCatActivity.categories()

#  process(keywords,categories,array_csv) 
 
  processActivity(keywords,categories,array_csv)    



if __name__ == '__main__':
  main()
