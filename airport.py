airports = 'PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM'.split(' ')
routes = [
    ['PHX', 'LAX'],
    ['PHX', 'JFK'],
    ['JFK', 'OKC'],
    ['JFK', 'HEL'],
    ['JFK', 'LOS'],
    ['MEX', 'LAX'],
    ['MEX', 'BKK'],
    ['MEX', 'LIM'],
    ['MEX', 'EZE'],
    ['LIM', 'BKK']
]


adjacencyList = {}

def addNode(airport):
    adjacencyList.update({airport:[]})

def addEdge(origin, destination):
    adjacencyList[origin].append(destination)
    adjacencyList[destination].append(origin)

for airport in airports:
    addNode(airport)
for route in routes:
    addEdge(*route)

print(adjacencyList)