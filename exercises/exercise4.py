"""
    Get first, second best scores from the list.
    List may contain duplicates.
    Ex: [86,86,85,85,85,83,23,45,84,1,2,0] => should get 86, 85
"""

scores = [15,65,89,156,894,464,686,568,1231,894,510.5,546]

sorted_scores = sorted(scores,reverse=True)

print('The top 2 scores are ', sorted_scores[0],sorted_scores[1])