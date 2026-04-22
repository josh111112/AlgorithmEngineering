def main():
    try:
        n = int(input())
        gene_ids = list(map(int, input().split()))

    except (EOFError, ValueError) as e:
        print(f"Error reading input: {e}")
    
    sorted_genes = sorted(gene_ids)
    out_of_order = set()
    
    for i in range(n):
        if gene_ids[i] != sorted_genes[i]:
            out_of_order.add(i)
    
    if len(out_of_order) >= 2:
        start = min(out_of_order) + 1
        end = max(out_of_order) + 1
        
        s_idx = start - 1
        e_idx = end - 1
        
        if len(out_of_order) == 2:
            test_arr = list(gene_ids)
            test_arr[s_idx], test_arr[e_idx] = test_arr[e_idx], test_arr[s_idx]
            
            if test_arr == sorted_genes:
                print("yes")
                print("swap", start, end)
            else:
                print("no")
        else:
            test_arr = list(gene_ids)
            
            left = s_idx
            right = e_idx
            while left < right:
                test_arr[left], test_arr[right] = test_arr[right], test_arr[left]
                left += 1
                right -= 1
            
            if test_arr == sorted_genes:
                print("yes")
                print("reverse", start, end)
            else:
                print("no")
    else:
        print("yes")

if __name__ == "__main__":
    main()