from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds",4)
        
        self.assertTrue('War of the Worlds' in test_object.book_list['book_name'].unique())
    def test_2_add_book(self):
        test_object2 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object2.add_book("War of the Worlds",4)
        test_object2.add_book("War of the Worlds",4)
        
        expected = 1
        
        self.assertEqual(expected,len(test_object2.book_list))
    def test_3_has_read(self):
         
        test_object3 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object3.add_book("War of the Worlds",4)
        
        self.assertTrue(test_object3.has_read("War of the Worlds"))
        
    def test_4_has_read(self):
        test_object4 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object4.add_book("War of the Worlds",4)
        
        self.assertFalse(test_object4.has_read("hey"))
        
    def test_5_num_books_read(self):
        test_object5 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object5.add_book("War of the Worlds",4)
        test_object5.add_book("Nightengale",5)
        test_object5.add_book("Lying Game",1)
        
        expected = 3
        
        self.assertEqual(test_object5.num_books_read(),expected)
        
    def test_6_fav_books(self):
        test_object5 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object5.add_book("War of the Worlds",4)
        test_object5.add_book("Nightengale",5)
        test_object5.add_book("Lying Game",1)
        
        favs = test_object5.fav_books()
        self.assertTrue(all(i>3 for i in favs['book_rating']))
        # assertTrue(test_object5.book_list.loc[book_list['rating']>3] == fav_books)
        
        
if __name__ == '__main__':

    unittest.main(verbosity=3)
        