#!/usr/bin/python
#WeiBo.py

import os
import operator
import CountTime
import CountDate
import CountThread

def write_into_file(dict_statics, str_filename):
    outfile = open(str_filename, 'w');
    for key in sorted(dict_statics):
      outfile.write(str(key) + "\t" + str(dict_statics[key]) + "\n\r");
    outfile.close();

if __name__ == '__main__':
  in_path = "task3/";
  path = "count_thread/"
  filenames=os.listdir(in_path);
  for name in filenames:  
#    res = CountTime.static_weibo_by_time(in_path + name);
#    res = CountDate.analyse_weibo_by_date(in_path+name);
    res = CountThread.analyse_follower_by_threads(in_path+name);
    write_into_file(res, path+name[:-4]+"_count_date.txt");


