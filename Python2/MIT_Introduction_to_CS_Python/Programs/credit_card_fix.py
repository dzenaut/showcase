balance = 4773
AnnualInterest = 20
AnnualInterestRate = 18 / 12.0 / 100

interval = 10
low = 0
high = balance
test = True

while test:
	balance = 4773
	guess = float((high + low) / 2)
	print guess
	for month in range(1, 13):

		trans_balance = balance - guess
		if trans_balance > 0:
			balance = trans_balance + trans_balance * AnnualInterestRate
		else:
			balance = 0
	
	

		if balance == 0 and month < 12:
			high = guess
			break
		elif balance == 0 and month == 12:
			test = False
			break
		elif balance > 0 and month == 12:
			low = guess
			break

pre_guess = float(round(guess, -1))
print pre_guess

test = True
while test:
	balance = 4773
	guess = pre_guess - 10.0
	for month in range(1, 13):
		trans_balance = balance - guess
		balance = trans_balance + trans_balance * AnnualInterestRate

		if balance > 0 and month == 12:
			guess = pre_guess
			test = False
			break
		elif balance <= 0 and month == 12:
			pre_guess = guess
			break

print "Done:", pre_guess


	


