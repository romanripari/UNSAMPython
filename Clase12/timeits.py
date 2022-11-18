# %%
import time
import timeit as tt
tt.timeit('time.sleep(1)',number = 1)
# PC Trabajo: 1.0104982
#             1.0028375999999994 
# Out[3]: 1.0010360410087742
# %%
tt.timeit('"-".join(str(n) for n in range(100))', number = 10000)
# 0.3746807000000001
# %%
tt.timeit('"-".join(str(n) for n in range(100))', number = 10000)
# %%
tt.timeit('"-".join([str(n) for n in range(100)])', number = 10000)
# %%
tt.timeit('"-".join(map(str, range(100)))', number = 10000)

# %%
