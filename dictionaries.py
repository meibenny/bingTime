"""
    dictionaries.py  Supporting module for bingTimeGUI. Provides travel time
    through different paths.
    
    Copyright (C) 2012  Joseph Grillo & Benny Mei
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    LICENSE: This is open-source software released under the terms of the
    GPL (http://www.gnu.org/licenses/gpl.html).
"""


C4Dict = {"C4":"0", "Appalachian":"15", "CIW Dining Hall":"10", \
          "Hinman Dining Hall":"20", "Lecture Hall":"15", \
          "Science Buildings":"25", "Bartle Library":"10",\
          "Fine Arts":"12", "Union(Old)":"5"}

AppDict = {"C4":"15", "Appalachian":"0", "CIW Dining Hall":"10",\
           "Hinman Dining Hall":"10", "Lecture Hall":"15",\
           "Science Buildings":"25", "Bartle Library":"10",\
           "Fine Arts":"12", "Union(Old)":"10"}

CIWDict = {"C4":"10", "Appalachian":"10", "CIW Dining Hall":"0",\
           "Hinman Dining Hall":"15", "Lecture Hall":"15",\
           "Science Buildings":"20", "Bartle Library":"5",\
           "Fine Arts":"7", "Union(Old)":"5"}

HinmanDict = {"C4":"20", "Appalachian":"10", "CIW Dining Hall":"15", \
              "Hinman Dining Hall":"0", "Lecture Hall":"5", \
              "Science Buildings":"15", "Bartle Library":"15",\
              "Fine Arts":"17", "Union(Old)":"10"}

LHDict = {"C4":"15", "Appalachian":"15", "CIW Dining Hall":"15", \
          "Hinman Dining Hall":"5", "Lecture Hall":"0",\
          "Science Buildings":"5", "Bartle Library":"5", \
          "Fine Arts":"7", "Union(Old)":"10"}

SciDict = {"C4":"25", "Appalachian":"25", "CIW Dining Hall":"20", \
           "Hinman Dining Hall":"15", "Lecture Hall":"5", \
           "Science Buildings":"0", "Bartle Library":"7", \
           "Fine Arts":"5", "Union(Old)":"12"}

BartleDict = {"C4":"10", "Appalachian":"10", "CIW Dining Hall":"5", \
              "Hinman Dining Hall":"15", "Lecture Hall":"5",\
              "Science Buildings":"7", "Bartle Library":"0",\
              "Fine Arts":"2", "Union(Old)":"5"}

FADict = {"C4":"7",  "Appalachian":"10", "CIW Dining Hall":"7", \
          "Hinman Dining Hall":"15", "Lecture Hall":"5",\
          "Science Buildings":"5", "Bartle Library":"2",\
          "Fine Arts":"0", "Union(Old)":"5"}

UnionDict = {"C4":"5", "Appalachian":"10", "CIW Dining Hall":"5", \
             "Hinman Dining Hall":"10", "Lecture Hall":"10",\
             "Science Buildings":"12", "Bartle Library":"5",\
             "Fine Arts":"5", "Union(Old)":"0"}




def getTime(location, destination):
    if location == "C4":
        msg = C4Dict[destination]
    elif location == "Appalachian":
        msg = AppDict[destination]
    elif location == "CIW Dining Hall":
        msg = CIWDict[destination]
    elif location == "Hinman Dining Hall":
        msg = HinmanDict[destination]
    elif location == "Lecture Hall":
        msg = LHDict[destination]
    elif location == "Science Buildings":
        msg = SciDict[destination]
    elif location == "Bartle Library":
        msg = BartleDict[destination]
    elif location == "Fine Arts":
        msg = FADict[destination]
    else:
        msg = UnionDict[destination]
    return msg
