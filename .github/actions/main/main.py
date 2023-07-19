import sys,os
name=os.getenv('NAME')

def main():
   if name == "jayanth":
      print("sucsses")
   sample={
      "jayanth":"success",
      "varshith":"failed"
   }
   add=(name)
   print(sample[name])
