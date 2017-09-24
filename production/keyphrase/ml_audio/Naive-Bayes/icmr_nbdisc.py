import orange,  orngFSS
import orngTree

#Constructs a Learner
class Learner(object):
    def __new__(cls, examples=None, name='discretized bayes', **kwds):
        learner = object.__new__(cls, **kwds)
        if examples:
            learner.__init__(name)
            return learner(examples)
        else:
            return learner

    def __init__(self, name='discretized bayes'):
        self.name = name

    #Discretization is performed on the samples
    #Then the samples are fed into learner
    def __call__(self, data, weight=None):
        disc = orange.Preprocessor_discretize(data, method=orange.EntropyDiscretization())
        #show_values(disc, "Entropy based discretization") 
        model = orange.BayesLearner(disc, weight,  adjustThreshold=0)
        #print "model.distribution", model.distribution
        #print "model.conditionalDistributions", model.conditionalDistributions
        return Classifier(classifier = model)

#Constructs a classifier
class Classifier:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    def __call__(self, example, resultType = orange.GetBoth):
        return self.classifier(example, resultType)
