![Image description](https://miro.medium.com/max/2978/1*rmq7bd3GFjcwfXtkrBQaPQ.png)
# pnat
Network Analysis Tool around Python-Igraph Library for  graph-theoretic parameters evaluation offering a variety of functions useful for bioinformatics including community detection and interactive visualisation of graph  offering menu-driven simple to use an approach
( Initial version of code : https://github.com/nitinp14920914/igraphtool)

## pip install 

	pip install pnat


## Table of contents
* [Installation](#installation)
* [List of Files](#list-of-contents)
* [Network Analysis Tool Usage](#Netwowrk-analysis-tool-usage)
* [List of Functions](#List-of-functions) 
* [Contact Information](#contact-information)

## Installation

Dependencies 
	  
    python2.7/3.6
	Matplotlib v3.1.1
	python-igraph v0.7.1.post6
	Networkx v2.3
	pyvis v0.1.7.0

Matplotlib

	Debian / Ubuntu :  sudo apt-get install python-matplotlib
	Fedora / Redhat :  sudo yum install python-matplotlib

	for pip
	python -m pip install -U pip setuptools
	python -m pip install matplotlib
	python -m pip install pyvis
	

python-igraph

	Debian / Ubuntu : sudo apt-get install python-igraph
	Fedora / Redhat : sudo yum install python-igraph

	using pip
	pip install python-igraph

NetworkX

	python -m pip install networkx
	
Pyvis
	
	python -m pip install pyvis
	


## List of Files 

    pnat.py
    readme

## Network Analysis Tool Usage

Usage 
	
    python pnat.py -format filename
	
For help 
	
	  python pnat.py -h or --help

* Enter the function number you want 

* It Returns output for a selected function 

* Network output files are written in graphml format

* A directory named temp is created on very first initialisation of script  

* There is also a ./temp directory associated with pnat.py where plots/figures/are exported and saved  


## List of Functions 
        
 	usage -format [filename]

	format: adjacencncy matrix -adj  edgelist -edgelist  graphml -graphml  lgl -lgl  random network -random
 
	=========== Feature List v1.0 =====================
	Parameter Evaluation........................###
		Degree Distribution Histogram...........(1)
		Centrality : 
			* Eigenvector centrality........(2)
			* Betweenness centrality........(3)
		Average path length.....................(4)
		Degree distribution.....................(5)
		Clustering coefficient..................(6)
			* Average Clustering coefficient[1]
			* Each-nodes Clustering coeff.  [2]
		Shortest path between two nodes.........(7)
		Shortest path between all nodes.........(8)
		Degree distribution power law...........(9)
		Functional motifs......................(10)
		Modularity.............................(13)
		Connectivity : 
			vertex * For given two vertex..(14)
		       	       *Overall................(15)
			Edge   * For given two vertex..(16)
		       	       *Overall................(17)
		No. of clusters........................(18)
		Diameter...............................(23)
		Average path length....................(24)
		Giant_component Extraction.............(25)
	Know-your Graph.............................###
		Maximum degree nodes.... ........... . (30)
		Minimum degree nodes.... ...........  .(31)
		Neighbour vertex : 
			* For two specified vertes.....(11)
			* For all vertex of graph......(12)
		Node label from its node id(Every node)(20)
		Node label from its node id(Every node)(21)
	Saving/Writing Graph........................###
		Adjacency matrix.......................(19)
		Edgelist...............................(22)
		Interactive Plot.......................(34)
	Editing Graph Data .........................###
		Add vertex(single)..............  ..   (26)
		Add vertices(many)..................   (27)
		Delete vertex(single)................ .(28)
		Delete vertices(many).... ........... .(29)
		Deleting all nodes saving in file .....(32)
	Community Detection/Structure..........    .###
		Community Detection/Structure..........(33)
		* Community_walktrap           [1]
		* Compare_communities          [2]
		* Community_edge_betweenness   [3]
		* Community_infomap            [4]
		* Community_label_propagation  [5]

## Contact Information

For any trouble and query feel free we would love to respond 
 
* nitin53_sit@jnu.ac.in
* andrew@jnu.ac.in
* nitinp14920914@gmail.com



