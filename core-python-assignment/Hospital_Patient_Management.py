def hospital():
    patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
    ]
    def search():
        a=[]
        search_disease = "Flu"
        for i in patients:
            if i["Disease"]==search_disease:
                a.append(i["Name"])
        print("Patients with Flu:",a)
    search()
hospital()
    