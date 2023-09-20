from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    def setUp(self):
        """This function tests the graph class functions that allow us to add aspects to a graph after the graph has been created, this includes
        adding and removing vertices and edges"""
    r'''''

    Sydney
      \       
        \   5870 miles
          \              2113 miles             
            London -------------------- Paris
            |                                 |       
            |                                 |   
  5711 miles|                                 | 189 miles  
            |                                 |   
            |                                 |   
            Shanghai ----------------------Brussels
                             5598
        '''
        self.g = Graph()

        self.g.add_vertex("London")
        self.g.add_vertex("Paris")
        self.g.add_vertex("Brussels")
        self.g.add_vertex("Shanghai")
        self.g.add_vertex("Sydney")

        self.g.add_edge("London", "Paris", 2113)
        self.g.add_edge("Paris", "Brussels", 189)
        self.g.add_edge("Brussels", "Shanghai", 5598)
        self.g.add_edge("Shanghai", "London", 5711)
        self.g.add_edge("London", "Sydney", 5870)


        self.add_vertex("Rome")
        self.assertTrue("Rome" in self.g)
        self.g.remove_vertex("Rome")
        self.assertFalse("Rome" in self.g)
        self.g.add_edge("Rome", "London", 132)
        self.assertEqual(self.g.nbrs["Rome"]["London"], 132)
        self.g.remove_edge("Rome", "London", 132)
        self.assertNotEqual(self.g.nbrs["Rome"]["London"],  132)
    
class test_GraphTraversal(unittest.TestCase):
    def setUp(self):
        """This functions is creating the graph that will be used to test all of the traversal functions"""
        
        r'''
        Sydney
          \       
           \   5870 miles
            \              2113 miles             
                London -------------------- Paris
                |                                 |       
                |                                 |   
      5711 miles|                                 | 189 miles  
                |                                 |   
                |                                 |   
                Shanghai ----------------------Brussels
                                5598
        '''    
        
        self.g = Graph()

        self.g.add_vertex("London")
        self.g.add_vertex("Paris")
        self.g.add_vertex("Brussels")
        self.g.add_vertex("Shanghai")
        self.g.add_vertex("Sydney")

        self.g.add_edge("London", "Paris", 2113)
        self.g.add_edge("Paris", "Brussels", 189)
        self.g.add_edge("Brussels", "Shanghai", 5598)
        self.g.add_edge("Shanghai", "London", 5711)
        self.g.add_edge("London", "Sydney", 5870)

        

    def test_fewest_flights(self):
        """This function is testing the fewest_flights function which finds the smallest number of flights that needs to be made to reach a 
        specific destination """
        #Alg: BFS
        #Why: I used BFS for this because it uses a Queue to find the shortest number of flights that needs to be taken which is better because it will only return the values absolutely needed so it won't have to go through anything unecessary"
        self.assertEqual(self.g.fewest_flights("London"), ({'London': None, 'Paris': 'London', 'Shanghai': 'London', 'Brussels': 'Shanghai'}, {'London': 0, 'Paris': 1, 'Shanghai': 1, 'Brussels': 2, "Sydney": 1}))
        

    
    def test_shortest_path(self):
        """This function tests the shortest_path function which finds the shortest path to get to each of the cities in the graph, from a preselected
        city, this is done using the edge weights"""
        #Alg: Dijkstra's
        #Why: I used Dijkstra's for this function because it will find the shortest way to get to each city from a specified city
        self.assertEqual(self.g.shortest_path("London"), ({'London': None, 'Paris': 'London', 'Shanghai': 'London', 'Brussels': 'Paris', "Sydney" : "London"}, {'London': 0, 'Paris': 2113, 'Shanghai': 5711, 'Brussels': 2302, "Sydney":5870}))
         
    
    def test_minimum_salt(self):
        """This function tests the minimum_salt function which finds the shortest path connecting all of the cities in one strectch, starting from
        a preselected city, this is also done using the edge weights"""
        #Alg: Prim's
        #Why: I used Prim's for this because it will find the path connecting all of the cities together in the smallest number of miles
        self.assertEqual(self.g.minimum_salt("London"), ({"London": None, "Sydney": "London", "Shanghai": "London", "Paris": "London", "Brussels": "Paris"}, {'London': 0, 'Paris': 2113, 'Shanghai': 5711, 'Brussels': 189, "Sydney": 5870}))
        

unittest.main()