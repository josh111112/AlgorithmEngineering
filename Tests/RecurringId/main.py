def main():
    num_ids = int(input())
    dicty = dict()
    for _ in range(num_ids):
        currkey = int(input())
        if currkey not in dicty:
            dicty[currkey] = 1
        else:
            dicty[currkey] += 1
    sorted_dict = dict(sorted(dicty.items()))
    max_key = max(sorted_dict, key=sorted_dict.get)
    print(max_key)
if __name__ == "__main__":
    main()