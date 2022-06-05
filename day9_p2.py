import os
bids={} 
biding_finish=False
def fhbider(binding_record):
    highest_bid=0
    for bidder in binding_record:
        bid_amount=binding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f'the winner is ${winner} with a bid of ${highest_bid}')


while not biding_finish:
    name=input('What is your Name :')
    price=int(input('What is your bid: $'))
    bids[name]=price
    continue_input=input('Are there any other bidders! type Yes or No: ').lower()
    if continue_input=='no':
        biding_finish=True
        fhbider(bids)
    elif continue_input=='yes':
        os.system('cls')
    
