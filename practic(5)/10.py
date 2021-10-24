# 5 (0,3)

import random

articles = ["the", "a", "one", "some", "any"]
nouns = ["boy", "girl", "dog", "town", "car"]
verbs = ["drove", "jumped", "ran", "walked", "skipped"]
prepositions = ["to", "from", "over", "under", "on"]

article0 = random.randint(0, len(articles) - 1)
noun0 = random.randint(0, len(nouns) - 1)
verb0 = random.randint(0, len(verbs) - 1)
preposition0 = random.randint(0, len(prepositions) - 1)
preposition1 = random.randint(0, len(prepositions) - 1)
article1 = random.randint(0, len(articles) - 1)
noun1 = random.randint(0, len(nouns) - 1)

print(
    articles[article0], 
    nouns[noun0],
    verbs[verb0],
    prepositions[preposition0],
    prepositions[preposition1],
    articles[article1],
    nouns[noun1]
)