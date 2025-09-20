def solution(nums):
    choices = len(nums) // 2
    set_choices = len(set(nums))

    if choices <= set_choices:
        return choices
    elif choices > set_choices:
        return set_choices