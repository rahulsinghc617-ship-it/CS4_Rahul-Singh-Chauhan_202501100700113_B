f
ile_name = "CS4.txt" 
with open(file_name, "r") as file: 
content = file.read() 
print("----- Using read() -----") 
print(content) 
with open(file_name, "r") as file: 
    print("\n----- Using readline() -----") 
    print(file.readline()) 
    print(file.readline()) 
 
with open(file_name, "r") as file: 
    lines = file.readlines() 
    print("\n----- Using readlines() -----") 
     
     
    print("Total number of lines:", len(lines)) 
         
     
    print("\nFirst 2 lines:") 
    print(lines[:2]) 
     
     
    print("\nLast 2 lines:") 
    print(lines[-2:]) 
 
 
 
log_count = { 
    "INFO": 0, 
    "WARNING": 0, 
    "ERROR": 0 
} 
 
for line in lines: 
    if "INFO" in line: 
        log_count["INFO"] += 1 
    if "WARNING" in line: 
        log_count["WARNING"] += 1 
    if "ERROR" in line: 
        log_count["ERROR"] += 1 
 
print("\nLog Count:", log_count) 
 
 
 
info_logs = [] 
warning_logs = [] 
error_logs = [] 
 
for line in lines: 
    if "INFO" in line: 
        info_logs.append(line) 
    if "WARNING" in line: 
        warning_logs.append(line) 
    if "ERROR" in line: 
        error_logs.append(line) 
 
with open("info_logs.txt", "w") as f: 
f.writelines(info_logs) 
with open("warning_logs.txt", "w") as f: 
f.writelines(warning_logs) 
with open("error_logs.txt", "w") as f: 
f.writelines(error_logs) 
print("\nFiltered files created successfully.") 
keyword = input("\nEnter keyword to search (INFO/WARNING/ERROR): 
") 
results = [] 
for line in lines: 
if keyword in line: 
print(line.strip()) 
results.append(line) 
with open("search_result.txt", "w") as f: 
f.writelines(results) 
print("\nSearch results saved to search_result.txt") 
 
 
 
with open(file_name, "r") as file: 
     
    print("\n--- First 50 characters ---") 
    print(file.read(50)) 
     
     
    file.seek(0) 
    print("\n--- After seek(0) ---") 
    print(file.read(50)) 
     
     
    file.seek(0) 
    data = file.read() 
    middle = len(data) // 2 
     
    file.seek(middle) 
    print("\n--- From Middle ---") 
    print(file.read(50)) 
     
     
    file.seek(0) 
    data = file.read() 
     
f
ile.seek(len(data) - 100) 
print("\n--- Last 100 characters ---") 
print(file.read())