file_obj = open("data.txt")
lines = file_obj.readlines()
print len(lines)

temp = "HUM:ind Who was the Charlie perfume woman ?"
def split_lable_and_text(raw_text):
    print raw_text.split(" ",2)

map(split_lable_and_text,lines)
