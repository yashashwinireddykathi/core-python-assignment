def feedback():
    python_ratings = [5, 4, 3, 5, 2, 4, 1, 5]
    def pos_feedback():
        c=0
        for i in python_ratings:
            if(i==4 or i==5):
                c=c+1
        if len(python_ratings) == 0:
            print("No ratings available")
        else:
            print("Positive Feedback:",round(((c/len(python_ratings))*100),1),"%")
    pos_feedback()
feedback()
