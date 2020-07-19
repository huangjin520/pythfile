with  open("test1.txt",'rb') as open_object:
    header=open_object.read(4)
    data=open_object.read()
    print("{0}标题\n{1}数据".format(header,data))
for line in open_object