# Synthetic Accounting Demonstrator

This is a **separate, deliberately small public demonstration**, not the private pilot code. It uses fictional instruments (`AAA`, `BBB`) and artificial reference prices, with no external Python dependencies or data-provider access.

It demonstrates three bookkeeping invariants:

1. A 4-for-1 split alters share count and per-share marking basis but does **not** create portfolio value.
2. Declaring a dividend receivable and subsequently paying it must **not** credit that dividend twice.
3. Explicit transaction fees decrease marked equity by the same amount when reference prices do not change.

```shell
python examples/synthetic_accounting/demo.py
python -m unittest discover -s examples/synthetic_accounting -p 'test_*.py' -v
```

The example omits venue/execution semantics, live orders, shorting, slippage, tax, settlement and other production accounting details. A dividend `ex` event uses the position held at that synthetic event; it is **not** a full real-world entitlement engine. It is not appropriate for trading or financial decisions.
