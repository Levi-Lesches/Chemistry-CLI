class Element: 
  """
  An element of the periodic table. 

  Properties
  - symbol: str
    The atomic symbol for this element
  """
  def __init__(self, symbol): 
    self.symbol = symbol
  def __str__(self): return self.symbol
  def __repr__(self): return f"Element({self.symbol})"
  def __hash__(self): return hash(self.symbol)
  def __eq__(self, other): 
    return type(other) is Element and self.symbol == other.symbol
