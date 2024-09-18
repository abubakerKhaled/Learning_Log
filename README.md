# Learning Log Application

## Overview

Learning Log is a dynamic web application designed to empower users in their learning journey. It serves as a personal knowledge management system, allowing users to track their learning progress across various topics of interest.

## Key Features

- **Topic Management**: Users can create, view, and organize topics they're interested in learning.
- **Journal Entries**: For each topic, users can add, edit, and review detailed journal entries to document their learning process.
- **User Authentication**: Secure registration and login system to ensure privacy of user data.
- **Responsive Design**: Accessible on various devices for learning on-the-go.
- **Enhanced Security**: Uses `admin_honeypot` to add an additional layer of security by creating a honeypot for bots attempting to access the admin interface.

## User Journey

1. **Home Page**: 
   - Provides an overview of the application's purpose and benefits.
   - Invites new users to register or existing users to log in.

2. **Dashboard** (Post-login):
   - Displays an overview of the user's topics and recent entries.
   - Provides quick access to create new topics or entries.

3. **Topic Management**:
   - Users can create new topics of interest.
   - View a list of all topics they're currently learning.
   - Option to archive or delete topics if needed.

4. **Entry Management**:
   - Add new journal entries to specific topics.
   - Edit existing entries to update progress or correct information.
   - View entries chronologically or by topic.

## Security Note

To enhance security, the application uses the `admin_honeypot` module. This module provides a honeypot for automated bots that may attempt to access the admin interface. The actual Django admin interface is secured under a different path (`theboss/`).

## Getting Started

[Include instructions for setting up the development environment, installing dependencies, and running the application locally.]

## Contributing

We welcome contributions to the Learning Log application! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contact

For any queries or support, please contact [aboubkerkhaled77@gmail.com].
