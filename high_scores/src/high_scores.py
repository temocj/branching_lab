def latest(scores):
    return scores[:].pop()


def personal_best(scores):
    sorted_scores = scores[:]
    sorted_scores.sort()
    return sorted_scores[-1]

def personal_top_three(scores):
    sorted_scores = scores[:]
    sorted_scores.sort()
    sorted_scores.reverse()
    return sorted_scores[:3]
