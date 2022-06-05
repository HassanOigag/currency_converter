import requests
import json
def get_rates(url):
    response = requests.get(url)
    if response:
        return json.loads(response.text)
    return None

def calculate_total(amount, rate, desired_currency):
    total = amount * rate
    print(f"You received {total} {desired_currency.upper()}.")

def get_currency_code():
    return input().strip().lower()
    
if __name__ == "__main__":
    current_currency = get_currency_code()
    if current_currency == "":
        print("empy!!!")
        exit()
    url = f"https://www.floatrates.com/daily/{current_currency}.json"
    data = get_rates(url)
    if data == None:
        print("currency does not exist")
        exit()
    cache = {}
    while True:
        desired_currency = get_currency_code()
        if desired_currency == "":
            break
        try:
            amount = float(input())
        except ValueError:
            break
        print("Checking the chache...")
        if desired_currency in cache:
            print("Oh! It is in the cache!")
            calculate_total(amount, cache[desired_currency], desired_currency)
        else:
            print("Sorry, but it is not in the cache!")
            data = get_rates(url)
            cache[desired_currency] = data[desired_currency]['rate']
            calculate_total(amount, cache[desired_currency], desired_currency)
            
