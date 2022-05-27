# Querys Sparql
import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON

class Eventos:

    def nombreEvento(self, name):
        global auxDic
        g = rdflib.Graph()

        g.parse("docs/output.nt")

        q = f"""
        SELECT ?name ?description ?image ?url ?tipoEvento ?startDate ?endDate ?isAccesibleForFree ?nombre 
        ?addressRegion ?addressLocality ?streetAddress ?postalCode ?audience ?evento ?estado
            WHERE{{
               ?evento <http://vocab.linkeddata.es/datosabiertos/def/cultura-ocio/agenda#documentacion> ?documentacion .
               ?evento <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras#equipamiento> ?equipamiento .
               ?equipamiento <http://schema.org/address> ?address .
               ?documentacion <http://schema.org/name> ?name .
                    FILTER regex(?name, "{name}") .
               ?documentacion <http://schema.org/description> ?description .
               ?documentacion <http://schema.org/image> ?image . 
               ?documentacion <http://schema.org/url> ?url .
               ?evento <http://vocab.linkeddata.es/datosabiertos/kos/cultura-ocio/agenda#tipo-evento> ?tipoEvento .
               ?evento <http://schema.org/startDate> ?startDate .
               ?evento <http://schema.org/endDate> ?endDate . 
               ?evento <http://schema.org/isAccesibleForFree> ?isAccesibleForFree .
               ?evento <http://schema.org/eventStatus> ?estado .
               ?equipamiento <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras#nombre> ?nombre .
               ?address <http://schema.org/addressRegion> ?addressRegion .
               ?address <http://schema.org/addressLocality> ?addressLocality .
               ?address <http://schema.org/streetAddress> ?streetAddress .
               ?address <http://schema.org/postalCode> ?postalCode  .
               ?evento <http://schema.org/audience> ?audience .
        }} GROUP BY ?name ORDER BY ?name
        """
        gres = g.query(q)

        resultado = []
        for row in gres:
            auxDic = self.completaRowAux(row)
            resultado.append(auxDic)
        return resultado

    def completaRowAux(self, row):
        cuatro = row[4].replace("http://vocab.linkeddata.es/datosabiertos/kos/cultura-ocio/agenda/tipo-evento/", "")
        cinco=row[5].replace("T", " ").replace("+01:00", "")
        seis = row[6].replace("T", " ").replace("+01:00", "")
        siete = row[7].replace("true", "Si").replace("false", "No")
        quince = row[14].replace("http://vocab.linkeddata.es/datosabiertos/recurso/cultura-ocio/agenda/", "")
        auxDic = {'name': row[0], 'description':row[1], 'image':row[2], 'url':row[3], 'tipoEvento':cuatro, 
        'startDate':cinco, 'endDate':seis, 'isAccesibleForFree':siete, 'nombre': row[8], 'addressRegion':row[9],
        'addressLocality':row[10], 'streetAddress':row[11], 'postalCode':row[12], 'audience':row[13], 'evento':row[14], 'eventoMini':quince}  
        return auxDic


