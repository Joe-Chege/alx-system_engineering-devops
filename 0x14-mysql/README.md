# Project: 0x14. MySQL

## Introduction
This project focuses on setting up a MySQL database infrastructure, including installation, user management, replication, and backup strategies. The tasks involve configuring primary and replica servers, managing users, and ensuring data redundancy and security.

## Concepts
In this project, you will explore the following concepts:
- **Database Administration:** Understanding the main role of a database, creating and managing databases and tables, and ensuring data integrity and security.
- **Web Stack Debugging:** Debugging web applications and database interactions to identify and fix issues.
- **MySQL Installation:** Installing MySQL 5.7.x on designated servers and verifying the installation.
- **Database Replication:** Setting up replication between a primary MySQL server and a replica server for data redundancy and load distribution.
- **Database Backup Strategy:** Implementing a backup strategy for MySQL databases, including creating database dumps and storing them securely.

## Tasks

### Task 0: Install MySQL
Install MySQL 5.7.x on both web-01 and web-02 servers. Ensure that the installation is successful and that the MySQL version is correct.

### Task 1: Let us in!
Create a MySQL user named `holberton_user` on both web-01 and web-02 servers. Grant the necessary permissions to this user and ensure that SSH access is set up for both servers. Make sure that the user can check the primary/replica status of your databases.

### Task 2: If only you could see what I've seen with your eyes
Create a database named `tyrell_corp` on the primary MySQL server (web-01). Within this database, create a table named `nexus6` and add at least one entry to it. Grant `holberton_user` SELECT permissions on this table for verification purposes.

### Task 3: Quite an experience to live in fear, isn't it?
Create a new MySQL user named `replica_user` on the primary MySQL server (web-01). Ensure that this user has the appropriate permissions to replicate the primary MySQL server. Verify the user's permissions using `holberton_user`'s SELECT privileges on the `mysql.user` table.

### Task 4: Setup a Primary-Replica infrastructure using MySQL
Set up replication for the `tyrell_corp` database. Configure the primary MySQL server (web-01) and the replica MySQL server (web-02) appropriately. Verify the replication by adding a new record in the table via MySQL on web-01 and checking if it has been replicated to web-02.

### Task 5: MySQL backup
Write a Bash script that generates a MySQL dump containing all your MySQL databases. The dump file should be named `backup.sql` and should be compressed into a tar.gz archive with the format `day-month-year.tar.gz`. The script should accept a password as an argument for connecting to the MySQL database.

## Requirements
- Use allowed editors: `vi`, `vim`, `emacs`.
- All files should be interpreted on Ubuntu 16.04 LTS.
- All files should end with a new line.
- Include a `README.md` file at the root of the project folder.
- All Bash script files must be executable and pass `Shellcheck` without any error.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- Your MySQL primary should be hosted on `web-01` with the bind-address parameter commented out.
- Your MySQL replica should be hosted on `web-02`.
- Ensure that UFW is allowing connections on port 3306 (default MySQL port) for replication to work.

## Author
*Sylvain Kalache, co-founder at Holberton School*

## Project Deadline
Start: October 17, 2023, 6:00 AM  
End: October 18, 2023, 6:00 AM  
Checker will be released at October 17, 2023, 12:00 PM  
Auto review will be launched at the deadline.

## Important Notes
- Do not copy and paste someone else’s work. Plagiarism is strictly forbidden and will result in removal from the program.
- Ensure all tasks are completed to meet the specified learning objectives.
- Use the provided resources to enhance your understanding of the concepts.
- Implement secure practices and verify the functionality of your configurations.