import rubik

twists = ( rubik.F, rubik.L, rubik.Fi, rubik.Li, rubik.U, rubik.Ui, rubik.perm_apply(rubik.F, rubik.F),
           rubik.perm_apply(rubik.L, rubik.L), rubik.perm_apply(rubik.U, rubik.U) )

def adjacency(pos):
    adj_list = []
    for t in twists: 
        p = rubik.perm_apply(t, pos)
        adj_list.append(p)
    return adj_list
    
    

def positions_at_level(level):
    """
    Using BFS, returns the number of cube configurations that are
    exactly a given number of levels away from the starting position
    (rubik.I), using the rubik.quarter_twists move set.
    """
    
    
    if level == 0:
        return i
    
    blevel = {rubik.I:0}
    parent = {rubik.I: None}
    i = 1

    frontier = [rubik.I]
   
    while frontier and i<= level:
        
        fnext = []
        #print frontier

        
        for u in frontier:
            Adj = adjacency(u)
            #print Adj
            for v in Adj:
                
                if v not in blevel:
                    blevel[v] = i
                    parent[v] = u
                    fnext.append(v)

        frontier = fnext
        i += 1
    
    return len(fnext)

    
