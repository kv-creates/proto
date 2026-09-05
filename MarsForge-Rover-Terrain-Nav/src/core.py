import math, heapq
def slope_cost(elev, x1,y1,x2,y2):
    dz=abs(elev[y2][x2]-elev[y1][x1])
    dist=math.hypot(x2-x1,y2-y1)
    slope=dz/max(0.1,dist)
    return slope*5 + dist
def astar(elev, start, goal):
    # elev 2D list
    open=[(0,start)]
    came={start:None}
    g={start:0}
    while open:
        _,cur=heapq.heappop(open)
        if cur==goal: break
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nxt=(cur[0]+dx,cur[1]+dy)
            if 0<=nxt[0]<len(elev[0]) and 0<=nxt[1]<len(elev):
                cost=g[cur]+slope_cost(elev,cur[0],cur[1],nxt[0],nxt[1])
                if nxt not in g or cost<g[nxt]:
                    g[nxt]=cost
                    f=cost+math.hypot(goal[0]-nxt[0],goal[1]-nxt[1])
                    heapq.heappush(open,(f,nxt))
                    came[nxt]=cur
    # reconstruct
    if goal not in came: return None
    path=[]; cur=goal
    while cur:
        path.append(cur); cur=came[cur]
    return list(reversed(path))