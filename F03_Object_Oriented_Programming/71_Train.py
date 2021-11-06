class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.customer = []
        self.bookedSeat = -1
    
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}.")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs.{self.fare} ")
    
    def bookTicket(self, customerName, customerAge, adhar, customerPhone):
        if(self.seats > 0):
            self.seats -= 1
            self.bookedSeat += 1
            self.customer.append({'Customer Name':customerName, 'Customer Age': customerAge, 'Adhar No.': adhar,'Customer Phone Number': customerPhone, 'Seat Number' : self.bookedSeat + 1})
            print("Seat Booked: ",self.customer[self.bookedSeat], ' fare = ', self.fare)
        else:
            print('Sorry this train is full! Kindly try in tatkal.')
    # def cancelTicket(self, seatNo):
    #     self.customer.remove()

intercity = Train("Intercity Express 14015", 90, 300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket('Ashmit Gupta', 19, '1234-5678-9987-6543','+91-8299538244')
intercity.getStatus()
# intercity.fareInfo()