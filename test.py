from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD

g = Graph()
g.parse("C:/Users/polin/PycharmProjects/Skin_Care_Advice/untitled-ontology-21", format = "xml")
for index, (s, p, o) in enumerate(g):
    print(s, p, o)
    if index == 2:
        break
m = Namespace("http://www.semanticweb.org/33602/ontologies/2023/0/untitled-ontology-3#")
g.add((m.test2, RDF.type, m.Moisturizer))
g.serialize(destination='test.rdf', format='xml')