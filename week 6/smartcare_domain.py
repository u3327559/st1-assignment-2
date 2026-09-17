class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.appointments = []

    def get_appointment_history(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id
        self.name = name
        self.appointments = []

    def check_availability(self, date, time):
        pass

    def get_schedule(self):
        pass


class Appointment:
    def __init__(self, appointment_id, date, time, patient, practitioner):
        self.appointment_id = appointment_id
        self.date = date
        self.time = time
        self.status = "Scheduled"
        
        self.patient = patient
        self.practitioner = practitioner

    def update_status(self, new_status):
        pass