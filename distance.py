# encoding: utf-8
import math

BaiDuLongitude = 116.455386
BaiDuLatitude = 39.964626

DingTalkLongitude = 116.44781467014
DingTalkLatitude = 39.958173556858

LongitudeDiffValue = (DingTalkLongitude - BaiDuLongitude) * 111
LatitudeDiffValue = (math.cos(math.radians(DingTalkLatitude)) - math.cos(math.radians(BaiDuLatitude))) * 111

print('两点间距离约',round(pow((pow(LongitudeDiffValue, 2) + pow(LatitudeDiffValue, 2)), 0.5)*1000,2),'米')
