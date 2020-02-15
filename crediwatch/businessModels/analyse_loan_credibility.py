import pandas as pd
from commons import Logger
logger = Logger.get_logger("CrediWatch")


def check_loan_credibility(x_factors:dict, contrib_factors=None):

    """
    :param x_factors: {x1:12,x2:323  .... }
    :param contrib_factors:
    :return:
    """
    base_score = 0
    if len(x_factors) != 0:
        logger.info("xfactors {}".format(x_factors))
        base_score = 0.717*x_factors["x1"]+0.847*x_factors["x2"]+0.42*x_factors["x3"]+3.107*x_factors["x4"]+0.998*x_factors["x5"]
        logger.info("base score: {}".format(base_score))
    else:
        base_score = 0

    if base_score < 0.9:
        loan_status = True
    else:
        loan_status = False

    return {"status": loan_status}