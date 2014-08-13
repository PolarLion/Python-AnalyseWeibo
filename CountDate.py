
import re

class Date:
    month_dic = [0, 0, 31, 59, 89, 120, 150, 181, 212, 242, 273, 303, 334];
    def __init__(self, y=1990, m=4, d=4):
      self.year = y;
      self.month = m;
      self.day = d;

    def is_leap_year():
      if 0 == year % 400 or (0 != year % 100 and 0 == year % 4):
        return True;
      else:
        return False;

    def get_days():
      if month > 2 and is_leap_year():
        return month_dic[month] + day + 1;
      else:
        return month_dic[month] + day;

    def days_to_date():
      print("do nothing");

def get_str_date(string):
    pat = re.compile("\d{4}-\d\d-\d\d");
    res = re.findall(pat, string);
    if len(res) > 0 :
      strs = re.split("-", res[0]);
      return True, strs[0]+strs[1]+strs[2];
    else:
      return False, str(0);

def get_date(string):
    pat = re.compile("\d{4}-\d\d-\d\d");
    res = re.findall(pat, string);
    if len(res) > 0 :
      strs = re.split("-", res[0]);
      return True,  Date(int(strs[0]), int(strs[1]), int(strs[2]));
    else :
      return False, Date;


def analyse_weibo_by_date(str_filename):
    count_date = {};
    infile = open(str_filename);
    for line in infile:
      line = infile.readline();
      if len(line) < 1 :
        continue;
      got_date, str_date = get_str_date(line);
      if not got_date:
        continue;
      if str_date in count_date :
        count_date[str_date] += 1;
      else:
        count_date[str_date] = 1;
    infile.close();
    return count_date;


