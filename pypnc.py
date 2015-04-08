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

def process(keywords,categories,array):
  array_curr = array

  total_debit = [0.0] * len(keywords)
  total_credit = [0.0] * len(keywords)
  total_unknown = []

  for idx_row,row in enumerate(array):
#    print "row = ", row
    keyword_found = False
    for idx_key,keyword in enumerate(keywords):
      a = re.compile(str(keyword[0]))
      if a.search(str(row[2])):
        keyword_found = True
#        print "idx_row = ", idx_row
#        print "idx_key = ", idx_key
#        print "keyword[0] = ", keyword[0]
#        print "row[2] = ", str(row[2])
        for idx_cat,category in enumerate(categories):
          print "keyword[1]", str(keyword[1])
          if category==str(keyword[1]):      
#            print "category = ", category
#            print "str(keyword[1]) = ", str(keyword[1])
#            sys.exit(0)
#            print "row[5] = ", row[5]  
#            print '"DEBIT" in str(row[5])', "DEBIT" in str(row[5])  
#            raw_input("Press Enter to continue...")
            if "DEBIT" in str(row[5]):
              total_debit[idx_cat] = total_debit[idx_cat] + float(row[1])
#            elif "CREDIT" in str(row[5]):
            else: 
              total_credit[idx_cat] = total_credit[idx_cat] + float(row[1])
#            print "idx_cat = ", idx_cat
#            print "total_debit = ",total_debit[idx_cat]
#            print "total_credit = ",total_credit[idx_cat]

      elif keyword_found==False and idx_key == len(keywords)-1:
        print "unknown keyword = ", row
        total_unknown.append(float(row[1])) 

  for idx_cat,category in enumerate(categories):
    print "category = ", category, "\t\t", "total = ", total_credit[idx_cat]
  print "------------------------------------------------"
  print "total_credit = ", sum(total_credit)
  print "------------------------------------------------"
  for idx_cat,category in enumerate(categories):
    print "category = ", category, "\t\t", "total = ", total_debit[idx_cat]
  print "------------------------------------------------"
  print "total_debit = ", sum(total_debit)
  print "------------------------------------------------"
  print "total_unknown = ", sum(total_unknown)
  print "------------------------------------------------"
  print "total_credit - total_debit = ", sum(total_credit) - sum(total_debit)

def processActivity(keywords,categories,array):
  array_curr = array

  total_debit = [0.0] * len(keywords)
  total_credit = [0.0] * len(keywords)
  total_unknown_debit = []
  total_unknown_credit = []

  for idx_cat,category in enumerate(categories):
    print "-----------------------------------"
    print "category = ", str(category)
    print "-----------------------------------"  
    for idx_key,keyword in enumerate(keywords): 
      for idx_row,row in enumerate(array):
        keyword_found = False
        a = re.compile(str(keyword[0]),re.IGNORECASE)
        if a.search(str(row[1])):
          keyword_found = True
#        for idx_cat,category in enumerate(categories):
          if category==str(keyword[1]):
            print "row[1:3] = ", str(row[1:3])      
            if not str(row[3]): #DEBIT
              cost_string = str(row[2]) 
              cost = float(cost_string.replace('$', '').replace(',',''))
              total_debit[idx_cat] = total_debit[idx_cat] + cost
            else: #CREDIT
              cost_string = str(row[3]) 
              cost = float(cost_string.replace('$', '').replace(',',''))
              total_credit[idx_cat] = total_credit[idx_cat] + cost
#            print "idx_cat = ", idx_cat
#            print "total_debit = ",total_debit[idx_cat]
#            print "total_credit = ",total_credit[idx_cat]
#        print "idx_key = ", idx_key
#        print "len(keywords) = ", len(keywords)
#        print "keyword_found = ", keyword_found
        elif keyword_found==False and idx_row == len(array):
          print "unknown keyword = ", row
          if not str(row[3]): #DEBIT
            cost_string = str(row[2])
            cost = float(cost_string.replace('$', '').replace(',',''))
            total_unknown_debit.append(cost) 
          else: #CREDIT
            cost_string = str(row[3])
            cost = float(cost_string.replace('$', '').replace(',',''))
            total_unknown_credit.append(cost) 
    print "total credit = {1}".format(category,total_credit[idx_cat])
    print "total debit = {1}".format(category,total_debit[idx_cat])      

  for idx_cat,category in enumerate(categories):
#    print ("category = " + str(category) + "\t\t" + "total = " + str(total_credit[idx_cat])).expandtabs(10)
    print "category: {0:20} total = {1}".format(category,total_credit[idx_cat])
  print "------------------------------------------------"
  print "total_credit = ", sum(total_credit)
  print "------------------------------------------------"
  for idx_cat,category in enumerate(categories):
#    print ("category = " + str(category) + "\t\t" + "total = " + str(total_debit[idx_cat])).expandtabs(10)
    print "category: {0:20} total = {1}".format(category,total_debit[idx_cat])
  print "------------------------------------------------"
  print "total_debit = ", sum(total_debit)
  print "------------------------------------------------"
  print "total_unknown_debit = ", sum(total_unknown_debit)
  print "------------------------------------------------"
  print "total_unknown_credit = ", sum(total_unknown_credit)
  print "------------------------------------------------"
  print "total_credit - total_debit = ", sum(total_credit) - sum(total_debit)



def main():
  file_csv = sys.argv[1]
  print 'file csv = ', file_csv
  date = sys.argv[2]
#  array_csv = open_csv_remove_first_line(file_csv)

  array_csv = open_csv_remove_first_line_activity(file_csv)

  createDB()
  keywords = loadDB()

  categories = larkinCatActivity.categories()

#  process(keywords,categories,array_csv) 
 
  processActivity(keywords,categories,array_csv)    



if __name__ == '__main__':
  main()
