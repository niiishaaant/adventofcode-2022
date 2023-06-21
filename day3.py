from utils.fileio import read_file


def get_priority(ch: str) -> int:
    return ord(ch) - ord('a') + 1 if ch.islower() else ord(ch) - ord('A') + 27


def part_one(sacks: str) -> int:
    sum_of_prios = 0
    for sack in sacks.split():
        half = len(sack) // 2
        common = set(sack[half:]).intersection(sack[:half])
        sum_of_prios += get_priority(common.pop())
    return sum_of_prios


def part_two(sacks: str) -> int:
    sum_of_prios = 0
    sacks = sacks.split()
    for i in range(0, len(sacks), 3):
        common = set(sacks[i]) & set(sacks[i + 1]) & set(sacks[i + 2])
        sum_of_prios += get_priority(common.pop())
    return sum_of_prios


sacks = read_file('./dadady3.txt')

print(part_one(sacks))
print(part_two(sacks))
