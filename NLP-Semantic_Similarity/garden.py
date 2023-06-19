import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["The old man the boat.", "The horse raced past the barn fell.", "Mary gave the child a Band-Aid",  "That Jill is never here hurts", "The cotton clothing is made of grows in Mississippi"]

# loop through each sentence in gardenpathSentences array
for i in gardenpathSentences:
    doc =nlp(i) 
    print([(i, i.label_, i.label) for i in doc.ents])
 
      

entity_person = spacy.explain('PERSON')
print(f"PERSON:{entity_person}")

entity_gpe = spacy.explain('GPE')
print(f"GPE:{entity_gpe}")
 
 # spaCy coprretly identifies Jill and Mary as persons as they are intended to be
 # spaCy correctly identifies Mississippi as a GPe (country, city, or state)


