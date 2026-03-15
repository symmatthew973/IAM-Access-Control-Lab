import json
from datetime import datetime


def log_event(event):
    with open("audit_log.txt", "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {event}\n")


class IAMSystem:
    def __init__(self, users_file: str, resources_file: str):
        self.users_file = users_file
        self.resources_file = resources_file
        self.users = self.load_json(users_file)
        self.resources = self.load_json(resources_file)

    def load_json(self, filename: str):
        with open(filename, "r") as file:
            return json.load(file)

    def save_users(self):
        with open(self.users_file, "w") as file:
            json.dump(self.users, file, indent=2)

    def find_user(self, name: str):
        for user in self.users:
            if user["name"].lower() == name.lower():
                return user
        return None

    def provision_user(self, name: str, department: str, role: str):
        if self.find_user(name):
            print(f"[!] User {name} already exists.")
            log_event(f"PROVISION FAILED: {name} already exists")
            return

        new_user = {
            "name": name,
            "department": department,
            "role": role,
            "active": True
        }
        self.users.append(new_user)
        self.save_users()
        print(f"[+] Provisioned user: {name} ({role}, {department})")
        log_event(f"USER PROVISIONED: {name} ({role}, {department})")

    def deprovision_user(self, name: str):
        user = self.find_user(name)
        if not user:
            print(f"[!] User {name} not found.")
            log_event(f"DEPROVISION FAILED: {name} not found")
            return

        user["active"] = False
        self.save_users()
        print(f"[-] Deprovisioned user: {name}")
        log_event(f"USER DEPROVISIONED: {name}")

    def check_access(self, name: str, resource: str):
        user = self.find_user(name)

        if not user:
            print(f"[!] Access denied: user {name} does not exist.")
            log_event(f"ACCESS DENIED: unknown user {name} attempted {resource}")
            return False

        if not user["active"]:
            print(f"[!] Access denied: user {name} is inactive.")
            log_event(f"ACCESS DENIED: inactive user {name} attempted {resource}")
            return False

        if resource not in self.resources:
            print(f"[!] Resource {resource} does not exist.")
            log_event(f"ACCESS FAILED: resource {resource} does not exist")
            return False

        allowed_roles = self.resources[resource]

        if user["role"] in allowed_roles:
            print(f"[+] Access granted: {name} -> {resource}")
            log_event(f"ACCESS GRANTED: {name} -> {resource}")
            return True
        else:
            print(f"[!] Access denied: {name} -> {resource}")
            log_event(f"ACCESS DENIED: {name} attempted unauthorized access to {resource}")
            return False

    def list_users(self):
        print("\n=== Current Users ===")
        for user in self.users:
            status = "Active" if user["active"] else "Inactive"
            print(
                f"{user['name']} | Dept: {user['department']} | "
                f"Role: {user['role']} | Status: {status}"
            )

    def list_resources(self):
        print("\n=== Resources and Allowed Roles ===")
        for resource, roles in self.resources.items():
            print(f"{resource}: {', '.join(roles)}")


def main():
    iam = IAMSystem("users.json", "resources.json")

    iam.list_users()
    iam.list_resources()

    print("\n=== Access Checks ===")
    iam.check_access("Alice", "HR_Portal")
    iam.check_access("Bob", "Finance_System")
    iam.check_access("Charlie", "Employee_Directory")

    print("\n=== Provision New User ===")
    iam.provision_user("Dana", "Engineering", "Engineer")
    iam.check_access("Dana", "Code_Repository")

    print("\n=== Deprovision User ===")
    iam.deprovision_user("Bob")
    iam.check_access("Bob", "Code_Repository")

    print("\n=== Final User List ===")
    iam.list_users()


if __name__ == "__main__":
    main()