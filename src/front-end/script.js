// Create a object to store the current Year
let fullYear = new Date().getFullYear()

// Load or initialize visit counter
let visitCounter = parseInt(localStorage.getItem("visit_counter") || "0")

// Load or create a user ID 
let userId = localStorage.getItem("user_id")
if (!userId) { // it does not exist then create
    userId = crypto.randomUUID()
    localStorage.setItem("user_id", userId)
}

// Increment visit counter and store it
visitCounter +=1
localStorage.setItem("visit_counter", visitCounter)

// Create the HTML content
let html = `
    Copyright ${fullYear} 
    <a href="www.github.com\egiberne" target="_blank">
    egiberne@github 
    </a>
    It is your #${visitCounter} visit
`
// Display the content
document.getElementById('footer').innerHTML= html
document.getElementById('aside').innerHTML= html