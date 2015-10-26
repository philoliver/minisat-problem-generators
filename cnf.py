# Represents the conjunctive normal form (CNF)
# in the format that can be read by minisat.
# The CNF is built by added Clauses.
class CNF(object):
  def __init__(self, title):
    self._cnf = "c "+title+"\n"
  
  def add_clause(self, clause):
    if clause.ended is True:
      self._cnf += str(clause) + "\n"
    else:
      raise Exception("Clause has to be ended before it is attached to the CNF")
  
  def __str__(self):
    return self._cnf


# Represents a clause, i.e a part of a CNF
# and is in such a format that it can be read by minisat.
class Clause(object):
  def __init__(self):
    self._clause = ""
    self._ended = False
    
  def add_literal(self, literal):
    if self._ended is False:
      self._clause += str(literal) + " "
    else:
      raise Exception("Clause can not be changed once its ended.")
  
  @property
  def ended(self):
    return self._ended
  
  def end(self):
    if self.ended is False:
      self._clause += "0"
      self._ended = True
    else:
      raise Exception("Clause already ended.")
    
  def __str__(self):
    return self._clause