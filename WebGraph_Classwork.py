
# coding: utf-8

# In[404]:

import urllib.request
from bs4 import BeautifulSoup
class MyQueue:
    def __init__(self):
        self.queue_data = []
        
    def isempty(self):
        return self.queue_data == []
        
    def push(self, value):
        self.queue_data.append(value)
    
    def pop(self):
        if self.isempty():
            return None
        else:
            return_value = self.queue_data[0]
            self.queue_data = self.queue_data[1:]
            return return_value
            #return self.queue_data.pop()

class WebGraph:
    def __init__(self):
        self.graph = {}
        
    def add_node(self, label):
        if label in self.graph:
            pass
        self.graph[label] = []
    
    #Adds a directed edge from label1 to label2
    def add_edge(self, label1, label2):
        self.graph[label1].append(label2)
    
    #Adds a list of edges with each item in the list of the form [label1, label2]
    def add_edges(self, edgelist):
        for item in edgelist:
            self.add_edge(item[0], item[1])
    
    def link_discovery(self, url):
        self.add_node(url)
        url_split = urllib.parse.urlsplit(url)
        shtml = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(shtml)
        links = soup.find_all('a')

        for link in links:
            if 'href' in link.attrs:
                discovered_url = link.get('href')
                self.add_edge(url, discovered_url)
        return self.graph[url]
    
    def bfs(self, starting_node, max_nodes_visited=None):
        queue = MyQueue()
        queue.push(starting_node)
        visited = {}
        visited[starting_node] = list()
        count = max_nodes_visited
		if count is None:
			pass
		else:
			while count > 0:
				while not queue.isempty():
					v = queue.pop()
					url_links = self.link_discovery(v)
					for link in url_links:
						if link not in visited.values():
							visited[v].append(link)
							queue.push(link)
					count -= 1
					if count == 0:
						break
        return visited






