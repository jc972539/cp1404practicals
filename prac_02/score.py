"""Output score"""

def main():
    """From users' input, prints result"""
    score = float(input("Enter score: "))
    return_result(score)
    print(return_result(score))

def return_result(score):
    """Calculate result"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()