import os
import csv
from django.shortcuts import render
from django.conf import settings

def search_player(request):
    query = request.GET.get('query', '').strip().lower()
    players = []
    grades = set()

    # Absolute path to the CSV file
    csv_path = os.path.join(settings.BASE_DIR, 'players/players.csv')

    # Load players from CSV
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Normalize player data
            player = {key: value.strip() for key, value in row.items()}
            player['Grade'] = player['Grade'].upper()
            players.append(player)
            grades.add(player['Grade'])

    result = []

    if query:
        # Check for both Grade and ID in the query
        for player in players:
            grade_id = f"{player['Grade'].lower()}{player['Id']}"
            if query == grade_id or query in player['Name'].lower():
                result.append(player)

    # Sort grades for display
    grades = sorted(grades)

    # Debugging output
    print(f"Query: {query}")
    print(f"Players Loaded: {players}")
    print(f"Resulting Players: {result}")

    return render(request, 'players/search.html', {'players': result, 'grades': grades, 'query': query})
