import RestrictedPython
from RestrictedPython import compile_restricted, limited_builtins, safe_builtins, utility_builtins
from RestrictedPython.PrintCollector import PrintCollector
from pathos.multiprocessing import ProcessPool
import multiprocess
class safe_process:
  def __init__(self, code: str = None):
    self.console: str = 'Console vide'
    self.pool = ProcessPool(nodes=4)
    if code is None:
      self.code: str = ''
    else:
      self.code: str = code

  def append_code(self, code: str):
    self.code += f'\n{code}'

  def reset_code(self):
    self.code: str = ''

  def reset_console(self):
    self.console: str = ''

  def reset(self, thing_to_reset: str = "all"):
    if thing_to_reset.lower() == 'all':
      self.code: str = ''
      self.console: str = ''
    elif thing_to_reset.lower() == 'console':
      self.console: str = ''
    elif thing_to_reset.lower() == 'code':
      self.code: str = ''
    else:
      raise ValueError("Selection de reset : all | code | console")
    

  def execute(self, *, timeout: int = 10):
    self.console = 'Chargement (code en execution)...'
    result = self.pool.apipe(interpret, self.code)
    output: str = None
    try:
      output = result.get(timeout=timeout)
    except multiprocess.context.TimeoutError:
      output: str = "Loop infinie"
    except Exception as e:
      output: str = "Error" + e
    self.console: str = output

def interpret(code: str):
  data: dict = {"_print_": PrintCollector, "__builtins__": {**limited_builtins, **safe_builtins, **utility_builtins, "all": all, "any": any, "_getiter_": RestrictedPython.Eval.default_guarded_getiter, "_iter_unpack_sequence_": RestrictedPython.Guards.guarded_iter_unpack_sequence},"_getattr_": RestrictedPython.Guards.safer_getattr}
  exec(compile_restricted(code + "\nresults = printed", filename="<string>", mode="exec"), data, None)
  return data["results"]
