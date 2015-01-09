""" outpatient individual payment
   <!-- http://purl.obolibrary.org/obo/MEBDO_0000415 -->

    <owl:NamedIndividual rdf:about="&obo;MEBDO_0000415">
        <rdf:type rdf:resource="&obo;MEBDO_0000043"/>
        <rdfs:label xml:lang="en">outpatient service 1</rdfs:label>
        <obo:MEBDO_0000026 rdf:resource="&obo;MEBDO_0000408"/>
        <obo:MEBDO_0000414 rdf:resource="&obo;MEBDO_0000416"/>
        <obo:MEBDO_0000417 rdf:resource="&obo;MEBDO_0000418"/>
        <obo:MEBDO_0000414 rdf:resource="&obo;MEBDO_0000419"/>
    </owl:NamedIndividual>
    


    <!-- http://purl.obolibrary.org/obo/MEBDO_0000416 -->

    <owl:NamedIndividual rdf:about="&obo;MEBDO_0000416">
        <rdf:type rdf:resource="&obo;MEBDO_0000032"/>
        <rdfs:label xml:lang="en">161.58</rdfs:label>
    </owl:NamedIndividual>
    


    <!-- http://purl.obolibrary.org/obo/MEBDO_0000418 -->

    <owl:NamedIndividual rdf:about="&obo;MEBDO_0000418">
        <rdf:type rdf:resource="&obo;MEBDO_0000027"/>
        <rdfs:label xml:lang="en">1053</rdfs:label>
        <obo:MEBDO_0000028 rdf:datatype="&xsd;integer">2012</obo:MEBDO_0000028>
    </owl:NamedIndividual>
    


    <!-- http://purl.obolibrary.org/obo/MEBDO_0000419 -->

    <owl:NamedIndividual rdf:about="&obo;MEBDO_0000419">
        <rdf:type rdf:resource="&obo;MEBDO_0000022"/>
        <rdfs:label xml:lang="en">33.59</rdfs:label>
    </owl:NamedIndividual>
    

"""

from openpyxl import load_workbook

wb = load_workbook(filename = 'Medicare_Provider_Charge_Outpatient_APC30_CY2012.xlsx')
ws = wb.get_sheet_by_name( name = 'opps_apc_summary')

