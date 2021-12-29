from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Graph(Base):
    __tablename__ = 'graphs'
    
    id = Column(Integer, primary_key=True, index=True)
    vertices = relationship('GraphVertex', back_populates='graph', cascade='all, delete-orphan')


class GraphVertex(Base):
    __tablename__ = 'vertices'
    
    id = Column(Integer, primary_key=True, index=True)
    graph_id = Column(Integer, ForeignKey('graphs.id'))
    graph = relationship('Graph', back_populates='vertices')
    edges = relationship('GraphEdge', cascade='all, delete-orphan', primaryjoin='or_(GraphVertex.id == GraphEdge.vertex1_id, GraphVertex.id == GraphEdge.vertex2_id)')
    
    
class GraphEdge(Base):
    __tablename__ = 'edges'
    
    id = Column(Integer, primary_key=True, index=True)
    weight = Column(Integer, index=True)
    vertex1_id = Column(Integer, ForeignKey('vertices.id'))
    vertex2_id = Column(Integer, ForeignKey('vertices.id'))
    # vertices = relationship('GraphVertex', back_populates='edges', foreign_keys=[vertex1_id, vertex2_id])
    