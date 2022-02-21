class Garage():

    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]       #list of tickets
        self.space = [1,2,3,4,5,6,7,8,9,10]         #list of space
        self.current = {}                           #dictionary for current ticket after a ticket is taken


    def GetTicket(self):
        if self.tickets:
            print(f'Your ticket number is {self.tickets[0]}')

            self.current[self.tickets[0]] = 'unpaid' #a dictionary holding a list of available tickets at index [0] which is 1 in the given list
            print(self.current)

            self.tickets.pop(0) #tickets reduce by 1 in list by using .pop() method, we're able to pull out a specific number in a given list

            self.space.pop(0) #space reduce by 1 in list
            
            print(f'Available Space After{self.space}') #available space after a ticket is given out


    
    def payForParking(self):
        payment= int(input('What is your ticket number ?'))

        if self.current.get(payment) == "unpaid":  #using .get() method to pull the user input of their ticket number 
            self.current[payment]= 'paid'          #When user choose option "Pay", it will change "unpaid" to "paid"

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
            

        elif self.current[payment] == "unpaid":
            print("Please pay before leaving")

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