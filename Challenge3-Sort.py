#Write a function that sorts the following string of height given in Feet and Inches in ascending order:
# 5’2,6’7,5’1,6’11
# 5’8,6’6,7’1,6’8

def string_height(s):
    s_list = s.split(',')
    #print(s_list)
    a = []
    for i in s_list:
        a.append(i.split("'"))
    #print(a)
    ht = []
    for i in range(0,len(a)):
        ht.append(int(a[i][1]) + int(a[i][0])*12)
    #print(ht)
    zip_data = list(zip(ht,s_list))
    #print(zip_data)
    sort_data = sorted(zip_data)
    #print(sort_data)
    tuples = zip(*sort_data)
    list1, list2 = [list(tuple) for tuple in tuples]
    print(list1)
    print(list2)
string_height("5'2,6'7,5'1,6'11")
string_height("5'8,6'6,7'1,6'8")