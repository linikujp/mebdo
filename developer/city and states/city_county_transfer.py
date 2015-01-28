"""
   

Make output an import file  




    <!-- http://dbpedia.org/resource/United_Sates -->

    <owl:NamedIndividual rdf:about="http://dbpedia.org/resource/United_Sates">
        <rdf:type rdf:resource="&obo;MEBDO_0000020"/>
        <rdfs:label xml:lang="en">United_States</rdfs:label>
    </owl:NamedIndividual>
    


    <!-- http://dbpedia.org/resource/Georgia_(U.S._state) -->

    <owl:NamedIndividual rdf:about="http://dbpedia.org/resource/Georgia_(U.S._state)">
        <rdf:type rdf:resource="&obo;MEBDO_0000011"/>
        <rdfs:label xml:lang="en">Georgia_(U.S._state)</rdfs:label>
        <obo:BFO_0000176 rdf:resource="http://dbpedia.org/resource/Georgia_(U.S._state)"/>
    </owl:NamedIndividual>
    


    <!-- http://dbpedia.org/resource/Hephzibah,_Georgia -->

    <owl:NamedIndividual rdf:about="http://dbpedia.org/resource/Hephzibah,_Georgia">
        <rdf:type rdf:resource="&obo;MEBDO_0000010"/>
        <rdfs:label xml:lang="en">Hephzibah,_Georgia</rdfs:label>
        <obo:BFO_0000176 rdf:resource="http://dbpedia.org/resource/Richmond_County,_Georgia"/>
        <obo:MEBDO_0000410 rdf:resource="&obo;MEBDO_0000412"/>
    </owl:NamedIndividual>
    


    <!-- http://dbpedia.org/resource/Richmond_County,_Georgia -->

    <owl:NamedIndividual rdf:about="http://dbpedia.org/resource/Richmond_County,_Georgia">
        <rdf:type rdf:resource="&obo;MEBDO_0000015"/>
        <rdfs:label xml:lang="en">Richmond_County,_Georgia</rdfs:label>
        <obo:BFO_0000176 rdf:resource="http://dbpedia.org/resource/Hephzibah,_Georgia"/>
    </owl:NamedIndividual>
    


    <!-- http://purl.obolibrary.org/obo/MEBDO_0000412 -->

    <owl:NamedIndividual rdf:about="&obo;MEBDO_0000412">
        <rdf:type rdf:resource="&obo;MEBDO_0000012"/>
        <rdfs:label xml:lang="en">30815 zip code zone in 2012</rdfs:label>
    </owl:NamedIndividual>

"""

from openpyxl import load_workbook

objectpropertyList = ['MEBDO_0000410','BFO_0000176']
classList = ['MEBDO_0000020','MEBDO_0000010','MEBDO_0000011','MEBDO_0000012', 'MEBDO_0000015']

fileName = 'mebdo_city_county_import.owl'
updateFile =  open('mebdo_city_county_import.owl','a')

US_state_city_county_postalCode.xls

updateFile.write('<?xml version="1.0"?>\n')
updateFile.write('<rdf:RDF xmlns="http://purl.obolirary.org/obo/mebdo/' + fileName +'#"\n')
updateFile.write('     xml:base="http://purl.obolirary.org/obo/mebdo/' + fileName + '"\n')
updateFile.write('     xmlns:obo="http://purl.obolibrary.org/obo/"\n     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"\n     xmlns:owl="http://www.w3.org/2002/07/owl#"\n     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"\n     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n')
updateFile.write('    <owl:Ontology rdf:about="http://purl.obolirary.org/obo/mebdo/'+ fileName +'"/>\n\n\n')
updateFile.write('    <!-- \n    ///////////////////////////////////////////////////////////////////////////////////////\n    //\n    // Object Properties\n    //\n    ///////////////////////////////////////////////////////////////////////////////////////\n     -->\n\n')

