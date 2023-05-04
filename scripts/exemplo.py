"""
Exemplo v0.0.1. Esse script simboliza um exemplo de como o docopt funciona.
Primeiro, são preprocessados os datasets, em seguida extraidas as features
e, por fim, treinados os modelos.

Usage:
    exemplo.py [--features=<f>] [--datasets=<ds>]

Options:
    -h --help           Shows the documentation.
    --datasets=<ds>     Allows the user to specify which datasets they want to use [default: openmic,jamendo].
    --features=<f>      Allows the user to define which feature extraction they want to use [default: vggish].
"""
from docopt import docopt
import sys

sys.path.append('../')

from src.dataset.mtg_jamendo import MTGJamendo

if __name__ == "__main__":
    arguments = docopt(__doc__, version="Exemplo v0.0.1")
    dataset = MTGJamendo()