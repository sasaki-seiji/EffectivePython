#!/usr/bin/env python3

# Copyright 2014 Brett Slatkin, Pearson Education Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
print("Example 1 : localtime, strftime")
from time import localtime, strftime

now = 1407694710
local_tuple = localtime(now)
print("local_tuple:", repr(local_tuple))
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)


# Example 2
print("\nExample 2 : strptime, mktime")
from time import mktime, strptime

time_tuple = strptime(time_str, time_format)
print("time_tuple:", repr(time_tuple))
utc_now = mktime(time_tuple)
print(utc_now)


# Example 3
print("\nExample 3 : strptime, strftime")
parse_format = '%Y-%m-%d %H:%M:%S %Z'
# 2016.07.04 change
#depart_sfo = '2014-05-01 15:45:16 PDT'
depart_sfo = '2014-05-01 15:45:16 JST'
time_tuple = strptime(depart_sfo, parse_format)
print("time_tuple:", repr(time_tuple))
time_str = strftime(time_format, time_tuple)
print(time_str)


# Example 4
print("\nExample 4 : strptime('... EDT')")
try:
    arrival_nyc = '2014-05-01 23:33:24 EDT'
    time_tuple = strptime(arrival_nyc, time_format)
except:
    logging.exception('Expected')
else:
    assert False


# Example 5
print("\nExample 5 : datetime")
from datetime import datetime, timezone

now = datetime(2014, 8, 10, 18, 18, 30)
print("now:", repr(now))
now_utc = now.replace(tzinfo=timezone.utc)
print("now_utc:", repr(now_utc))
now_local = now_utc.astimezone()
print("now_local:", repr(now_local))
print(now_local)


# Example 6
print("\nExample 6 : datetime.strptime")
time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
print("now:", repr(now))
time_tuple = now.timetuple()
print("time_tuple:", repr(time_tuple))
utc_now = mktime(time_tuple)
print(utc_now)


# Example 7
print("\nExample 7 : pytz US/Eastern->utc")
import pytz
arrival_nyc = '2014-05-01 23:33:24'
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
print("nyc_dt_naive", repr(nyc_dt_naive))
eastern = pytz.timezone('US/Eastern')
print("eastern:", repr(eastern))
nyc_dt = eastern.localize(nyc_dt_naive)
print("nyc_dt:", repr(nyc_dt))
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
print("utc_dt:", repr(utc_dt))
print(utc_dt)


# Example 8
print("\nExample 8 : pytz utc->US/Pacific")
pacific = pytz.timezone('US/Pacific')
sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
print(sf_dt)


# Example 9
print("\nExample 9 : pytz utc->Asia/Katmandu")
nepal = pytz.timezone('Asia/Katmandu')
nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
print(nepal_dt)
