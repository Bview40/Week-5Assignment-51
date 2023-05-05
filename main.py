stocks_dict = {
"AMZN" : "1750.00" ,
"TSLA" : "77.50" ,
"AAPL" : "85.65" ,
"MSFT" : "250.00" ,
"APLE" : "750.00" ,
"MO" : "50.50" ,
"AMC" : "25.15" ,
"UNH" : "65.00" ,
"META" : "28.75" , 
"ROKU" : "15.25" ,
}
x = input("Please enter your stock symbol: ")
#z = stocks_dict[x]
#print (z)
z = stocks_dict.get(x, "That ticker symbol was NOT found!")
print (z)
