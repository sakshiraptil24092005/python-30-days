bill = float(input("enter total bill :"))
tip_percentage = float(input("enter tip percentage:"))
people = int(input("total number of people:"))
tip = tip_percentage/100
bill = bill+tip
share = bill/ people
print("TIP AMOUNT:",tip,)
print("TOTAL BILL:",bill)
print("EACH PERSON PAY:",share)
