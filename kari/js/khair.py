print ("Hello world")

hrs = float(input("Enter Hours"))
rate = float(input("Enyer Rate:"))
pay= hrs*rateprint("Pay:",pay)

hrs = input("Enter Hours")
h = float(hrs)
rate = float(input("Enter Rate:"))
if h >40 :
    rate1 =(rate * 1.5)* (h-40)
    pay = ((h-5)*rate) + rate1
    print (pay)

    score = float(raw_input("Enter Score"))
    if (score>1.0):
        print("out of range")
        elif score >= 0.9:
            print ("A")
        elif score >= 0.8:
            print ("B")
        elif score >= 0.7:
            print ("C")
        elif score >= 0.6:
            print ("D")
        elif score <= 0.6:
            print ("F")