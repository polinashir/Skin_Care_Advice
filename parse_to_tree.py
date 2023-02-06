from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD

g = Graph()
g.parse("C:/Users/polin/PycharmProjects/Skin_Care_Advice/untitled-ontology-21", format = "xml")
m_prod = Namespace("http://www.semanticweb.org/33602/ontologies/2023/0/untitled-ontology-21#")
m_prop = Namespace("http://www.semanticweb.org/33602/ontologies/2023/1/untitled-ontology-21#")
m_obj = Namespace("http://www.semanticweb.org/polin/ontologies/2023/0/untitled-ontology-21#")
def add_product(list_products, section):
    for nom_produit in list_products:
        g.add((m_prod[nom_produit], RDF.type, m_prod[section]))
def add_property(subject, predicate, object):
    obj = Literal(object)
    g.add((m_prod[subject], m_prop[predicate], obj))

def add_object(subject, predicate, object):
    g.add((m_prod[subject], m_obj[predicate], m_prod[object]))
#nom produit, concent, numero<
def add_products_for_class(list_prod, pred, section):
    for prod in list_prod:
        add_object(prod, pred, section)

def add_percantage(list_prod, pred, section):
    for (prod, concent) in zip(list_prod, section):
        if(concent!='NaN'):
            add_property(prod, pred, concent)
def save():
    for index, (s, p, o) in enumerate(g):
        if "has_active_substance" in s:
            print(s, p, o)
    g.serialize(destination='ontology.rdf', format='xml')
