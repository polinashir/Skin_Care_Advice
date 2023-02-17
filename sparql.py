import rdflib
from rdflib import Graph
import rdflib
def actifs(usage):
    g = Graph()
    g.parse("untitled-ontology-51", format = "xml")
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

def produits(actif, product_type, r):
    g = Graph()
    g.parse("untitled-ontology-51", format = "xml")
    #my_ontology = Namespace("http://www.semanticweb.org/33602/ontologies/2023/0/untitled-ontology-3#")

    k = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX foaf: <http://www.semanticweb.org/polin/ontologies/2023/0/untitled-ontology-21#>
    PREFIX foaf2: <http://www.semanticweb.org/33602/ontologies/2023/1/untitled-ontology-21#>
    PREFIX foaf3: <http://www.semanticweb.org/33602/ontologies/2023/0/untitled-ontology-21#>

    SELECT DISTINCT ?x ?u ?s ?p
    WHERE{
        ?x foaf:has_active_substance foaf3:"""+actif+""".
        ?x rdf:type foaf3:"""+product_type+""".
        ?x rdf:type foaf2:"""+r+""".
        ?x foaf2:marque ?u.
        ?x foaf2:price ?p.
        OPTIONAL{ ?x foaf2:concentration ?s.}
    }
    """
    qres = g.query(k)
    prod=[]
    for row in qres:
        r = []
        r.append(actif)
        r.append(str(row.x).split("#")[1].replace("_", " ").replace("pourcent", "%"))
        r.append(str(row.u).replace("_", " ").replace("pourcent", "%"))
        r.append(str(row.s))
        r.append(int(row.p))
        prod.append(r)
    return prod

def all_products(list_usages,list_product_type,list_range):
    actif = []
    for usage in list_usages:
        actif.append([actifs(usage), usage])
    prods= []
    for i in range (len(actif)):
        actiff = actif[i][0]
        for act in actiff:
            for product_type in list_product_type:
                for r in list_range:
                    li = produits(act, product_type,r)
                    for one in li:
                        one.append(actif[i][1])
                        prods.append(one)
    return prods