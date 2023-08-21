from art import logo
from art import vs 
from game_data import data
import random

def format_data(account):
  """Format the account data into printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"
  
score = 0
print(logo)
game_should_continue = True
random_account_b = random.choice(data)

while game_should_continue:
  random_account_a = random_account_b
  random_account_b = random.choice(data)
  if random_account_a == random_account_b:
    random_account_b = random.choice(data)
  
  def check_answer(user_guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
      return user_guess == "a"
    else:
      return user_guess == "b"
  
  print(f"Compare A: {format_data(random_account_a)}")
  print(vs)
  print(f"Compare B: {format_data(random_account_b)}")
  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_follower_count = int(random_account_a["follower_count"])
  b_follower_count = int(random_account_b["follower_count"])
  
  is_correct = check_answer(user_guess, a_follower_count, b_follower_count)
  if is_correct:
    score += 1
    print(f"You are right! Your score {score}. ")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Your score {score}.")



  

