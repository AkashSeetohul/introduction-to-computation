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

#  Lab assignment 2
#  Based on Professor Cormen's examples and instructions
#  Author Tooryanand Seetohul

from city import City
from write_and_create import *
from quicksort import quicksort

city_list = []

open_and_create_list("world_cities.txt", city_list)

#  sort cities by population name
City.__gt__ = City.name_gt
quicksort(city_list)
write_file("cities_alpha.txt", city_list)

#  sort cities by population
City.__gt__ = City.population_lt
quicksort(city_list)
write_file("cities_population.txt", city_list)

#  sort cities by latitude
City.__gt__ = City.latitude_gt
quicksort(city_list)
write_file("cities_latitude.txt", city_list)
