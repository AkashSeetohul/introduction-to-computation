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

class City:
    #  initializing the instance variables
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude

    #  __str__ for print
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

    #  comparison function for name
    def name_gt(self, other):
        return self.name.lower() > other.name.lower()

    #  comparison function for population
    def population_lt(self, other):
        return self.population < other.population

    #  comparison function for latitude
    def latitude_gt(self, other):
        return self.latitude > other.latitude
