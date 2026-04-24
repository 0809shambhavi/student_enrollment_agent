# tools.py

programs = {
    "computer science": {
        "name": "BSc Computer Science",
        "duration": "4 years",
        "tuition": "$40,000/year",
        "prerequisites": ["High School Math", "Basic Programming"]
    },
    "data science": {
        "name": "MSc Data Science",
        "duration": "2 years",
        "tuition": "$50,000/year",
        "prerequisites": ["Python", "Statistics"]
    },
    "business administration": {
        "name": "MBA",
        "duration": "2 years",
        "tuition": "$60,000/year",
        "prerequisites": ["Bachelor's Degree", "Work Experience"]
    }
}

deadlines = {
    "computer science": {
        "application_deadline": "June 30",
        "document_deadline": "July 15",
        "decision_date": "August 10"
    },
    "data science": {
        "application_deadline": "May 30",
        "document_deadline": "June 10",
        "decision_date": "July 5"
    },
    "business administration": {
        "application_deadline": "April 30",
        "document_deadline": "May 10",
        "decision_date": "June 1"
    }
}

applications = {
    "APP-1042": {
        "name": "John Doe",
        "program": "computer science",
        "status": "Documents Pending",
        "next_step": "Submit transcripts and recommendation letter"
    },
    "APP-2043": {
        "name": "Alice Smith",
        "program": "data science",
        "status": "Under Review",
        "next_step": "Wait for decision"
    },
    "APP-3098": {
        "name": "Bob Lee",
        "program": "business administration",
        "status": "Accepted",
        "next_step": "Pay admission fee"
    }
}


def get_program_info(program_name: str):
    return programs.get(program_name.lower())


def get_deadlines(program_name: str):
    return deadlines.get(program_name.lower())


def check_application_status(applicant_id: str):
    return applications.get(applicant_id)