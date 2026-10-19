"""Run with python examples/synthetic_accounting/demo.py."""
from accounting import SyntheticLedger

def main():
    ledger=SyntheticLedger()
    print("SYNTHETIC ACCOUNTING DEMONSTRATION — NOT A BACKTEST")
    print("All symbols, prices and events are fictional.")
    print("initial",ledger.snapshot())
    ledger.buy("AAA","2","100",fee="1")
    ledger.buy("BBB","1","200",fee="1")
    print("purchases",ledger.snapshot())
    before=ledger.equity()
    ledger.split("AAA","4","split-001")
    assert ledger.equity()==before
    print("split",ledger.snapshot())
    ledger.dividend_ex("AAA","0.50","dividend-001")
    print("dividend entitlement",ledger.snapshot())
    before=ledger.equity()
    ledger.dividend_pay("dividend-001")
    assert ledger.equity()==before
    print("dividend payment",ledger.snapshot())
    ledger.sell("BBB","1","200",fee="1")
    print("sale",ledger.snapshot())
    print("No market data, investment signals, real orders or financial-return claims.")

if __name__=="__main__": main()
