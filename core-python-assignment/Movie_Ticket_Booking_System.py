def movie_booking():
    total_seats = 10
    booked_seats = [2, 5, 7]
    def book(seat):
        if seat in booked_seats:
            print("Seat", seat, "is already booked")
        else:
            booked_seats.append(seat)
    def cancel(seat):
        if seat in booked_seats:
            booked_seats.remove(seat)
        else:
            print("Seat", seat, "is not booked")
    book(3)
    cancel(5)
    avail_seats=[]
    for i in range(1,total_seats+1):
        if i in booked_seats:
            exit
        else:
            avail_seats.append(i)
    print("Available seats:",avail_seats)
movie_booking()