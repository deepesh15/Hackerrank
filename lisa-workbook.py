n,k = map(int,input().split())
arr = list(map(int,input().split()))
page_count =1
special_count =0
for i in range(len(arr)):
    num_of_problems = arr[i]
    num_of_full_pages,leftover_probs = divmod(num_of_problems,k)
    total_pages = num_of_full_pages+(1 if leftover_probs else 0)
    probs_in_chap = iter(range(1,arr[i]+1))

    for _ in range(total_pages):
        probs_on_page = [next(probs_in_chap,None)for _ in range(k)]
        if page_count in probs_on_page:
            special_count+=1
        page_count+=1
print(special_count)