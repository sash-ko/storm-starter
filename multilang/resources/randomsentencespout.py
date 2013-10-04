import storm
import time
import random

class RandomSentenceSpout(storm.Spout):

    def nextTuple(self):
        sentences = [
            "the cow jumped over the moon",
            "an apple a day keeps the doctor away",
            "four score and seven years ago",
            "snow white and the seven dwarfs",
            "i am at two with nature"
        ]

        time.sleep(0.5)
        storm.emit([random.choice(sentences)])

if __name__ == '__main__':
    RandomSentenceSpout().run()
