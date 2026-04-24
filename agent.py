# agent.py

import re
from tools import get_program_info, get_deadlines, check_application_status


class EnrollmentAgent:
    def __init__(self, memory):
        self.memory = memory

    def handle(self, user_input: str):
        text = user_input.lower()

        print("\n[THOUGHT] Processing user input...")

        # -----------------------------
        # 1. ENTITY EXTRACTION
        # -----------------------------
        # Extract program
        if "computer science" in text:
            self.memory.set("program", "computer science")
            print("[OBSERVATION] Detected program: computer science")

        elif "data science" in text:
            self.memory.set("program", "data science")
            print("[OBSERVATION] Detected program: data science")

        elif "business" in text:
            self.memory.set("program", "business administration")
            print("[OBSERVATION] Detected program: business administration")

        # Extract applicant ID using regex
        match = re.search(r'APP-\d+', user_input.upper())
        if match:
            applicant_id = match.group()
            self.memory.set("applicant_id", applicant_id)
            print(f"[OBSERVATION] Detected applicant ID: {applicant_id}")

        # -----------------------------
        # 2. INTENT DETECTION
        # -----------------------------
        if "program" in text or "offer" in text:
            intent = "program_info"
        elif "deadline" in text:
            intent = "deadlines"
        elif "status" in text:
            intent = "application_status"
        elif "fee waiver" in text:
            intent = "unsupported"
        elif "document" in text:
            intent = "documents"
        else:
            intent = "unknown"

        print(f"[THOUGHT] Detected intent: {intent}")

        # -----------------------------
        # 3. TOOL CALLING + RESPONSE
        # -----------------------------

        # --- Program Info ---
        if intent == "program_info":
            program = self.memory.get("program")

            if not program:
                return "Could you specify which program you're interested in?"

            print("[ACTION] Calling get_program_info")

            info = get_program_info(program)

            if info:
                print("[OBSERVATION] Program info retrieved")
                return (
                    f"We offer {info['name']} which is {info['duration']} long. "
                    f"Tuition is {info['tuition']}. "
                    f"Prerequisites include: {', '.join(info['prerequisites'])}."
                )
            else:
                return "I couldn't find that program."

        # --- Deadlines ---
        elif intent == "deadlines":
            program = self.memory.get("program")

            if not program:
                return "Please tell me which program you're asking about."

            print("[ACTION] Calling get_deadlines")

            dl = get_deadlines(program)

            if dl:
                print("[OBSERVATION] Deadline info retrieved")
                return (
                    f"For {program.title()}, the application deadline is {dl['application_deadline']}, "
                    f"documents must be submitted by {dl['document_deadline']}, "
                    f"and decisions are announced on {dl['decision_date']}."
                )
            else:
                return "I couldn't find deadline information for that program."

        # --- Application Status ---
        elif intent == "application_status":
            app_id = self.memory.get("applicant_id")

            if not app_id:
                return "Please provide your applicant ID."

            print("[ACTION] Calling check_application_status")

            status = check_application_status(app_id)

            if status:
                print("[OBSERVATION] Application status retrieved")
                self.memory.set("last_status", status)

                return (
                    f"Hi {status['name']}, your application for {status['program'].title()} is currently "
                    f"'{status['status']}'. Next step: {status['next_step']}."
                )
            else:
                return "I couldn't find your application. Please check your applicant ID."

        # --- Documents (follow-up intent) ---
        elif intent == "documents":
            status = self.memory.get("last_status")

            if status:
                print("[OBSERVATION] Using previous application status")
                return f"You still need to: {status['next_step']}."
            else:
                return "I need your application status first. Please provide your applicant ID."

        # --- Unsupported ---
        elif intent == "unsupported":
            print("[THOUGHT] Unsupported query → escalate")
            return (
                "I can't help with fee waivers directly, but I can connect you to an enrollment counselor. "
                "Would you like that?"
            )

        # --- Unknown ---
        else:
            print("[THOUGHT] Could not determine intent")
            return "I'm not sure how to help with that. Could you clarify?"