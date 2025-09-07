def performance():
    students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
    def avg():
        s = sum(students["John"])/len(students["John"])
        a = sum(students["Alice"])/len(students["Alice"])
        b = sum(students["Bob"])/len(students["Bob"])
        averages = {"John": round(s, 2), "Alice": round(a, 2), "Bob": round(b, 2)}
        print("Average Marks:",averages)
        if s >= a and s >= b:
            top = "John"
        elif a >= s and a >= b:
            top = "Alice"
        else:
            top = "Bob"
        print("Top Performer:", top)
    avg()
performance()
