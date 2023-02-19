# link:https://quantrimang.com/hoc/hon-100-bai-tap-python-co-loi-giai-code-mau-142456#mcetoc_1btoaqi390 
# Ex1:Tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5
'''j=[]
for i in range(2000,3500):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print(','.join(j))
'''
#ex2: tính giai thừa của một số cho trước
x = int(input('Nhập số:'))
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
print(fact(x))