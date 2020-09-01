TERMS_RDF = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/skosno#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://dataverk.nav.no> a skos:Collection ;
    rdfs:label "Godkjente begreper"@nb ;
    dct:description "NAV godkjente begreper"@nb ;
    dct:publisher <https://data.brreg.no/enhetsregisteret/oppslag/enheter/889640782> ;
    skos:member <https://dataverk.nav.no/begrep/BEGREP-1694> .

<https://dataverk.nav.no/begrep/BEGREP-1694> a skos:Concept ;
    dct:modified "2020-05-05"^^xsd:date ;
    dct:publisher <https://data.brreg.no/enhetsregisteret/oppslag/enheter/889640782> ;
    dct:subject "Ytelsesavdelingen"@nb ;
    skosxl:prefLabel [ a skosxl:Label ;
            skosxl:literalForm "Business Use Case (EESSI)"@nb ] ;
    dcat:contactPoint [ a vcard:Organization ;
            vcard:hasEmail <mailto:begrepskatalogen@nav.no> ;
            vcard:hasOrganizationName ""@nb ] ;
    ns1:definisjon [ a ns1:Definisjon ;
            rdfs:label "<p>Et bruksområde av Use Case som beskriver typiske forretningsoperasjoner mellom en aktør på utsiden og en organisasjon.</p>"@nb ;
            dct:source [ rdfs:label "<p>EESSI Architecture Overview Document</p>"@nb ] ;
            ns1:forholdTilKilde ns1:basertPåKilde ] .

"""
