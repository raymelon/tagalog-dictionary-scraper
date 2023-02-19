class MoverException(Exception):
  def __init__(self, *args):
    self.args = args

  def __str__(self):
    return ' '.join(map(lambda el: str(el), self.args))