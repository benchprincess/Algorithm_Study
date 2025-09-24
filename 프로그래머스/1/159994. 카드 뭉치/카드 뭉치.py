def solution(cards1, cards2, goal):
    cards1_idx = 0
    cards2_idx = 0
    goal_count = 0

    while goal_count < len(goal):
        if cards1_idx < len(cards1) and goal[goal_count] == cards1[cards1_idx]:
            cards1_idx += 1
            goal_count += 1
        elif cards2_idx < len(cards2) and goal[goal_count] == cards2[cards2_idx]:
            cards2_idx += 1
            goal_count += 1
        else:
            return "No"

    return "Yes"