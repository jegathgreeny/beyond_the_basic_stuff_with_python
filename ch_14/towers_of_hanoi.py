import sys

TOTAL_DISKS = 5

# Start with all disks on Tower A.
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    """The tower dictionary has keys "A", "B", and "C" and values
    that are lists representing a tower of disks. The list contains
    integers representing disks of different sizes, and the start of
    the list is the bottom of the tower. For a game with 5 disks,
    the list [5, 4, 3, 2, 1] represents a completed tower. The blank
    list [] represents a tower of no disks. The list [1, 3] has a
    larger disk on top of a smaller disk and is an invalid
    configuration. The list [3, 1] is allowed since smaller disks
    can go on top of larger ones."""

    towers = {"A": SOLVED_TOWER[:], "B": [], "C": []}

    # Keeps track of the number of moves used.
    total_moves = 0

    # Runs a single turn on each iteration of this loop.
    while True:

        # Increments for each move.
        total_moves += 1

        # Display the towers and disks.
        display_towers(towers)
        # Ask for user to move.
        from_tower, to_tower = get_player_move(towers)

        # Move the top disk from  from_tower to to_tower.
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        # Check if user have solved the puzzle.
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            # Display the towers one last time.
            display_towers(towers)
            print("You have solved the puzzle!")
            print(f"In {total_moves} moves.")
            print("You win!\n")
            if total_moves > 31:
                print("The minimum moves to finish the game is 31.")
            else:
                print("You finished the game within the minimum number of moves.")
            sys.exit()


def display_towers(towers):
    """Display the three towers with their disks."""
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)
            else:
                display_disk(tower[level])

        print()
    # Display the tower labels A, B and C.
    space = " " * TOTAL_DISKS
    print(f"{space} A{space}{space} B{space}{space} C\n")


def display_disk(width):
    """Displays a disk of the given width. A width of 0 means no disk."""
    space = " " * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk.
        print(f"{space}||{space}", end="")
    else:
        # Display the disk.
        disk = "@" * width
        label = str(width).rjust(2, "_")
        print(f"{space}{disk}{label}{disk}{space}", end="")


def get_player_move(towers):
    """Asks the player for a move. Returns (from_tower, to_tower)."""

    # Keep asking until the move is valid.
    while True:
        print("Enter the letters of 'from' and 'to' towers, or quit.")
        print("(e.g., AB to move a disk from tower A to tower B.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        # Make sure the user entered valid tower letters.
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of AB, AC, BA, BC, CA or CB")
            # Ask player again for their move.
            continue

        from_tower, to_tower = response[0], response[1]
        # The "from" tower can't be an empty tower.
        if len(towers[from_tower]) == 0:
            print("You selected a tower with no disks.")
            # Ask the player again for their move.
            continue

        # Any disk can be moved onto a empty "to" string
        elif len(towers[to_tower]) == 0:
            return from_tower, to_tower

        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            # Ask the player again for their move.
            continue

        else:
            return from_tower, to_tower


if __name__ == "__main__":
    main()
