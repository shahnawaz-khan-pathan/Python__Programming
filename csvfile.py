import csv 
    
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    

rows = [ ['Sahib', 'Cs', '2019', '9.0'], 
         ['krit', 'Cs', '2019', '9.1'], 
         ['Raj', 'IT', '2019', '9.3'], 
         ['Neha', 'ME', '2019', '9.5'], 
         ['Prateek', 'ME', '2019', '7.8'], 
         ['Sahil', 'TT', '2019', '9.1']] 
    
 
filename = "university_records.csv"
    
 
with open(filename, 'w') as csvfile: 

    csvwriter = csv.writer(csvfile) 
        
    
    csvwriter.writerow(fields) 
        
    
    csvwriter.writerows(rows)