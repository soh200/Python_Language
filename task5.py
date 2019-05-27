# displaying the no. of days in a month
p=str(input(" enter the month "))
s=p.lower()
if ( s=='april' or s=='june' or s=='september' or s=='november' ):
    print(" the no. of days ", str(30))
elif (s=='february'):
    print(" the no. of days= ", str(28))
else:
    print(" the no. of days= ", str(31))
