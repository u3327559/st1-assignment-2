## TASK 1: Basic Input/Output
print("Welcome to SmartCare: Clinical Appointment Booking System.")
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

print("\n--- TASK 1 ENHANCED & PART G IMPROVEMENT ---")

# A list to store all appointments
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    # 1. Check for blank patient name
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    
    # 2. PART G IMPROVEMENT: Prevent double-booking
    for existing_appointment in appointments:
        if existing_appointment["practitioner"] == practitioner_name and existing_appointment["time"] == appointment_time:
            print(f"Booking Failed: {practitioner_name} is already booked at {appointment_time}.")
            return  
            
    # 3. Create a dictionary for the appointment
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    # 4. Add the appointment to the list
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
    else:
        for appointment in appointments:
            print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")


print("\n--- PART F: Testing Scenarios ---")

# 1. Normal appointment
book_appointment("Alina Jackson", "Dr. John Doe", "2026-09-10 10:00 AM")
print("Normal appointment booked successfully.")

# 2. Two appointments for the same practitioner at the same time (The second one will now show as failed)
book_appointment("Alice Myers", "Dr. Jane Roe", "2026-09-11 02:00 PM")
book_appointment("Alex Jones", "Dr. Jane Roe", "2026-09-11 02:00 PM")

# 3. Strange input (None)
print("Testing strange input (None)...")
try:
    book_appointment(None, "Dr. Adams", None)
except Exception as e:
    print(f"Strange input caught: {e}")

# 4. Blank patient name
print("Attempting blank patient name...")
# book_appointment("", "Dr. Smith", "2026-09-12 10:00 AM") 
# IMPORTANT: If you uncomment the line above, the program will crash due to a ValueError!

print("\n--- Final Appointment ---")
display_appointments()
