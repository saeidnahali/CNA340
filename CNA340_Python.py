print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12")

dict1={"Oil change":35,"Tire rotation":19,"Car wash":7,"Car wax":12,"-":"No service"}

print("\nSelect first service:")
ser1=input()
print("Select second service:")
ser2=input()

#test
print("\nDavy's auto shop invoice\n")

if ser1!='-' and ser2!='-':
    print("Service 1: "+ser1+", $"+ str(dict1[ser1]))
    print("Service 2: "+ser2+", $"+ str(dict1[ser2]))
    Total=dict1[ser1]+dict1[ser2]
elif ser1=='-':
    print("Service 1: "+"No service")
    print("Service 2: "+ser2+", $"+ str(dict1[ser2]))
    Total=dict1[ser2]
else:
    print("Service 1: "+ser1+", $"+ str(dict1[ser1]))
    print("Service 2: "+"No service")
    Total=dict1[ser1]

print("\nTotal: $"+str(Total))
