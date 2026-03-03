import spacy
base=spacy.load("en_core_web_sm")
text="""Mr.G.Mano is a highly skilled software engineer who has been working efficiently at infosys for the past ten years. He completed his Master's degree in CSE forom Anna University and is currently living in VIrudhunagar."""
doc=base(text)
print("NOUN PHRASES(NP):")
for chunk in doc.noun_chunks:
    print(chunk.text)
print("\nVERB PHRASES(VP):")
for token in doc:
    if token.pos_=="VERB":
        print(token.text)
print("\nADJECTIVE PHRASES(ADJ):")
for token in doc:
    if token.pos_=="ADJ":
        print(token.text)
print("\nADVERB PHRASES(ADV):")
for token in doc:
    if token.pos_=="ADV":
        print(token.text)
