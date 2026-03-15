# IAM Access Control Lab

## Overview
This project simulates a basic Identity and Access Management (IAM) system using Python.  
It demonstrates how organizations manage user identities, enforce access permissions, and track security events.

The system implements Role-Based Access Control (RBAC), user provisioning and deprovisioning, and audit logging for security monitoring.

## Features
- Role-Based Access Control (RBAC)
- User provisioning
- User deprovisioning
- Least privilege enforcement
- Security audit logging

## Technologies Used
- Python
- JSON
- Git / GitHub

## System Architecture
- `users.json` stores user identities and roles
- `resources.json` defines which roles can access specific systems
- `access_control.py` contains the core IAM logic and access enforcement
- `audit_log.txt` records access events and security logs

## Example Workflow
1. Users and resources are loaded from JSON files
2. A user attempts to access a protected resource
3. The system verifies role permissions
4. Access is granted or denied
5. The event is recorded in the audit log

## Example Output
Example terminal output:

- Access granted: Alice -> HR_Portal
- Access denied: Bob -> Finance_System
- User Dana provisioned
- User Bob deprovisioned

## Security Concepts Demonstrated
- Identity lifecycle management
- Role-based authorization
- Least privilege
- Access auditing
- Unauthorized access detection
