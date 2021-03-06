import matplotlib.pyplot as plt
from igraph import *
from pyvis.network import Network
import networkx as nx
import sys
import os


#####colour pallet ###
def prRed(skk): print("\033[91m{}\033[00m" .format(skk))#menu 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))#fig save 
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk))#no. of nodes 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk))#input 
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk))#code end 
def prLightGray(skk): print("\033[97m{}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m{}\033[00m" .format(skk)) 

def menu():
	prGreen ('\n'+'	=========== Feature List v1.0 =====================')
	prGreen ('	Parameter Evaluation........................###')
	prRed ('\t'+'	Degree Distribution Histogram...........(1)')
	prRed ('\t'+'	Centrality : ')
	prRed ('\t'+'		* Eigenvector centrality........(2)')
	prRed ('\t'+'		* Betweenness centrality........(3)')
	prRed ('\t'+'	Average path length.....................(4)')
	prRed ('\t'+'	Degree distribution.....................(5)')
	prRed ('\t'+'	Clustering coefficient..................(6)')
	prRed ('\t'+'		* Average Clustering coefficient[1]')
	prRed ('\t'+'		* Each-nodes Clustering coeff.  [2]')
	prRed ('\t'+'	Shortest path between two nodes.........(7)')
	prRed ('\t'+'	Shortest path between all nodes.........(8)')
	prRed ('\t'+'	Degree distribution power law...........(9)')
	prRed ('\t'+'	Functional motifs......................(10)')
	prRed ('\t'+'	Modularity.............................(13)')	
	prRed ('\t'+'	Connectivity : '		)
	prRed ('\t'+'		vertex * For given two vertex..(14)')	
	prRed ('\t'+'	       	       *Overall................(15)')
	prRed ('\t'+'		Edge   * For given two vertex..(16)')
	prRed ('\t'+'	       	       *Overall................(17)')	
	prRed ('\t'+'	No. of clusters........................(18)')
	prRed ('\t'+'	Diameter...............................(23)')
	prRed ('\t'+'	Average path length....................(24)')
	prRed ('\t'+'	Giant_component Extraction.............(25)')
	prGreen ('	Know-your Graph.............................###')
	prRed ('\t'+'	Maximum degree nodes.... ........... . (30)')
	prRed ('\t'+'	Minimum degree nodes.... ...........  .(31)')
	prRed ('\t'+'	Neighbour vertex : ')
	prRed ('\t'+'\t'+'\t'+'* For two specified vertes.....(11)')
	prRed ('\t'+'\t'+'\t'+'* For all vertex of graph......(12)')
	prRed ('\t'+'	Node label from its node id(Every node)(20)')
	prRed ('\t'+'	Node label from its node id(Every node)(21)')
	prGreen ('	Saving/Writing Graph........................###')
	prRed ('\t'+'	Adjacency matrix.......................(19)')
	prRed ('\t'+'	Edgelist...............................(22)')
	prRed ('\t'+'	Interactive Plot.......................(34)')
	prGreen ('	Editing Graph Data .........................###')
	prRed ('\t'+'	Add vertex(single)..............  ..   (26)')
	prRed ('\t'+'	Add vertices(many)..................   (27)')
	prRed ('\t'+'	Delete vertex(single)................ .(28)')
	prRed ('\t'+'	Delete vertices(many).... ........... .(29)')
	prRed ('\t'+'	Deleting all nodes saving in file .....(32)')
	prGreen ('	Community Detection/Structure..........    .###')
	prRed ('\t'+'	Community Detection/Structure..........(33)')
	prRed('\t'+'\t'+'* Community_walktrap           [1]')
	prRed('\t'+'\t'+'* Compare_communities          [2]')
	prRed('\t'+'\t'+'* Community_edge_betweenness   [3]')
	prRed('\t'+'\t'+'* Community_infomap            [4]')
	prRed('\t'+'\t'+'* Community_label_propagation  [5]'+'\n')



########## create temp dir ####

l = os.listdir(os.getcwd())
if 'temp' not in l:
	os.mkdir('temp')
else:
	pass 

#######help function ####


if len(sys.argv) < 2 :
	print ('	usage -format [filename]')
	print('		!!!Input file Missing!!! Try --h or -H or --help')
	sys.exit()
