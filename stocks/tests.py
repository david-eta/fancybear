# """
# Functionality:
# - This test case class ('stocksTestCase') contains test methods for the 'Stock' model.

# Test Methods:
# 1. test_stock_creation: Tests the creation of a stock instance.
# 2. test_stock_deletion: Tests the deletion of a stock instance.
# 3. test_stock_retrieval: Tests the retrieval of a stock instance.
# 4. test_null_handling: Tests the handling of null values for the 'user' field (which doesn't exist in the 'Stock' model).
# 5. test_negative_quantity_self: Tests that the quantity of a stock is not negative.
# 6. test_update_stock: Tests the update of a stock instance.

# Note:
# - These test methods ensure that the 'Stock' model behaves as expected in terms of creation, deletion, retrieval, handling of null values, and updates.
# - The 'test_null_handling' and 'test_negative_quantity_self' methods may not be applicable to the 'Stock' model as it doesn't have a 'user' or 'quantity' field.
# - There's a redundant import statement for the 'Stock' model.
# - The 'test_negative_quantity_self' method should be renamed appropriately to reflect its purpose accurately.
# """

# from django.test import TestCase
# from stocks.models import Stock
# from stocks.models import Stock
# # Create your tests here.

      
# class stocksTestCase(TestCase):
#     def setUp(self):
#         self.ticker = "AAPL"
#         self.name = "Apple"
#         self.price = 30
#         self.category = "Tech"

#     def test_stock_creation(self):
#         '''Test the creation of a stock'''
#         # initialise object
#         stock  = Stock.objects.create(self.ticker, self.name, self.price, self.category)
#         # ensure creation works and is the same as what we have in the db
#         self.assertIsInstance(stock, Stock)
#         self.assertEqual(stock.ticker, self.ticker)
#         self.assertEqual(stock.name, self.name)
#         self.assertEqual(stock.price, self.price)
#         self.assertEqual(stock.category, self.category)

#     def test_stock_deletion(self):
#         '''Test the deletion of a stock'''
#         stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
#         stock.delete()
#         # make sure it's gone after deletion
#         self.assertFalse(Stock.objects.filter(id=stock.id).exists())

#     def test_stock_retrieval(self):
#         '''Test the retrieval of a stock'''
#         stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
#         retrieved_stock = Stock.objects.get(id=stock.id)
#         self.assertEqual(retrieved_stock, stock)
    
#     def test_null_handling(self):
#         '''Test the handling of null values for the user field'''
#         stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
#         self.assertIsNone(stock.user)
    
#     def test_negative_quantity_self(self):
#         '''Make sure there is no negative value for the stock quantity field'''
#         stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
#         self.assertGreaterEqual(stock.quantity, 0)

#     def test_update_stock(self):
#         '''Test the update of a stock'''
#         # initialise object
#         stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
#         # update stock
#         stock.price = 50
#         stock.save()
#         # ensure update works and is the same as what we have in the db
#         self.assertEqual(stock.price, 50)
