import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. 

# open, read files - store in array 'sentences'
my_file = open("movies.txt", "r")
sentences = my_file.readlines()          

planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

# function to determine most similar movie to planet hulk
    # loop through sentences and compare similarity with model sentence
    # then store the most similar movie and score to be output
def similarity(sentence_to_compare):
    model_sentence = nlp(sentence_to_compare)
    highest_similarity = 0
    for sentence in sentences:
    # 'sentence[9:-2]' - remove 'Movie X :' and '\n' for more 
    #  accurate similarity scores
        similarity = nlp(sentence[9:-2]).similarity(model_sentence) 
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_sentence = sentence.strip('\n')
    return most_similar_sentence, highest_similarity

# output movie title and similarity score to Planet Hulk
print(f"{similarity(planet_hulk)[0][:7]} is most similar to Planet Hulk with a similarity score of {similarity(planet_hulk)[1]}")
