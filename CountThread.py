import re

def get_usrid(string):
    pat = re.compile("\d{9}\d?");
    res = re.findall(pat, string);
    if len(res) > 0:
      return True, res[0];
    else:
      return False, str(0);

def analyse_follower_by_threads(str_filename):
    count_threads = {};
    infile = open(str_filename);
    for line in infile:
      line = infile.readline();
      got_id, usrid = get_usrid(line);
      if not got_id:
        continue;
      if usrid in count_threads:
        count_threads[usrid] += 1;
      else:
        count_threads[usrid] = 1;
    infile.close();
    return count_threads;
