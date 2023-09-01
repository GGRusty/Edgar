- the taxonomy is the common language framework for XBRL reporting 
- the taxonomy schema is the heart of the taxonomy and defines the concepts of the taxonomy and is used to tag the data
- linkbases are individual XML files that bring structure to concepts and link them to additional information
- relation linkbases create hierarchiacal relationships between concepts and define the relationships between concepts
    - the structures are created using XLink and extend links
    - the locators reference the concepts of the taxonomy which are declared in the schema 
    - arcs are used to define the relationships between concepts such as assetscurrent and assets'

    - calculation linkbases define the relationships between concepts that are used in calculations such as assetscurrent + assetsnoncurrent = assets
    - presentation linkbases describe the order in whihc concepts should be presented in a report 
    - definition linkbases provide additional information about concepts For example, a link with the arcrole “essence-alias” can be used to emphasize that two concepts cover the same or very similar subject matter.

- reference linkbases add resources to concepts
    - label linkbases add labels to concepts
    - reference linkbases add resources to concepts such as non xbrl files such as laws and regulations

