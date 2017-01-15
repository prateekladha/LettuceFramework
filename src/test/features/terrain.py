from app.application import app
from lettuce import *
from nose.tools import *

@before.all
def before_all():
    print "Hello there!"
    print "Lettuce will start to run tests right now..."
    world.app = app.test_client()
    assert_equal.im_class.maxDiff = None

@after.all
def say_goodbye(total):
    print "Congratulations, %d of %d scenarios passed!" % (
        total.scenarios_ran,
        total.scenarios_passed
    )
    print "Goodbye!"

@before.each_feature
def setup_some_feature(feature):
    print "Running the feature %r, at file %s" % (
        feature.name,
        feature.described_at.file
    )

@after.each_feature
def teardown_some_feature(feature):
    print "The feature %r just has just ran" % feature.name

@before.each_step
def setup_some_step(step):
    print "running step %r, defined at %s" % (
        step.sentence,
        step.defined_at.file
    )

@after.each_step
def teardown_some_step(step):
    if not step.hashes:
       print "no tables in the step"

@before.each_outline
def setup_some_scenario(scenario, outline):
    print "We are now going to run scenario {0}".format(scenario.name)

@after.each_outline
def complete_some_scenario(scenario, outline):
    print "We are now finished scenario {0}".format(scenario.name)