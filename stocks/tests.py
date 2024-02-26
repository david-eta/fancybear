from django.test import TestCase
from stocks.models import Stock
from stocks.models import Stock
# Create your tests here.

      
class stocksTestCase(TestCase):
    def setUp(self):
        self.ticker = "AAPL"
        self.name = "Apple"
        self.price = 30
        self.category = "Tech"

    def test_stock_creation(self):
        '''Test the creation of a stock'''
        # initialise object
        stock  = Stock.objects.create(self.ticker, self.name, self.price, self.category)
        # ensure creation works and is the same as what we have in the db
        self.assertIsInstance(stock, Stock)
        self.assertEqual(stock.ticker, self.ticker)
        self.assertEqual(stock.name, self.name)
        self.assertEqual(stock.price, self.price)
        self.assertEqual(stock.category, self.category)

    def test_stock_deletion(self):
        '''Test the deletion of a stock'''
        stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
        stock.delete()
        # make sure it's gone after deletion
        self.assertFalse(Stock.objects.filter(id=stock.id).exists())

    def test_stock_retrieval(self):
        '''Test the retrieval of a stock'''
        stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
        retrieved_stock = Stock.objects.get(id=stock.id)
        self.assertEqual(retrieved_stock, stock)
    
    def test_null_handling(self):
        '''Test the handling of null values for the user field'''
        stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
        self.assertIsNone(stock.user)
    
    def test_negative_quantity_self(self):
        '''Make sure there is no negative value for the stock quantity field'''
        stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
        self.assertGreaterEqual(stock.quantity, 0)

    def test_update_stock(self):
        '''Test the update of a stock'''
        # initialise object
        stock = Stock.objects.create(self.ticker, self.name, self.price, self.category)
        # update stock
        stock.price = 50
        stock.save()
        # ensure update works and is the same as what we have in the db
        self.assertEqual(stock.price, 50)
