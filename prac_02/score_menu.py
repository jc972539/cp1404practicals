"""Give score result based on users' input"""

def main():
    """Start menu program"""
    print("(G)et\n(P)rint\n(S)how\n(Q)uit")
    choice = input(">>> ")
    menu(choice, score)

    #TODO (I believe the error is in relation to the fact that the program requires the user to input "G" first but it's not certain)

def user_score():
    """Get score from user"""
    score = float(input("Enter score: "))
    return score

def return_result(score):
    """Calculates the result from score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def menu(choice, score):
    """Run menu selection"""
    while choice != "Q":
        if choice == "G":
            user_score()
        elif choice == "P":
            return_result(score)
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print("(G)et\n(P)rint\n(S)how\n(Q)uit")
        choice = input(">>> ")
    print("Goodbye.")

main()