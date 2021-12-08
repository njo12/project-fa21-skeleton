from parse import read_input_file, read_output_file, write_output_file
import Task
import os
import math
from random import seed
from random import randint

def preprocess(orig, dp) :
    
    for i in range(len(dp)):
        dp[i] = orig[dp[i]-1]
    return dp


def switchTwo(tasks):
  for _ in range(2):
    u = randint(0, len(tasks) - 1)
    v = randint(0, len(tasks) - 1)
    tasks[u], tasks[v] = tasks[v], tasks[u]
  return tasks
	
def moneyCalc(task, ts_after):
  if ts_after > 0:
    return task.get_late_benefit(ts_after)
  return task.get_max_benefit()


def profit(tasks):
  tasksCopy = tasks[:]
  totalProfit = 0
  t = 0
  while t < 1440 and tasksCopy:
    x = tasksCopy.pop(0)
    totalProfit += moneyCalc(x, t - x.get_deadline())
    t += x.get_duration()
  return totalProfit


def sa(tasks):
  best = tasks
  bestPro = profit(tasks)
  counter = 0
  for j in range(1000):
    counter += 1
    test = switchTwo(best[:])
    pt = profit(test)
    if pt > bestPro:
      best = test
      bestPro = pt
      counter = 0
  best = [t.get_task_id() for t in best]
  return best

if __name__ == '__main__':
    for size in os.listdir('inputs/'):
        if size not in ['small', 'medium', 'large']:
            continue
        for input_file in os.listdir('inputs/{}/'.format(size)):
            if size not in input_file:
                continue
            input_path = 'inputs/{}/{}'.format(size, input_file)
            input_path2 = 'outputs/{}/{}.out'.format(size, input_file[:-3])
            output_path = 'output/{}/{}.out'.format(size, input_file[:-3])
            print(input_path, output_path)
            #os.mkdir(output_path)
            original_input = read_input_file(input_path)
            dp_output = read_output_file(input_path2)
            output = preprocess(original_input, dp_output)
            out = sa(output)
            write_output_file(output_path, out)