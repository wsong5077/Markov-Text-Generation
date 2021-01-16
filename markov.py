import random
PUNCTUATION = [".", "!", "?"]

def dollarify(wordList, k):
    """This function embeds k of special $ delimiters in the list of words
       Input: A list of words and a positive integer k corresponding to the number of $ delimiter.
       Output: A list of words with special $ delimiters embedded"""
    L=['$']*k
    for i in range(len(wordList)):
        if len(wordList[i])!=1:
            if i==len(wordList)-1: 
                L=L+[wordList[i]]
                break
            else: L=L+[wordList[i]]+['$']*k
        else:
            L=L+[wordList[i]]
    return L

def markov_model(wordList,k):
    """This function builds an nth order Markov model for a given list of words.
       Input:  A list of words and a positive integer n corresponding to the order of the Markov model.
       Output:  A dictionary in which the keys are n-tuples of words and/or dollar signs and the value associated 
       with each key is the list of words that follow that n-tuple."""
    D={}
    M=dollarify(wordList,k)
    for i in range(len(M)-k):
        K=[]
        for j in range(i,i+k):
            K.append(M[j])
        a=0
        for element in K:
            if len(element)==1:
                a+=0
            else: a+=1
        if a!=0: pass
        else:
            if k==1:
                if (M[i],) in D: D[(M[i],)].append(M[i+1])
                else: D[(M[i],)]=[M[i+1]]
            else:                
                if tuple(K) in D: D[tuple(K)].append(M[i+k])
                else: D[tuple(K)]=[M[i+k]]
    return D

def gen_from_model(mmodel, numwords):
    """This function generates words from a model.
       Input: A Markov model named mmodel, an integer, numwords, which is the number of words for it to print from that model
       Output: numwords words generated from the Markov model"""
    L=list(mmodel.keys())
    string=''
    l=len(L[0])*['$']
    for i in range(numwords):
        lst=list(mmodel[tuple(l)])
        if len(string)>=4 and string[-4]=='B' and string[-2]=='B' and 'B' in lst:
            lst.remove('B')
        elif len(string)>=4 and string[-4]=='D' and string[-2]=='D' and 'D' in lst:
            lst.remove('D')
        elif len(string)>=2 and string[-2] not in PUNCTUATION and 'A' in lst:
            lst.remove('A')
        elif len(string)>=2 and string[-2]=='C' and 'B' in lst:
            lst.remove('B')
        elif i==numwords:
            for j in range(len(lst)):
                if len(lst[j])==1:
                    lst.remove(lst[j])
        c1=random.choice(lst)
        string+=c1+' '
        if len(c1)!=1:
            l=len(L[0])*['$']
        else:
            l=l[1:]+[c1]
    print (string)

def markov(filename,k,length):
    """This function opens a file, reads in the contents, generates the k-th order Markov model, and then generates output of the given length.
       Input:a string containing a file name, the model parameter k, and a positive integer length indicating the length of the output that you'd like to have generated.
       Output: words of given length generated from the file"""
    f=open(filename,"r")
    inputList = f.readlines()
    cleanList = [x.strip("\n") for x in inputList]
    D=markov_model(cleanList,k)
    return gen_from_model(D,length)

"""in beauties niggarding: ſelfe now thy by ſelfe time by Making as thy the thine increaſe, by thy beare a famine freſh increaſe, thee. beauties aboundance fewell, thy Pitty thou 
ſelfe the chorle But in thy might gaudy ſelfe riper graue now thy that world,or Pitty Thou Thy deceaſe, that deceaſe, die, with bud ſhould thee. thine lights Making bud be, as 
where And art die, increaſe, ſelfe flame be, Within the the And makſt by freſh thou burieſt fewell, only bright makſt ſhould art lies, And tender that thy worlds But we where that art fewell, chorle to Roſe"""