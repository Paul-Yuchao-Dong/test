__author__ = 'Paul YC Dong'

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
        (G[node1])[node2] = 0
    (G[node1])[node2] += 1
    if node2 not in G:
        G[node2] = {}
        (G[node2])[node1] = 0
    (G[node2])[node1] += 1
    return G

#1 read file line by line and build a representation of the relationship like CS[comic1] = [SuperH1], [SuperH2], ...
i=0
CS={}
Str1_bg = 1
Str1_ed = 0
Str2_bg = 0
Str2_ed = 0
with open(r'C:\Users\Paul YC Dong\PycharmProjects\test\comics.txt') as fp:
    for line in iter(fp.readline, ''):
        #if i>5: break
        Str1_ed = line.find('"', Str1_bg)
        Str2_bg = line.find('"', Str1_ed+1)+1
        Str2_ed = line.find('"', Str2_bg)
        SuperH = line[Str1_bg:Str1_ed]
        comic = line[Str2_bg:Str2_ed]
        #print(line, SuperH, Comic)
        if comic in CS:
            CS[comic].append(SuperH)
        else:
            CS[comic]=[SuperH]
#print CS

#2 iterate thru each comic book and if both superheoros are in one comic, make and/or update link on them on g, so that g[superH1][superH2]=strength of their link
G={}
for comic in CS:
    length = len(CS[comic])
    for i in range(length-1):
        for j in range(i+1,length):
            make_link(G, (CS[comic])[i], (CS[comic])[j])

print G

#3 find the highest strength in G and printout its related SuperH1 and SuperH2
