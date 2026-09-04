## Part C - AI as Tutor

**My Prompt:**
> Act as a Python tutor. I am learning introductory software technology. Here is a small appointment-booking function:
> (Pasted Task 1 Enhanced code here)
> 1. Explain what the code does.
> 2. Identify three limitations.
> 3. Suggest improvements.
> 4. Do not rewrite the whole application.
> 5. Ask me two questions to test my understanding.

**Microsoft Copilot's Response:**
📝 What the code does
appointments list: Keeps track of all booked appointments as dictionaries inside a list.

book_appointment function: Creates a dictionary with patient, practitioner, and time, then adds it to the list. It also checks that the patient name isn’t empty.

display_appointments function: Prints all appointments in a readable format. If none exist, it shows a message.

Program flow: Welcomes the user, books two sample appointments, and displays them.

⚠️ Three limitations
No duplicate check: The system allows multiple appointments at the same time with the same practitioner.

No persistence: Appointments vanish when the program ends because they’re only stored in memory.

No cancellation or editing: Once booked, appointments cannot be changed or removed.

💡 Suggested improvements
Add validation: Ensure practitioner name and appointment time are not empty.

Implement persistence: Save appointments to a file (like JSON or CSV) so they remain after the program closes.

Add management functions: Create functions to cancel or reschedule appointments.

❓ Two questions for you
Why is a dictionary used to store each appointment instead of just a list of strings?

What would happen if you called display_appointments() before booking any appointments?

**My Answers to Copilot's Questions:**
1. A dictionary is basically a collection of key value pairs that are used to store context about the data stored (e.g."patient": "Alice Smith"). This makes it easier for anyone to understand the code and makes it more readable and organized because anyone can easily tell which key represents what. On the other hand, A list is only store those values which are in a linear format (e.g. "Alice Smith", "Dr. John Doe"). That's why, in order to tell which string is referring to which category, one must remember the specific order of the elements.
2. The program would successfully run, and it would print out "No appointments recorded". The "display_appointments()" function has a specific "if not appointments:" it checks at the very beginning to handle this scenario and allows the function to exit properly instead of crashing or looping continuously on an empty list.

## Part D - Generate an Alternative

**My Prompt:**
> Create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Do not use a database or a GUI.

**Microsoft Copilot's Response:**
```python
# # A list to store all appointments
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    # Create a dictionary for the appointment
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    # Add the appointment to the list
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
    else:
        for appointment in appointments:
            print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

# Example usage
book_appointment("Alice Smith", "Dr. John Doe", "2026-09-05 10:00 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "2026-09-05 11:30 AM")

display_appointments()