elif sys.argv[1] == True  or '-h' or '-H' or '--help'  :
	print ('	usage -format [filename]'+'\n')
	print ('	format: adjacencncy matrix -adj  edgelist -edgelist  graphml -graphml  lgl -lgl  random network -random' +'\n' )



######interactive plot ####

def interactive(file_in,form):
	i=Network(height=1080,width=1920) #can specify your screen resolution
	i.toggle_hide_edges_on_drag(False)
	i.barnes_hut()
	form=str(sys.argv[1])
	if sys.argv[1] == '-edgelist':
		i.from_nx(nx.read_weighted_edgelist(file_in)) 
		i.show("./temp/"+str(sys.argv[2])+".html")
	elif sys.argv[1] == '-graphml':
		i.from_nx(nx.read_graphml(file_in)) 
		i.show(str(sys.argv[2])+".html")



#####input file ####

if sys.argv[1] == '-adj':
	g=Graph.Read_Adjacency(sys.argv[2])
	print ('\033[93mNo. of nodes in given file : \033[00m',  len(g.vs))
	print ('\033[93mNo. of edges in given file : \033[00m',  len(EdgeSeq(g)))
	layout = g.layout('kk')
	plot(g,target='./temp/graph_with_nodes'+str(sys.argv[2])+'.png',layout = layout)
	prGreen('figure is saved under ./temp/ ')

elif sys.argv[1] == '-edgelist':
	g=Graph.Read_Ncol(sys.argv[2], names=True, weights="if_present", directed=True)
	print ('\033[93mNo. of nodes in given file : \033[00m',  len(g.vs))
	print ('\033[93mNo. of edges in given file : \033[00m',  len(EdgeSeq(g)))
	a = [ ]               
	a = g.degree()
	c = [ ]
	for i in range(len(g.vs)):  
		c.append(str(i)) 
	g.vs['label'] = c     
	layout = g.layout('kk')
	plot(g,target='./temp/graph_with_nodes'+str(sys.argv[2])+'.png',layout = layout)
	prGreen('figure is saved under ./temp/ ')
	#interactive(sys.argv[2],sys.argv[1])

elif sys.argv[1] == '-graphml':
	g=Graph.Read_GraphML(sys.argv[2])
	print ('\033[93mNo. of nodes in given file : \033[00m',  len(g.vs))
	print ('\033[93mNo. of edges in given file : \033[00m',  len(EdgeSeq(g)))
	layout = g.layout('kk') 
	plot(g ,target='./temp/graph_with_nodes'+str(sys.argv[2])+'.png',layout = layout)
	prGreen('figure is saved under ./temp/ ')
	#interactive(sys.argv[2],sys.argv[1])

elif sys.argv[1] == '-adj':
	g=Graph.Read_(sys.argv[2])
	print ('\033[93mNo. of nodes in given file : \033[00m',  len(g.vs))
	print ('\033[93mNo. of edges in given file : \033[00m',  len(EdgeSeq(g)))
	layout = g.layout_sphere('kk')   
	plot(g,target='./temp/graph_with_nodes'+str(sys.argv[2])+'.png',layout = layout)
	prGreen('figure is saved under ./temp/ ')

elif sys.argv[1] == '-lgl':
	g=Graph.Read_Lgl,(sys.argv[2])
	print ('\033[93mNo. of nodes in given file : \033[00m',  len(g.vs))
	print ('\033[93mNo. of edges in given file : \033[00m',  len(EdgeSeq(g)))
	layout = g.layout('kk')
	plot(g,target='./temp/graph_with_nodes'+str(sys.argv[2])+'.png',layout = layout)
	prGreen('figure is saved under ./temp/ ')

elif sys.argv[1] == '-random':
	num = eval(input("Enter the number of nodes: "))
	g = Graph.GRG(num,0.1)
	c = [ ]
	for i in range(num):  
		c.append(str(i)) 
	g.vs['label'] = c     
	a = [ ]               
	a = g.degree()
	layout = g.layout('kk')
	plot(g,target='./temp/graph_with_nodes'+str(num)+'.png' , layout = layout)
	prGreen('figure is saved under ./temp/ ')
	i=Network(height=1080,width=1920) #can specify your screen resolution
	i.toggle_hide_edges_on_drag(False)
	i.barnes_hut()
	prob = float(input("Probability for edge creation: "))
	i.from_nx(nx.gnp_random_graph(num, prob, seed=None, directed=False)) 
	i.show('graph_with_nodes'+str(num)+".html")


