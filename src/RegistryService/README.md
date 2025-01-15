# RegistryService
## Classes
```mermaid
classDiagram
    class StudentDomain {
        + string ID
        + string Name
        + string Email
        + List<PasswordDomain> Passwords
        + datetime CreatedAt
        + datetime UpdatedAt
        + bool Active
        + ToJson() string
    }

    class PasswordDomain {
        + string Hash        
        + datetime CreatedAt
        + ToJson() string
    }

    class RegistryService {
        + repository data~StudentDomain~
        + Insert(StudentDomain) string
        + Update(StudentDomain) bool
        + Inactivate(string id) bool
        + Activate(string id) bool
        + GetByID(string id) StudentDomain
    }

    class AuthService {
        + repository data~PasswordDomain~
        + Insert(string id, string pass) void
        + Check(string id, string pass) bool        
    }
```
## MER
```mermaid
erDiagram
    Student {
        string ID
        string Name
        string Email
        datetime CreatedAt
        datetime UpdatedAt
        bool Active
    }

    Password {
        string StudentID
        string Hash
        datetime CreatedAt
    }

    Student ||--|{ Password : contains

    LoginResult {
        string StudentID
        bool Success
        datetime CreatedAt
    }

    Student ||--|{ LoginResult : contains
```

