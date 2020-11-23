#// nhập link nơi mún liệt kê tất cả tập tin
folder=input('nhập tên file:') 
folder=r"{}".format(folder)
list=[]
listnew=[]
import os
#list all file in folder
x=os.listdir(folder)
print(x)
#lấy thông tin về chi tiết 1 file cụ thể: epoch time, timestap
for file in x:
    a=os.path.join(folder,file)
    #.st_time chỉ cụ thể thông tin cần lấy
    b=os.stat(a).st_ctime
    info=(file,b)
    list.append(info)
print(list)
def takesecond(elem):
    return elem[1]
list.sort(key=takesecond,reverse=True)
print('sorted list:',list)
# giảm dần theo dung lượng
def human(size):
    B="B"
    KB="KB"
    MB="MB"
    GB="GB"
    TB="TB"
    Unit=[B,KB,MB,GB,TB]
    HUMANFMT="%.2f %s"
    HUMANRADIX=1024.0
    for listnew in Unit[:-1]:
        if size < HUMANRADIX:
            return HUMANFMT%(size,listnew)
        size /=HUMANRADIX

    return HUMANFMT % (size,Unit[-1])
    for listnew in x:
    x=os.path.join(folder,file)
    #.st_time chỉ cụ thể thông tin cần lấy
    m=os.stat(x).st_size
    info=(file,m)
    listnew.append(info)
print(listnew)
def takesecond(elem):
    return elem[1]
list.sort(key=takesecond,reverse=True)
print('sorted list:',listnew)