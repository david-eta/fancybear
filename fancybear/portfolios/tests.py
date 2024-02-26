from django.test import TestCase
from portfolios.models import Portfolio
from django.contrib.auth.models import User
from stocks.models import Stock

class PortfoliosTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.stock = Stock.objects.create(ticker='AAPL', name='Apple Inc.', price=500, category='Tech')
        self.quantity = 69

    def test_portfolio_creation(self):
        '''Test the creation of a Portfolio'''
        # initialise object
        portfolio = Portfolio.objects.create(user=self.user, stock=self.stock, quantity=self.quantity)
        # ensure creation works and is the same as what we have in the db
        self.assertIsInstance(portfolio, Portfolio)
        self.assertEqual(portfolio.user, self.user)
        self.assertEqual(portfolio.stock, self.stock)
        self.assertEqual(portfolio.quantity, self.quantity)

    def test_portfolio_deletion(self):
        '''Test the deletion of a Portfolio'''
        portfolio = Portfolio.objects.create(user=self.user, stock=self.stock, quantity=self.quantity)
        portfolio.delete()
        # make sure it's gone after deletion
        self.assertFalse(Portfolio.objects.filter(id=portfolio.id).exists())

    def test_portfolio_retrieval(self):
        '''Test the retrieval of a portfolio'''
        portfolio = Portfolio.objects.create(user=self.user, stock=self.stock, quantity=self.quantity)
        retrieved_portfolio = Portfolio.objects.get(id=portfolio.id)
        self.assertEqual(retrieved_portfolio, portfolio)
    
    def test_null_handling(self):
        '''Test the handling of null values for the user field'''
        portfolio = Portfolio.objects.create(user=None, stock=self.stock, quantity=self.quantity)
        self.assertIsNone(portfolio.user)
        
    def test_positive_quantity(self):
        '''Test that the quantity of a portfolio is always positive'''
        portfolio = Portfolio.objects.create(user=self.user, stock=self.stock, quantity=-1)
        self.assertGreaterEqual(portfolio.quantity, 0)
        
        
def test_zero_or_negative_quantity(self):
    '''Test that the quantity of a portfolio is null when all stocks have been sold or deleted'''
    portfolio = Portfolio.objects.create(user=self.user, stock=self.stock, quantity=0)
    self.assertIsNone(portfolio.quantity)        
    
def test_price_update(self):
    '''Test that the total value of a portfolio reflects the updated price of the stock'''
    portfolio = Portfolio.objects.create(user=self.user, stock=self.stock, quantity=self.quantity)
    initial_total_value = portfolio.stock.price * portfolio.quantity
    self.stock.price += 100
    self.stock.save()
    updated_total_value = portfolio.stock.price * portfolio.quantity
    self.assertGreater(updated_total_value, initial_total_value)
    
def test_quantity_change(self):
    '''Test that the quantity of a stock in a portfolio changes when stocks are bought or sold'''
    portfolio = Portfolio.objects.create(user=self.user, stock=self.stock, quantity=self.quantity)
    portfolio.buy(10)
    self.assertEqual(portfolio.quantity, self.quantity + 10)
    portfolio.sell(5)
    self.assertEqual(portfolio.quantity, self.quantity + 5)
    

