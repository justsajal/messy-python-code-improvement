"""Refactored version of a simple number statistics script."""


def parse_numbers(raw_text: str) -> list[int]:
    """Convert whitespace-separated values to integers."""
    numbers = []
    for item in raw_text.split():
        try:
            numbers.append(int(item))
        except ValueError:
            print(f"Skipping invalid value: {item!r}")
    return numbers


def display_statistics(numbers: list[int]) -> None:
    """Display the numbers, sum, and average."""
    if not numbers:
        print("No valid numbers were entered.")
        return

    total = sum(numbers)
    average = total / len(numbers)

    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")


def main() -> None:
    raw_text = input("Enter numbers separated by spaces: ")
    numbers = parse_numbers(raw_text)
    display_statistics(numbers)


if __name__ == "__main__":
    main()
