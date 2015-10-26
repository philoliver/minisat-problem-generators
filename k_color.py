#!/usr/bin/env python    
import argparse
from k_color_minisat_problem import KColorProblem


def make_args_parser():
  parser = argparse.ArgumentParser( description='Generates or interpretes the k-color problem for the MiniSat solver', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('--file', required=True, type=str, help='The path to a text file. Either output for the problem or input of the solution')
  parser.add_argument('--action', required=True, type=str, help='Either "generate" or "interprete"')
  return parser.parse_args()


def write_file(file, content):
  text_file = open(file, "w")
  text_file.write(content)
  text_file.close()
    
    
def read_file(file):
  text_file = open(file, "r")
  content = text_file.read()
  text_file.close()
  return content
    
    
def run():
  args = make_args_parser()
  
  if args.action not in ["generate", "interprete"]:
    raise Exception("Action has to be either 'generate' or 'interprete'.")
    
  else:
    problem = KColorProblem()
    if args.action == "generate":
      write_file(args.file, problem.generate_minisat_problem())
      
    else:
      solution = read_file(args.file)
      print (problem.interprete_minisat_problem(solution))


if __name__ == "__main__":
    run()
  
  