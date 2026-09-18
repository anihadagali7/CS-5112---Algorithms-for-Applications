"""
input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals.
output: Dictionary mapping students to hospitals.

TODO: Implement the Gale-Shapley algorithm to run in O(n^2).
"""

def stable_matching(file) -> dict:
    n = 0
    doctors_pref = []
    hospitals_pref = []
        
    with open(file, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])
    
    doctor_rank = {}
    for doctor in range(n):
        doctor_rank[doctor] = {}
        rank = 0
        for hospital in doctors_pref[doctor]:
            doctor_rank[doctor][hospital] = rank
            rank = rank + 1

    doctor_to_hospital = {}

    # this only saves the index
    next_proposal = []
    for i in range(n):
        next_proposal.append(0)

    free_hospitals = list(range(0, n))

    while len(free_hospitals) > 0:
        current_hospital = free_hospitals.pop()
        next_index = next_proposal[current_hospital]
        top_doctor = hospitals_pref[current_hospital][next_index]
        next_proposal[current_hospital] = next_proposal[current_hospital] + 1

        # if doctor has already been paired
        if top_doctor not in doctor_to_hospital:
            doctor_to_hospital[top_doctor] = current_hospital
        else:
            already_paired_hospital = doctor_to_hospital[top_doctor]
            
            current_hospital_index = doctor_rank[top_doctor][current_hospital]
            already_paired_hospital_index = doctor_rank[top_doctor][already_paired_hospital]

            # if existing pair is better or worse than new option
            if current_hospital_index < already_paired_hospital_index:
                doctor_to_hospital[top_doctor] = current_hospital
                free_hospitals.append(already_paired_hospital)
            else:
                free_hospitals.append(current_hospital)

    return doctor_to_hospital
