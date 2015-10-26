# minisat-problem-generators
A few python scripts to generate problems which can be read by MiniSat.

## Problems
So far the script knows how to generate the k-coloring problem.
The graph is currently hard coded. However, changing it should be easy.

## Usage
To generate a problem use:

```python k_color.py --file problem.txt --action generate```

To interpret the solution from MiniSat use:

```python k_color.py --file solution.txt --action interpret ```
