# parseTranscripts.py
# loads in audio transcriptions and extracts event times



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
            if line[20:-4] is 'sp'  or not line[20:-4]:
                continue     
            
            label.append(line[20:-4])
            start.append(content[c-2][19:-2])
            stop.append(content[c-1][19:-2])
            tier.append(tiers[t])
        
    events = {'label':label,'start':start,'stop':stop,'tier':tier}
    return events


