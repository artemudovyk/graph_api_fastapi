from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from graphs import crud, models, schemas
from graphs.database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# GRAPHS
@app.get("/graphs/", response_model=List[schemas.Graph])
def get_graphs_list(db: Session = Depends(get_db)):
    return crud.get_all_graphs(db=db)


@app.get("/graphs/{graph_id}/", response_model=schemas.Graph)
def get_graph(graph_id: int, db: Session = Depends(get_db)):
    return crud.get_graph(db=db, graph_id=graph_id)


@app.post("/graphs/", response_model=schemas.Graph)
def create_graph(graph: schemas.GraphCreate, db: Session = Depends(get_db)):
    return crud.create_graph(db=db, graph=graph)


@app.delete("/graphs/{graph_id}/")
def delete_graph(graph_id: int, db: Session = Depends(get_db)):
    return crud.delete_graph(db=db, graph_id=graph_id)


# VERTICES
@app.post("/vertices/", response_model=schemas.GraphVertex)
def create_vertex(vertex: schemas.GraphVertexCreate, db: Session = Depends(get_db)):
    return crud.create_vertex(db=db, vertex=vertex)


@app.delete("/vertices/{vertex_id}/")
def delete_vertex(vertex_id: int, db: Session = Depends(get_db)):
    return crud.delete_vertex(db=db, vertex_id=vertex_id)


@app.get("/vertices/{vertex_id}/adjacent/", response_model=List[schemas.GraphVertex])
def get_adjacent_vertices(vertex_id: int, db: Session = Depends(get_db)):
    return crud.get_adjacent_vertices(db=db, vertex_id=vertex_id)


# Edges
@app.post("/edges/", response_model=schemas.GraphEdge)
def create_edge(edge: schemas.GraphEdgeCreate, db: Session = Depends(get_db)):
    # Check if vertices are from the same graph
    graph1 = crud.get_graph_by_vertex_id(db=db, vertex_id=edge.vertex1_id)
    graph2 = crud.get_graph_by_vertex_id(db=db, vertex_id=edge.vertex2_id)
    if graph1.id != graph2.id:
        raise HTTPException(status_code=404, detail=f'Submited vertices are from different graphs. vertex1={edge.vertex1_id} is from graph={graph1.id}, vertex2={edge.vertex2_id} is from graph={graph2.id}')
    else:
        return crud.create_edge(db=db, edge=edge)


@app.delete("/edges/{edge_id}/")
def delete_edge(edge_id: int, db: Session = Depends(get_db)):
    return crud.delete_edge(db=db, edge_id=edge_id)


# Algorithms
@app.get("/algos/dfs/graph/{graph_id}/vertex/{vertex_id}/", response_model=List[schemas.GraphVertex])
def algos_dfs(graph_id: int, vertex_id: int, db: Session = Depends(get_db)):
    graph = crud.get_graph(db=db, graph_id=graph_id)
    start_vertex = crud.get_vertex(db=db, vertex_id=vertex_id)
    
    # Check if vertex is in submited graph
    if start_vertex not in graph.vertices:
        raise HTTPException(status_code=404, detail=f'Submited vertex is from different graph. vertex={vertex_id} is from graph={start_vertex.graph_id}, but you submited graph={graph_id}')
    
    visited, stack = set(), [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            adjacent = set(crud.get_adjacent_vertices(db=db, vertex_id=vertex.id))
            stack.extend(adjacent - visited)
    
    return visited