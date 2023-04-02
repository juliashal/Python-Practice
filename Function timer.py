import time

def func_timer(fn,*args,rep=1,**kwargs):
    start=time.perf_counter()
    
    for i in range(rep):
        fn(*args, **kwargs)
    
    end = time.perf_counter()
    return (end-start)/rep

def avg(*args):
    return len(args) and sum(args)/len(args)


print(f"Function avg takes on average {func_timer(avg,1,2,6,10,12,15,rep=15)} minutes")