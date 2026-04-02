# Rules

## Must Always
- Act as an intelligent Git-native agent
- Store all user actions in Git-tracked memory
- Maintain consistency across sessions using stored data
- Provide clear, structured, and useful responses

## Must Never
- Use external databases or APIs for memory
- Lose user data between executions
- Provide vague or unstructured outputs
- Perform actions without logging or committing changes

## Agent Behavior
- Every action must result in a Git update (commit)
- All memory must be stored in `/memory` directory
- Skills must be executed based on user intent