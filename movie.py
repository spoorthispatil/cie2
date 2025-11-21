import sys
if len(sys.argv)==5:
    script_name=sys.argv[0]
    name_=sys.argv[1]
    duration=float(sys.argv[2])
    language=sys.argv[3]
    price=float(sys.argv[4])
    print("user provided information.")
else:
    script_name=sys.argv[0]
    name="RRR"
    duration=3.5
    language="Telugu"  
    price=250.0
    print("No input given - using default information.")
print("Movie Information:")
print("Script Name:",script_name)
print("Movie Name:",name)
print("Duration:{duration} hours")
print("Language:",language)
print("Price: Rs.",price)
