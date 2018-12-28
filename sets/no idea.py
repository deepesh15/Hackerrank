if __name__ == '__main__':
    happiness =0
    n,m = (input().split())
    arr = set(input().split())
    st1 = set((input().split()))        #this is the one which i like
    st2 = set((input().split()))        #this is the one which i dislike
    like = set(st1 & arr)
    dislike = set(st2 & arr)
    happiness = len(like) - len(dislike)
    print(str(happiness))

