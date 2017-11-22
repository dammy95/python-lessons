import csv


if __name__ == '__main__':
  sum_ = 0
  wf = open('example2.csv', 'w')
  with open('example.csv') as f:
    r = csv.reader(f)
    w = csv.writer(wf)
    for row in r:
      sum_ += int(row[0])
      w.writerow([row[0]])
    w.writerow([sum_])
