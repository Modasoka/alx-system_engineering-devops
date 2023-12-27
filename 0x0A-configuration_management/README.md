# Configuration Management Project

## Overview

This project focuses on configuration management using Puppet for automating and managing infrastructure.

## Resources

Before diving into the project, it's recommended to go through the following resources:

- [Intro to Configuration Management](link-to-intro): Gain a foundational understanding of configuration management concepts.
- [Puppet Resource Type: File](link-to-resource-types): Explore Puppet's file resource type for managing files and directories.
- [Puppet’s Declarative Language](link-to-declarative-language): Learn about Puppet's declarative language and the shift from scripting to modeling.
- [Puppet lint](link-to-puppet-lint): Understand and apply Puppet linting to ensure clean and consistent code.
- [Puppet Emacs Mode](link-to-emacs-mode): Enhance your Puppet coding experience with Emacs mode.

## Requirements

### General

1. **Platform Compatibility:**
   - All files will be interpreted on Ubuntu 20.04 LTS.

2. **File Standards:**
   - Ensure all files end with a new line.

3. **README File:**
   - Include a mandatory `README.md` file at the root of the project folder.

4. **Puppet Manifests:**
   - Manifests must pass puppet-lint version 2.1.1 without any errors.
   - Manifests must run without error.

5. **Manifest Documentation:**
   - The first line of each Puppet manifest must be a comment explaining its purpose.
   - Manifest files must have the extension `.pp`.

## Getting Started

To start using this configuration management project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
