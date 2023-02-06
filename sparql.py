import rdflib
from rdflib import Graph
def actifs(usage):
    g = Graph()
    g.parse("ontology3.rdf", format = "xml")
    #my_ontology = Namespace("http://www.semanticweb.org/33602/ontologies/2023/0/untitled-ontology-3#")

    k = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX foaf: <http://www.semanticweb.org/polin/ontologies/2023/0/untitled-ontology-21#>
    SELECT DISTINCT ?x
    WHERE{
        ?x foaf:isUsedFor foaf:"""+usage+""".
    }
    """
    qres = g.query(k)
    actifs=[]
    for row in qres:
        actifs.append(str(row.x).split("#")[1])
    return actifs

def produits(actif):
    g = Graph()
    g.parse("ontology3.rdf", format = "xml")
    #my_ontology = Namespace("http://www.semanticweb.org/33602/ontologies/2023/0/untitled-ontology-3#")

    k = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX foaf: <http://www.semanticweb.org/polin/ontologies/2023/0/untitled-ontology-21#>
    PREFIX foaf2: <http://www.semanticweb.org/33602/ontologies/2023/1/untitled-ontology-21#>
    PREFIX foaf3: <http://www.semanticweb.org/33602/ontologies/2023/0/untitled-ontology-21#>

    SELECT DISTINCT ?x ?u ?s
    WHERE{
        ?x foaf:has_active_substance foaf3:"""+actif+""".
        ?x foaf2:marque ?u.
        OPTIONAL{ ?x foaf2:concentration ?s.}
    }
    """
    qres = g.query(k)
    prod=[]
    for row in qres:
        r = []
        r.append(str(row.x).split("#")[1])
        r.append(str(row.u))
        r.append(str(row.s))
        prod.append(r)
    return prod

def all_products(list_usages):
    actif = []
    for usage in list_usages:
        actif.append(actifs(usage))
    actiff = [item for sublist in actif for item in sublist]
    prods= []
    for act in actiff:
        li = produits(act)
        for one in li:
            prods.append(one)
    return prods