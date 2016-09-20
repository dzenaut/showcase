balance = float(raw_input("Enter balance: "))
AnnualInterest = float(raw_input("Enter annual interest: "))
MinimumPayRate = float(raw_input("Enter Minumum Payment Rate: "))
MinimumPayRate /= 100

AnnualInterestRate = AnnualInterest/ 12.0
AnnualInterestRate /= 100

month = 1
total_paid = 0

while month <= 12:

	trans_balance = balance - balance * MinimumPayRate
	MinumumPayment = balance - trans_balance
	total_paid += MinumumPayment
	balance = trans_balance + trans_balance * AnnualInterestRate

	print "month:", month
	print "balance:", round(balance, 2)
	print "minimum payment:", round(MinumumPayment, 2)
	
	month += 1

print "Total paid:", round(total_paid, 2)