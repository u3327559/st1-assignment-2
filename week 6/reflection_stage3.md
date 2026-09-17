# Stage 3 Lab Reflection

**What was the hardest modelling decision to make? Where did you think that AI has overdesigned? What evidence did you use to make your final choice?**

The decision to allocate the behavior for preventing duplicate bookings (FR-04) was the most challenging one. Initially, it seemed logical to attribute this responsibility to the Appointment Class but in the end, I concluded that by implementing the `check_availability()` method in Practitioner class was more appropriate. This is because the Practitioner is the entity that actually "Owns" their schedule so they should be responsible for their own workload management. 

When you look at the AI model, you can notice that it is overdesigned in many places. For instance, it suggests System Level Classes such as `ClinicController` and `AppointmentManager` instead of using Domain Specific Concepts. Moreover, the AI omitted the explicitly specified scope of the system under the v0.2 specification, which excluded the Billing and Payment Classes. 

Finally, I based my final decision on the trace of requirements to classes. Specifically, All Implemented Classes, Attributes and methods that could be related to a Specific Concept that is mentioned and required in the Eight Confirmed Functional Requirements (FR-01 to FR-08).
