﻿def counter(start_at=0):
    count=[start_at]
    def incr():
        count[0]+=1
        return count[0]
    return incr

Ptr_incr=counter(5)
print(Ptr_incr())
