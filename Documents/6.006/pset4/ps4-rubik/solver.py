import rubik



twists = ( rubik.F, rubik.L, rubik.Fi, rubik.Li, rubik.U, rubik.Ui)
           
def adjacency(pos):
    adj_list = []
    for t in twists: 
        p = rubik.perm_apply(t, pos)
        adj_list.append(p)
    return adj_list

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    Assumes the rubik.quarter_twists move set.
    """
    
    blevel1 = {start:0}
    parent1 = {start: None}
     
    blevel2 = {end:0}
    parent2 = {end: None}
    i = 1
    


    while frontier1 != frontier2:
    
        frontier1 = [start]
        frontier2 = [end]

        while frontier1 and frontier2:
        
            fnext = []
            fnext2 = []
            
        
            #print frontier

        
            for u in xrange(len(frontier1)):
                Adj = adjacency(frontier1[u])
                Adj2 = adjacency(frontier2[u])
                #print Adj
                for v in xrange(len(Adj)):
                
                    if Adj[v] not in blevel or Adj2[v] not in blevel2:
                        blevel1[Adj[v]] = i
                        parent1[Adj[v]] = frontier1[u]
                        blevel2[Adj2[v]] = i
                        parent2[Adj2[v]] = frontier2[u]
                        
                        fnext.append(Adj[v])
                        fnext2.append(Adj2[v])

        
            frontier1 = fnext
            frontier2 = fnext2
            i += 1

    for f in fnext2:
        fnext.append(f)
        
    return fnext
    
  
