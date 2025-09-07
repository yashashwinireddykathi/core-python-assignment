def taxi():
    python_trips = [5, 10, 3]
    def fare():
        b=50
        t=0
        c=1
        for i in python_trips:
            a=b+i*10
            print(f"Trip {c}:${a}")
            t=t+a
            c=c+1
        print(f"Total Fare:${t}")
    fare()
taxi()