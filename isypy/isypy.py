# -*- coding: utf-8 -*-
"""
@author: Charles-David Hebert
"""
import logging

from . import monte_carlo
from . import ising
from . import tools


def run_isypy(yy_params) -> None:
    """

    Parameters
    ----------
    yy_params: yaml
        The parameters in yaml format

    Returns
    -------

    """

    logging.basicConfig(
        format="%(asctime)s: %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        level=logging.DEBUG,
    )

    tools.log_info("Start Running isypy !")

    mc_machine = monte_carlo.MonteCarlo(yy_params, ising.Ising)
    mc_machine.run_simulation()
