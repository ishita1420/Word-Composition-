import time
def readingword(fn):
    with open(fn, 'r') as file:
        wrd = file.read().splitlines()
    return wrd
def findwords(fn):
    wrd=readingword(fn)
    w_set = set(wrd)
    wrd.sort(key=len, reverse=True)
    start = time.time()
    def comp(w):
        if not w:
            return False
        for i in range(1, len(w)):
            if w[:i] in w_set and (w[i:] in w_set or comp(w[i:])):
                return True
        return False
    l = ""
    sl = ""
    for w in wrd:
        if comp(w):
            if len(w) > len(l):
                sl = l
                l = w
            elif len(w) > len(sl):
                sl = w
    end= time.time()
    overall_time = (end - start) * 1000
    print(f"Longest Compound Word: {l}")
    print(f"Second Longest Compound Word: {sl}")
    print(f"Time taken to process file Input_02.txt: {overall_time:.2f} milliseconds")
findwords(r"C:\Users\Ishita Nigam\Downloads\Input_02.txt")
