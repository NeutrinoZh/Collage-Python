import winsound

sounds = [
    (659,250), (659,250), (659,300), (523,250), (659,250),
    (784,300), (392,300), (523,275), (392,275), (330,275),
    (440,250), (494,250), (466,275), (440,275), (392,275),
    (659,250), (784,250), (880,275), (698,275), (784,225),
    (659,250), (523,250), (587,225), (494,225)
]

freq = []
duration = []

for a, b in sounds:
    freq.append(a)
    duration.append(b)

for i in range(len(sounds)):
    winsound.Beep(freq[i], duration[i])