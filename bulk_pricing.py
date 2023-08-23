
""" Calculate the price of an order of magnets according to a bulk
pricing scheme. """

import sys


def get_cost(numOfMag):
  """ 
  get cost takes in number of magnets and returns the price of purchasing that number of magnets
  Requires an int greater than 0, raises value or type error if not
  """
  
  # initializing priceper, which is price per magnet
  pricePer = .75
  if numOfMag <= 0:
    raise ValueError("The number of magnets must be greater than 0.")
  
  # determine which price bracket, under 50 not checked since priceper is initialzed with that bracket value 
  if numOfMag >= 50 and numOfMag <= 99:
    pricePer = .72
  elif numOfMag  >= 100 and numOfMag <= 999:
    pricePer = .7
  elif numOfMag >= 1000:
    pricePer = .67
  
  # calculate and format to two decimal points
  total_price = pricePer * numOfMag
  total_price = format(total_price, '.2f')
  return total_price



if __name__ == "__main__":
    try:
        magnets = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a number of magnets as a command-line"
                 " argument")
    except ValueError:
        sys.exit("could not convert " + sys.argv[1] + " into an integer")
    print(get_cost(magnets))



# TEST_PRICING.PY, COPY AND PASTE THIS IS IN A NEW SCRIPT
import pytest
import exercise_2 as e2

def test_price():
    """
    testing various magnet number values
    """

    # tests complete successfully, exceptions are properly raised when asserting incorrect values
    assert e2.get_cost(75)
    assert e2.get_cost(99)
    assert e2.get_cost(4)
    assert e2.get_cost(49)
    assert e2.get_cost(1)
    assert e2.get_cost(100000)
    assert e2.get_cost(475)
    assert e2.get_cost(72)
