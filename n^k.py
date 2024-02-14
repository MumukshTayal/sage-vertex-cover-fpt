# if G has no edges then return true
# if k=0 then return false
# let uw be some edge of G
# if VertexCoverFPT(G-u, k-1) then return true
# if VertexCoverFPT(G-w, k-1) then return true
# return false

def VertexCoverFPT(G, k):
  if noExistingEdges(G):
    return True
  if k == 0:
    return False
  for u in G:
    # print(u,k)
    if VertexCoverFPT(removeVertex(G,u), k-1):
      return True
  return False

def noExistingEdges(G):
  for vertex in G:
    if len(G[vertex]) != 0:
      return False
  return True

def removeVertex(G, u):
  copy = G.copy()
  del copy[u]
  
  for vertex in copy:
    if u in copy[vertex]:
      copy[vertex] = copy[vertex] - {u}
  # print(copy)
  return copy

Graph = {1:{2,4},2:{1,3,4,5},3:{2,4},4:{1,2,3,5},5:{2,4,6},6:{5}}
if VertexCoverFPT(Graph, 3):
  print("Satisfied")
else:
  print("Need bigger k")
