from abc import ABC, abstractmethod
from Matrix import Matrix

class IWeightedGraph(ABC): # Interface for a Weighted Graph
    __slots__ = (
        "_directional" # Protected readonly interface element
    )

    def __init__(self, directional):
        self._directional = directional # Determines if the graph has directional edges or not

    @abstractmethod
    def add_vertex(self, links: dict) -> int:
        """ Adds a vertex to the graph, using the `links` dict (with key:vertex_index, value:link_weight), returns the index (name) of the vertex """
        pass
    
    @abstractmethod
    def get_vertex(self, index: int) -> dict:
        """ Returns a `links` dict (with key:vertex_index, value:link_weight) from the index (name) of the vertex you want to get """
        pass

    @abstractmethod
    def set_vertex(self, index: int, links: dict):
        """ Sets the vertex `index` edges using the `links` dict (with key:vertex_index, value:link_weight) """
        pass

    @abstractmethod
    def get_matrix(self) -> Matrix:
        """ Returns an adjacency matrix representing the current graph """
        pass
