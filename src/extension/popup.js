// Build out a simple extension that when clicked on will start to run all the files and get the information
// I also would like it to display the messages that would be sent out to the console and have the ability to give it an ok
document.getElementById('activate_button').addEventListener("click", function() {
    fetch("http://localhost:3000/offerUpbot", {
        method: "POST",
})});

let button = document.getElementById('activate_button');
button.addEventListener('click', sendPostRequest(/* The URL of the current page your are on */));

/**
 * This function is called when the button is clicked.
 * @param {string} url - The URL to send the POST request to.
 * @returns {void}
 */
let sendPostRequest = (url) => {
    // TBD 
};