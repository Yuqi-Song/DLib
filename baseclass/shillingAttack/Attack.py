from tool.attackConfig import attackConfig
from collections import defaultdict
import sys
sys.path.append('../')

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




