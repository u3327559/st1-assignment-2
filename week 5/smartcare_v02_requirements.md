# SmartCare v0.2 - Requirements Specification Template

## 1. Problem and Scope
* **Problem:** SmartCare currently uses manual spreadsheets and paper records which create problems such as Duplicate Bookings, Difficulty Locating Patient Information, Inconsistent Appointment Statuses, and Lack of Reliable Appointment History.
* **In Scope:** A maintainable management system covering Patient Profiles, Practitioner Profiles, Appointment Scheduling, and Historical Appointment Tracking.
* **Out of Scope:** Billing, Payment Processing, Automated Clinical Diagnostics, and Patient Portal.
* **Provisional:** Automated SMS/email appointment reminder.

## 2. Stakeholders

| Stakeholder | Need | Evidence |
| :--- | :--- | :--- |
| **Receptionist / Front Desk Staff** | A simplified approach to locating patient information and scheduling appointments without unnecessary scheduling conflicts. | The client brief says that the staff is currently reporting Duplicate Bookings and Difficulty in Finding Patient Information. |
| **Clinic Management** | A simple, easy to support accurate system for tracking booking status and history. | The brief states that the management wants a small maintainable system and mentions issues with Inconsistent Appointment Status and Limited Appointment History. |
| **Practitioners** | Reliable, accurate access to their daily schedules and patient appointments. | The brief requires the inclusion of a Practitioner and Appointment System. |
| **Patients** | Ability to accurately schedule their appointments without the risk of double booking or lost records. | Indicated by the direct operational impact of the Duplicate Bookings and Lost Records mentioned in the brief. |

## 3. Functional Requirements
* **FR-01:** The developed system shall enable Staff to Create, Edit, and Save Patient Profile.
* **FR-02:** The developed system shall enable Staff to search for an existing patient profile using a Name or Unique ID.
* **FR-03:** The developed system shall enable Staff to make New Appointments by linking their patient profiles to a specific practitioner.
* **FR-04:** The developed system shall prohibit the creation of any appointments with the same practitioner on the same date and time.
* **FR-05:** The developed system shall enable Staff to Update the Status of An Appointment to reflect the new state. (e.g., Scheduled, Completed, Cancelled).
* **FR-06:** The developed system shall store and display all cancelled and completed appointments along with all other details in the patient's appointment history.
* **FR-07:** The developed system shall allow Practitioners and Staff to sort and view a list of their upcoming schedule of appointments by specific Dates, Times and Practitioner names.
* **FR-08:** The developed system shall allow Management to Create, Edit, and Archive Practitioner Profiles.

## 4. Non-Functional Requirements
* **NFR-01 (Maintainability):** The system's code will be modular and well documented to ensure that its maintenance remains a Small and Maintainable application for future IT support.
* **NFR-02 (Data Integrity):** The system will require all mandatory patient and appointment fields to be filled before a new appointment is saved to the database.
* **NFR-03 (Usability):** The system’s interface should be designed in such a way that it takes less than two minutes for a person to book an appointment with minimal training.
* **NFR-04 (Reliability):** The system will be able to store appointments reliably by preventing multiple users from storing different appointments at the same time.

## 5. User Stories
* **US-01:** As a front desk receptionist, I would like to be able to search for a patient by their name to avoid having to scroll through countless manual spreadsheets to find required information.
* **US-02:** As a receptionist, I would like the system to notify me if there are any attempted double booking of a time slot to prevent having duplicate appointments.
* **US-03:** As a clinic manager, I would like to be able to see a log of a patient's previous appointments to view their history of visits.
* **US-04:** As a practitioner, I would like to see a filtered list of my appointments for the day to know what patients I need to treat on a daily basis.

## 6. Acceptance Criteria

**Criteria for US-01 (Patient Search):**
* **GIVEN** the receptionist is on the main dashboard screen, **WHEN** they input a valid patient name into the search bar and submit, **THEN** the system retrieves and displays the matching patient profile.

**Criteria for US-02 (Negative Scenario - Duplicate Booking Prevention):**
* **GIVEN** that there’s an existing appointment for Dr. Smith scheduled for 10:00 AM, **WHEN** the receptionist tries to make a new appointment for Dr. Smith at 10:00 AM, **THEN** the system should not allow the request and should reject the booking action and display a "Time Slot Unavailable" error message.

**Criteria for US-03 (Status and History Tracking):**
* **GIVEN** an active appointment is currently marked as 'Scheduled', **WHEN** the receptionist updates the status dropdown to 'Cancelled', **THEN** the system will update the status and retain the record in the patient's appointment history view.

## 7. Assumptions and Open Questions
* **Assumption:** The clinic works in the same timezone location.
* **Open Question:** Is there a need to import historical data from the previous paper records and spreadsheets need to be migrated into the new system, or will it be necessary to build the database from scratch?
* **Open Question:** What personal fields (e.g., Phone Number, Date of Birth, etc) are required by Law to identify a Patient.

## 8. AI Requirements Review Record

| AI suggestion | Evidence? | Decision | Reason | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **Implement Role Based Access Control (RBAC) Separating Receptionist and Management views.** | Assumption Requiring Validation | Accepted | Standard security practice for medical software so it fits with the distinct stakeholders identified. | Add Provisional NFR for basic User Permissions. |
| **Add a Telehealth Video Conferencing Module.** | Unsupported | Rejected | This directly violates the main requirements of developing a Small, Maintainable System. | Flagged as Out of Scope. |
| **Define the Specific Response Times for the Patient Search Function.** | Assumption Requiring Validation | Modified | NFRs should be testable, Quickly in US-01 is subjective currently. | Update the US-01 criteria to include a 2-second maximum retrieval time. |