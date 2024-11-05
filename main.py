from cat import Cat

print('welcome to my cat game')

name = input('enter cat name')
colour = input('enter colour')
my_cat=Cat(name,colour)
while True:
    action = input("""
what would you like to do
1. train
2.feed
3.play
4.sleep
""")
    if action == '1':
        my_cat.train()
    elif action == '2':
        my_cat.feed()
    elif action == '3':
        my_cat.play()
    elif action =='4':
        my_cat.sleep()
    
        