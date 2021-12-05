import math
def getSol(n, en, dl, dur, p):
  #dp[t] = max profit at time t
  #for each time t' before t find max profit using unused events from t'.
  dp = [0 for i in range(1500)]
  used = [[] for i in range(1500)]
  for i in range(1,1500):
    for j in range(i):
      for k in range(n):
        if dur[k] <= i - j:
          if k not in used[j]:
            if(dp[j] + getProfit(p[k], i, dl[k]) > dp[i]):
              dp[i] = dp[j] + getProfit(p[k], i, dl[k])
              used[i] = [l for l in used[j]] + [k]
              #if i == 1421:
               # print(str(k) + " " + str(j) + " " + str(dp[j]) + " " + str(getProfit(p[k], i, dl[k])))
      if(dp[j] > dp[i]):
        dp[i] = dp[j]
        used[i] = [l for l in used[j]]
  ansp = 0
  ans = []
  for i in range(1441):
    if(ansp < dp[i]):
      ansp = dp[i]
      ans = used[i]
  for i in range(len(ans)):
    ans[i] += 1
  return ansp, ans
  #print(ansp)
  #print(ans)
  #print(dp[1421])
  #print(used[1421])

def getProfit(p,time, deadline):
  return p / (math.exp(0.0170 * (max(0, time - deadline))))
#print(getProfit(10, 5, 0))
#solve(2, [1,2], [5, 1420], [1,1420], [10,15])