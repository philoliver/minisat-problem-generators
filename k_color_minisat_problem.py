import networkx as nx
from itertools import combinations
from cnf import CNF
from cnf import Clause
  
class KColorProblem(object):
  def __init__(self):
    self.colors = ["Red", "Green", "Blue"]
    self.countries = ["Spain", "Portugal", "France", "Italy", "Switzerland", "Germany", "Belgium"]
    
    self.G = nx.Graph()
    self.G.add_nodes_from(self.countries)
    
    self.G.add_edge("Spain", "Portugal")
    self.G.add_edge("Spain", "France")
    self.G.add_edge("France", "Italy")
    self.G.add_edge("France", "Switzerland")
    self.G.add_edge("France", "Germany")
    self.G.add_edge("France", "Belgium")
    self.G.add_edge("Italy","Switzerland")
    self.G.add_edge("Switzerland", "Germany")
    self.G.add_edge("Germany","Belgium")
  
  def _convert_to_literal(self, country, color):
    return self.countries.index(country)*len(self.colors)+self.colors.index(color)+1
    
  def _convert_from_literal(self, literal):
    country_idx = (literal-1)/len(self.colors)
    color_idx = literal-(country_idx*len(self.colors))
    return self.countries[country_idx], self.colors[color_idx-1]

  # Each vertex has at least one color
  # for-all: v where 1<=v<=V and 1<=k<=K one clause:
  #   pv,1 or pv,2 ... or pv,k
  def _at_leat_one_color(self, cnf):
    for country in self.G.nodes():
      clause = Clause()
      for color in self.colors:
        literal = self._convert_to_literal(country, color)
        clause.add_literal(literal)
      clause.end()
      cnf.add_clause(clause)

  # Each vertex has maximum one color
  # for-all: v,k,k' where 1<=v<=V and 1<=k<k'<=K one clause:
  #   -pv,k or -pv,k' ...
  def _max_one_color(self, cnf):
    for country in self.G.nodes():
      for color_combos in combinations(self.colors, 2):
        clause = Clause()
        clause.add_literal( -self._convert_to_literal(country, color_combos[0]) )
        clause.add_literal( -self._convert_to_literal(country, color_combos[1]) )
        clause.end()
        cnf.add_clause(clause)

  # Neighboring verteces have different colors
  # for-all: v, v', k where 1<=v,v'<=V and (v, v') element of L (list of neighbors) and 1<=k<=K
  def _different_colors(self, cnf):
    for country in self.G.nodes():
      for neighbor in self.G.neighbors(country):
        for color in self.colors:
          clause = Clause()
          clause.add_literal( -self._convert_to_literal(country, color) )
          clause.add_literal( -self._convert_to_literal(neighbor, color) )
          clause.end()
          cnf.add_clause(clause)

  def _parse_solution(self, solution):
    solution = solution.split("\n")[1] # Ommit first line
    solution = solution.split(" ") # ["-1", "2"...]
    return map(int, solution) # [-1, 2...]

  def generate_minisat_problem(self):
    cnf = CNF("Generated K-Color Problem")
    self._at_leat_one_color(cnf)
    self._max_one_color(cnf)
    self._different_colors(cnf)
    return str(cnf)
    
  def interprete_minisat_problem(self, solution):
    literals = self._parse_solution(solution)
    interpretation = ""
    
    for literal in literals:
      if literal > 0:
        country, color = self._convert_from_literal(literal)
        interpretation += country + " => " + color + "\n"
        
    return interpretation