# Stage 3 Tutorial Activities

## Candidate Concepts

| Candidate | Class? | Reason |
| :--- | :--- | :--- |
| **Patient** | Yes | It is a core domain entity that has its own particular state (e.g., Name, ID) and Behavior. |
| **Practitioner** | Yes | It is a core domain entity that has its own schedule behavior and state(e.g., Name, ID). |
| **Appointment** | Yes | It is a core transactional entity which connects a Patient to a Practitioner, having particular state data (e.g., Date, Time, Status). |
| **Name** | No | The term Name is simply an attribute of type (string) of either Patient or Practitioner Class, not an independent business entity with its own life cycle. |
| **Clinic** | No | In this particular case, the Clinic is the environment within which things happen. Creating a single Clinic class for it that would hold everything is a very bad practice, often referred to as God Object. |
| **Database** | No | A database is an infrastructure/implementation detail, not a business entity. The main reason is that you need to preserve your objects to a database, that is an implementation detail and has almost nothing to do with the domain model. |
| **Cancellation** | No | Cancellation is an Action or the Status of an Appointment, is not a Physical or Conceptual Object. |
| **Status** | No | Status is just an Attribute or an Enumeration that belongs to an Appointment. |

## CRC Cards

**Patient**

| Responsibilities | Collaborators |
| :--- | :--- |
| Know about Personal Details (Name, ID) | Appointment |
| Know about Appointment History | |

**Practitioner**

| Responsibilities | Collaborators |
| :--- | :--- |
| Know about Personal details (Name, ID) | Appointment |
| Know about Availability and Assigned Schedule | |

**Appointment**

| Responsibilities | Collaborators |
| :--- | :--- |
| Know about Scheduled Date and Time | Patient |
| Know about Current Status (Scheduled, Cancelled or Completed) | Practitioner |
| Link a particular Patient to a specific Practitioner | |

## Relationship Reasoning

**Patient to Appointment: Which relationship and why?** 
It is basically a one to many relationship which means that a single Patient may have multiple Appointments over their lifetime but a single Appointment is only connected to one Patient at the same time. 

**Practitioner to Appointment: what multiplicity?** 
The multiplicity is One to zero-or-many. This means one Practitioner can have no Appointments if they are new or have a schedule. They can also have Appointments but every Appointment is linked to just one Practitioner. 

**Should Appointment inherit from the Patient?** 
No. Inheritance is reserved for (is-a) relationships (like Surgeon is type of a Practitioner). An Appointment is not a Patient, but rather an association to a Patient.

**Does the Clinic need to own every object?**
No. In domain modeling, there is usually no need to force every object to be owned and managed by a single clinic object. This would introduce non required logic and result in a much more tightly coupled application. Let objects manage themselves and reference other objects as needed.

## AI Model Critique

The suggestions that are given by AI (e.g, PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine, etc.) are examples of overengineering. When building a domain model we should be focused on business objects like Patient and Appointment, but the AI suggests about the implementation details such as Managers/Controllers etc. This implies that the AI is thinking about code implementations (such as Databases or Routing) rather than a domain model. Additionally, some suggested objects like NotificationManager would not be required for a simple scheduling application as required.
