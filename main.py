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
        is_dead = my_cat.train()
        if is_dead == "DEAD":
            break
        my_cat.show_stats()
        
    elif action == '2':
        is_dead = my_cat.feed()
        if is_dead == "DEAD":
            break
        my_cat.show_stats()
    elif action == '3':
        is_dead = my_cat.play()
        if is_dead == "DEAD":
            break
        my_cat.show_stats()
    elif action =='4':
        is_dead = my_cat.sleep()
        if is_dead == "DEAD":
            break
        my_cat.show_stats()
    
    
        