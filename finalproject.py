'''G := set of pages
for each page p in G do
    p.auth = 1 // p.auth is the authority score of the page p
    p.hub = 1 // p.hub is the hub score of the page p

function HubsAndAuthorities(G)
    for step from 1 to k do // run the algorithm for k steps
        for each page p in G do  // update all authority values first
            p.auth = 0
            for each page q in p.incomingNeighbors do // p.incomingNeighbors is the set of pages that link to p
                p.auth += q.hub
        for each page p in G do  // then update all hub values
            p.hub = 0
            for each page r in p.outgoingNeighbors do // p.outgoingNeighbors is the set of pages that p links to
                p.hub += r.auth'''
import numpy as np

class Page:
    def __init__(self, index, neighbors: list):
        self.authVal = self.hubVal = 0
        self.oldAuthVal = self.oldHubVal = 1
        self.neighbors = neighbors
        self.index = index

    def __repr__(self):
        return f'index: {self.index}, neighbors: {self.neighbors}'

# initialize adj list
'''
0 -> 1, 2, 3
1 -> 2
2 -> 3, 4
3 -> 
4 -> 0, 1
'''
adjList = {}
a = None
while True:
    dataInput = input('Enter data or b to break ').split()
    if dataInput == ['b']: break
    a = [int(i) for i in dataInput]
    key = a[0]
    val = a[1:]
    adjList[key] = val

#adjList = {0 : [1, 2, 3], 1: [2], 2: {3, 4}, 3 : [], 4 : [0, 1]}

G = [Page(i, adjList[i]) for i in adjList]

def HubsAndAuthorities(G: list) -> None:
    
    for i in range(100):
        for page in G:
            for nei in page.neighbors:
                page.hubVal += G[nei].oldAuthVal
                G[nei].authVal += page.oldHubVal

        sumAuth = sumHub = 0
        for page in G:
            sumAuth += page.authVal
            sumHub += page.hubVal

        for page in G:
            page.authVal /= sumAuth
            page.oldAuthVal = page.authVal
            page.authVal = 0
            page.hubVal /= sumHub
            page.oldHubVal = page.hubVal
            page.hubVal = 0

        

        '''for page in G:
            print(f'Old AuthVal: {page.oldAuthVal}, Old HubVal: {page.oldHubVal}')
            #, New AuthVal: {page.authVal}, New HubVal: {page.hubVal}')
        print()'''

    # get list of all the stuffs
    authValList = []
    hubValList = []
    for page in G:
        authValList.append(page.oldAuthVal)
        hubValList.append(page.oldHubVal)

    print(authValList)
    print(hubValList)

    return np.argsort(authValList)[::-1], np.argsort(hubValList)[::-1]

'''vals = bestAuthVals, bestHubVals = HubsAndAuthorities(G)

for av, hv in vals:
    print(f'')'''

print(HubsAndAuthorities(G))

#print(f'Websites with the best Authority values: {bestAuthVals} \nWebsites with the best Hub values: {bestHubVals}')

