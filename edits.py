import unittest
import pdb

def checkedits(word1, word2):

    idx = 0
    edits = 0

    if len(word1) == len(word2): # Change
        
        for idx, let in enumerate(word1):
            if let != word2[idx]:
                edits += 1
        if edits <= 1:
            return True
        else:
            return False
        
    elif len(word1) - 1 == len(word2): # Delete
        
        idx1 = 0
        idx2 = 0
        # pdb.set_trace()
        while idx1 < len(word1) and idx2 < len(word2):

            if word1[idx1] != word2[idx2]:
                edits += 1
                idx2 -= 1
            idx1 += 1
            idx2 += 1

        if edits <= 1:
            return True
        else:
            return False
        
    elif len(word1) + 1 == len(word2): # Insert

        idx1 = 0
        idx2 = 0
        while idx1 < len(word1) and idx2 < len(word2):

            if word1[idx] != word2[idx]:
                edits += 1
                idx1 -= 1
            idx1 += 1
            idx2 += 1

        if edits <= 1:
            return True
        else:
            return False
    else:
        return False


class TestCheckEdits(unittest.TestCase):
    
    def test_checkedits(self):
        self.assertTrue(checkedits('word1', 'word1'))
        self.assertTrue(checkedits('word1', 'word'))
        self.assertTrue(checkedits('word1', 'wod1'))
        self.assertTrue(checkedits('word1', 'wourd1'))
        self.assertTrue(checkedits('word1', 'wword1'))
        self.assertTrue(checkedits('word1', 'word1'))
        self.assertTrue(checkedits('word1', 'word13'))
        self.assertTrue(checkedits('word1', '2ord1'))
        self.assertFalse(checkedits('word1', 'wo1'))
        self.assertFalse(checkedits('word1', 'word123'))
        self.assertFalse(checkedits('word1', 'wurk1'))
        self.assertFalse(checkedits('word1', 'wwword1'))
        self.assertFalse(checkedits('word1', 'rd1'))
        self.assertFalse(checkedits('word1', 'wo13'))

if __name__ == '__main__':

    unittest.main(argv=[''], verbosity=2, exit=False)

