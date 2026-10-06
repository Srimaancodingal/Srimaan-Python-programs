from datetime import date , time , datetime
today = date.today ()
now = datetime.now ()
print ("Today's date is : " , today)
print ("Today's date and time is  : " , now)
print ("Components of date is ", today.day , today.month , today.year)
