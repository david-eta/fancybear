# """
# Defines test cases for the Trade model.

# Test Cases:
#     - test_trade_creation: Tests the creation of a trade instance.
#     - test_trade_deletion: Tests the deletion of a trade instance.
#     - test_trade_retrieval: Tests the retrieval of a trade instance.
#     - test_null_handling: Tests the handling of null values for the user field.

# Dependencies:
#     - django.test.TestCase: Base class for Django test cases.
#     - trades.models.Trade: Trade model for testing.
#     - django.contrib.auth.models.User: User model for creating test users.
#     - stocks.models.Stock: Stock model for creating test stocks.
#     - datetime.datetime: Module for manipulating dates and times.

# """

# from django.test import TestCase
# from trades.models import Trade
# from django.contrib.auth.models import User
# from stocks.models import Stock
# from datetime import datetime
# # Create your tests here.

# class tradesTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
#         self.stock = Stock.objects.create(ticker='AAPL', name='Apple Inc.', price=500, category='Tech')
#         self.quantity = 10
#         self.date = datetime.now().date()
#         self.time = datetime.now().time()
#         self.action = "buy"

#     def test_trade_creation(self):
#         '''Test the creation of a trade'''
#         # initialise object
#         trade = Trade.objects.create(self.user, self.stock, self.quantity, self.date, self.time, self.action)
#         # ensure creation works and is the same as what we have in the db
#         self.assertIsInstance(trade, Trade)
#         self.assertEqual(trade.user, self.user)
#         self.assertEqual(trade.stock, self.stock)
#         self.assertEqual(trade.quantity, self.quantity)
#         self.assertEqual(trade.date, self.time)
#         self.assertEqual(trade.action, self.action)

#     def test_trade_deletion(self):
#         '''Test the deletion of a trade'''
#         trade = Trade.objects.create(self.user, self.stock, self.quantity, self.date, self.time, self.action)
#         trade.delete()
#         # make sure it's gone after deletion
#         self.assertFalse(Trade.objects.filter(id=trade.id).exists())

#     def test_trade_retrieval(self):
#         '''Test the retrieval of a trade'''
#         trade = Trade.objects.create(self.user, self.stock, self.quantity, self.date, self.time, self.action)
#         retrieved_trade = Trade.objects.get(id=trade.id)
#         self.assertEqual(retrieved_trade, trade)
    
#     def test_null_handling(self):
#         '''Test the handling of null values for the user field'''
#         trade = Trade.objects.create(user=None, stock=self.stock)
#         self.assertIsNone(trade.user)
        
    