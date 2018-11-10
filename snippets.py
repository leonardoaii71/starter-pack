import spacy
import hunspell


nlp = spacy.load('es')
hunspell.Hunspell('es_ANY')

doc = nlp()
