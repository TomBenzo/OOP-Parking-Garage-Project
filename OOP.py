class Garage():

    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]       #list of tickets
        self.space = [1,2,3,4,5,6,7,8,9,10]         #list of space
        self.current = {}                           #dictionary for current ticket after a ticket is taken


    def GetTicket(self):
        if self.tickets:
            print(f'Your ticket number is {self.tickets[0]}')       #self.tickets is holding an index at position 0, which is ticket number 1

            self.current[self.tickets[0]] = 'unpaid' #after taking in user input
            print(self.current)                      #the payment status will be "unpaid" until looping through the "Pay" process

            self.tickets.pop(0) #tickets reduce by 1 in list by using .pop() method, we're able to pull out a specific number in a given list

            self.space.pop(0) #space reduce by 1 in list
            
            print(f'Available Space After{self.space}')         #available space after a ticket is given out
            print(f'Avaialble Tickets After{self.tickets}')     #available tickets after a ticket is given out 

    
    def payForParking(self):
        payment= int(input('What is your ticket number ?'))

        if self.current[payment] == "unpaid":      #if a user ticket number matches an unpaid status of a parking spot, after going through the "Pay" process
            self.current[payment]= "paid"          # it will change "unpaid" to "paid"

        print(self.current)

    
    def leaveGarage(self):
        payment = int(input('Please enter your ticket number'))

        if self.current[payment] == "paid":
            print("Thank you for choosing us!")
            
            self.tickets.append(payment) #adding paid ticket back into the list and sorted in order // increase +1
           
            self.space.append(payment) #adding space back into the list and sorted in order // increase +1
           
            x = sorted(self.tickets)
            
            print(x)

            y= sorted(self.space)

            print(y)
            

        elif self.current[payment] == "unpaid":    #if user try to leave without paying, this message will pop up if the payment status remains "unpaid"
            print("Please pay before leaving")     # test by skipping "Pay" step and choose "Leave" instead

    def runGarage(self):
        while True:
            ans = input("What do you want to do? (GetTicket/Pay/Leave/Quit)")

            if ans == "GetTicket":
                Garage.GetTicket(self)
                pass
            
            elif ans == "Pay":
                Garage.payForParking(self)
                pass

            elif ans == "Leave":
                Garage.leaveGarage(self)
                pass

            elif ans == "Quit":
                print('Thanks for choosing us')
                break
        return

Parking = Garage()

Parking.runGarage()