# Quality Assurance Tracker POC

# Database simulation using dictionaries
qa_records = {}
quality_issues = {}
quality_checks = {}

# CRUD: QA Records
def create_qa_record(project_name, deliverable, status):
    qa_id = len(qa_records) + 1
    qa_records[qa_id] = {
        "project_name": project_name,
        "deliverable": deliverable,
        "status": status
    }
    return qa_id

def read_qa_record(qa_id):
    return qa_records.get(qa_id)

def update_qa_record(qa_id, project_name=None, deliverable=None, status=None):
    if qa_id in qa_records:
        if project_name:
            qa_records[qa_id]["project_name"] = project_name
        if deliverable:
            qa_records[qa_id]["deliverable"] = deliverable
        if status:
            qa_records[qa_id]["status"] = status
        print(f"QA record {qa_id} updated.")
    else:
        print(f"QA record {qa_id} not found.")

def delete_qa_record(qa_id):
    if qa_id in qa_records:
        del qa_records[qa_id]
        print(f"QA record {qa_id} deleted.")
    else:
        print(f"QA record {qa_id} not found.")

# Manage Quality Issues
def manage_quality_issues():
    project_name = input("Enter project name: ")
    issue_description = input("Enter issue description: ")
    issue_id = len(quality_issues) + 1
    quality_issues[issue_id] = {
        "project_name": project_name,
        "issue_description": issue_description,
        "status": "Open"
    }
    print(f"Quality issue '{issue_description}' logged for project '{project_name}' with issue ID {issue_id}")

def resolve_quality_issue():
    issue_id = int(input("Enter issue ID to resolve: "))
    if issue_id in quality_issues:
        resolution = input("Enter resolution description: ")
        quality_issues[issue_id]["status"] = "Resolved"
        quality_issues[issue_id]["resolution"] = resolution
        print(f"Quality issue {issue_id} resolved: {resolution}")
    else:
        print(f"Issue ID {issue_id} not found.")

# Log Quality Checks
def log_quality_checks():
    project_name = input("Enter project name: ")
    deliverable = input("Enter deliverable: ")
    check_description = input("Enter check description: ")
    outcome = input("Enter outcome (Pass/Fail): ")
    check_id = len(quality_checks) + 1
    quality_checks[check_id] = {
        "project_name": project_name,
        "deliverable": deliverable,
        "check_description": check_description,
        "outcome": outcome
    }
    print(f"Quality check '{check_description}' logged for project '{project_name}' with check ID {check_id}")

# Display Records
def display_records():
    print("\nQA Records:")
    for qa_id, details in qa_records.items():
        print(f"ID: {qa_id}, Project: {details['project_name']}, Deliverable: {details['deliverable']}, Status: {details['status']}")
    
    print("\nQuality Issues:")
    for issue_id, details in quality_issues.items():
        print(f"ID: {issue_id}, Project: {details['project_name']}, Description: {details['issue_description']}, Status: {details['status']}")
    
    print("\nQuality Checks:")
    for check_id, details in quality_checks.items():
        print(f"ID: {check_id}, Project: {details['project_name']}, Deliverable: {details['deliverable']}, Check: {details['check_description']}, Outcome: {details['outcome']}")

# Menu
def menu():
    while True:
        print("\nQuality Assurance Tracker Menu")
        print("1. Create QA Record")
        print("2. Update QA Record")
        print("3. Delete QA Record")
        print("4. Manage Quality Issues")
        print("5. Resolve Quality Issue")
        print("6. Log Quality Checks")
        print("7. Display Records")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            project_name = input("Enter project name: ")
            deliverable = input("Enter deliverable: ")
            status = input("Enter status: ")
            create_qa_record(project_name, deliverable, status)
        elif choice == '2':
            qa_id = int(input("Enter QA record ID to update: "))
            project_name = input("Enter new project name (leave blank to keep current): ")
            deliverable = input("Enter new deliverable (leave blank to keep current): ")
            status = input("Enter new status (leave blank to keep current): ")
            update_qa_record(qa_id, project_name or None, deliverable or None, status or None)
        elif choice == '3':
            qa_id = int(input("Enter QA record ID to delete: "))
            delete_qa_record(qa_id)
        elif choice == '4':
            manage_quality_issues()
        elif choice == '5':
            resolve_quality_issue()
        elif choice == '6':
            log_quality_checks()
        elif choice == '7':
            display_records()
        elif choice == '8':
            print("Exiting the Quality Assurance Tracker.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the menu
menu()
