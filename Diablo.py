def min_gold_to_pass_level(m, d, k, c):
    monsters_left = m
    durability = d
    repairs_needed = 0

    while monsters_left > 0:
        if durability <= k and monsters_left > 1:
            repairs_needed += c 
            durability = d
        else:
            monsters_left -= 1
            durability -= k

    return repairs_needed

def main():
    input_data = list(map(int, input().split()))

    m, d, k, c = input_data

    result = min_gold_to_pass_level(m, d, k, c)
    print(result)

if __name__ == "__main__":
    main()
