package main

import (
	"fmt"
	"html/template"
	"net/http"
)

var tmpl = template.Must(template.New("main").Parse(`
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ .Title }}</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Arial', sans-serif;
    }
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f3f3f3;
    }
    .container {
      background-color: white;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      text-align: center;
      width: 300px;
    }
    input[type="text"], input[type="password"] {
      width: 100%;
      padding: 0.8rem;
      margin: 1rem 0;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #007bff;
      color: white;
      padding: 0.8rem 1.2rem;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      width: 100%;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>{{ .Message }}</h1>
    {{ if .LoginForm }}
    <form method="POST" action="/home">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required placeholder="Enter your username">
      
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required placeholder="Enter your password">
      
      <button type="submit">Login</button>
    </form>
    {{ else }}
    <p>Welcome, {{ .Username }}!</p>
    <a href="/">Logout</a>
    {{ end }}
  </div>
</body>
</html>
`))

// Struct for passing data to the template
type PageData struct {
	Title     string
	Message   string
	LoginForm bool
	Username  string
}

func main() {
	http.HandleFunc("/", loginPage)
	http.HandleFunc("/home", homePage)

	fmt.Println("Server running on http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}

func loginPage(w http.ResponseWriter, r *http.Request) {
	data := PageData{
		Title:     "Login Page",
		Message:   "Please Login",
		LoginForm: true,
	}
	tmpl.Execute(w, data)
}

func homePage(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Redirect(w, r, "/", http.StatusSeeOther)
		return
	}

	username := r.FormValue("username")
	password := r.FormValue("password")

	// Basic validation (In real applications, validate securely)
	if username == "" || password == "" {
		http.Redirect(w, r, "/", http.StatusSeeOther)
		return
	}

	data := PageData{
		Title:     "Home Page",
		Message:   "Welcome to the Home Page!",
		LoginForm: false,
		Username:  username,
	}
	tmpl.Execute(w, data)
}