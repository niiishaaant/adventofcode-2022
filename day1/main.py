from utilities.fileinputoutput import readFile


def get_calories_per_elf(lst: str) -> list:
    return lst.split('\n\n')


def get_calories_carried_by_elf(calories_per_elf: list) -> int:
    return sum([int(calories) for calories in calories_per_elf.split('\n')])


def get_highest_calories_carried_by_elf(calories_per_elf: list) -> int:
    return max([get_calories_carried_by_elf(calories) for calories in calories_per_elf])


def get_sum_of_calories_carried_by_top_3_elves(calories_per_elf: list) -> int:
    return sum(sorted([get_calories_carried_by_elf(calories) for calories in calories_per_elf], reverse=True)[:3])


def runner():
    calories_per_elf = get_calories_per_elf(readFile('input.txt'))
    print(get_highest_calories_carried_by_elf(calories_per_elf))
    print(get_sum_of_calories_carried_by_top_3_elves(calories_per_elf))


if __name__ == '__main__':
    runner()
