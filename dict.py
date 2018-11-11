dict={0:"Hi",1:"hello"}
print(dict)

newdict=dict.fromkeys(dict,10)  #copy keys from dict and create new one with keys and speicifed value
print(newdict)

copydict= dict.copy()
print(copydict)
print(dict)
print(dict)
dict[2]="Hello Pyhton"
print(copydict,dict)

print(dict.get(1))

print(dict.has_key(0))

print(dict.items())

#Iteration of dicts
for k,v in dict.items():
    print("Key {} and the value is {}".format(k,v))
for i in dict:     #print keys
    print i
for i in dict.iteritems():   #print key,value pairs
    print i
for i in dict:
    if(i==0):
        print dict[i]   #print value of a particular key
for i in dict.iterkeys():
    print "The keys are {}".format(i)
    print "the value is {}".format(dict[i])
for i in dict.itervalues():
     print "the value is {}".format(i)

        
print(dict.has_key(1)) #check if a key is present

newlist=dict.keys()  #Returns list of keys
print(newlist)
print(dict.keys()) 
print(dict.values())  #Returns list of values
print(dict.pop(0))  #Remove K,v pair from index 0
 
print(dict.popitem())
print(dict)
dict[1]="Hello"
dict[0]="Hi"

print(dict.viewitems())
print(dict.viewkeys())
print(len(dict))

#Sorting Dictionaries with value pair
import operator
dict_sorted=sorted(dict.items(), key=operator.itemgetter(1))  #change index value to 0 for sorting by keys
print(dict_sorted)
print(dict)

dict_sorted1=sorted(dict.items(),key= lambda x: x[0],reverse=True)
print(dict_sorted1)
dict_sorted1.append("Just adeed")
print(dict_sorted1[0][1])
print(dict_sorted1[3])

ze=dict.update(dict_sorted)
print(ze)



