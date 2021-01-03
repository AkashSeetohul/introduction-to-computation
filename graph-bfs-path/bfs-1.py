#Copyright 2020 Tooryanand Seetohul

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

#  Lab assignment 3
#  Based on Professor Cormen's instructions
#  Author Tooryanand Seetohul

from collections import deque

def bfs(start, end):
    frontier = deque()

    #  appending the first Vertex object
    frontier.append(start)

    #  dictionary to hold the backpointers
    backpointers = {}

    path = []

    #  start vertex should not have a backpointer
    backpointers[start] = None

    #  if frontier is not empty
    while len(frontier):
        current_vertex = frontier.popleft()

        #  check if current vertex is at the end
        if current_vertex == end:
            while current_vertex:
                #   append to path
                path.append(current_vertex)
                current_vertex = backpointers[current_vertex]
            return path

        else:
            #  get the list of neighbor
            neighbor_list = current_vertex.get_neighbors()

            #  append the list of neighbors
            for vertex in neighbor_list:
                if vertex not in backpointers:
                    frontier.append(vertex)
                    backpointers[vertex] = current_vertex

    #  return an empty list if no possible path found
    return []
