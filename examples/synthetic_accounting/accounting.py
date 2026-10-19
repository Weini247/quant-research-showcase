"""A standalone fictional cash-and-shares ledger; not a trading engine."""
from dataclasses import dataclass, field
from decimal import Decimal

def dec(x):
    if isinstance(x,(float,bool)):
        raise TypeError("Pass exact quantities using str, int or Decimal")
    return Decimal(x)

@dataclass
class SyntheticLedger:
    cash: Decimal=Decimal("10000")
    holdings: dict[str,Decimal]=field(default_factory=dict)
    marks: dict[str,Decimal]=field(default_factory=dict)
    receivables: dict[str,Decimal]=field(default_factory=dict)
    seen_events: set[str]=field(default_factory=set)
    fees: Decimal=Decimal("0")

    def __post_init__(self): self.cash=dec(self.cash)
    def _symbol(self,s):
        if not isinstance(s,str) or not s.strip(): raise ValueError("Empty symbol")
    def _positive(self,x):
        if not x.is_finite() or x<=0: raise ValueError("Nonpositive/nonfinite value")
    def _fee(self,x):
        f=dec(x)
        if not f.is_finite() or f<0: raise ValueError("Invalid fee")
        return f
    def mark(self,s,price):
        self._symbol(s); p=dec(price); self._positive(p);self.marks[s]=p
    def buy(self,s,quantity,price,fee="0"):
        self._symbol(s);q,p,f=dec(quantity),dec(price),self._fee(fee)
        self._positive(q);self._positive(p)
        total=q*p+f
        if self.cash<total: raise ValueError("Insufficient cash")
        self.cash-=total;self.holdings[s]=self.holdings.get(s,Decimal("0"))+q
        self.marks[s]=p;self.fees+=f
    def sell(self,s,quantity,price,fee="0"):
        self._symbol(s);q,p,f=dec(quantity),dec(price),self._fee(fee)
        self._positive(q);self._positive(p)
        if self.holdings.get(s,Decimal("0"))<q: raise ValueError("Insufficient holdings")
        self.cash+=q*p-f;self.holdings[s]-=q;self.marks[s]=p;self.fees+=f
    def split(self,s,ratio_new_per_old,event_id):
        self._symbol(s);r=dec(ratio_new_per_old);self._positive(r)
        if event_id in self.seen_events: raise ValueError("Duplicate split")
        if s not in self.holdings or s not in self.marks: raise ValueError("Unknown position")
        self.holdings[s]*=r;self.marks[s]/=r;self.seen_events.add(event_id)
    def dividend_ex(self,s,amount_per_share,event_id):
        self._symbol(s);d=dec(amount_per_share);self._positive(d)
        if event_id in self.seen_events: raise ValueError("Duplicate entitlement")
        amount=self.holdings.get(s,Decimal("0"))*d
        self.receivables[event_id]=amount;self.seen_events.add(event_id)
        return amount
    def dividend_pay(self,event_id):
        if event_id not in self.receivables: raise ValueError("Unknown/already paid dividend")
        amount=self.receivables.pop(event_id);self.cash+=amount;return amount
    def equity(self):
        return self.cash+sum((q*self.marks[s] for s,q in self.holdings.items()),Decimal("0"))+sum(self.receivables.values(),Decimal("0"))
    def snapshot(self):
        return {"cash":str(self.cash),"equity":str(self.equity()),"fees":str(self.fees),"receivables":str(sum(self.receivables.values(),Decimal("0")))}
