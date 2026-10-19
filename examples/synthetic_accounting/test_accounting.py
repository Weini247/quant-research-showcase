"""Unittest-only checks on deterministic synthetic data."""
import unittest
from decimal import Decimal
from accounting import SyntheticLedger,dec

class TestSyntheticAccounting(unittest.TestCase):
    def test_buy_sets_positions_and_cash(self):
        p=SyntheticLedger();p.buy("AAA","2","100",fee="1")
        self.assertEqual(p.cash,Decimal("9799"));self.assertEqual(p.holdings["AAA"],Decimal("2"));self.assertEqual(p.equity(),Decimal("9999"))
    def test_split_changes_share_basis_without_creating_equity(self):
        p=SyntheticLedger();p.buy("AAA","2","100");v=p.equity();p.split("AAA","4","split-1")
        self.assertEqual(p.holdings["AAA"],Decimal("8"));self.assertEqual(p.marks["AAA"],Decimal("25"));self.assertEqual(p.equity(),v)
    def test_dividend_entitlement_and_payment_not_double_counted(self):
        p=SyntheticLedger();p.buy("AAA","2","100");v=p.equity();p.dividend_ex("AAA","0.50","div-1")
        self.assertEqual(p.receivables["div-1"],Decimal("1.00"));self.assertEqual(p.equity(),v+Decimal("1.00"))
        w=p.equity();p.dividend_pay("div-1");self.assertEqual(p.equity(),w);self.assertEqual(p.receivables,{})
    def test_duplicate_split_rejected(self):
        p=SyntheticLedger();p.buy("AAA","1","100");p.split("AAA","2","split-1")
        with self.assertRaises(ValueError):p.split("AAA","2","split-1")
    def test_duplicate_dividend_entitlement_rejected(self):
        p=SyntheticLedger();p.buy("AAA","1","100");p.dividend_ex("AAA","0.5","div-1")
        with self.assertRaises(ValueError):p.dividend_ex("AAA","0.5","div-1")
    def test_duplicate_payment_rejected(self):
        p=SyntheticLedger();p.buy("AAA","1","100");p.dividend_ex("AAA","1","div-1");p.dividend_pay("div-1")
        with self.assertRaises(ValueError):p.dividend_pay("div-1")
    def test_sell_cannot_create_short(self):
        p=SyntheticLedger()
        with self.assertRaises(ValueError):p.sell("AAA","1","100")
    def test_fees_reconcile(self):
        p=SyntheticLedger();p.buy("AAA","1","100",fee="1");p.sell("AAA","1","100",fee="1")
        self.assertEqual(p.equity(),Decimal("9998"));self.assertEqual(p.fees,Decimal("2"))
    def test_float_inputs_rejected(self):
        with self.assertRaises(TypeError):dec(0.1)
    def test_nonfinite_price_rejected(self):
        p=SyntheticLedger()
        with self.assertRaises(ValueError):p.buy("AAA","1",Decimal("NaN"))
    def test_zero_position_has_no_dividend_entitlement(self):
        p=SyntheticLedger();self.assertEqual(p.dividend_ex("AAA","1","div-1"),Decimal("0"));p.dividend_pay("div-1");self.assertEqual(p.cash,Decimal("10000"))
    def test_no_unfunded_purchase(self):
        p=SyntheticLedger(cash=Decimal("20"))
        with self.assertRaises(ValueError):p.buy("AAA","1","21")

if __name__=="__main__": unittest.main()
