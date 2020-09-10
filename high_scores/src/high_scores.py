def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    sorted_scores = scores[:]
    sorted_scores.sort(reverse = True)
    return sorted_scores[:3]
