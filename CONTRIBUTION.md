# Contributing Guidelines

Thank you for considering contributing to this project! We appreciate your interest and welcome contributions from the community. Whether you're reporting a bug, proposing a new feature, or improving our documentation, your input is valuable.

## Table of Contents

- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)
- [Pull Requests](#pull-requests)
- [Code of Conduct](#code-of-conduct)
- [Feedback and Discussions](#feedback-and-discussions)
- [License Information](#license-information)

Here's how you can get involved and contribute to the project:

## Bug Reports

If you encounter a bug or issue while using our app, please help us by reporting it. To submit a bug report, follow these steps:

1. Go to the Issues section of our GitHub repository. [GitHub Issues](#github-issues)
2. Check if a similar issue has already been reported. If not, click on the "New Issue" button.
3. Provide a clear and detailed description of the issue you encountered, including any error messages or steps to reproduce the problem.
4. Add relevant labels or tags to categorize the issue (e.g., "bug," "enhancement," "documentation," etc.).

**Great Bug Reports** tend to have:

    - A quick summary and/or background
    - Steps to reproduce (be specific and include sample code if possible)
    - Expected behaviour vs. actual behavior
    - Notes (possibly including why you think this might be happening or any unsuccessful attempts at resolving it)

People _love_ thorough bug reports.

## Feature Requests

If you have an idea for a new feature or improvement that you'd like to see in our app, please let us know. To submit a feature request, follow these steps:

1. Go to the Issues section of our GitHub repository. [GitHub Issues](#github-issues)
2. Click on the "New Issue" button.
3. Clearly describe the new feature or enhancement you have in mind, including its use case and benefits.
4. Add the "enhancement" label to the issue to help us identify it as a feature request.

## Pull Requests

If you'd like to contribute code or documentation changes to the project, you can do so by submitting a pull request (PR). Here's how to create a pull request:

1. Fork our repository to your GitHub account.
2. Clone your forked repository to your local machine.

### Create a branch

Change to the repository directory on your computer:

#### For Backend

```
cd spitfire-events/Backend
```

#### For Mobile

```
cd spitfire-events/Mobile
```

Now create a branch using the `git switch` command:

```bash
git switch -c feature-name
```

Make your changes, following our coding style and guidelines.

1. If you've added code that should be tested, add tests.
2. If you've changed APIs, update the documentation.
3. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and other parameters.
4. Ensure the test suite passes.
5. Make sure your code lints.

Commit your changes and push them to your forked repository:

```bash
    git add .
    git commit -m "Add feature-name"
    git push origin feature-name
```

1. Go to the Pull Requests section of our repository.
2. Click on the "New Pull Request" button.
3. Select the branch containing your changes from your forked repository.
4. Provide a clear and concise description of your changes in the PR description.
5. Submit the pull request, and we'll review your changes as soon as possible.

## License Information

Any contributions you make will be under the MIT Software License. In short, when you submit code changes, your submissions are understood to be under the same [MIT License](#LICENSE) that covers the project.

## Code of Conduct

We expect all contributors to adhere to our Code of Conduct. Please be respectful and considerate of others when participating in discussions and contributing to the project.

## Feedback and Discussions

If you have general questions, suggestions, or want to discuss ideas with the community, you can also participate in discussions in the Discussions section.

Your contributions help make our project better, and we're grateful for your support! If you have any questions or need further assistance, feel free to reach out to us via the project's communication channels.
