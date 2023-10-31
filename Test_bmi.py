from unittest import result

import Lab2.bmi as bmi


def test_bmi_normal_weight():
   height = 1.8
   weight = 75
   result = bmi.calculate_bmi(height,weight)

   assert (result == 0)


def test_bmi_over_weight():
   height = 1.8
   weight = 90
   result = bmi.calculate_bmi(height, weight)

   assert (result == 1)

def test_bmi_under_weight():

   height = 1.8
   weight = 50
   result = bmi.calculate_bmi(height, weight)

   assert (result == -1)