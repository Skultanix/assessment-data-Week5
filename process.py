# Opens the text file and stores it as variable "log_file"
log_file = open("um-server-01.txt")

#defines a function "sales_report" that takes log_file as an argument
def sales_reports(log_file):
    #for every line in log_file
    for line in log_file:
        #set the line equal to the line that has all white space removed to the right
        line = line.rstrip()
        #define the variable "day" as the first 3 items in the line array
        day = line[0:3]
        #if the day is equal to Mon (Tue)..
        if day == "Mon":
            #print the line
            print(line)
    
sales_reports(log_file)
