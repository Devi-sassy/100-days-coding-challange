if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Convert map to list and remove duplicates
    scores = list(set(arr))

    # Sort the scores
    scores.sort()

    # Print the runner-up score
    print(scores[-2])