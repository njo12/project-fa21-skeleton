from parse import read_input_file, write_output_file
import Task
import os

threshold = 1440

def moneyCalc(task, ts_after):
  if ts_after > 0 and ts_after <= threshold:
    return task.get_late_benefit(ts_after)
  return task.get_max_benefit()
  

def solve(tasks):
    maxProfit = [0] * 1440
    orderIgloos = [[]] * 1440
    for i in range(1440):
        localMax = 0
        localBestIgloo = None
        for task in tasks:
          curr_igloo = task.get_task_id()
          if task.get_deadline() + threshold >= i and i >= task.get_duration() and task.get_task_id() not in orderIgloos[i - task.get_duration()]:
            # if i < deadline
            localProfit = moneyCalc(task, i - task.get_deadline()) + maxProfit[i - task.get_duration()]
            #else use min benefit
            if localMax < localProfit:
              localMax = localProfit
              localBestIgloo = task
        if localBestIgloo:
            orderIgloos[i] = orderIgloos[i - localBestIgloo.get_duration()] + [localBestIgloo.get_task_id()]
        else:
            orderIgloos[i] = orderIgloos[i - 1]      
        maxProfit[i]= localMax
    max_ind = maxProfit.index(max(maxProfit))
    return orderIgloos[max_ind]


# Here's an example of how to run your solver.
if __name__ == '__main__':
    for size in os.listdir('inputs/'):
        if size not in ['small', 'medium', 'large']:
            continue
        for input_file in os.listdir('inputs/{}/'.format(size)):
            if size not in input_file:
                continue
            input_path = 'inputs/{}/{}'.format(size, input_file)
            output_path = 'outputs/{}/{}.out'.format(size, input_file[:-3])
            print(input_path, output_path)
            #os.mkdir(output_path)
            tasks = read_input_file(input_path)
            output = solve(tasks)
            write_output_file(output_path, output)