# Copyright (c) 2011-2012 Ryan Bourgeois <bluedragonx@gmail.com>
#
# This project is free software according to the BSD-modified license. Refer to
# the LICENSE file for complete details.
"""
Base test case classes.
"""


class BaseCase(unittest.TestCase):

    """
    Set up test data for test cases.
    """

    def setUp(self):
        """Set up test data."""
        self.outputpath = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), 'output')

        self.models = [
            DummyModel('apple', 
                'a red fruit that grows on trees'),
            DummyModel('carrot', 
                'an orange vegetable that grows in the ground'),
            DummyModel('kiwi',
                'a brown fruit that is not a flightless bird')]
        self.model = self.models[0]

        fs = FieldSet(DummyModel)
        fs.configure(include=[fs.name, fs.text])
        self.fieldset_rw = fs.bind(self.model)
        fs.configure(include=[fs.name, fs.text], readonly=True)
        self.fieldset_ro = fs.bind(self.model)

        grid = Grid(DummyModel)
        grid.configure(include=[grid.name, grid.text])
        self.grid_rw = grid.bind(self.models)
        grid.configure(include=[grid.name, grid.text], readonly=True)
        self.grid_ro = grid.bind(self.models)

    def get_output(self, name):
        """Get the contents of an output file."""
        outputfile = os.path.join(self.outputpath, "%s.out" % name)
        with open(outputfile) as fd:
            return fd.read()

