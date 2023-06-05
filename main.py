print("\t\t\t____Welcome the the Auction____\n")


import max_bid

name=input("What is your name? : ")
bid=input("What's your bid? : $")

bidder_list=[{
        "name": name,
        "bid": bid,
    }]

def newBidder(newName, newBid):
    new_bidder={}
    new_bidder["name"]=newName
    new_bidder["bid"]=newBid
    bidder_list.append(new_bidder)

#[{'name': 'ravi', 'bid': '23'}, {'name': 'soni', 'bid': '15'}, {'name': 'raf', 'bid': '35'}]    


end_of_loop = False

while not end_of_loop:
    answer=input("\nAre there any other bidders? yes or no : ")
    if answer == "yes":
        newName=input("\nWhat is your name? : ")
        newBid=input("What's your bid? : $")
        newBidder(newName, newBid)
    else:
        end_of_loop = True
 
highest_bid, highest_bidder = max_bid.max_bid(bidder_list)

print("\t\n\n -- Let's find out what's the highest Bid and highest_bidder --\n")
print(f" who's the highest Bidder : {highest_bidder} \n")
print(f" what's the highest Bid   : ${highest_bid} \n ")
print("-- Thank you so much for using our Auction App -- \n ---- We are closing the program ---- ")

