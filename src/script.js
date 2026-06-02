// Create a object to store the current Year
let fullYear = new Date().getFullYear()

// Load or initialize visit counter
let visitCount = parseInt(localStorage.getItem("visit_count") || "0")

// Increment visit count and store it
visitCount++;
localStorage.setItem("visit_count", visitCount);

// Create the HTML content
let html = `
    Copyright ${fullYear} 
    <a href="www.github.com\egiberne" target="_blank">
    egiberne@github 
    </a>
    visit #${visitCount}
`
// Display the values 
document.getElementById('footer').innerHTML= html
document.getElementById('aside').innerHTML= html