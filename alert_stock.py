from yahoo_fin import stock_info
from playsound import playsound

company_name = input("Enter the name of company : ")
price = int(input("Enter the price i bought this : "))
quantity = int(input("Enter the quantity : "))
price_to_alert  = int(input("At which price i want alert : "))


while(True):
    current_price = stock_info.get_live_price(company_name)
    print("Current Profit : ", (current_price - price)*quantity)
    
    if(current_price <=price_to_alert):
        playsound("sound.mp3")
    



