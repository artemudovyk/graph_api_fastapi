# from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List
    
    
# Graph Edge
class GraphEdgeBase(BaseModel):
    weight: int
    vertex1_id: int
    vertex2_id: int


class GraphEdgeCreate(GraphEdgeBase):
    pass


class GraphEdge(GraphEdgeBase):
    id: int 
    # vertices: List[GraphVertex] = []
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        
    
# Graph Vertex
class GraphVertexBase(BaseModel):
    graph_id: int


class GraphVertexCreate(GraphVertexBase):
    pass


class GraphVertex(GraphVertexBase):
    id: int
    # graph: Graph
    edges: List[GraphEdge] = []
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        

# Graph
class GraphBase(BaseModel):
    pass


class GraphCreate(GraphBase):
    pass


class Graph(GraphBase):
    id: int
    vertices: List[GraphVertex] = []
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True