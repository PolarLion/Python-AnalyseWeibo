import re


def get_time(string):
    pat = re.compile("\d\d:\d\d:\d\d");
    res = re.findall(pat, string);
    if len(res) > 0 :
      strs = re.split(":", res[0]);
      return True,  int(strs[0]) + int(strs[1]) / 60 + int(strs[2]) / 3600;
    else:
      return False, 0.0

def get_near_clock(float_time):
    return int(float_time + 0.5);

def analyse_weibo_by_time(str_filename):
    count_time = {};
    infile = open(str_filename, 'r');
    count_line = 0;
    for line in infile:
      line = infile.readline();
      if len(line) < 1 :
        continue;
      time = 0.0;
      got_time, time = get_time(line);
      if not got_time:
        continue;
      clock = get_near_clock(time);
      if clock in count_time:
        count_time[clock] += 1;
      else:
        count_time[clock] = 1;
    infile.close();
    return count_time;

