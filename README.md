IAM Access Control Lab

Introduction

This is a Python simulation of a straightforward Identity and Access Management – or IAM – system. The lab shows how companies might deal with identities, oversee access, and watch out for security occurrences.

The system includes Role-Based Access Control, or RBAC, user provisioning, user deprovisioning, and security checking.

Features

 Role-Based Access Control (RBAC)
 User provisioning
 User deprovisioning
 Enforcement of least privilege
 Security auditing

Technologies

 Python
 JSON
 Git / GitHub

How it’s Built

 `users.json`: holds details of users and their roles;
 `resources.json`: holds details of which roles are allowed to use which resources;
 `access_control.py`: holds the code that manages identities and controls access to resources;
 `audit_log.txt`: holds a record of access requests and security details.

How it Works

The system gets users and resources from the JSON files.

Then, a user asks for access to a resource.

The system sees if the user’s role gives them permission to use that resource.

The user is either allowed or not allowed access to the resource.

An item is added to the audit log.

What You’ll See

Here’s some of what the system might display when it’s running:

Access granted: Alice -> HR_Portal
Access denied: Bob -> Finance_System
User Dana provisioned
User Bob deprovisioned

Security Ideas Shown

 Managing identities over time
 Authorisation based on roles
 Least privilege
 Access auditing
* Finding attempts to get access without permission.


