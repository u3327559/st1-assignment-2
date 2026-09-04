## Part B - Human-Written Prototype Limitations
After running the initial human-written prototype, I have found the following five limitations:
1. **No Data Persistence:** The list of appointments are only stored in memory and they are lost when the Python terminates the script's execution.
2. **Hardcoded Data Entry:** The program does not authorize the receptionist to enter any details for a new appointment, instead it is hardcoded when the function book_appointment(‘Alice Smith’) is called.
3. **No Conflict Validation:** The book_appointment method only checks if the patient name is empty but does not confirm if the Expert is available at that time which means it can be double booked.
4. **No Time Format Validation:** The appointment_time accepts any string format. A user can type anything instead of using an actual date-time string, and the system will accept it without a problem.
5. **Missing Edit/Delete Functionality:** The prototype is only authorized to add and view the appointments. If any patient wants to cancel or requests rescheduling, there is no proper function available to delete or edit an entry.

## Part H - Final Reflection

1. **What did you build before using AI?**  
Before using AI, I created a basic prototype in PYTHON for a SmartCare clinic that used lists and dictionaries to store patient names, practitioners, and appointment times. It worked fine for basic data entry but it had significant limitations, including lacking check validation for a double-bookings.

2. **What did AI help you understand?**  
With the help of Microsoft Copilot as a tutor, it helped me to better understand dictionary structures and why conditional checks (e.g, "if not appointments:") are necessary to prevent crashes when dealing with empty lists. 

3. **Did AI make assumptions?**  
When writing the alternative code, the AI properly followed my requirements of not using databases and GUIs. However, it assumed that all input data would be correctly formatted and actually skipped the basic error handling (the blank name check) that existed in the original human code.

4. **How did you verify the AI output?**  
I verified the output by testing the code on several test scenarios in Python, by using it in normal appointments, intentional double-bookings and blank strings values to see exactly where the logic would break. 

5. **What engineering work remained for you?**  
The AI's version was overly simplistic so the core engineering work was left for me, I had to manually design and implement a loop that would check existing records and avoids scheduling a practitioner twice.
