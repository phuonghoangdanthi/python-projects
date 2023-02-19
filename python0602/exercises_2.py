'''ex3:Với số nguyên n nhất định,
 hãy viết chương trình để tạo ra một dictionary chứa (i, i*i)
   như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.'''
n=int(input("Nhập vào một số:"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)

''''EX4: Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu
        phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.'''

values=input("Nhập vào các giá trị:")
l=values.split(",")
t=tuple(l)
print (l)
print (t)