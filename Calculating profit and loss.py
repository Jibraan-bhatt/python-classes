#Selling price and Cost price
selling_p=int(input("Enter Selling price:"))
cost_p=int(input("Enter Cost price:"))
loss=cost_p-selling_p
profit=selling_p-cost_p

if(cost_p > selling_p) :
    print("You're at loss:(")
    print("loss percentage:", (loss/cost_p)*100, "%")
else :
    print("You're at profit!")
    print("profit percentage:", (profit/cost_p)*100,"%")