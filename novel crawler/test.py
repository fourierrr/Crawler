#-*-coding:UTF-8-*-
import sys;
total=30000
for i in range(0,total):
  percent=float(i)*100/float(total)
  # sys.stdout.write("6666")
  # sys.stdout.write("%\r")

  sys.stdout.write('666/87469   '+"%.4f%% "%percent+'\r')
  # sys.stdout.write("%r")
  sys.stdout.flush()
sys.stdout.write("100%!finish!\r")
sys.stdout.flush()