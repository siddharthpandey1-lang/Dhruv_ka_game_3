import random

def toss():
    print("Toss Time!")
    user_call = input("Choose Heads or Tails (H/T): ").strip().upper()
    toss_result = random.choice(['H', 'T'])
    print(f"Toss result: {'Heads' if toss_result == 'H' else 'Tails'}")
    if user_call == toss_result:
        print("You won the toss!")
        choice = input("Bat or Bowl first? (bat/bowl): ").strip().lower()
        return 'user', choice
    else:
        print("Computer won the toss!")
        comp_choice = random.choice(['bat', 'bowl'])
        print(f"Computer chooses to {comp_choice} first.")
        return 'comp', comp_choice

def play_innings(batting, balls=6):
    runs = 0
    wickets = 0
    for ball in range(1, balls+1):
        if batting == 'user':
            user_run = int(input(f"Ball {ball}: Enter your run (1-50): "))
            comp_bowl = random.randint(1,50)
            print(f"Computer bowled: {comp_bowl}")
            if user_run == comp_bowl:
                print("Out!")
                wickets += 3
                break
            else:
                runs += user_run
        else:
            comp_run = random.randint(1,6)
            user_bowl = int(input(f"Ball {ball}: Enter your bowl (1-6): "))
            print(f"Computer played: {comp_run}")
            if comp_run == user_bowl:
                print("You got the wicket!")
                wickets += 3
                break
            else:
                runs += comp_run
    print(f"Innings over! Runs: {runs}, Wickets: {wickets}")
    return runs

def cricket_game():
    print("Welcome to Simple Cricket Game!")
    toss_winner, choice = toss()
    if (toss_winner == 'user' and choice == 'bat') or (toss_winner == 'comp' and choice == 'bowl'):
        print("You are batting first.")
        user_score = play_innings('user')
        print("Computer is batting now. Target:", user_score+1)
        comp_score = play_innings('comp')
    else:
        print("Computer is batting first.")
        comp_score = play_innings('comp')
        print("You are batting now. Target:", comp_score+1)
        user_score = play_innings('user')
    print(f"Final Scores - You: {user_score}, Computer: {comp_score}")
    if user_score > comp_score:
        print("Congratulations! You win!")
    elif user_score < comp_score:
        print("Computer wins! Better luck next time.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    cricket_game()