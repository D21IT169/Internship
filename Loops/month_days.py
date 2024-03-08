month = input("Enter the name of Month: ")
 
if month == "February":
	print("No. of days: 28/29 days")
elif month in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Invalid month name")