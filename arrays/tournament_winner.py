import time

def tournamentWinner(competitions, results):
    winners = {}
    start = time.time()
    for i,comp in enumerate(competitions):
        winner = comp[0] if results[i] == 1 else comp[1]
        if winner in list(winners.keys()):
            winners[winner] += 1
        else:
            winners[winner] = 1
    max_winner = max(winners, key = winners.get)
    end = time.time()
    return max_winner, end - start

def tournamentWinner2(competitions, results):
    winners = {}
    start = time.time()
    for i,comp in enumerate(competitions):
        winner = comp[0] if results[i] == 1 else comp[1]
        winners[winner] = winners.get(winner,0) + 1
    max_winner = max(winners, key = winners.get)
    end = time.time()
    return max_winner, end - start

if __name__ == "__main__":
    competitions = [
        ["HTML","C#"],
        ["C#","Python"],
        ["Python","HTML"]
    ]
    results = [0,0,1]
    winner, time1 = tournamentWinner(competitions, results)
    print(winner, time1)
    winner, time2 = tournamentWinner2(competitions, results)
    print(winner, time2)