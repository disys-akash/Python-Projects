class gpay: 
    def __init__(self):
        #print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-GPAY-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        self.__uname = str(input("Enter name : "))
        if type(self.__uname) == str:
           print("Name verified sucessfully \n")
        else:
            raise TypeError("Invalid name or check your name once again and try again")
        
    def check_mnumber(self):
        self.__unumber = eval (input("Enter Mobile Number : "))
        if type(self.__unumber)==str:
            if len(self.__unumber)==10:
                print(self.__unumber,)
                print("Mobile number verified sucessfully \n")
            else:
                raise TypeError("Check your mobile number : ")
        else:
            raise ValueError("Invalid Type check your Mobile name and Try Again")
    def check_mail(self):
        self.__umailid = input("Enter Mail ID :")
        if type(self.__umailid) == str:
            if len(self.__umailid) <35:
                print(self.__umailid)
                print("Email id verified sucessfully \n")
            else:
                raise TypeError("check your Emailid")
        else:
            raise ValueError("Invalid Email Address")
    def check_upi(self):
        self.__upi = input("Enter upi id :")
        if type(self.__upi) == str:
            if len(self.__upi) <16:
                print(self.__upi)
                print("Upi id verified sucessfully \n")
                print("sucessfully verified your account \n")
            else:
                raise TypeError("check your Upi")
        else:
            raise ValueError("Invalid upi")
class bank(gpay):
    def __init__(self):
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-SetUp your bank account-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    def check_bank(self):
        self.ubank = input("Enter your bank")
        self.uaccno = input("Enter Bank Account number")
        if len (self.uaccno) <=17:
            print("Succesfully Verified account number")
        else:
            raise TypeError("Check your bank account number")
    def pin_creation(self):
        self.pin = input("Set up a 4 digit upi pin ")
        if len(self.pin) == 4:
            self.repin = input("re enter pin")
            if self.pin==self.repin:
                print("Pin Setup Sucessful")
            else:
                raise TypeError("Incorrect pin , Try again")
        else:
            print("Re-enter 4 digit pin")
class userdata(bank):
    def __init__(self):
            self.alldata=[self.__uname,self.__unumber,self.__umailid,self.__upi,self.ubank,self.uaccnos,elf.pin]
            print(self.alldata)
class payment(bank):
    def __init__(self):
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-Payment-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    def reciver_data(self,ifsc):
        self.__rname = input("Enter Reciver's Name : ")
        if type(self.__rname) == str:
                self.bankname= input("Enter Reciber's Bank :")
                
                self.__ifsccode = ifsc
                print (ifsc)
                if len(self.__ifsccode) == 11:

                    print("IFSC CODE verified")
                else:
                    raise ValueError("Inalid IFSC code \n check the code again")
        else:
            raise TypeError("Invalid Type Name")

    def transcaction(self):
            self.__raccno = input("Enter Reciver's Account number : ")
            if len (self.__raccno) <=17:
                    self.__reaccno1=input(" Re-Enter Reciver's Account number : ")
                    if self.__reaccno1 == self.__raccno:
                           print("Account Number verified")
                    else:
                         raise ValueError("Account Number mismatched Try again")
            else:
                raise ValueError("maximum number of limit crossed check and try agani")
    def e(self):
            self.amount = input("Enter amount to be transfered : ")
            self.pin = input("Enter your 4 digit pin to make transcaction : ")
            if self.pin == "0075":
                print("Transcaction sucess \n")
                print("you earned a new scratch card")

            else:
                print("Incorect pin try again")
user = gpay()
user.check_mnumber()
user.check_mail()
user.check_upi()
user1=bank()
user1.check_bank()
user1.pin_creation()
#user2 = userdata()
user3 = payment()
user3.reciver_data("CIUB0000517")
user3.transcaction()
user3.e()

