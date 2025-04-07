import adminotp
import sendmail1
details={
        101 : ["varsha","varshareddy1645@gmail.com","PFS21",40000],
        102 : ["Vishnu","vishnuvardhanreddy5635@gmail.com","DA7",35000],
        103 : ["Hari","varshachinni100@gmail.com","DS6",15000]
    }
admin_email = input("Enter Adim email id: ")
x = adminotp.otp(admin_email)
if x == True:
    print("Mails Sending in Progress")
    for data in details:
        if details[data][-1] < 40000:
            sendmail1.send_message1(details[data][1],details[data][0],details[data][-1])
    
    print("All Mails Sent Successfully")  
else:
    print("Wrong OTP Entered, Verification Failed !")
