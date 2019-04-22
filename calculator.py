import math

print("\t________calculator_________")

def sum(a,b):
	a+=b
	return a

def sub(a,b):
	if a>b:
	    a-=b
	    return a
	else:
	    b-=a
	    return b

def mul(a,b):
	a*=b
	return a

def div(a,b):
	q=a/b
	r=a%b
	print("\n quotient is : %s" %q)
	print("\n remainder is : %s" %r)

def sqr(a):
	x=math.sqrt(a)
	return x

while (True):
	print("\n\n choose the operation you want to perform:")
	print("\n\t1.ADDITION")
	print("\n\t2.SUBTRACTION")
	print("\n\t3.MULTIPLICATION")
	print("\n\t4.DIVISION")
	print("\n\t5.SQUARE ROOT")
	print("\n\t6.EXIT")


	choice = int(input('>'))

	if  choice == 1:
	      print("\n\n enter two numbers:")
	      num1=int(input('>'))
	      num2=int(input('>'))
	      s=sum(num1,num2)
	      print("\n The sum is : %s"  )
	
	elif choice == 2:
	      print("\n\n enter two numbers:")
	      num1=int(input('>'))
	      num2=int(input('>'))
	      m=sum(num1,num2)
	      print("\n The difference is : %s"  %m)

	elif choice==3:
		print("\n\n enter two numbers:")
		num1=int(input('>'))
		num2=int(input('>'))
		p=sum(num1,num2)
		print("\n The product is : %s"  %p)

	elif choice==4:
		print("\n\n enter two numbers:")
		num1=int(input('>'))
		num2=int(input('>'))
		div(num1,num2)
	

	elif choice==5:
		print("\n\n enter two numbers:")
		num1=int(input('>'))
		r=sqr(num1)
		print("\n The square root is : %s"  %r)

	else:
          		print("\nyou choose to exit.bye.........")
          		break

