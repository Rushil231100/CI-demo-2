import main
def test_multiply():
  result = main.multiply(3, 4)
  result_2 = main.multiply(2, 3)
  print("running tests..")
  assert result_2 == 4
  assert result == 12
