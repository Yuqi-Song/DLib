from tool.attackConfig import attackConfig
from collections import defaultdict
from tool.File import FileIO
import os
import sys
sys.path.append('../')
import numpy as np
import random

class Attack(object):
    def __init__(self, conf):
        self.config = attackConfig(conf)
        self.itemProfile = defaultdict(dict)
        self.attackSize = float(self.config['attackSize'])
        self.fillerSize = float(self.config['fillerSize'])
        self.selectedSize = float(self.config['selectedSize'])
        self.targetCount = int(self.config['targetCount'])
        self.targetScore = float(self.config['targetScore'])
        self.threshold = float(self.config['threshold'])
        self.minCount = int(self.config['minCount'])
        self.maxCount = int(self.config['maxCount'])
        self.minScore = float(self.config['minScore'])
        self.maxScore = float(self.config['maxScore'])
        self.outputDir = self.config['outputDir']
        self.startUserID = 0


        print(self.outputDir)
        self.userProfile = FileIO.loadRate(self.config, self.config['ratings'])

        if not os.path.exists(self.outputDir):
            os.makedirs(self.outputDir)
        for user in self.userProfile:
            for item in self.userProfile[user]:
                self.itemProfile[item][user] = self.userProfile[user][item]
        self.spamProfile = defaultdict(dict)
        self.spamItem = defaultdict(list) #items rated by spammers
        self.targetItems = []
        self.itemAverage = {}
        self.getAverageRating()
        self.insertSpam()
        self.generateLabels('labels.txt')
        self.generateProfiles('profiles.txt')



    def getAverageRating(self):
        for itemID in self.itemProfile:
            li = self.itemProfile[itemID].values()
            self.itemAverage[itemID] = float(sum(li)) / len(li)


    def selectTarget(self,):
        print ('Selecting target items...')
        print ('-'*80)
        print ('Target item       Average rating of the item')
        itemList = self.itemProfile.keys()

        #itemList.sort()

        sorted(itemList)
        while len(self.targetItems) < self.targetCount:
            target = np.random.randint(len(itemList)) #generate a target order at random

            if len(self.itemProfile[str(list(itemList)[target])]) < self.maxCount and len(self.itemProfile[str(list(itemList)[target])]) > self.minCount \
                    and str(list(itemList)[target]) not in self.targetItems \
                    and self.itemAverage[str(list(itemList)[target])] <= self.threshold:
                self.targetItems.append(str(list(itemList)[target]))
                print(str(list(itemList)[target]),'                  ',self.itemAverage[str(list(itemList)[target])])

    def getFillerItems(self):
        mu = int(self.fillerSize*len(self.itemProfile))
        sigma = int(0.1*mu)
        markedItemsCount = abs(int(round(random.gauss(mu, sigma))))
        markedItems = np.random.randint(len(self.itemProfile), size=markedItemsCount)
        return markedItems.tolist()

    def insertSpam(self,startID=0):
        pass

    def loadTarget(self,filename):
        with open(filename) as f:
            for line in f:
                self.targetItems.append(line.strip())

    def generateLabels(self,filename):
        labels = []
        path = self.outputDir + filename
        with open(path,'w') as f:
            for user in self.spamProfile:
                labels.append(user+' 1\n')
            for user in self.userProfile:
                labels.append(user+' 0\n')
            f.writelines(labels)
        print ('User profiles have been output to '+(self.config['outputDir'])+'.')

    def generateProfiles(self,filename):
        ratings = []
        path = self.outputDir+filename
        with open(path, 'w') as f:
            for user in self.userProfile:
                for item in self.userProfile[user]:
                    ratings.append(user+' '+item+' '+str(self.userProfile[user][item])+'\n')

            for user in self.spamProfile:
                for item in self.spamProfile[user]:
                    ratings.append(user + ' ' + item + ' ' + str(self.spamProfile[user][item])+'\n')
            f.writelines(ratings)
        print ('User labels have been output to '+(self.config['outputDir'])+'.')




