medicalcause=input("Do you have a medical cause (Y/N): ").upper ()
if medicalcause== 'Y':
    print ("You are allowed for the exam")
else:
    attendence= int(input ("Enter attendence"))
    if attendence<=75:
        print ("You are not allowed for the exam")
    else: 
        print ("You are allowed for the exam")
