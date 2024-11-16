# ASCII art logo for the program
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | |  ''-.
                          |       |_| |_             _| |_ ..-'
                          |_______| '-' `'---------'` '-'
                 *  *     )"""""""(      *  *  
                  \  \   /_________\    /  /  
                   \  \.-------------. /  /  
                    \ /_______________\  /
'''

def find_highest_bidder(bidders):
    """Find and display the highest bidder."""
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

def main():
    """Main function to run the blind bidding program."""
    print(logo)
    print("Welcome to the secret auction program!")
    bidders = {}
    while True:
        # Get bidder's name and bid amount
        name = input("What is your name? : ")
        bid = int(input("What is your bid? : $ "))

        # Add the bidder's details to the dictionary
        bidders[name] = bid

        # Check if there are more bidders
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if more_bidders == "yes":
            print("\n" * 50)  # Clear the screen
        elif more_bidders == "no":
            break

    # Find and announce the winner
    find_highest_bidder(bidders)

if __name__ == "__main__":
    main()