######functions #### 



while True :
	try:	
		menu()
		user = eval(input('\033[94m Type the no of function wanted \033[00m : '))

		if user == 1 :
			b = g.degree_distribution(bin_width=1)
			print ('degree histogram',b)
			a = [ ]               
			a = g.degree()
			plt.hist(a, bins=range(0,(max(a))),density=1,stacked='True', facecolor='b')
			plt.xlabel('Number of Nodes')
			plt.ylabel('Degree')
			plt.title('Degree Distribution')
			plt.savefig("./temp/hist.png",dpi=300)
			plt.show()
			prGreen('figure is saved under ./temp/ ')
			 

		if user == 5 : 
			c=[]
			for i in range(len(g.vs)):
				c.append(str(i)) 
			g.vs['label'] = c
			a = [ ]
			a = g.degree()
			degree=open('degree_distribution.txt','w')
			for deg in range(len(c)):
				degree.write('degree vertex id'+'\t'+str(a[deg])+'\t'+str(c[deg])+'\n')
			print ('degree distribution (degree, vertex id) file is saved degree_distribution.txt' )

		if user == 7 : 	
			start = input("Enter the name(which is integer here) of the node from which the shortest path is to be calculated : ")
			end = input("Enter the name(which is integer here) of the node to which the shortest path is to be calculated : ")
			print  ('shortest path', g.get_all_shortest_paths(start, to=end, weights=None, mode=OUT))
		if user == 8 : 	
			print  ('shortest path', g.shortest_paths(source=None, target=None, weights=None, mode=ALL))
		if user == 6 :
			prRed ('\t'+'clustering coefficient')
			prRed('\t'+'\t'+'Average clustering coefficient   [1]')
			prRed('\t'+'\t'+'Each clustering coefficient      [2]'+'\n')
			user = int(input('\033[94m Type the no of function wanted \033[00m : '))		 
			if user == 1 :
				print ('Each nodes clustering coefficient', g.transitivity_avglocal_undirected(mode='zero'))
			if user == 2 :
				print ('Each nodes clustering coefficient', g.transitivity_local_undirected(mode='zero'))
				 

		if user == 3 : 
			startc = input("Enter the start node from which betweenness centrality to be calculated : ")
			endc = input("Enter the end node till which betweenness centrality to be calculated :  ")
			print ('betweenness centrality', g.betweenness(startc,endc))
		if user == 2 : 
			print ('eigenvector centrality',g.eigenvector_centrality(directed=True,scale=True,weights=None,return_eigenvalue=False))
		if user ==  9 : 
			deg=g.Static_Power_Law(len(g.vs),10,exponent_out=2,exponent_in=-1,loops=False,multiple=False,finite_size_correction=True)
			plot(deg)
			print ('Degree distribution(power law)', deg)
		if user == 4 : 
			print ('average path length', g.average_path_length(directed=False,unconn=True))
		if user == 10 : 
			print (' no. of functional motif ', g.motifs_randesu_no(size=3,cut_prob=None,))
		if user == 12 : 
			print ('neighbourhood vertice for each', g.neighborhood(vertices=None,order=1,mode=ALL))
		if user == 11 : 
			neighbors=input('type the vertics to whom neighbour vertex needed: ')
			print ('neighbour vertices to gien vertices', g.neighbors(neighbors,mode=ALL))
		if user == 13 : 
			membership=a 
			print ('modularity', g.modularity(membership,weights=None))
		if user == 14 : 
			x=input('connectivity from: ')
			y=input('connectivity to : ')
			print  ('connectivity from one node to another', g.vertex_connectivity(source=x,target=y,checks=True,neighbors="error"))
		if user == 15 : 	
			print  ('vertex connectivity overall', g.vertex_connectivity(source=-1,target=-1,checks=True,neighbors="error"))
		if user == 16 : 
			source=input('source vertex : ')
			target=input('target vertex : ')
			print ('edge connectivity ', g.edge_connectivity(source=source,target=target,checks=True))
		if user == 17 : 	
			print ('overall connectivity', g.edge_connectivity(source=-1,target=-1,checks=True))
		if user == 19 : 
			g.get_adjacency(type=GET_ADJACENCY_BOTH,eids=True)
			g.write_adjacency('matrix.txt')
			print ('adjacency matrix saved in file ')

		if user == 18 : 
			print ('no of clusters of the graph', len(g.clusters(mode=STRONG)))
		if user == 20 :
			node=input('type the node id : ')
			print (g.vs[node])
		if user == 21 :
			for i in range(len(g.vs)):
				print (i, g.vs[i])
		if user == 22 :
			edgelist=g.get_inclist(mode=OUT)
			fout=open("edgelist.txt",'w')
			fout.write(str(edgelist))
			print ("edgelist saved")
			fout.close()
		if user == 23 :
			print ("Diameter is " , (g.diameter(directed=True, unconn=True, weights=None)))

		if user == 24 :
			print (g.average_path_length(directed=False,unconn=True))
		if user == 25 :
			print (g.clusters( ).giant ( ).write_graphml("gaint_component.graphml"))
			print ('gaint component is saved in graphml file')

		if user == 26:
			n=input(' single vertex to be added attribute:  ')
			g.add_vertex(n)
			print (g.write_graphml("new_added_single_node.graphml"))
			print ('new added vertice is saved in graphml file ')

		if user == 27:
			n=input('the number of vertices to be added, :  ')
			g.add_vertices(n)
			g.write_graphml("new_added_many_node.graphml")
			print ('new added vertice is saved in graphml file ')

		if user == 28:
			dlt=input('id of vertices to be deleted:  ')
			g.delete_vertices(dlt)
			g.write_graphml("new_deleted__node.graphml")
			print ('Deleted vertex FILE is graphml file ')

		if user == 29:
			s =raw_input('ids of vertices to be deleted saprated by space:  ')
			dlt_list=list(map(int, s.split()))
			g.delete_vertices(dlt_list)
			g.write_graphml("new_deleted__node.graphml")
			print ('Deleted vertex FILE is graphml file ')


		if user == 30:
			a=g.degree()
			print ('node with max degree' , max(a), g.vs[max(a)])

		if user == 31:
			a=g.degree()
			print ('node with max degree', min(a), g.vs[min(a)])

		if user == 32:
			num=0
			j=0
			while num == 0:
				g.delete_vertices(0)
				if len(g.vs) ==1:
					break
				g.write_edgelist(str(os.getcwd())+"/temp/deleted_node_"+str(j)+".txt")
				print ( 'files complete and saved after deleting node :- ' ,  str(j))
				j +=1

		if user == 33:
			prRed ('\t'+'Community Detection')
			prRed('\t'+'\t'+'Community_walktrap            [1]')
			prRed('\t'+'\t'+'Compare_communities           [2]')
			prRed('\t'+'\t'+'Community_edge_betweenness    [3]')
			prRed('\t'+'\t'+'Community_infomap             [4]')
			prRed('\t'+'\t'+'Community_label_propagation   [5]'+'\n')
		
			
			user = int(input('\033[94m Type the no of function wanted \033[00m : '))
			
			if user == 1:
				dendo=g.community_walktrap(weights=None, steps=4)
				print(dendo)
			if user == 2:
				try:
					print((g.clusters()))
					line=g.clusters()
					print((line[0]))
					method=input("\n\033[94m Type the input method \n 1)vi \n 2)meila \n 3)nmi \n 4)danon \n 5)split-join \n 6)rand \n 7)adjusted_rand \033[00m :  ")
					comm1=eval(input("Select the community1/list to compare : "))
					comm2=eval(input("Select the community1/list to compare : "))
					print(compare_communities(comm1,comm2, method=str(method), remove_none=False))
				except ValueError:
					print('!!!!!!ERROR !!!!! "The two membership vectors must be equal in length" !!!!!!ERROR !!!!!')
					
			if user == 3:
				print(g.community_edge_betweenness(directed=True, weights=None))
			if user == 4:
				print(g.community_infomap(edge_weights=None, vertex_weights=None, trials=10))
			if user == 5:
				print(g.community_label_propagation(weights=None, initial=None, fixed=None))
			if user == 6:
				print(g.community_optimal_modularity(weights=None)) # takes undirected only 
		
		if user == 34:
			print ('\033[93mNo. of nodes in given file : \033[00m',  len(g.vs))
			print ('\033[93mNo. of edges in given file : \033[00m',  len(EdgeSeq(g)))
			prGreen('plot is saved under as .html ')
			interactive(sys.argv[2],sys.argv[1])	
	
	except NameError:
   		prCyan("!!!!!! NO Input Selected !!!!!!")
   		sys.exit()	

