from collections import defaultdict


def tally(tournament_results):
    data = defaultdict(list)
    team2_result_map = {"win": "loss", "loss": "win", "draw": "draw"}
    for row in tournament_results:
        team1, team2, team1_result = row.split(";")
        data[team1].append(team1_result)
        data[team2].append(team2_result_map[team1_result])

    results = []
    for team, results_team in data.items():
        result_line = [team, len(results_team), results_team.count("win"), results_team.count("draw"),
                       results_team.count("loss"), results_team.count("win") * 3 + results_team.count("draw")]
        results.append(result_line)

    results.sort(reverse=False, key=lambda x: x[0])  # by name
    results.sort(reverse=True, key=lambda x: x[5])  # by points
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for line_result in results:
        table.append('{: <30} | {: >2} | {: >2} | {: >2} | {: >2} | {: >2}'.format(*line_result))

    return table