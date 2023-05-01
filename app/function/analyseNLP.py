def GetEmotionScore(text:str):

    positive_vocab = []
    negative_vocab = []

    res = ""

    with open("../data/negative-sentiment-words", 'r') as f:
        for line in f:
            negative_vocab.append(line.rstrip())

    with open("../data/positive-sentiment-words.txt", 'r') as f:
        for line in f:
            positive_vocab.append(line.rstrip())
    

    #requires tokenized input but Thai usually does not contain spaces between words

    sentences = [text]

    mainAll = 0 # of 100
    mainPos = 0 # of 100 (100 / mainAll) main Pos
    mainNeg = 0 # of 100

    for sentence in sentences:
        neg = 0
        pos = 0
        all = 0
        # print(sentence)
        words = sentence.split(' ')
        for word in words:
            if word in positive_vocab:
                pos = pos + 1
                all = all + 1
            if word in negative_vocab:
                neg = neg + 1
                all = all + 1

        if pos > neg:
            print('positive')
            res = "positive"
        elif neg > pos:
            print('negative')
            res = "negative"
        else:
            print('neutral')
            res = "neutral"
    mainAll = all
    mainPos = pos
    mainNeg = neg
    

    return {
        "emotion": {
            "Positive": (100 / mainAll) * mainPos,
            "Negative": (100 / mainAll) * mainNeg,
        },
        "analysis": res
    }