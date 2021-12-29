# graph_api_fastapi

Small API (Python+FastAPI) that allows you to manage graph structures + get the results of DFS algorithm.

You can create graph, add vertices and edges. Checks if we are editing correct vertices that are part of the active graph are in place, e.g.:
```python
if start_vertex not in graph.vertices:
        raise HTTPException(status_code=404, detail=f'Submited vertex is from different graph. vertex={vertex_id} is from graph={start_vertex.graph_id}, but you submited graph={graph_id}')
```

## How to install
To start application with Docker:
```
$ git clone https://github.com/artemudovyk/graph_api_fastapi
$ cd graph_api_fastapi
$ docker-compose build
$ docker-compose up -d
```
Open website on http://localhost:8000/. 

API docs can be accessed at http://localhost:8000/docs or http://localhost:8000/redoc.

![image](https://user-images.githubusercontent.com/58283675/147695953-51514b23-69d2-45d9-be6d-6ed96cb14820.png)


## Examples
Get all graphs
![image](https://user-images.githubusercontent.com/58283675/147693631-eee126fc-9b18-48ee-980b-073e6c623c3f.png)

Create new graph
![image](https://user-images.githubusercontent.com/58283675/147696496-5148dac3-2f1c-4f9d-a225-319a56c01793.png)

Create new vertex
![image](https://user-images.githubusercontent.com/58283675/147696484-d92c75b8-73c6-4a49-acab-45eb8197be3c.png)

Create new edge
![image](https://user-images.githubusercontent.com/58283675/147696469-e1839695-d185-42bb-a5f3-714bdcb0c878.png)

Delete graph
![image](https://user-images.githubusercontent.com/58283675/147696520-243490c8-e955-4489-92af-6467d44fdc8b.png)


DFS (Depth-First Search) Algorithm for graph id=4 and with starting point in vertex id=1
![image](https://user-images.githubusercontent.com/58283675/147693711-1c7e3e05-9999-41e0-9f06-c11336a9a735.png)


## Task description:

Create small **API** (not an app with UI) that allows you to manage graph structures.

### Requirements🤓:

- ✅endpoint to create empty graph
- ✅endpoint to add vertex to graph
- ✅endpoint to remove vertex from graph
- ✅endpoint to add edge to graph
- ✅endpoint to remove edge from graph
- ✅endpoint to get graph
- ✅endpoint to get all graphs
- ✅endpoint to remove graph
- ✅use SQL like DB
- ✅use ORM
- ✅follow REST principles where possible
- ✅not to use Flask and Django (any other web framework is allowed)

### Will be a plus😇:

- ✅endpoint to perform basic algorithm on graph (DFS/BFS or something like this)

### References🧐:

- [https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics))
- [https://medium.com/pragmatech/orm-for-python-b63cfbc39e7f](https://medium.com/pragmatech/orm-for-python-b63cfbc39e7f)
- [https://wiki.python.org/moin/WebFrameworks](https://wiki.python.org/moin/WebFrameworks)
