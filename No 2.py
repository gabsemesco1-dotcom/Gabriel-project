#Freelance work time conversion
hourly_rate = float(85000)
hours = float(5)
minutes = float(45)

decimal_hours = hours + (minutes / 60)
total_payment = decimal_hours * hourly_rate

print("Total payment:", total_payment)