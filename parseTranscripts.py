# parseTranscripts.py
# loads in audio transcriptions and extracts event times
# Currently doesn't work with phrase tier transcripts
import numpy as np

def parseTextGrid(fname,badTimes):
    with open(fname) as tg:
        content = tg.readlines()

    label = []
    start = []
    stop = []
    tier = []

    
    t = 0;
    c = -1;
    tiers = ['phoneme','word','phrase']
    for line in content:
        c = c+1;
        if 'item [2]:' in line:
            t = 1;
        if 'item [3]:' in line:
            t = 2;
        if 'text =' in line:
            if line[20:-3] == 'sp'  or not line[20:-3]:
                continue     
            
            label.append(line[20:-3])
            start.append(float(content[c-2][19:-2]))
            stop.append(float(content[c-1][19:-2]))
            tier.append(tiers[t])
    label = np.array(label)
    start = np.array(start)
    stop = np.array(stop)
    tier = np.array(tier)
    
    phones = np.where(tier == 'phoneme')[0]
    words = np.where(tier == 'word')[0]
    
    contained_by = [-1]*label.size
    contains = [-1]*label.size
    position = np.ones(label.size)*-1
    
    if t == 2:  #If this transript has a phrase tier
        phrase = np.where(tier == 'phrase')
        for ind in phrase:
            position[ind] = 1   #phrase is highest, therefore pos is always 1
            contained_by[ind] = -1;
            
            #Find contained words and phonemes
            lower = start[ind] - 0.01
            upper = stop[ind] + 0.01
            startCandidates = np.where(start >= lower)[0]
            stopCandidates = np.where(stop <= upper)[0]     
            intersect = np.intersect1d(startCandidates,stopCandidates)
            contains[ind] = list(np.intersect1d(startCandidates,stopCandidates))
            contains[ind].remove(ind)
            contains[ind] = np.array(contains[ind])
            
    for ind in words:
        if t == 1: #If no phrase tier, word is highest tier
            position[ind] = 1
            contained_by[ind] = -1;   
        
        #Find contained phonemes
        lower = start[ind] - 0.01
        upper = stop[ind] + 0.01
        startCandidates = np.where(start >= lower)[0]
        stopCandidates = np.where(stop <= upper)[0]     
        intersect = np.intersect1d(startCandidates,stopCandidates)
        cont = list(intersect)
        cont.remove(ind)
        contains[ind] = cont       
        for i in cont:
            contained_by[i] = ind

        
    for ind in phones:
        
        #Find words and prases that is contained by
        
        sameWord = np.where(np.asarray(contained_by) == contained_by[ind])[0]
        position[ind] = np.where(sameWord == ind)[0] + 1
        
       
    contains = np.asarray(contains, dtype=object)
    contained_by = np.asarray(contained_by, dtype=object)
                 
    events = {'label':label,'start':start,'stop':stop,'tier':tier,'contains':contains,'contained_by':contained_by,'position':position}
    return events


