"""
input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals.
output: Dictionary mapping students to hospitals.

TODO: Implement the Gale-Shapley algorithm to run in O(n^2).
"""


def stable_matching() -> dict:
    n = 0
    doctors_pref = []
    hospitals_pref = []
        
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))
    # input_path = os.path.join(base_dir, "input", "test_public_n2.txt")
    input_path = os.path.join(base_dir, "a_test.txt")

    with open(input_path, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])
    
    pairs = {}
    
    free_hospitals = list(range(0, n))
    
    while free_hospitals:
        current_hospital = free_hospitals[0]
        current_hospital_preferences = hospitals_pref[current_hospital]
        
        top_doctor = current_hospital_preferences[0]
        
        if(top_doctor not in pairs):
            pairs[top_doctor] = current_hospital
            
            free_hospitals.pop(0)
            current_hospital_preferences.pop(0)
            # hospitals_pref[current_hospital].pop(0)
            
        else:
            
            already_paired_hospital = pairs.get(top_doctor)
            
            top_doctor_preferences = doctors_pref[top_doctor]
            
            current_hospital_index = top_doctor_preferences.index(current_hospital)
            
            already_paired_hospital_index = top_doctor_preferences.index(already_paired_hospital)
            
            if(current_hospital_index < already_paired_hospital_index):
                pairs[top_doctor] = current_hospital
                free_hospitals.append(already_paired_hospital)
                
                free_hospitals.pop(0)
                current_hospital_preferences.pop(0)
                # hospitals_pref[current_hospital].pop(0)
            else:
                current_hospital_preferences.pop(0)
                

    return pairs


print("c.py: ", stable_matching())