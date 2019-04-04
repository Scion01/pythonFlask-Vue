import numpy as np
#numpy is lib for math tools
import pandas as pd
#for reading csv datasets
#dataset.ID dataset.TIMESTAMP to access each column/attribute
#Questions 1) Print Titles of All Stories between timestamps A and timestamps B
#2) Print names of top 3 publishers along with titles of their stories
#3) Print first n  stories sorted by title names in ascending order where n is a user input
class NewsAnalyzer:

    def __init__(self):
        self.dataset = pd.read_csv("news.csv")
        #preprocess your dataset here!
    
    #in each of the functions below ypu just need to return the correct output
    #for example if dataset.ID is your answer then return datatset.ID
    def prob1(self,t1,t2):
        times = self.dataset[(self.dataset.TIMESTAMP>t1)&(self.dataset.TIMESTAMP<t2)]
        return list(times.TITLE)
    
    def prob2(self):
        pub = self.dataset.PUBLISHER
        pub_unique = pub.drop_duplicates()
        pub_unique = list(pub_unique)
        out = []
        sum_max =0
        index = 0
        count = 0
        pub = list(pub)
        for i in range(0,3):
            sum_max=0
            index = 0
            count =0
            for j in range(0,len(pub_unique)):
                count =0
                for k in pub:
                    if(pub_unique[j] == k):
                        count = count+1
                if count > sum_max:
                    sum_max = count
                    index = j
            out.append(pub_unique[index])
            pub_unique.remove(pub_unique[index])
        titles = self.dataset.TITLE
        titles = list(titles)
        final_out = []
        for i in out:
            final_out.append(i)
            for j in range(0,len(titles)):
                if i == pub[j]:
                    final_out.append(titles[j])
        return final_out
    
    def prob3(self,n):
        df=self.dataset.sort_values('TITLE')
        return list(df[0:n].TITLE)
