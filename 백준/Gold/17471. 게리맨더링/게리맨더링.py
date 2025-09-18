from collections import deque
N = int(input())
people = list(map(int,input().split(" ")))
connected = [[False]*N for _ in range(N)]
for i in range(N):
    temp = list(map(int,input().split(" ")))
    for j in range(1,len(temp)):
        connected[i][temp[j]-1]=True
selected = [False]*N

#result = 999999
def subSet(cur):
    if (cur==N):
        groupA=[]
        groupB=[]
        for i in range(N):
            if(selected[i]):
                groupA.append(i)
            else:
                groupB.append(i)
        if(len(groupA)==0 or len(groupB)==0): return
        global visited
        visited= [False]*N
        bfs(groupA)
        countA=0
        for i in groupA:
            if visited[i]==False: return
            countA+=people[i]
        visited= [False]*N
        bfs(groupB)
        countB=0
        for i in groupB:
            if visited[i]==False: return
            countB+=people[i]
        result.append(abs(countA-countB))
        #result = min(result,abs(countA-countB))
        return
       
    selected[cur]=True
    subSet(cur+1)
    selected[cur]=False
    subSet(cur+1)
def bfs(group):
    queue = deque()
    queue.append(group[0])
    visited[group[0]]=True
    while(queue):
        start = queue.popleft()
        for i in group:
            if(visited[i]==True): continue
            if(connected[start][i]==True):
                visited[i]=True
                queue.append(i)
    return
result = []
subSet(0)
if(len(result)==0):
    result.append(-1)
print(min(result))