import random

num_flip=int(input("enter the number of times to flip a coin: "))

if num_flip<0:
   print("enter a postive integer:")
else:
   head=0
   tail=0

   for _ in range(num_flip):
      
      if random.random()<0.5:
         head=head+1
      else:
         tail=tail+1

head_percentage=(head/num_flip)*100
tail_percentage=(tail/num_flip)*100

print(f"head: {head_percentage}%")
print(f"tail: {tail_percentage}%")

