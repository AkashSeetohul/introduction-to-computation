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

from city import City

#  function to open file and create a list of references to world cities
def open_and_create_list(file_name, city_list):
    #  opening the text
    world_cities = open(file_name)

    #  looping through each line
    for line in world_cities:
        temp1 = line.strip() #  removing all whitespaces
        temporary_list = temp1.split(",") #  creating list with all six attributes

        #  creating a City object
        city = City(temporary_list[0], temporary_list[1], temporary_list[2], int(temporary_list[3]), float(temporary_list[4]), float(temporary_list[5]))

        #  appending the reference to the master city list
        city_list.append(city)

    #  closing the text
    world_cities.close()

#  function to write into file
def write_file(file_name, city_list):
    #  opening the blank text file cities_out.txt
    out_file = open(file_name, "w")

    #  looping the master list
    for city in city_list:
        sentence = str(city) + "\n"
        out_file.write(sentence)

    #  close the text file cities_out
    out_file.close()

#  empty list to hold all references of cities
city_list = []

open_and_create_list("world_cities.txt", city_list)
write_file("cities_out.txt", city_list)
