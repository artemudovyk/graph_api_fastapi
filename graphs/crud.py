from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas

# GRAPHS
def get_graph(db: Session, graph_id: int):
    return db.query(models.Graph).get(graph_id)


def get_graph_by_vertex_id(db: Session, vertex_id: int):
    vertex = db.query(models.GraphVertex).get(vertex_id)
    if not vertex:
        raise HTTPException(status_code=404, detail=f'Vertex id={vertex_id} not found')
    graph = db.query(models.Graph).get(vertex.graph_id)
    return graph


def get_all_graphs(db: Session):
    return db.query(models.Graph).all()


def create_graph(db: Session, graph: schemas.GraphCreate):
    db_graph = models.Graph(**graph.dict())
    db.add(db_graph)
    db.commit()
    db.refresh(db_graph)
    return db_graph


def delete_graph(db: Session, graph_id: int):
    db_graph = db.query(models.Graph).get(graph_id)
    if not db_graph:
        raise HTTPException(status_code=404, detail=f'Graph id={graph_id} not found')
    db.delete(db_graph)
    db.commit()
    return { 'ok': True }


# VERTICES
def get_vertex(db: Session, vertex_id: int):
    return db.query(models.GraphVertex).get(vertex_id)


def create_vertex(db: Session, vertex: schemas.GraphVertexCreate):
    db_vertex = models.GraphVertex(**vertex.dict())
    db.add(db_vertex)
    db.commit()
    db.refresh(db_vertex)
    return db_vertex


def delete_vertex(db: Session, vertex_id: int):
    db_vertex = db.query(models.GraphVertex).get(vertex_id)
    if not db_vertex:
        raise HTTPException(status_code=404, detail=f'Vertex id={vertex_id} not found')
    db.delete(db_vertex)
    db.commit()
    return { 'ok': True }


def get_adjacent_vertices(db: Session, vertex_id: int):
    vertex = db.query(models.GraphVertex).get(vertex_id)

    adjacent_vertices = []
    for edge in vertex.edges:
        if edge.vertex1_id != vertex.id:
            vertex1 = db.query(models.GraphVertex).get(edge.vertex1_id)
            adjacent_vertices.append(vertex1)
        else:
            vertex2 = db.query(models.GraphVertex).get(edge.vertex2_id)
            adjacent_vertices.append(vertex2)
            
    return adjacent_vertices


# EDGES
def create_edge(db: Session, edge: schemas.GraphEdgeCreate):
    db_edge = models.GraphEdge(**edge.dict())
    db.add(db_edge)
    db.commit()
    db.refresh(db_edge)
    return db_edge


def delete_edge(db: Session, edge_id: int):
    db_edge = db.query(models.GraphEdge).get(edge_id)
    if not db_edge:
        raise HTTPException(status_code=404, detail=f'Edge id={edge_id} not found')
    db.delete(db_edge)
    db.commit()
    return { 'ok': True }