import difflib
import Levenshtein

def similar_lvst_jaro(str1, str2):
     return Levenshtein.jaro(str1, str2)
 
def similar_lvst_hamming(str1, str2):
     return Levenshtein.hamming(str1, str2)
 
def similar_lvst_distance(str1, str2):
     return Levenshtein.distance(str1, str2)

str4 = " detect occlusion and run auto control mode implication next terminate auto control not air ok signal implication terminate auto control mode corroborate arterial line and corroborate pulse wave and cuff implication select arterial line corroborate pulse wave and cuff and not corroborate arterial line implication select pulse wave not corroborate arterial line and not corroborate pulse wave and cuff implication select cuff plug pump and ready infusate and clear occlusion line implication not terminate auto control mode plug pump and ready infusate and clear occlusion implication start auto control button enter auto control mode implication next inflate cuff press start auto control button and not cuff implication issue alarm and provide override selection press alarm reset button implication not alarm "
s4 = " occlusion detected and auto control mode running implication next auto control be terminated Air Ok signal remains implication no principal low in 3 seconds arterial line and pulse wave and cuff available implication arterial line selected pulse wave and cuff available and arterial line available implication pulse wave selected arterial line lost implication then pulse wave selected pulse wave lost implication then cuff selected auto control mode entered implication next eventually cuff be inflated manual mode running and start auto control button pressed implication auto control mode running start auto control button pressed and cuff available implication alarm issued and override selection provided alarm reset button pressed implication alarm disabled "

print(difflib.SequenceMatcher(None, str4, s4).quick_ratio())
print(similar_lvst_jaro(str4, s4))
print(similar_lvst_distance(str4, s4))



Str1 = " push o1 or push i1 implication next reach floor1  push o2 or push i2 implication next reach floor2  push o3 or push i3 implication next reach floor3  push o1 implication next reach floor1 implication next push o1 U reach floor1  push o2 implication next reach floor2 implication next push o2 U reach floor2  push o3 implication next reach floor3 implication next push o3 U reach floor3  push i1 implication next reach floor1 implication next push i1 U reach floor1  push i2 implication next reach floor2 implication next push i2 U reach floor2  push i3 implication next reach floor3 implication next push i3 U reach floor3  idle implication next open door "
s1 = "o1 or i1 pushed implication next floor1 be reached o2 or i2 pushed implication next floor2 be reached o3 or i3 pushed implication next floor3 be reached o1 pushed implication next o1 implication next  floor1 reached implication next o2 pushed implication next o2  implication next floor2 reached implication next o3 pushed i1 pushed implication next i1 implication next  floor1 reached implication next i2 pushed implication next i2  implication next floor2 reached implication next i3 pushed elevator idle implication next door be opened "


print(difflib.SequenceMatcher(None, Str1, s1).quick_ratio())
print(similar_lvst_jaro(Str1, s1))
print(similar_lvst_distance(Str1, s1))

str2 = "not r2 and not r3 and not r4 and r1 r1 implication r1 or r3 r2 implication r2 or r4 r3 implication r3 or r4 r4 implication r4 or r3 not r1 or r3 implication not person W r1 or r3 not r2 or r4 implication not medic W r2 or r4 person implication next carryperson carryperson implication not medic implication nextcarryperson W medic not r2 or not r6 or not r3 or not r4 or not r5 or not r7 or not r8 or not r9 and r1"
s2 = " Initially r2 or r3 or r4 available and r1 available r1 true implication robot move to r1 r2 or r3 r2 true implication robot move to r2 r1 or r4 r3 true implication robot move to r3 r1 or r4 r4 true implication robot move to r4 r2 or r3 r1 or r3 becomes until Person available Medic available until true r2 or r4 becomes implication next true carryPerson available until person available implication next carryPerson be available Initially r2 or r3 or r4 or r5 or r6 or r7 or r8 or r9 available and r1 available"
print(difflib.SequenceMatcher(None, str2, s2).quick_ratio())
print(similar_lvst_jaro(str2, s2))
print(similar_lvst_distance(str2, s2))


str3 = "introduction screen implication next selection procedure select anything implication X ordering procedure not select anything implication X introduction screen order something implication X order processing procedure not order something implication X introduction screen terminate order processing procedure implication introduction screen select specifical offer||select group selection||select back button  select back button implication terminate selection procedure  select specifical offer implication display system information  select specifical offer implication display special display information "
s3 = "introduction screen available implication eventually selection procedure enabled selection procedure terminates implication next anything selected selection procedure terminates implication next anything selected something ordered implication next introduction screen enabled ordering procedure terminates implication next something ordered Introduction screen enabled implication next Introduction screen enabled Specifical offer or group selection or back button selected in selection procedure back button selected implication selection procedure terminates special offer procedure terminates implication next Specifical offer selected implication system information displayed Specifical offer selected implication special display information displayed "

print(difflib.SequenceMatcher(None, str3, s3).quick_ratio())
print(similar_lvst_jaro(str3, s3))
print(similar_lvst_distance(str3, s3))



