import unittest

def checkedits(w1, w2):
    state = 0
    idx1 = idx2 = 0

    while idx1 < len(w1) and idx2 < len(w2):

        if w1[idx1] != w2[idx2]:
            # peak
            try:
                # check for change
                if w1[idx1+1] == w2[idx2+1]:
                    state += 1
                    idx1 += 1
                    idx2 += 1
                # check for delete in w2
                elif w1[idx+1] == w2[idx2]:
                    state += 1
                    idx1 += 2
                    idx2 += 1
                # check for insert
                elif w1[idx] == w2[idx2+1]:
                    state += 1
                    idx1 += 1
                    idx2 += 2
                else:
                    return False
            except IndexError:
                state += 1
        
        return state == 0 or state == 3

class TestCheckEdits(unittest.TestCase):

    def test_checkedits(self):
        self.assertTrue(checkedits('word1', 'word1'))
        self.assertTrue(checkedits('word1', 'word'))
        self.assertTrue(checkedits('word1', 'wod1'))
        self.assertTrue(checkedits('word1', 'wourd1'))
        self.assertTrue(checkedits('word1', 'wword1'))
        self.assertTrue(checkedits('word1', 'word1'))
        self.assertTrue(checkedits('word1', 'word13'))
        #self.assertTrue(checkedits('word1', '2ord1'))
        self.assertFalse(checkedits('word1', 'wo1'))
        self.assertFalse(checkedits('word1', 'word123'))
        self.assertFalse(checkedits('word1', 'wurk1'))
        self.assertFalse(checkedits('word1', 'wwword1'))
        self.assertFalse(checkedits('word1', 'rd1'))
        self.assertFalse(checkedits('word1', 'wo13'))

if __name__ == '__main__':

    unittest.main(argv=[''], verbosity=2, exit=False)
