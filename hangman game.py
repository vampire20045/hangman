import random
stage=['''
 +-----+
  |    |
  0    |
/ | \  |
 /  \  |
========''','''
  +-----+
  |     |
  0     |
/ | \   |
 /      |
========''','''
  +-----+
  |     |
  0     |
/ | \   |
        |
=========''','''
  +-----+
  |     |
  0     |
/ |     |
        |
=========''','''
   +-----+
   |     |
   0     |
  /      |
         |
==========  ''','''
  +-----+
  |     |
  0     |
        |
        |
==========''','''
  +------+
  |      |
         |
         |
         |
==========''']
lives=6 # no of lives a user have
print("Hint: all furits name")
word=["apple","orange","grapes","banana","pineapple","guava","lichi","strawberry","pomegranate"]
p=random.choice(word)
k=len(p)
display=[]

str=""
for j in range(1,k+1):
    display=display+["_"]
print(display)
"""use a while loop to let the user guess again the loop should only stop once the user has guessed all the letters in the chosen word and display has no more blacks then you can tell the user they have won"""
end_of_game=False
while not end_of_game:
    n=input("enter your choice").lower()

    for  position in range(len(p)):

        letter=p[position]
        if  letter==n:
            display[position]=letter
    if n not in p:
        lives-=1
        if lives==0:
            end_of_game=True
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("you win")
    print(stage[lives])
        
        

    
        
        
    

