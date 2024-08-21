
from secretauctionprograme_art import logo

# Ask the name and price

# Need to save the data into a dictionary {name: price}

# Anyone else want to bid also? Add to dictionary -> otherwise...
    
# ... Compare bids and find highest price

print(logo)

bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}!")

while continue_bidding:
    name = input("What is your name? \n")
    price = int(input("What is your bid? In $. \n"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)
        

