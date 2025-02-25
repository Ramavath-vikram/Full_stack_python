a=20
b=30
temp=a
a=b
b=temp
print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))


#swapping without using third variable
a=5
b=10
a,b=b,a
print("a",a,"b",b)
