0x0A. Configuration management

## Requirements

### General

- All your files will be interpreted on Ubuntu 20.04 LTS.
- All your files should end with a new line.
- A README.md file at the root of the folder of the project is mandatory.
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
- Your Puppet manifests files must end with the extension .pp.

### Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

- Install puppet:
  ```
  $ apt-get install -y ruby=1:2.7+1 --allow-downgrades
  $ apt-get install -y ruby-augeas
  $ apt-get install -y ruby-shadow
  $ apt-get install -y puppet
  ```

- Puppet 5 Docs

- Install puppet-lint:
  ```
  $ gem install puppet-lint
  ```

## Tasks

### Task 1: Create a File

- Using Puppet, create a file in /tmp.
- Requirements:
  - File path is /tmp/school.
  - File permission is 0744.
  - File owner is www-data.
  - File group is www-data.
  - File contains "I love Puppet".

### Task 2: Install a Package

- Using Puppet, install Flask from pip3.
- Requirements:
  - Install Flask.
  - Version must be 2.1.0.

### Task 3: Execute a Command

- Using Puppet, create a manifest that kills a process named "killmenow".
- Requirements:
  - Must use the exec Puppet resource.
  - Must use pkill.

## Resources

- Read or watch:
  - Intro to Configuration Management
  - Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
  - Puppet’s Declarative Language: Modeling Instead of Scripting
  - Puppet lint
  - Puppet emacs mode

## Copyright

© 2023 ALX, All rights reserved.

---

You can replace the placeholders with actual links and details as needed. This README file provides an overview of the project, its tasks, requirements, and key information for anyone working on or reviewing the project.