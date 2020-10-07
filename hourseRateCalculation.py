# Write a program to prompt the user for hours and rate per hour using raw input to compute gross pay. 

def computepay(hours, rate):
	if hours > 40: 
		extraHours = hours - 40
		calculate = (40 * rate) + (extraHours * (rate * 1.5))
		return calculate
	else: 
		calculate = hours * rate
		return calculate

hours = float(raw_input("Enter Hours: "))
rate = float(raw_input("Enter Rate: "))
print computepay(hours, rate)


