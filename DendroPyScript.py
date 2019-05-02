#! /usr/bin/env python

import dendropy
import os

def rf_unweighted(tree1_path,tree2_path):
	taxa = dendropy.TaxonNamespace() #set taxa same for all
	tree1=dendropy.Tree.get_from_path(tree1_path,schema='newick',taxon_namespace=taxa)
	tree2=dendropy.Tree.get_from_path(tree2_path,schema='newick',taxon_namespace=taxa)
	tree1.encode_bipartitions()
	tree2.encode_bipartitions()
	dist=dendropy.calculate.treecompare.symmetric_difference(tree1,tree2)
	return dist

def euclid_dist(tree1_path,tree2_path):
	taxa = dendropy.TaxonNamespace() #set taxa same for all
	tree1=dendropy.Tree.get_from_path(tree1_path,schema='nexus',taxon_namespace=taxa)
	tree2=dendropy.Tree.get_from_path(tree2_path,schema='nexus',taxon_namespace=taxa)
	tree1.encode_bipartitions()
	tree2.encode_bipartitions()
	dist=dendropy.calculate.treecompare.euclidean_distance(tree1,tree2)
	return dist

def rf_weighted(tree1_path,tree2_path):
	taxa = dendropy.TaxonNamespace() #set taxa same for all
	tree1=dendropy.Tree.get_from_path(tree1_path,schema='nexus',taxon_namespace=taxa)
	tree2=dendropy.Tree.get_from_path(tree2_path,schema='nexus',taxon_namespace=taxa)
	tree1.encode_bipartitions()
	tree2.encode_bipartitions()
	dist=dendropy.calculate.treecompare.weighted_robinson_foulds_distance(tree1,tree2)
return dist

# /Users/ethanbartel/Desktop/TreeScaper/CCA/Unweighted/Newick_species_tree_files/Newick_species_trees.t
#Initial Path
#/Users/ethanbartel/Desktop/TreeScaper/CCA/Unweighted/Newick_species_trees_unrooted_unweighted_RF-distance.out
#Major Path
#/Users/ethanbartel/Desktop/TreeScaper/CCA/Unweighted/Majorization/Newick_species_trees_URF_2D_CCA_DIS_MAJORIZATION.out
#MetroPath
#/Users/ethanbartel/Desktop/TreeScaper/CCA/Unweighted/Metropolis/Newick_species_trees_URF_2D_CCA_DIS_METROPOLIS.out
#GSPath
#/Users/ethanbartel/Desktop/TreeScaper/CCA/Unweighted/Gauss Seidel/Newick_species_trees_URF_2D_CCA_DIS_GAUSS_SEIDEL.out
#Stochastic Path
#/Users/ethanbartel/Desktop/TreeScaper/CCA/Unweighted/Stochastic/Newick_species_trees_URF_2D_CCA_DIS_STOCHASTIC.out
