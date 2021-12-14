print("\t\t\tWelcome To YummyTummy\n")
print("\t\t\tRigester to get started\n")
class login:
    def __init__(self):
        self.__uname = str(input("Enter name with initial : "))
        if type(self.__uname) == str:
           print("Name verified sucessfully \n")
        else:
            raise TypeError("Invalid name or check your name once again and try again")
    def unum(self):
        self.__unumber =  input("Enter Mobile Number : ")
        
        if type(self.__unumber)==str:
            if len(self.__unumber)==10:
                print(self.__unumber,)
                print("Mobile number verified sucessfully \n")
            else:
                raise TypeError("Check your mobile number : ")
        else:
            raise ValueError("Invalid Type check your Mobile name and Try Again")
    def mailid_verify(self):
        self.__umailid = input("Enter Mail ID :")
        if type(self.__umailid) == str:
            if len(self.__umailid) <35:
                print(self.__umailid)
                print("Email id verified sucessfully \n")
            else:
                raise TypeError("check your Emailid")
        else:
            raise ValueError("Invalid Email Address")
    
class hotels:        
    def selct_area(self,*args):
        self.areadb = args
        print(self.areadb)
        self.__area=input("Currently delevering to the abovelocations \n Choose a location")
        for i in args:
            if i == self.__area:
                    print("Showing hotels in ",i)
    def selct_hotels(self):
        if self.__area == "Avadi":
            print("SS hydrabad \n  Ratings - ⭐⭐⭐⭐⭐")
            print("Guesto Express \n Ratings - ⭐⭐⭐")
            print("Quality resturant \n Ratings - ⭐⭐⭐⭐")
            print("A2B \n Ratings - ⭐⭐⭐⭐")
            #self.hotel_selct = input("Choose a hotel")
        else:
            raise ValueError("-NO-HOTELS-FOUND-NEAR-YOU")
            if self.__area == "T Nagar":
                print("Takkur Briyani \n  Ratings - ⭐⭐⭐⭐")
                print("Absolute Barbecues T-Nagar \n Ratings - ⭐⭐⭐⭐")
                print("COAL BARBECUES \n Ratings - ⭐⭐⭐⭐")
                print("Yamoideen \n Ratings - ⭐⭐⭐⭐⭐")
                #self.hotel_selct = input("Choose a hotel")
            else:
                raise ValueError("-NO-HOTELS-FOUND-NEAR-YOU")
                if self.__area == "Porur":
                    print("Salem RR Briyani \n  Ratings - ⭐⭐⭐⭐")
                    print("  \n Ratings - ⭐⭐⭐⭐")
                    print("wangs Kitchen \n Ratings - ⭐⭐⭐⭐")
                    print("Cresent \n Ratings - ⭐⭐⭐⭐⭐")
                    #self.hotel_selct = input("Choose a hotel")
                else:
                    raise ValueError("-NO-HOTELS-FOUND-NEAR-YOU")
                    if self.__area == "Saidapet":
                        print("The Waterfall Restaurant \n  Ratings - ⭐⭐⭐⭐")
                        print("Vasco's T-Nagar \n Ratings - ⭐⭐⭐⭐")
                        print("The Coffee Place \n Ratings - ⭐⭐⭐⭐")
                        print("The Scallion \n Ratings - ⭐⭐⭐⭐⭐")
                        #self.hotel_selct = input("Choose a hotel")
                    else:
                        raise ValueError("-NO-HOTELS-FOUND-NEAR-YOU")
                        if self.__area == "Thiruvanmiyur":
                            print("Writes's caf \n  Ratings - ⭐⭐⭐⭐")
                            print("Madurai Kumar Mess \n Ratings - ⭐⭐⭐⭐")
                            print("SS hydrabad \n Ratings - ⭐⭐⭐⭐")
                            print("NALAN'S GRAVY \n Ratings - ⭐⭐⭐⭐⭐")
                            #self.hotel_selct = input("Choose a hotel")
                        else:
                            raise ValueError("-NO-HOTELS-FOUND-NEAR-YOU")
class dishes(hotels):
    def __init__(self):
        self.chotel = input("Choose an hotel")
        self.hlist = ["SS hydrabad","NALAN'S GRAVY","A2B","Quality resturant","Guesto Express","Takkur Briyani","SS hydrabad","Absolute Barbecues T-Nagar","COAL BARBECUES","Yamoideen","Salem RR Briyani","Hotel Saravana Bhavan","wangs Kitchen","Cresent","The Waterfall Restaurant","Vasco's T-Nagar","The Coffee Place","The Scallion","Writes's caf","Madurai Kumar Mess"]
        self.alldishes = {"pannergobi":"Rs250","aloomatar":"Rs199","frenchfries":"Rs99","manchurian":"249","sizzler":"Rs99","wintersquash":"Rs79","mac&cheese":"Rs249","upma":"Rs499"}

    def menu(self):
        print(self.alldishes)
        for i in self.hlist:
            if i == self.chotel:
                print(self.alldishes)
    def orderstatus(self):
            self.__orderdetails = input("Please Enter Your Order")
            for i in self.alldishes:
                if  k in i.items():
                        if k == self.__orderdetails:
                            print(k)
    def recipt(self):
        print("order placed succesfully for",self.__uname)
        print("payment mode : COD")
        
    

        
#customer = login()
#customer.unum()
#customer.mailid_verify()
#customer1=hotels()
#customer1.selct_area("Avadi","T Nagar","Saidapet","Porur","Thiruvanmiyur")        
#customer1.selct_hotels()
customer2 = dishes()
customer2.menu()
customer2.orderstatus()
customer2.recipt()
