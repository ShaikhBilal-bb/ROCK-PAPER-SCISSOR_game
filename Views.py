from django.shortcuts import render, redirect
import random

# Initialize points
def initialize_points():
    return {'user': 0, 'computer': 0}

# Determine winner of a round
def check_round(user_choice, comp_choice, points):
    if user_choice == comp_choice:
        return "Tie"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        points['user'] += 1
        return "User wins this round"
    else:
        points['computer'] += 1
        return "Computer wins this round"

# Determine the overall winner
def overall_winner(points):
    if points['user'] > points['computer']:
        return "User wins the game"
    elif points['user'] < points['computer']:
        return "Computer wins the game"
    else:
        return "It's a tie"

# Home page view
def home(request):
    if request.method == 'POST':
        user_choice = request.POST.get('choice')
        num_rounds = int(request.POST.get('rounds', 1))

        if 'points' not in request.session:
            request.session['points'] = initialize_points()
        points = request.session['points']

        results = []
        for _ in range(num_rounds):
            comp_choice = random.choice(["rock", "paper", "scissors"])
            result = check_round(user_choice, comp_choice, points)
            results.append(f"Computer chose: {comp_choice}, You chose: {user_choice} - {result}")

        request.session['points'] = points
        request.session['results'] = results
        return redirect('points')

    return render(request, 'game/home.html')

# Points page view
def points(request):
    points = request.session.get('points', initialize_points())
    results = request.session.get('results', [])
    winner = overall_winner(points)

    context = {
        'user_points': points['user'],
        'computer_points': points['computer'],
        'results': results,
        'final_winner': winner
    }

    if request.method == 'POST':
        request.session.flush()  # Reset session
        return redirect('home')

    return render(request, 'game/points.html', context)
