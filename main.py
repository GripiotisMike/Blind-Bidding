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

x = True
while x:
  print (logo)
  bidders = {}
  name = input("Welcome to the secret auction programm! \n What is your name? : ")
  bid = int(input ("What is your bid? : $ "))
  bidders[name] = bid
  k = input ("Are there any other bidders? \n Type 'yes' or 'no': ")
  if k == "yes":
    print ("\n" * 100)
  elif k == "no":
    x = False
    pointer = ""
    max = 0
    for i in bidders:
      if bidders[i] > max:
        pointer = i
        max = bidders[i]
    print (f"The winner is {pointer} with a bid of ${max}")
