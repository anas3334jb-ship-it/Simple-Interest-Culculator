# SIMPLE INTEREST CALCULATOR

principle = float(input('enter the principle value : '))
rate = float(input('enter rate of interest : '))
time = float(input('enter the time(in years) : '))

simple_interest = (principle*rate*time)/100
print("Simple Interest:", simple_interest)