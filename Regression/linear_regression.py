import csv
import math
import numpy
import statsmodels.api as sm

def data():
  list1,list2,list3,list4,list5,output=[],[],[],[],[],[]
  with open('parse_traceroute.csv') as inf:
      reader=csv.reader(inf)
      for row in reader:
      	list1.append(float(row[1]))
  with open('parse_hping.csv') as f:
      reader=csv.reader(f)
      for row in reader:
      	list2.append(float(row[1]))
        list3.append(float(row[2]))
        list4.append(float(row[3]))
        list5.append(float(row[4]))

  z = zip(list1[:251],list2[:251],list4[:251],list5[:251])
  input1=[list(elem) for elem in z]
  input1=sm.add_constant(input1)
  result=sm.OLS(list3[:251],input1).fit()
  out=result.params
  print "***",out,"***"
  
  x = zip(list1[251:],list2[251:],list4[251:],list5[251:])
  count = 1
  diff_sum = 0
  mape=0
  ssc=0

  for line in x:
    predicted_value = out[1]*line[0]+out[2]*line[1]+out[3]*line[2]+out[4]*line[3]+out[0]
    actual_value = list3[250+count]
    count+=1
    print actual_value, predicted_value
    if actual_value==0:
        continue
    diff_sum+=abs(predicted_value-actual_value)
    mape+=(abs(predicted_value-actual_value)*100)/actual_value
    ssc+=(abs(predicted_value-actual_value)*abs(predicted_value-actual_value))
  
  print "Avg Diff", diff_sum/(count-1)
  print "MAPE", mape/(count-1)
  print "SSC", ssc
  
data()

