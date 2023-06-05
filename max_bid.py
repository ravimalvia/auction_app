def max_bid(bidder_list):
    maximum_bid=0
    for i in range(len(bidder_list)):
                if int(bidder_list[i]["bid"])>=maximum_bid:
                    maximum_bid=int(bidder_list[i]["bid"]) 
                    highest_bidder=bidder_list[i]["name"]   
                else:
                    pass
    return maximum_bid, highest_bidder