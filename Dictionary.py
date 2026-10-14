student_data = {
    "id1": {"Studentname": "David" , "Class": "VI" ,"SubjectIntegration": "English, Math, Science"}, 
    "id2": {"Studentname": "Surya" , "Class": "VI" ,"SubjectIntegration": "English, Math, Science"}, 
    "id3": {"Studentname": "David" , "Class": "VI" ,"SubjectIntegration": "English, Math, Science"}, 
    "id4" : {"Studentname": "Radhika" , "Class": "VI" ,"SubjectIntegration": "English, Math, Science"}


}    
result = {}
seen_keys = []
for i, j in student_data.items ():
    unique_keys = (j["Studentname"], j["Class"] , j["SubjectIntegration"])
    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        result [i] = j
for k, v in result.items ():
    print (k,":", v)

