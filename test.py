def check_winner(grid):
    x_count = sum(row.count("X") for row in grid)
    if x_count % 2 == 1:
        return "Bob"
    else:
        return "Alice"


def main():
    N = int(input())  # Number of games

    for game in range(1, N + 1):
        grid = [input() for _ in range(3)]
        winner = check_winner(grid)
        print(f"Game #{game}: {winner}")


if __name__ == "__main__":
    main()
