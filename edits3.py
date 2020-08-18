import unittest
import pdb

def checkedits(word1, word2):
    def get_index(string, index):
        try:
            return string[index]
        except IndexError:
            return None

    state = 0
    idx1 = idx2 = 0
    print(word1, word2)

    loop = True

    while loop:

        # Get next element from word1 and word2
        w1 = get_index(word1, idx1)
        w2 = get_index(word2, idx2)

        if w1 != w2:
            state += 1

            # Check for replace
            if get_index(word1, idx1+1) == get_index(word2, idx2+1):
                pass # don't really need to do anything here

            # Check for delete in word2
            elif get_index(word1, idx1+1) == w2:
                idx1 += 1

            # Check for insert in word2
            elif w1 == get_index(word2, idx2+1):
                idx2 += 1


        if state > 1:
            loop = False
        elif w1 is None and w2 is None:
            loop = False


        idx1 += 1
        idx2 += 1

    return state <= 1

class TestCheckEdits(unittest.TestCase):

    def test_checkedits(self):
        self.assertTrue(checkedits('word1', 'word1'))
        self.assertTrue(checkedits('word1', 'word'))
        self.assertTrue(checkedits('word1', 'wod1'))
        self.assertTrue(checkedits('word1', 'wourd1'))
        self.assertTrue(checkedits('word1', 'wword1'))
        self.assertTrue(checkedits('word1', 'word1'))
        self.assertTrue(checkedits('word1', 'word13'))
        #pdb.set_trace()
        self.assertTrue(checkedits('word1', '2ord1'))
        self.assertFalse(checkedits('word1', 'wo1'))
        self.assertFalse(checkedits('word1', 'word123'))
        self.assertFalse(checkedits('word1', 'wurk1'))
        self.assertFalse(checkedits('word1', 'wwword1'))
        self.assertFalse(checkedits('word1', 'rd1'))
        self.assertFalse(checkedits('word1', 'wo13'))

if __name__ == '__main__':

    unittest.main(argv=[''], verbosity=2, exit=False)
