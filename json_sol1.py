'''Solution is given assuming the string has only round brackets and "&&" and "||" operators
also it is assumed that only one operator is enclosed inside brackets'''

#Steps used in this solution:
#1-Convert the string into more programming friendly form like removing double character(&&) into single characters(+)
#2-Sorting these operands and operators in postfix form
#3-Combing these individual operands into dictionary form
#4-Joinng them back in dictionary form
import sys
import json
str = input("Enter string")  # Reading input string
dict1 = {}  # Dictionary to save the values
for i in str:
    if i.isalpha():
        dict1[i] = str[str.index(i) + 2]


str = ''.join([i for i in str if not i.isdigit()])
str = str.replace("=", "")
str = str.replace(" ", "")
str = str.replace("&&", "+")  # Replacing && with + for easy of coding as it converts 2 string spaces to 1
str = str.replace("||", "-")  # Replacing || with - for easy of coding
pre_str = []  # initializing a list to store the prefix of the input string
stack = []  # stack used during conversion to pretfix
br_n = 0  # inlitialising integer representing no.of open and close brackets

for i in str:
    if i == "(":
        br_n += 1
    elif i == ")":
        br_n -= 1
if br_n != 0:  # exit if the brackets are unbalanced
    sys.exit("Give a valid string")


for i in str:
    if i == "(":  # handling the brackets
        stack.append(i)
    elif i == ")":
        while (stack[len(stack) - 1] != "("):
            pre_str.append(stack.pop())
        stack.pop()
    elif i == "+":  # handling "+" i.e. && operator
        stack.append(i)
    elif i == "-":  # handling "-" i.e. || operator
        stack.append(i)
    elif i.isalpha():  # handling the operands
        pre_str.append(i)
while (len(stack) != 0):  # handling the leftover operators of the stack
    pre_str.append(stack.pop())

opts= []    #list to store the operators in the string
for i in pre_str:
    if i == "+" or i == "-":
        opts.append(i)
r = "".join(i for i in pre_str) #converting the list into string to get the operands separately
opnds = []  #list containing the operands
x = r.split("-")
for i in x:
    x1 = i.split("+")
    opnds.extend(x1)
for i in opnds:
    if i == "":
        opnds.remove(i)
pre_str = []
#removing all the elements of the list to add them in dictionary form
#we later combine these dictionaries as required
for i in opnds:
    dict = {}     #dict,dict2 are temporary dictionaries
    l4 = list(i)    #temporary list
    for j in range(len(l4)):
        dict[l4[j]] = dict1[l4[j]]   #to give a dictionary in the form {operand:value}
    if len(l4) == 2:
        dict2 = {}
        if opts[0] == "+":
            dict2["and"] = dict   #converting "+" back to "and"
            pre_str.append(dict2)
            opts.pop(0)
        elif opts[0] == "-":   #converting "-" back to "or"
            dict2["or"] = dict
            pre_str.append(dict2)
            opts.pop(0)
    else:
        pre_str.append(dict)
        pre_str.append(opts[0])
        opts.pop(0)
for i in pre_str:    #removing the empty dictionaries the list
    if i == {}:
        pre_str.remove(i)
while len(opts) != 0:
    pre_str.append(opts[0])
    opts.pop(0)

i=0             #second level of combing dictionaries for the respective operators
j=len(pre_str)
while(i<j):
    dict2={}
    if pre_str[i]== "+":
        dict2["and"]= pre_str[i - 2:i]
        pre_str.pop(i - 1)
        pre_str.pop(i - 2)
        k=0
        for k in range(len(pre_str)):
            if pre_str[k]== "+":
                i=k
                break
        pre_str[i]=dict2
    elif pre_str[i]== "-":
        dict2["or"] = pre_str[i - 2:i]
        pre_str.pop(i - 1)
        pre_str.pop(i - 2)
        k = 0
        for k in range(len(pre_str)):
            if pre_str[k] == "-":
                i = k
                break
        pre_str[i] = dict2
        pass
    j=len(pre_str)
    i+=1
final_dict={}
final_dict["query"]=pre_str[0]

x=json.dumps(final_dict, indent=1)
print(x)



