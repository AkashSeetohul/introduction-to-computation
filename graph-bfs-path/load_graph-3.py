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

from vertex import Vertex

def load_graph(file_name):

    # opening the text file
    in_file = open(file_name, "r")

    #  creating an empty dictionary to hold the vertices
    vertices_dictionary = {}

    #  looping through every line in the file
    for line in in_file:
        temp1 = line.strip(" ")  #  removing the whitespaces
        temp2_list = temp1.split(";")  #  list of the 3 different attributes

        coordinates = temp2_list[2].split(",")  #  forming a list containing the x and y

        #  creating a vertex object
        vertex_object = Vertex(temp2_list[0], int(coordinates[0]), int(coordinates[1]))

        #  adding the object to the dictionary with the name as key
        vertices_dictionary[temp2_list[0]] = vertex_object

    #  closing the file
    in_file.close()

    #  re-opening the text file
    in_file = open(file_name, "r")

    #  looping through every line in the file
    for line in in_file:
        temp1 = line.strip("")  #  removing the whitespaces
        temp2_list = temp1.split(";")  #  list of the 3 different attributes

        #  key and name of vertex object in dictionary
        vertex_name = temp2_list[0].strip()

        #  searching for the names of the neighbors
        adjacency_temp = temp2_list[1].split(",")

        #  empty list to hold the names of the neighbors
        adjacency_names = []

        #  appending the neighbor names to the list
        for name in adjacency_temp:
            adjacency_names.append(name.strip())

        #  appending the adjacency vertex objects to the Vertex object
        for name in adjacency_names:
            vertices_dictionary[vertex_name].append_neighbor(vertices_dictionary[name])

    return vertices_dictionary
