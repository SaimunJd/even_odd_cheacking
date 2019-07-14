cheack=int(input("how many times you want to cheack? : "))
for i in range (cheack):
	num=int(input("enter a number: "))
	if(num<=1):
		print("its not even nor odd")
		
	elif(num%2==0):
		print("its even")
		
	else:
		print("its odd")
		
