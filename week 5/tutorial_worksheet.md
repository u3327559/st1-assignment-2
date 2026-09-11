## Activity 1 - Stakeholder Map

| Stakeholder | Need | Potential conflict |
| :--- | :--- | :--- |
| **Receptionist** | Efficiently Create, Update, and Manage Patient Appointments. | Desires a fast, less restricted user interface, which may conflict with IT's desire to impose restrictions on data validation and security steps. |
| **Practitioner / Doctor** | Accurately View Daily Schedules and Patient Details. | Needs detailed access to patient history, which needs to be balanced against patient privacy and data security policies. |
| **Management / Clinic Owner** | Reliable Reporting, Maintainability, and Tracking of All Appointment History. | Wants a new system that replaces paper records, but may clash with the IT department over the cost of enhanced features. |
| **Patient** | To have their Appointments Booked Accurately without Duplicate Errors. | Wants a seamless booking which could clash with the system needing a lot of data fields to register on the system. |
| **IT Support / Admin** | A Maintainable, Testable System that Securely Manages Data. | Prioritizes system stability and security, possibly limiting the flexibility desired by Receptionists or Management. |

## Activity 2 - Functional or Non-Functional?

* **Functional:** The system shall allow staff to cancel an appointment.
* **Non-functional:** The system must remain responsive for the course scale dataset.
* **Functional:** The system should retain cancelled appointments.
* **Non-functional:** Core business logic should be testable independently.
* **Functional:** The system shall be able to search for a patient by ID.

## Activity 3 - Repair Ambiguous Requirements

**The system should be easy to use.**
* **Problem:** Easy to Use is subjective which means that it cannot be objectively proved or disproved.
* **Clarification question:** What exact criteria will be able to determine a product’s usability (e.g., training time or the number of actions needed to schedule an appointment)?

**Patient search should be fast.**
* **Problem:** The term Fast is too vague and undefined.
* **Clarification question:** What is the maximum tolerable response time in seconds for a patient search query under a normal load?

**The system should securely manage data.**
* **Problem:** Securely Manage is vague and does not specifically provide any compliance requirements.
* **Clarification question:** Are there any particular Legal, Medical, or Technical Security Standards (such as data encryption regulations at rest) that the system must follow?

**Appointments should be easy to cancel.**
* **Problem:** Normally creates uncertainty, and Easy is unmeasurable.
* **Clarification question:** Under what particular conditions may an appointment be allowed to cancel as well as by what authority is this permissible.

## Activity 4 - AI Requirements Audit

| AI suggestion | Classification | Evidence / reason |
| :--- | :--- | :--- |
| **Patients Receive SMS Reminders.** | Assumption Requiring Validation | An advanced feature that is not covered in the basic idea of replacing paper/spreadsheets. Needs client approval for API costs. |
| **Facial Recognition Login.** | Unsupported / Out of Scope | An overly complex, expensive feature that invents requirements far beyond what would be needed for a Small Maintainable System. |
| **Receptionists Create Appointments.** | Confirmed | Core functionality needs to address the client's dilemma of replacing paper scheduling records. |
| **Online Payments.** | Unsupported / Out of Scope | This brief deals exclusively with Patient, Practitioner, and Appointment Management, and not with billing or e-commerce. |
| **Practitioners View Schedules.** | Confirmed | The most important business rules that need to be reviewed. Practitioners need to be able to see the appointments that have been logged in the system. |
| **AI Recommended Treatments.** | Unsupported / Out of Scope | This is a tool for administrative scheduling, not a clinical diagnosis system. It represents a massive overreach. |
| **Cancelled Appointments Remain in History.** | Confirmed | This is aligned directly with the client's stated problem of having Limited Appointment History with their current paper system. |

## Exit question

**Why is 'AI suggested it' not sufficient evidence for a requirement?**
AI lacks the concept of real world business context and the ability to negotiate scope or budget with stakeholders. It often hallucinates features that are unnecessarily advanced, like Facial Recognition or AI Diagnostics. These are entirely out of scope for a Small Maintainable Project, or that assumes certain workflows not indicated by the specific operational realities of the business. All requirements should be derived from the client’s brief or through direct stakeholder confirmation to ensure the software does what is mostly needed by the business without introducing unnecessary complexity.